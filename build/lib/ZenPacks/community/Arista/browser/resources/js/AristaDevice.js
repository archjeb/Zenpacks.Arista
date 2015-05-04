Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        overview.removeField('memory');
        overview.removeField('locking');
 
        overview.addField({
        name: 'arista_switch_memory',
        fieldLabel: _t('Total Memory')});

    });
});



Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_idsummary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        overview.removeField('serialNumber');
        overview.addField({
         name: 'arista_switch_serial',
         fieldLabel: _t('Serial Number')});
        
        overview.addField({
        name: 'arista_switch_version',
        fieldLabel: _t('EOS Version')});
        overview.addField({
        name: 'arista_switch_mac',
        fieldLabel: _t('System MAC Address')});

    });
});


(function(){
var ZC = Ext.ns('Zenoss.component');
ZC.registerName(
    'AristaTemperatureSensor',
    _t('Switch Temperature Sensor'),
    _t('Switch Temperature Sensors'));


ZC.AristaTemperatureSensorPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'AristaTemperatureSensor',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.AristaTemperatureSensorPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('AristaTemperatureSensorPanel', ZC.AristaTemperatureSensorPanel);


ZC.registerName(
    'AristaCPU',
    _t('Switch CPU'),
    _t('Switch CPUs'));
ZC.AristaCPUPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'AristaCPU',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.AristaCPUPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('AristaCPUPanel', ZC.AristaCPUPanel);

ZC.registerName(
    'AristaMemory',
    _t('Switch Memory and Filesystem'),
    _t('Switch Memory and Filesystems'));

ZC.AristaMemoryPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'AristaMemory',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'arista_storage_type'},
                {name: 'arista_storage_size'},
                {name: 'arista_storage_alloc_units'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'arista_storage_type',
                dataIndex: 'arista_storage_type',
                header: _t('Storage Type'),
                sortable: true,
                width: 120
            },{
                id: 'arista_storage_size',
                dataIndex: 'arista_storage_size',
                header: _t('Storage Size'),
                sortable: true,
                width: 120
            },{
                id: 'arista_storage_alloc_units',
                dataIndex: 'arista_storage_alloc_units',
                header: _t('Allocation Units'),
                sortable: true,
                width: 120
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.AristaMemoryPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('AristaMemoryPanel', ZC.AristaMemoryPanel);

})();
