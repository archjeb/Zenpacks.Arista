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
#Device Class Definition and device attributes for Arista Products

from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
 
class AristaDevice(Device):
    arista_switch_serial = None
    arista_switch_memory = None
    arista_switch_version = None
    arista_switch_mac = None
    arista_switch_model = None
 
    _properties = Device._properties + (
        {'id': 'arista_switch_serial', 'type': 'string'},
        {'id': 'arista_switch_memory', 'type': 'string'},
        {'id': 'arista_switch_version', 'type': 'string'},
        {'id': 'arista_switch_mac', 'type': 'string'},
        {'id': 'arista_switch_model', 'type': 'string'},
        )
    _relations = Device._relations + (
    ('temperature_sensors', ToManyCont(ToOne, 'ZenPacks.community.Arista.AristaTemperature', 'sensor_device', )),
    ('cpu_systems', ToManyCont(ToOne, 'ZenPacks.community.Arista.AristaCPU', 'cpu_device', )),
    ('memory_subsystems', ToManyCont(ToOne, 'ZenPacks.community.Arista.AristaMemory', 'memory_device', )),
    )
 
