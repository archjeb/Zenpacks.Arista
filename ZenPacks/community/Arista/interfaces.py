#Public Interface for Arista Device Class

from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.Zuul.interfaces.component import IComponentInfo
 
class IAristaDeviceInfo(IDeviceInfo):
    arista_switch_serial = schema.Int(title=_t('Serial Number of Switch'))
    arista_switch_memory = schema.Int(title=_t('Total Switch Memory'))
    arista_switch_version = schema.Int(title=_t('EOS Version'))
    arista_switch_mac = schema.Int(title=_t('System MAC Address'))


class IAristaTemperatureInfo(IComponentInfo):
    pass

class IAristaCPUInfo(IComponentInfo):
    pass

class IAristaMemoryInfo(IComponentInfo):
    arista_storage_type = schema.Int(title=_t('Storage Type'))
    arista_storage_alloc_units = schema.Int(title=_t('Storage Allocation Units'))
    arista_storage_size = schema.Int(title=_t('Size Size'))
