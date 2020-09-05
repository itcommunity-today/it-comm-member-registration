odoo.define('custom_auth_signup.signup', function (require) {
'use strict';
    var core = require('web.core');
    var wUtils = require('website.utils');
    var publicWidget = require('web.public.widget');
    var _t = core._t;
    publicWidget.registry.websiteSignupForm = publicWidget.Widget.extend({
        selector: '.oe_website_login_container',
        events: {
            'change #company_type': '_showHideSelectionField',
        },

        start: function () {
            return this._super.apply(this, arguments);
        },
        _showHideSelectionField: function(evt){
            evt.preventDefault();
            var self = this;
            var value = $(evt.currentTarget).val();
            if (value == 'person'){
                $('.field-grade').hide();
            }else{
                $('.field-grade').show();
            }
        },
    });        
});
