#Grab SNMP data for device level info

import logging
log = logging.getLogger('zen.Arista')

from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap



class Arista(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.2.1.47.1.1.1.1.11.1' : 'serialnumber',
        '.1.3.6.1.2.1.25.2.2.0' : 'hrMemorySize',
        '.1.3.6.1.2.1.47.1.1.1.1.10.1' : 'entPhysicalSoftwareRev',
        '.1.0.8802.1.1.2.1.3.2.0' : 'lldpLocChassisId',
        '.1.3.6.1.2.1.47.1.1.1.1.13.1' : 'entPhysicalModelName',
        })
     

    def process(self, device, results, log):
        import binascii
        log.info('Modeler %s processing data for device %s',self.name(), device.id)
        #Remember curls return blank value if serialnumber does not exist!
        #We need this because sometimes EOS instances like vEOS do not have a serial number
        #This will help prevent an exception from occuring and we just get a blank result
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
