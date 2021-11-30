<template>
  <div class="d-flex flex-column align-items-center">
    <svg
      class="progress-ring"
      height="120"
      width="120"
      viewBox="-50 -50 100 100"
    >
      <circle cx="0" cy="0" r="40" fill="none" stroke="#e6e6e6" stroke-width="10"/>
      <path
        stroke="#8c67ef"
        stroke-width="10"
        fill="none"
        r="40"
        cx="60"
        cy="60"
        :d="path"
        transform="rotate(180)"
      />
      
      <text text-anchor="middle" stroke="#000000" stroke-width="1px" dy=".3em">{{value_text}}</text>
 
    </svg>
    
    {{feature}}
  </div>
</template>

<script>
  export default {
    name: 'feature-amount',
    props: {
      value_text: {required: true, type: String },
      value: {required: true, type: String},
      feature: {required: true, type: String },
      max: {required: false, type: String},
    },
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
        var arch = `M 0, -40 A 40, 40,0,${large ? 1 : 0},1,${this.endX},${this.endY}`;
        if(this.value == this.max){
          arch = arch +  `A 40, 40,0,0,1,0,-40`;
        }
        return arch;
      },

      endX(){
        
        return Math.cos(this.theta - Math.PI * 0.5) * 40;
      },

      endY(){
        return Math.sin(this.theta - Math.PI * 0.5) * 40;
      },

      cssVars () {
        return{
          /* variables you want to pass to css */
          '--val': this.val,
          '--ub': this.ub,
        }
      },
    }
  };
</script>


<style css="Buefy">


  .d-flex {
  display: flex;
}

.flex-column {
  flex-direction: column;
}

.align-items-center {
      align-items: center;
}


</style>


