##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

# ZenPack Imports
from . import schema
from Products.ZenRelations.RelSchema import *


class AristaDevice(schema.AristaDevice):
    """
    Custom model code for AristaDevice class.  We need old relations
    to update existing instances such as object path
    """

    class_dynamicview_group = 'Devices'
    impacted_by = ['aristaCPUs', 'aristaMemorys', 'aristaTemperatures']

schema.AristaDevice._relations += (
    ('temperature_sensors', ToManyCont(ToOne,
     'ZenPacks.community.Arista.AristaTemperature', 'sensor_device', )),
    ('cpu_systems', ToManyCont(ToOne,
     'ZenPacks.community.Arista.AristaCPU', 'cpu_device', )),
    ('memory_subsystems', ToManyCont(ToOne,
     'ZenPacks.community.Arista.AristaMemory', 'memory_device', )),)
