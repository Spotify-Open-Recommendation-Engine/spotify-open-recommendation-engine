 <template>

  <div style="border-width:thick; border:solid; border-color:#8c67ef; border-radius: 15px 50px 30px 5px">
    <ul class="flex-container"> 
    <li>
      <FeatureAmount 
        feature="Tempo" 
        :value_text="tempo"
        :value="tempo"
        max="200"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Key" 
        :value_text="scale_key"
        value="100"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Popularity" 
        :value_text="popularity"
        :value="popularity"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Acousticness" 
        :value_text="acustic"
        :value="acustic"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Dancability" 
        :value_text="dance"
        :value="dance"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Energy" 
        :value_text="energy"
        :value="energy"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Instrumentalness" 
        :value_text="instrumentalness"
        :value="instrumentalness"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Speechiness" 
        :value_text="speechiness"
        :value="speechiness"
        max="100"
      />
    </li>
    <li>
      <FeatureAmount 
        feature="Valence" 
        :value_text="valence"
        :value="valence"
        max="100"
      />
    </li>  
  </ul>
</div>
</template>



<script>
import FeatureAmount from './FeatureAmount.vue'

export default { 
  props: {
    tempo: { required: true, type: String },
    scale_key: { required: true, type: String },
    popularity: { required: true, type: String },
    acustic: { required: true, type: String },
    dance: { required: true, type: String },
    acusticness: { required: true, type: String },
    energy: { required: true, type: String },
    instrumentalness: { required: true, type: String },
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

