(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{608:function(t,e,a){"use strict";a.r(e),a(150);var o=a(0),s=a(3),i=a(53),r=a(13);a(118),customElements.define("ha-store-auth-card",class extends(Object(r.a)(s.a)){static get template(){return o["a"]`
      <style include='ha-style'>
        paper-card {
          position: fixed;
          padding: 8px 0;
          bottom: 16px;
          right: 16px;
        }

        .card-actions {
          text-align: right;
          border-top: 0;
          margin-right: -4px;
        }

        :host(.small) paper-card {
          bottom: 0;
          left: 0;
          right: 0;
        }
      </style>
      <paper-card elevation="4">
        <div class='card-content'>
          [[localize('ui.auth_store.ask')]]
        </div>
        <div class='card-actions'>
          <paper-button on-click='_done'>[[localize('ui.auth_store.decline')]]</paper-button>
          <paper-button primary on-click='_save'>[[localize('ui.auth_store.confirm')]]</paper-button>
        </div>
      </paper-card>
    `}static get properties(){return{hass:Object}}ready(){super.ready(),this.classList.toggle("small",window.innerWidth<600)}_save(){Object(i.b)(),this._done()}_done(){const t=this.shadowRoot.querySelector("paper-card");t.style.transition="bottom .25s",t.style.bottom=`-${t.offsetHeight+8}px`,setTimeout(()=>this.parentNode.removeChild(this),300)}})}}]);
//# sourceMappingURL=cd80dbc553cbe7d3b3c2.chunk.js.map