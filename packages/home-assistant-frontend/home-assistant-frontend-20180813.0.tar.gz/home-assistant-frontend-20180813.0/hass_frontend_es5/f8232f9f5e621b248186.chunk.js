(window.webpackJsonp=window.webpackJsonp||[]).push([[17],{614:function(e,n,t){"use strict";t.r(n),t(154),t(153),t(119),t(54),t(151),t(212),t(198),t(152),t(104);var a=t(0),o=t(3),i=(t(129),t(118),t(77)),r=t(13),l=function(){function e(e,n){for(var t=0;t<n.length;t++){var a=n[t];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}return function(n,t,a){return t&&e(n.prototype,t),a&&e(n,a),n}}(),p=function e(n,t,a){null===n&&(n=Function.prototype);var o=Object.getOwnPropertyDescriptor(n,t);if(void 0===o){var i=Object.getPrototypeOf(n);return null===i?void 0:e(i,t,a)}if("value"in o)return o.value;var r=o.get;return void 0!==r?r.call(a):void 0},s=Object.freeze(Object.defineProperties(["\n    <style include='ha-style'>\n      :host {\n        -ms-user-select: initial;\n        -webkit-user-select: initial;\n        -moz-user-select: initial;\n      }\n\n      .content {\n        padding: 16px;\n        max-width: 600px;\n        margin: 0 auto;\n      }\n\n      paper-card {\n        display: block;\n      }\n\n      paper-item {\n        cursor: pointer;\n      }\n\n      .empty {\n        text-align: center;\n        color: var(--secondary-text-color);\n      }\n\n      .header {\n        @apply --paper-font-title;\n      }\n\n      .row {\n        display: flex;\n       justify-content: space-between;\n      }\n      paper-dialog {\n        border-radius: 2px;\n      }\n      paper-dialog p {\n        color: var(--secondary-text-color);\n      }\n\n      #mp3dialog paper-icon-button {\n        float: right;\n      }\n\n      @media all and (max-width: 450px) {\n        paper-dialog {\n          margin: 0;\n          width: 100%;\n          max-height: calc(100% - 64px);\n\n          position: fixed !important;\n          bottom: 0px;\n          left: 0px;\n          right: 0px;\n          overflow: scroll;\n          border-bottom-left-radius: 0px;\n          border-bottom-right-radius: 0px;\n        }\n\n        .content {\n          width: auto;\n          padding: 0;\n        }\n      }\n\n      .tip {\n        color: var(--secondary-text-color);\n        font-size: 14px;\n      }\n      .date {\n        color: var(--primary-text-color);\n      }\n    </style>\n\n    <app-header-layout has-scrolling-region>\n      <app-header slot=\"header\" fixed>\n        <app-toolbar>\n          <ha-menu-button narrow='[[narrow]]' show-menu='[[showMenu]]'></ha-menu-button>\n          <div main-title>[[localize('panel.mailbox')]]</div>\n        </app-toolbar>\n      </app-header>\n      <div class='content'>\n        <paper-card>\n          <template is='dom-if' if='[[!_messages.length]]'>\n            <div class='card-content empty'>\n              [[localize('ui.panel.mailbox.empty')]]\n            </div>\n          </template>\n          <template is='dom-repeat' items='[[_messages]]'>\n            <paper-item on-click='openMP3Dialog'>\n              <paper-item-body style=\"width:100%\" two-line>\n                <div class=\"row\">\n                  <div>[[item.caller]]</div>\n                  <div class=\"tip\">[[localize('ui.duration.second', 'count', item.duration)]]</div>\n                </div>\n                <div secondary>\n                  <span class=\"date\">[[item.timestamp]]</span> - [[item.message]]\n                </div>\n              </paper-item-body>\n            </paper-item>\n          </template>\n        </paper-card>\n      </div>\n    </app-header-layout>\n\n    <paper-dialog with-backdrop id=\"mp3dialog\" on-iron-overlay-closed=\"_mp3Closed\">\n      <h2>\n        [[localize('ui.panel.mailbox.playback_title')]]\n        <paper-icon-button\n          on-click='openDeleteDialog'\n          icon='hass:delete'\n        ></paper-icon-button>\n      </h2>\n      <div id=\"transcribe\"></div>\n      <div>\n        <audio id=\"mp3\" preload=\"none\" controls> <source id=\"mp3src\" src=\"\" type=\"audio/mpeg\" /></audio>\n      </div>\n    </paper-dialog>\n\n    <paper-dialog with-backdrop id=\"confirmdel\">\n      <p>[[localize('ui.panel.mailbox.delete_prompt')]]</p>\n      <div class=\"buttons\">\n        <paper-button dialog-dismiss>[[localize('ui.common.cancel')]]</paper-button>\n        <paper-button dialog-confirm autofocus on-click=\"deleteSelected\">[[localize('ui.panel.mailbox.delete_button')]]</paper-button>\n      </div>\n    </paper-dialog>\n    "],{raw:{value:Object.freeze(["\n    <style include='ha-style'>\n      :host {\n        -ms-user-select: initial;\n        -webkit-user-select: initial;\n        -moz-user-select: initial;\n      }\n\n      .content {\n        padding: 16px;\n        max-width: 600px;\n        margin: 0 auto;\n      }\n\n      paper-card {\n        display: block;\n      }\n\n      paper-item {\n        cursor: pointer;\n      }\n\n      .empty {\n        text-align: center;\n        color: var(--secondary-text-color);\n      }\n\n      .header {\n        @apply --paper-font-title;\n      }\n\n      .row {\n        display: flex;\n       justify-content: space-between;\n      }\n      paper-dialog {\n        border-radius: 2px;\n      }\n      paper-dialog p {\n        color: var(--secondary-text-color);\n      }\n\n      #mp3dialog paper-icon-button {\n        float: right;\n      }\n\n      @media all and (max-width: 450px) {\n        paper-dialog {\n          margin: 0;\n          width: 100%;\n          max-height: calc(100% - 64px);\n\n          position: fixed !important;\n          bottom: 0px;\n          left: 0px;\n          right: 0px;\n          overflow: scroll;\n          border-bottom-left-radius: 0px;\n          border-bottom-right-radius: 0px;\n        }\n\n        .content {\n          width: auto;\n          padding: 0;\n        }\n      }\n\n      .tip {\n        color: var(--secondary-text-color);\n        font-size: 14px;\n      }\n      .date {\n        color: var(--primary-text-color);\n      }\n    </style>\n\n    <app-header-layout has-scrolling-region>\n      <app-header slot=\"header\" fixed>\n        <app-toolbar>\n          <ha-menu-button narrow='[[narrow]]' show-menu='[[showMenu]]'></ha-menu-button>\n          <div main-title>[[localize('panel.mailbox')]]</div>\n        </app-toolbar>\n      </app-header>\n      <div class='content'>\n        <paper-card>\n          <template is='dom-if' if='[[!_messages.length]]'>\n            <div class='card-content empty'>\n              [[localize('ui.panel.mailbox.empty')]]\n            </div>\n          </template>\n          <template is='dom-repeat' items='[[_messages]]'>\n            <paper-item on-click='openMP3Dialog'>\n              <paper-item-body style=\"width:100%\" two-line>\n                <div class=\"row\">\n                  <div>[[item.caller]]</div>\n                  <div class=\"tip\">[[localize('ui.duration.second', 'count', item.duration)]]</div>\n                </div>\n                <div secondary>\n                  <span class=\"date\">[[item.timestamp]]</span> - [[item.message]]\n                </div>\n              </paper-item-body>\n            </paper-item>\n          </template>\n        </paper-card>\n      </div>\n    </app-header-layout>\n\n    <paper-dialog with-backdrop id=\"mp3dialog\" on-iron-overlay-closed=\"_mp3Closed\">\n      <h2>\n        [[localize('ui.panel.mailbox.playback_title')]]\n        <paper-icon-button\n          on-click='openDeleteDialog'\n          icon='hass:delete'\n        ></paper-icon-button>\n      </h2>\n      <div id=\"transcribe\"></div>\n      <div>\n        <audio id=\"mp3\" preload=\"none\" controls> <source id=\"mp3src\" src=\"\" type=\"audio/mpeg\" /></audio>\n      </div>\n    </paper-dialog>\n\n    <paper-dialog with-backdrop id=\"confirmdel\">\n      <p>[[localize('ui.panel.mailbox.delete_prompt')]]</p>\n      <div class=\"buttons\">\n        <paper-button dialog-dismiss>[[localize('ui.common.cancel')]]</paper-button>\n        <paper-button dialog-confirm autofocus on-click=\"deleteSelected\">[[localize('ui.panel.mailbox.delete_button')]]</paper-button>\n      </div>\n    </paper-dialog>\n    "])}})),c=function(e){function n(){return function(e,t){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this),function(e,n){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!n||"object"!=typeof n&&"function"!=typeof n?e:n}(this,(n.__proto__||Object.getPrototypeOf(n)).apply(this,arguments))}return function(e,n){if("function"!=typeof n&&null!==n)throw new TypeError("Super expression must either be null or a function, not "+typeof n);e.prototype=Object.create(n&&n.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),n&&(Object.setPrototypeOf?Object.setPrototypeOf(e,n):e.__proto__=n)}(n,Object(r.a)(o.a)),l(n,[{key:"connectedCallback",value:function(){p(n.prototype.__proto__||Object.getPrototypeOf(n.prototype),"connectedCallback",this).call(this),this.hassChanged=this.hassChanged.bind(this),this.hass.connection.subscribeEvents(this.hassChanged,"mailbox_updated").then(function(e){this._unsubEvents=e}.bind(this)),this.computePlatforms().then(function(e){this.platforms=e,this.hassChanged()}.bind(this))}},{key:"disconnectedCallback",value:function(){p(n.prototype.__proto__||Object.getPrototypeOf(n.prototype),"disconnectedCallback",this).call(this),this._unsubEvents&&this._unsubEvents()}},{key:"hassChanged",value:function(){this._messages||(this._messages=[]),this.getMessages().then(function(e){this._messages=e}.bind(this))}},{key:"openMP3Dialog",value:function(e){var n=e.model.item.platform;this.currentMessage=e.model.item,this.$.mp3dialog.open(),this.$.mp3src.src="/api/mailbox/media/"+n+"/"+e.model.item.sha,this.$.transcribe.innerText=e.model.item.message,this.$.mp3.load(),this.$.mp3.play()}},{key:"_mp3Closed",value:function(){this.$.mp3.pause()}},{key:"openDeleteDialog",value:function(){this.$.confirmdel.open()}},{key:"deleteSelected",value:function(){var e=this.currentMessage;this.hass.callApi("DELETE","mailbox/delete/"+e.platform+"/"+e.sha),this.$.mp3dialog.close()}},{key:"getMessages",value:function(){var e=this.platforms.map(function(e){return this.hass.callApi("GET","mailbox/messages/"+e).then(function(n){for(var t=[],a=n.length,o=0;o<a;o++){var r=Object(i.a)(new Date(1e3*n[o].info.origtime));t.push({timestamp:r,caller:n[o].info.callerid,message:n[o].text,sha:n[o].sha,duration:n[o].info.duration,platform:e})}return t})}.bind(this));return Promise.all(e).then(function(n){for(var t=e.length,a=[],o=0;o<t;o++)a=a.concat(n[o]);return a.sort(function(e,n){return new Date(n.timestamp)-new Date(e.timestamp)}),a})}},{key:"computePlatforms",value:function(){return this.hass.callApi("GET","mailbox/platforms")}}],[{key:"template",get:function(){return Object(a.a)(s)}},{key:"properties",get:function(){return{hass:{type:Object},narrow:{type:Boolean,value:!1},showMenu:{type:Boolean,value:!1},platforms:{type:Array},_messages:{type:Array},currentMessage:{type:Object}}}}]),n}();customElements.define("ha-panel-mailbox",c)}}]);
//# sourceMappingURL=f8232f9f5e621b248186.chunk.js.map