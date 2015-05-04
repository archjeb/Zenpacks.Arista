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
# Arista switch modeler for Memory and filesystems

import logging
log = logging.getLogger('zen.Arista')

from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap



class AristaMemory(SnmpPlugin):
    relname = 'memory_subsystems'
    modname = 'ZenPacks.community.Arista.AristaMemory'
    snmpGetTableMaps = (
        GetTableMap('hrStorageEntry',
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
    )    

    def process(self, device, results, log):
        storagelist = results[1].get('hrStorageEntry',{})
        rm = self.relMap()
        for snmpindex, row in storagelist.items():
            name = row.get('hrStorageDescr')
            storagesize = row.get('hrStorageSize')
            storageunits = row.get('hrStorageAllocationUnits')
            storagetype = row.get('hrStorageType') 
            if not name:
                log.warn('ignore memory or storage  with no name')
                continue

            om = self.objectMap()
            #Sanitize name
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex.strip('.')
            om.arista_storage_alloc_units = storageunits
            if storagetype == '.1.3.6.1.2.1.25.2.1.2':
                om.arista_storage_type = 'RAM'
            elif storagetype == '.1.3.6.1.2.1.25.2.1.9':
                om.arista_storage_type = 'Flash' 
            elif storagetype == '.1.3.6.1.2.1.25.2.1.3':
                om.arista_storage_type = 'Virtual Memory'
            elif storagetype == '.1.3.6.1.2.1.25.2.1.5':
                om.arista_storage_type = 'Removable Disk'
            else:
                om.arista_storage_type = 'Unknown'
            om.arista_storage_size = storagesize
            rm.append(om)
  
        return rm
