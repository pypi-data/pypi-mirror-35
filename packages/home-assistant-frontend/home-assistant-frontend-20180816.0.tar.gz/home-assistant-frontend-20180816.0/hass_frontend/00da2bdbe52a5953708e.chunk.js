(window.webpackJsonp=window.webpackJsonp||[]).push([[18],{615:function(e,a,l){"use strict";l.r(a),l(119);var t=l(0),o=l(3);l(129),l(118),customElements.define("ha-panel-iframe",class extends o.a{static get template(){return t["a"]`
    <style include='ha-style'>
      iframe {
        border: 0;
        width: 100%;
        height: calc(100% - 64px);
      }
    </style>
    <app-toolbar>
      <ha-menu-button narrow='[[narrow]]' show-menu='[[showMenu]]'></ha-menu-button>
      <div main-title>[[panel.title]]</div>
    </app-toolbar>

    <iframe
      src='[[panel.config.url]]'
      sandbox="allow-forms allow-popups allow-pointer-lock allow-same-origin allow-scripts"
      allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"
    ></iframe>
    `}static get properties(){return{panel:{type:Object},narrow:{type:Boolean},showMenu:{type:Boolean}}}})}}]);
//# sourceMappingURL=00da2bdbe52a5953708e.chunk.js.map