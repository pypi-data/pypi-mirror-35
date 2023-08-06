"""
   Copyright 2018 Globo.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import logging
from datetime import datetime

from pyzabbix import ZabbixMetric
from pyzabbix import ZabbixSender

from globomap_monitoring.settings import ZBX_PASSIVE_MONITOR
from globomap_monitoring.settings import ZBX_PASSIVE_PORT
from globomap_monitoring.settings import ZBX_PASSIVE_SERVER

LOGGER = logging.getLogger(__name__)


def send(monitor=None):
    monitor = monitor if monitor else ZBX_PASSIVE_MONITOR
    if not ZBX_PASSIVE_SERVER or not ZBX_PASSIVE_PORT or not monitor:
        LOGGER.error('Settings insufficient to passive monitoring')
        return

    zabbix_server = ZabbixSender(zabbix_server=ZBX_PASSIVE_SERVER,
                                 zabbix_port=int(ZBX_PASSIVE_PORT),
                                 chunk_size=2)

    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Creates the message
    passive_message_status = ZabbixMetric(ZBX_PASSIVE_MONITOR,
                                          'passive_message',
                                          'Working - {0}'.format(time_now))

    # Creates the status (0 - OK; 1 - Warning; 2 - Critical)
    passive_monitor_status = ZabbixMetric(ZBX_PASSIVE_MONITOR,
                                          'passive_check', 0)

    metrics = [passive_message_status, passive_monitor_status]
    result = zabbix_server.send(metrics)

    try:
        if result.failed == 0:
            LOGGER.info('Passive monitoring sent with success.')
            LOGGER.debug(result)
        else:
            LOGGER.error('Fail to sent Passive monitoring.')
    except AttributeError:
        LOGGER.error('Fail to verify return of Passive monitoring.')
