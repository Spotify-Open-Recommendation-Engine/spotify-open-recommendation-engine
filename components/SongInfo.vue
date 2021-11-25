 <template>
    <h3>{{song}}</h3>
    <h5>{{ artist }}</h5>

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
