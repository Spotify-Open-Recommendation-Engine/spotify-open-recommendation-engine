<template>
  <div class="d-flex flex-column align-items-center">
    <svg
      class="progress-ring"
      height="120"
      width="120"
    >
      <circle
        class="progess-ring__circle"
        stroke="blue"
        stroke-width="10"
        fill="transparent"
        r="52"
        cx="60"
        cy="60"
      >
      
      </circle
      ><text x="50%" y="50%" text-anchor="middle" stroke="#000000" stroke-width="2px" dy=".3em">{{value}}</text>
    </svg>
    
    {{feature}}
  </div>
</template>

<script>
  export default {
    name: 'feature-amount',
    props: {
      value: {required: true, type: String },
      feature: {required: true, type: String },
    }
  };
</script>

<style>
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




