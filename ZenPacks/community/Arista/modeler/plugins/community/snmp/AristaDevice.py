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


import logging
log = logging.getLogger('zen.Arista')

from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap



class AristaDevice(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.2.1.47.1.1.1.1.11.1' : 'serialnumber',
        '.1.3.6.1.2.1.25.2.2.0' : 'hrMemorySize',
        '.1.3.6.1.2.1.47.1.1.1.1.10.1' : 'entPhysicalSoftwareRev',
        '.1.0.8802.1.1.2.1.3.2.0' : 'lldpLocChassisId',
        '.1.3.6.1.2.1.47.1.1.1.1.13.1' : 'entPhysicalModelName',
        })
    

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
                    }
        ),
        GetTableMap('hostresourceproc',
                    '.1.3.6.1.2.1.25.3.2.1',
                    {
                        '.1': 'hrDeviceIndex',
                        '.2': 'hrDeviceType',
                        '.3': 'hrDeviceDescr',
                        '.5': 'hrDeviceStatus',
                        '.5': 'hrStorageSize',
                        '.6': 'hrStorageUsed',
                    }
        ),
        GetTableMap('hostresourceprocload',
                    '.1.3.6.1.2.1.25.3.3.1',
                    {
                        '.2': 'hrProcessorLoad',
                    } 
        ),
    )    

    def process(self, device, results, log):
        import binascii
        log.info('Modeler %s processing data for device %s',self.name(), device.id)
        #Remember curls return blank value if serialnumber does not exist!
        #We need this because sometimes EOS instances like vEOS do not have a serial number
        #This will help prevent an exception from occuring and we just get a blank result
        #rm = self.relMap()
        the_serial=results[0].get('serialnumber', {})
        the_memory=results[0].get('hrMemorySize',{})
        the_version=results[0].get('entPhysicalSoftwareRev',{})
        the_model=results[0].get('entPhysicalModelName',{})
        #We curently don't use the model info in this Zenpack release. Its already done via Manufacture 
        # through GUI and in the objects.xml file. Putting this here for future use.
        the_system_mac=results[0].get('lldpLocChassisId',{})
        #Its a hex string that needs to be tweaked
        formatted_system_mac=':'.join(s.encode('hex') for s in binascii.hexlify(the_system_mac).decode('hex'))
        return self.objectMap({
            'arista_switch_serial': the_serial,
	    'arista_switch_memory': the_memory,
            'arista_switch_version': the_version,
            'arista_switch_model': the_model,
            'arista_switch_mac': formatted_system_mac,
            })
