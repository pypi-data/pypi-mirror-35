# -*- coding: utf-8 -*-
'''
Server worker process
'''
from __future__ import absolute_import

# Import pythond stdlib
import os
import re
import time
import signal
import logging
import threading

# Import third party libs
import zmq
import umsgpack
from prometheus_client import Counter

# Import napalm-logs pkgs
import napalm_logs.ext.six as six
from napalm_logs.config import LST_IPC_URL
from napalm_logs.config import DEV_IPC_URL
from napalm_logs.config import PUB_PX_IPC_URL
from napalm_logs.config import UNKNOWN_DEVICE_NAME
from napalm_logs.proc import NapalmLogsProc
# exceptions
from napalm_logs.exceptions import NapalmLogsExit

log = logging.getLogger(__name__)


class NapalmLogsServerProc(NapalmLogsProc):
    '''
    Server sub-process class.
    '''
    def __init__(self,
                 opts,
                 config,
                 started_os_proc):
        self.opts = opts
        self.config = config
        self.started_os_proc = started_os_proc
        self.__up = False
        self.compiled_prefixes = None
        self._compile_prefixes()

    def _exit_gracefully(self, signum, _):
        log.debug('Caught signal in server process')
        self.stop()

    def _setup_ipc(self):
        '''
        Setup the IPC pub and sub.
        Subscript to the listener IPC
        and publish to the device specific IPC.
        '''
        log.debug('Setting up the server IPC puller to receive from the listener')
        self.ctx = zmq.Context()
        # subscribe to listener
        self.sub = self.ctx.socket(zmq.PULL)
        self.sub.bind(LST_IPC_URL)
        try:
            self.sub.setsockopt(zmq.HWM, self.opts['hwm'])
            # zmq 2
        except AttributeError:
            # zmq 3
            self.sub.setsockopt(zmq.RCVHWM, self.opts['hwm'])
        # device publishers
        log.debug('Creating the router ICP on the server')
        self.pub = self.ctx.socket(zmq.ROUTER)
        self.pub.bind(DEV_IPC_URL)
        try:
            self.pub.setsockopt(zmq.HWM, self.opts['hwm'])
            # zmq 2
        except AttributeError:
            # zmq 3
            self.pub.setsockopt(zmq.SNDHWM, self.opts['hwm'])
        # Pipe to the publishers
        self.publisher_pub = self.ctx.socket(zmq.PUB)
        self.publisher_pub.connect(PUB_PX_IPC_URL)
        try:
            self.publisher_pub.setsockopt(zmq.HWM, self.opts['hwm'])
            # zmq 2
        except AttributeError:
            # zmq 3
            self.publisher_pub.setsockopt(zmq.SNDHWM, self.opts['hwm'])

    def _compile_prefixes(self):
        '''
        Create a dict of all OS prefixes and their compiled regexs
        '''
        self.compiled_prefixes = {}
        for dev_os, os_config in self.config.items():
            if not os_config:
                continue
            self.compiled_prefixes[dev_os] = []
            for prefix in os_config.get('prefixes', []):
                values = prefix.get('values', {})
                line = prefix.get('line', '')
                if prefix.get('__python_fun__'):
                    self.compiled_prefixes[dev_os].append({
                        '__python_fun__': prefix['__python_fun__'],
                        '__python_mod__': prefix['__python_mod__']
                    })
                    continue  # if python profiler defined for this prefix,
                    # no need to go further, but jump to the next prefix
                # Add 'pri' and 'message' to the line, and values
                line = '{{pri}}{}{{message}}'.format(line)
                # PRI https://tools.ietf.org/html/rfc5424#section-6.2.1
                values['pri'] = r'\<(\d+)\>'
                values['message'] = '(.*)'
                # We will now figure out which position each value is in so we can use it with the match statement
                position = {}
                for key in values.keys():
                    position[line.find('{' + key + '}')] = key
                sorted_position = {}
                for i, elem in enumerate(sorted(position.items())):
                    sorted_position[elem[1]] = i + 1
                # Escape the line, then remove the escape for the curly bracets so they can be used when formatting
                escaped = re.escape(line).replace(r'\{', '{').replace(r'\}', '}')
                # Replace a whitespace with \s+
                escaped = escaped.replace(r'\ ', r'\s+')
                self.compiled_prefixes[dev_os].append({
                    'prefix': re.compile(escaped.format(**values)),
                    'prefix_positions': sorted_position,
                    'raw_prefix': escaped.format(**values),
                    'values': values
                })
        # log.debug('Compiled prefixes')
        # log.debug(self.compiled_prefixes)

    def _identify_prefix(self, msg, data):
        '''
        Check the message again each OS prefix and if matched return the
        message dict
        '''
        prefix_id = -1
        for prefix in data:
            msg_dict = {}
            prefix_id += 1
            match = None
            if '__python_fun__' in prefix:
                log.debug('Trying to match using the %s custom python profiler', prefix['__python_mod__'])
                try:
                    match = prefix['__python_fun__'](msg)
                except Exception:
                    log.error('Exception while parsing %s with the %s python profiler',
                              msg, prefix['__python_mod__'], exc_info=True)
            else:
                log.debug('Matching using YAML-defined profiler:')
                log.debug(prefix['raw_prefix'])
                match = prefix['prefix'].search(msg)
            if not match:
                log.debug('Match not found')
                continue
            if '__python_fun__' in prefix:
                log.debug('%s matched using the custom python profiler %s', msg, prefix['__python_mod__'])
                msg_dict = match  # the output as-is from the custom function
            else:
                positions = prefix.get('prefix_positions', {})
                values = prefix.get('values')
                msg_dict = {}
                for key in values.keys():
                    msg_dict[key] = match.group(positions.get(key))
            # Remove whitespace from the start or end of the message
            msg_dict['__prefix_id__'] = prefix_id
            msg_dict['message'] = msg_dict['message'].strip()

            # The pri has to be an int as it is retrived using regex '\<(\d+)\>'
            if 'pri' in msg_dict:
                msg_dict['facility'] = int(int(msg_dict['pri']) / 8)
                msg_dict['severity'] = int(int(msg_dict['pri']) - (msg_dict['facility'] * 8))
            return msg_dict

    def _identify_os(self, msg):
        '''
        Using the prefix of the syslog message,
        we are able to identify the operating system and then continue parsing.
        '''
        ret = []
        for dev_os, data in self.compiled_prefixes.items():
            # TODO Should we prevent attepmting to determine the OS for the blacklisted?
            # [mircea] I think its good from a logging perspective to know at least that
            #   that the server found the matching and it tells that it won't be processed
            #   further. Later, we could potentially add an option to control this.
            log.debug('Matching under %s', dev_os)
            msg_dict = self._identify_prefix(msg, data)
            if msg_dict:
                log.debug('Adding %s to list of matched OS', dev_os)
                ret.append((dev_os, msg_dict))
            else:
                log.debug('No match found for %s', dev_os)
        if not ret:
            log.debug('Not matched any OS')
            ret.append((None, msg_dict))
        return ret

    def start(self):
        '''
        Take the messages from the queue,
        inspect and identify the operating system,
        then queue the message correspondingly.
        '''
        # metric counters
        napalm_logs_server_messages_received = Counter(
            "napalm_logs_server_messages_received",
            "Count of messages received from listener processes"
        )
        napalm_logs_server_messages_with_identified_os = Counter(
            "napalm_logs_server_messages_with_identified_os",
            "Count of messages with positive os identification",
            ['device_os']
        )
        napalm_logs_server_messages_without_identified_os = Counter(
            "napalm_logs_server_messages_without_identified_os",
            "Count of messages with negative os identification"
        )
        napalm_logs_server_messages_failed_device_queuing = Counter(
            "napalm_logs_server_messages_failed_device_queuing",
            "Count of messages per device os that fail to be queued to a device process",
            ['device_os']
        )
        napalm_logs_server_messages_device_queued = Counter(
            "napalm_logs_server_messages_device_queued",
            "Count of messages queued to device processes",
            ['device_os']
        )
        napalm_logs_server_messages_unknown_queued = Counter(
            "napalm_logs_server_messages_unknown_queued",
            "Count of messages queued as unknown"
        )
        self._setup_ipc()
        # Start suicide polling thread
        thread = threading.Thread(target=self._suicide_when_without_parent, args=(os.getppid(),))
        thread.start()
        signal.signal(signal.SIGTERM, self._exit_gracefully)
        self.__up = True
        while self.__up:
            # Take messages from the main queue
            try:
                bin_obj = self.sub.recv()
                msg, address = umsgpack.unpackb(bin_obj, use_list=False)
            except zmq.ZMQError as error:
                if self.__up is False:
                    log.info('Exiting on process shutdown')
                    return
                else:
                    log.error(error, exc_info=True)
                    raise NapalmLogsExit(error)
            if six.PY3:
                msg = str(msg, 'utf-8')
            else:
                msg = msg.encode('utf-8')
            log.debug('[%s] Dequeued message from %s: %s', address, msg, time.time())
            napalm_logs_server_messages_received.inc()
            os_list = self._identify_os(msg)

            for dev_os, msg_dict in os_list:
                if dev_os and dev_os in self.started_os_proc:
                    # Identified the OS and the corresponding process is started.
                    # Then send the message in the right queue
                    log.debug('Identified OS: %s', dev_os)
                    log.debug('Queueing message to %s', dev_os)
                    if six.PY3:
                        dev_os = bytes(dev_os, 'utf-8')
                    self.pub.send_multipart([dev_os,
                                             umsgpack.packb((msg_dict, address))])
                    # self.os_pipes[dev_os].send((msg_dict, address))
                    napalm_logs_server_messages_with_identified_os.labels(device_os=dev_os).inc()
                    napalm_logs_server_messages_device_queued.labels(device_os=dev_os).inc()

                elif dev_os and dev_os not in self.started_os_proc:
                    # Identified the OS, but the corresponding process does not seem to be started.
                    log.info('Unable to queue the message to %s. Is the sub-process started?', dev_os)
                    napalm_logs_server_messages_with_identified_os.labels(device_os=dev_os).inc()
                    napalm_logs_server_messages_failed_device_queuing.labels(device_os=dev_os).inc()

                elif not dev_os and self.opts['_server_send_unknown']:
                    # OS not identified, but the user requested to publish the message as-is
                    log.debug('Unable to identify the OS, sending directly to the publishers')
                    to_publish = {
                        'ip': address,
                        'host': 'unknown',
                        'timestamp': int(time.time()),
                        'message_details': msg_dict,
                        'os': UNKNOWN_DEVICE_NAME,
                        'error': 'UNKNOWN',
                        'model_name': 'unknown'
                    }
                    self.publisher_pub.send(umsgpack.packb(to_publish))
                    napalm_logs_server_messages_unknown_queued.inc()
                    napalm_logs_server_messages_without_identified_os.inc()

                elif not dev_os and not self.opts['_server_send_unknown']:
                    # OS not identified and we are told to do nothing
                    log.debug('Unable to identify the OS')
                    napalm_logs_server_messages_without_identified_os.inc()

    def stop(self):
        log.info('Stopping server process')
        self.__up = False
        self.sub.close()
        self.pub.close()
        self.ctx.term()
