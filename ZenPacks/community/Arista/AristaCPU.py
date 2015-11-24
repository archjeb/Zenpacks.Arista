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


class AristaCPU(schema.AristaCPU):
    """Custom model code for AristaCPU class."""

    class_dynamicview_group = 'Arista CPUs'
    impacts = ['aristaDevice', ]

schema.AristaCPU._relations += (
    ('cpu_device', ToOne(ToManyCont,
     'ZenPacks.community.Arista.AristaDevice', 'cpu_systems',)),)
