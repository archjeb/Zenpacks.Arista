#Info interface for Arista Class

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from ZenPacks.community.Arista.interfaces import IAristaDeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.Arista.interfaces import (
    IAristaDeviceInfo,
    IAristaTemperatureInfo,
    IAristaCPUInfo,
    IAristaMemoryInfo,
    ) 

class AristaDeviceInfo(DeviceInfo):
    implements(IAristaDeviceInfo)
 
    arista_switch_serial = ProxyProperty('arista_switch_serial')
    arista_switch_memory = ProxyProperty('arista_switch_memory')
    arista_switch_version = ProxyProperty('arista_switch_version')
    arista_switch_mac = ProxyProperty('arista_switch_mac')

class AristaTemperatureInfo(ComponentInfo):
    implements(IAristaTemperatureInfo)

class AristaCPUInfo(ComponentInfo):
    implements(IAristaCPUInfo)


class AristaMemoryInfo(ComponentInfo):
    implements(IAristaMemoryInfo)

    arista_storage_type = ProxyProperty('arista_storage_type')
    arista_storage_alloc_units = ProxyProperty('arista_storage_alloc_units')
    arista_storage_size = ProxyProperty('arista_storage_size')
