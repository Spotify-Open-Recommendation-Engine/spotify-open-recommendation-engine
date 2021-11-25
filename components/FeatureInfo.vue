 <template>
    <h3>{{song}}</h3>
    <h5>{{ artist }}</h5>

  <ul class="flex-container">
  <li>
    <FeatureAmount 
      feature="Tempo" 
      :value="tempo"
    />
  </li>
  <li>
    <FeatureAmount 
      feature="Key" 
      :value="key"
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

</template>



<script>
import FeatureAmount from './FeatureAmount.vue'

export default { 
  props: {
    song: {required: true, type: String },
    artist: { required: true, type: String },
    tempo: { required: true, type: String },
    key: { required: true, type: String },
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



<!--

  <FeatureAmount 
      feature="Tempo" 
      :value="tempo"
    />
    <FeatureAmount 
      feature="Key" 
      :value="key"
    />    
    <FeatureAmount 
      feature="Popularity" 
      :value="popularity"
    />
    <FeatureAmount 
      feature="Acousticness" 
      :value="acustic"
    />
    <FeatureAmount 
      feature="Dancability" 
      :value="dance"
    />
    <FeatureAmount 
      feature="Energy" 
      :value="energy"
    />
    <FeatureAmount 
      feature="Instrumentalness" 
      :value="instrumentralness"
    />
    <FeatureAmount 
      feature="Speechiness" 
      :value="speechiness"
    />
    <FeatureAmount 
      feature="Valences" 
      :value="valence"
    />


-->