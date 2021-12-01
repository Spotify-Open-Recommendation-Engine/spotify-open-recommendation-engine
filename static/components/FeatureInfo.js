const FeatureInfoComponent = Vue.component('feature-info', {
  name: 'feature-info',
  data() {
    return {
      val: this.value,
      ub: this.max,
    }
  },
  computed: {
    theta(){
      var frac;
      if(this.value < this.max){
        frac = this.value/this.max;
      } else{
        frac = (this.value-1)/this.max;
      }

      return frac * 2 * Math.PI;
    },

    path(){
      const large = this.theta > Math.PI;
      var arch = `M 0, -25 A 25, 25,0,${large ? 1 : 0},1,${this.endX},${this.endY}`;
      if(this.value == this.max){
        arch = arch +  `A 25, 25,0,0,1,0,-25`;
      }
      return arch;
    },

    endX(){
      
      return Math.cos(this.theta - Math.PI * 0.5) * 25;
    },

    endY(){
      return Math.sin(this.theta - Math.PI * 0.5) * 25;
    },

    cssVars () {
      return{
        /* variables you want to pass to css */
        '--val': this.val,
        '--ub': this.ub,
      }
    },
  },
  props: {
    value_text: {required: true, type: String },
    value: {required: true, type: String},
    feature: {required: true, type: String },
    max: {required: false, type: String},
  },
  template: '  <div style="display: flex;flex-direction: column;align-items: center;">' +
	'    <svg' +
	'      class="progress-ring"' +
	'      height="120"' +
	'      width="120"' +
	'      viewBox="-50 -50 100 100"' +
	'    >' +
	'      <circle cx="0" cy="0" r="25" fill="none" stroke="#e6e6e6" stroke-width="10"/>' +
	'      <path' +
	'        stroke="#8c67ef"' +
	'        stroke-width="10"' +
	'        fill="none"' +
	'        r="25"' +
	'        cx="60"' +
	'        cy="60"' +
	'        :d="path"' +
	'        transform="rotate(180)"' +
	'      />' +
	'      ' +
	'      <text text-anchor="middle" stroke="#000000" stroke-width="1px" dy=".3em">{{value_text}}</text>' +
	' ' +
	'    </svg>' +
	'    ' +
	'    {{feature}}' +
	'  </div>'
});