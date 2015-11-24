##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
import logging
from zope.event import notify
from Products.Zuul.catalog.events import IndexingEvent
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPackMigration


log = logging.getLogger("zen.migrate")


class UpdateRelations(ZenPackMigration):
    """
    Update relations for NetAppInterface component
    """
    version = Version(0, 7, 0)


    def migrate(self, pack):
        _log = logging.getLogger('Zope.ZCatalog')
        _log.setLevel(logging.FATAL)
        log.info(
            "Update relations for /Arista devices"
        )

        dc = pack.dmd.Devices.getOrganizer('/Arista')
        for dev in dc.getDevices():

            log.info('Update relations for {0}'.format(dev.name()))
            dev.buildRelations()
            components = {'cpus': [], 'memorys': [], 'temperatures': []}

            # component AristaCPU
            for cpu in dev.cpu_systems():
                log.info('Remove old relation for {0} in {1}'.format(
                    cpu.name(), dev.name()))
                dev.cpu_systems._delObject(cpu.id)
                components['cpus'].append(cpu)

            # component AristaMemory
            for memory in dev.memory_subsystems():
                log.info('Remove old relation for {0} in {1}'.format(
                    memory.name(), dev.name()))
                dev.memory_subsystems._delObject(memory.id)
                components['memorys'].append(memory)

            # component AristaTemperature
            for temperature in dev.temperature_sensors():
                log.info('Remove old relation for {0} in {1}'.format(
                    temperature.name(), dev.name()))
                dev.temperature_sensors._delObject(temperature.id)
                components['temperatures'].append(temperature)

            for key, values in components.items():
                for obj in values:
                    log.info('Add new relation for {0} in {1}'.format(obj.name(),
                                                                      dev.name()))
                    obj.buildRelations()
                    if key == 'cpus':
                        dev.aristaCPUs._setObject(obj.id, obj)
                    elif key == 'memorys':
                        dev.aristaMemorys._setObject(obj.id, obj)
                    elif key == 'temperatures':
                        dev.aristaTemperatures._setObject(obj.id, obj)
                    obj.index_object()

            dev.index_object()

            # indexing devices and components for impact after updating
            notify(IndexingEvent(dev))
            for component in dev.getDeviceComponents():
                notify(IndexingEvent(component))

UpdateRelations()
