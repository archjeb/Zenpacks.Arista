##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from zope.interface import implements
from zope.component import adapts

from Products.Zuul.interfaces import IReportable
from ZenPacks.zenoss.ZenETL.reportable import\
    (DEFAULT_STRING_LENGTH, DeviceReportable, BaseReportable)
from .AristaDevice import AristaDevice
from .AristaCPU import AristaCPU
from .AristaMemory import AristaMemory
from .AristaTemperature import AristaTemperature


class AristaDeviceReportable(DeviceReportable):
    adapts(AristaDevice)
    implements(IReportable)

    def reportProperties(self):

        result = super(AristaDeviceReportable, self).reportProperties()
        result.append(('arista_switch_serial', 'string',
                       self.context.arista_switch_serial, DEFAULT_STRING_LENGTH))
        result.append(('arista_switch_memory', 'string',
                       self.context.arista_switch_memory, DEFAULT_STRING_LENGTH))
        result.append(('arista_switch_version', 'string',
                       self.context.arista_switch_version, DEFAULT_STRING_LENGTH))
        result.append(('arista_switch_mac', 'string',
                       self.context.arista_switch_mac, DEFAULT_STRING_LENGTH))
        result.append(('arista_switch_model', 'string',
                       self.context.arista_switch_model, DEFAULT_STRING_LENGTH))
        return result


class AristaCPUReportable(BaseReportable):
    adapts(AristaCPU)
    implements(IReportable)

    def reportProperties(self):
        eclass = self.entity_class_name
        for entry in super(AristaCPUReportable, self).reportProperties():
            yield entry
        yield (eclass + '_name', 'string', self.context.titleOrId(),
               DEFAULT_STRING_LENGTH)


class AristaMemoryReportable(BaseReportable):
    adapts(AristaMemory)
    implements(IReportable)

    def reportProperties(self):
        eclass = self.entity_class_name
        for entry in super(AristaMemoryReportable, self).reportProperties():
            yield entry
        yield (eclass + '_name', 'string', self.context.titleOrId(),
               DEFAULT_STRING_LENGTH)


class AristaTemperatureReportable(BaseReportable):
    adapts(AristaTemperature)
    implements(IReportable)

    def reportProperties(self):
        eclass = self.entity_class_name
        for entry in super(AristaTemperatureReportable, self).reportProperties():
            yield entry
        yield (eclass + '_name', 'string', self.context.titleOrId(),
               DEFAULT_STRING_LENGTH)
