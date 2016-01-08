#
# Copyright (c) 2015, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#  - Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#  - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#  - Neither the name of Arista Networks nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#
#    Version 0.7.0  - 4/29/2015
#    Written by:
#       Jeremy Georges - Arista Networks
#       jgeorges@arista.com
#
#    Revision history:
#       0.7.0 - initial release
#

#Device modeler for Arista Switches


import binascii
import logging
from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

log = logging.getLogger('zen.Arista')


class AristaDevice(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.2.1.47.1.1.1.1.11.1': 'serialnumber',
        '.1.3.6.1.2.1.25.2.2.0': 'hrMemorySize',
        '.1.3.6.1.2.1.47.1.1.1.1.10.1': 'entPhysicalSoftwareRev',
        '.1.0.8802.1.1.2.1.3.2.0': 'lldpLocChassisId',
        '.1.3.6.1.2.1.47.1.1.1.1.13.1': 'entPhysicalModelName'})

    snmpGetTableMaps = (
        GetTableMap('hostresourcestorage',
                    '.1.3.6.1.2.1.25.2.3.1',
                    {
                        '.1': 'hrStorageIndex',
                        '.2': 'hrStorageType',
                        '.3': 'hrStorageDescr',
                        '.4': 'hrStorageAllocationUnits',
                        '.5': 'hrStorageSize',
                        '.6': 'hrStorageUsed',
                    }),
        GetTableMap('hostresourceproc',
                    '.1.3.6.1.2.1.25.3.2.1',
                    {
                        '.1': 'hrDeviceIndex',
                        '.2': 'hrDeviceType',
                        '.3': 'hrDeviceDescr',
                        '.5': 'hrDeviceStatus',
                        '.5': 'hrStorageSize',
                        '.6': 'hrStorageUsed',
                    }),
        GetTableMap('hostresourceprocload',
                    '.1.3.6.1.2.1.25.3.3.1',
                    {
                        '.2': 'hrProcessorLoad',
                    }),
    )

    def process(self, device, results, log):

        log.info('Modeler {} processing data for device {}'.format(
                 self.name(), device.id))
        model = results[0].get('entPhysicalModelName', {})
        serial = results[0].get('serialnumber', {})
        memory = results[0].get('hrMemorySize', {})
        version = results[0].get('entPhysicalSoftwareRev', {})
        system_mac = results[0].get('lldpLocChassisId', {})

        try:
            formatted_system_mac = ':'.join(s.encode('hex')
                                            for s in binascii.hexlify(
                                                system_mac).decode('hex'))
        except TypeError:
            formatted_system_mac = None

        om = self.objectMap({
            'arista_switch_model': model,
            'arista_switch_serial': serial,
            'arista_switch_version': version,
            'arista_switch_memory': memory,
            'arista_switch_mac': formatted_system_mac})

        return om
