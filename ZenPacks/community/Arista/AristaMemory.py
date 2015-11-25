##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from . import schema
from Products.ZenRelations.RelSchema import *


class AristaMemory(schema.AristaMemory):
    """
    Custom model code for AristaMemory class.  We need old relations
    to update existing instances such as object path
    """

    class_dynamicview_group = 'Arista Memorys'
    impacts = ['aristaDevice', ]

schema.AristaMemory._relations += (
    ('memory_device', ToOne(ToManyCont,
     'ZenPacks.community.Arista.AristaDevice', 'memory_subsystems',)),)
