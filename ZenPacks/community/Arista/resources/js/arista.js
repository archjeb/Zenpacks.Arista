(function(){
    Ext.onReady(function() {
        var path = window.location.href;
        if (path.indexOf('/Devices/Arista/devices/') > 0){
            var DEVICE_OVERVIEW_SUMMARY = 'deviceoverviewpanel_summary';
            var DEVICE_OVERVIEW_IDSUMMARY = 'deviceoverviewpanel_idsummary';

            Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_IDSUMMARY, function(){
                var overview = Ext.getCmp(DEVICE_OVERVIEW_IDSUMMARY);
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

            Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_SUMMARY, function(){
                var overview = Ext.getCmp(DEVICE_OVERVIEW_SUMMARY);
                overview.removeField('memory');
                overview.removeField('locking');

                overview.addField({
                name: 'arista_switch_memory',
                fieldLabel: _t('Total Memory')});

            });
        }
    });
})();