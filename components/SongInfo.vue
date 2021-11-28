 <template>

  <div style="border-width:thick; border:solid; border-color:blue; border-radius: 15px 50px 30px 5px">
    <ul class="flex-container">
    <li>
      <container>
        <h1>{{song}}</h1>
        <h5 style="text-align:left">by</h5>
        <h5>{{ artist }}</h5>
      </container>
    </li>  
    <li>
      <FeatureAmount 
        feature="Tempo" 
        :value="tempo"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Key" 
        :value="scale_key"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Popularity" 
        :value="popularity"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Acousticness" 
        :value="acustic"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Dancability" 
        :value="dance"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Energy" 
        :value="energy"
      />
    </li>
  </ul>
</div>
</template>



<script>
import FeatureAmount from './FeatureAmount.vue'

export default { 
  props: {
    song: {required: true, type: String },
    artist: { required: true, type: String },
    tempo: { required: true, type: String },
    scale_key: { required: true, type: String },
    popularity: { required: true, type: String },
    acustic: { required: true, type: String },
    dance: { required: true, type: String },
    acusticness: { required: true, type: String },
    energy: { required: true, type: String },
    instrumentralness: { required: true, type: String },
    liveness: { required: true, type: String },
    speechiness: { required: true, type: String },
    valence: { required: true, type: String },
  },
  name: 'song-info',
  components: {
    FeatureAmount
  }
  
};

</script>

<style>
  .flex-container {
  /* We first create a flex layout context */
  display: flex;
  
  /* Then we define the flow direction 
     and if we allow the items to wrap 
   * Remember this is the same as:
   * flex-direction: row;
   * flex-wrap: wrap;
   */
  flex-flow: row wrap;
  
  /* Then we define how is distributed the remaining space */
  justify-content: space-around;
  
  padding: 0;
  margin: 0;
  list-style: none;
}

</style>

