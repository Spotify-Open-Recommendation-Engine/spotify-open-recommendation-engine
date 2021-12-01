const SongInfoComponent = Vue.component('song-info', {
  data () {
     // Your data here...
  },
  methods: {
     // Your methods here...
  },
  name: 'song-info',
  props: {
    tempo: { required: true, type: String },
    scale_key: { required: true, type: String },
    popularity: { required: true, type: String },
    dance: { required: true, type: String },
    acousticness: { required: true, type: String },
    energy: { required: true, type: String },
    instrumentalness: { required: true, type: String },
    liveness: { required: true, type: String },
    speechiness: { required: true, type: String },
    valence: { required: true, type: String },
  },
  template: '<div>' +
	'    <ul style="display: flex;flex-flow: row wrap;justify-content: space-around;padding: 0;margin: 0;list-style: none;"> ' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Tempo" ' +
	'        :value_text="tempo"' +
	'        :value="tempo"' +
	'        max="200"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Key" ' +
	'        :value_text="scale_key"' +
	'        value="100"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Popularity" ' +
	'        :value_text="popularity"' +
	'        :value="popularity"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Acousticness" ' +
	'        :value_text="acousticness"' +
	'        :value="acousticness"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Dancability" ' +
	'        :value_text="dance"' +
	'        :value="dance"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Energy" ' +
	'        :value_text="energy"' +
	'        :value="energy"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Instrumentalness" ' +
	'        :value_text="instrumentalness"' +
	'        :value="instrumentalness"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Speechiness" ' +
	'        :value_text="speechiness"' +
	'        :value="speechiness"' +
	'        max="100"' +
	'      />' +
	'    </li>' +
	'    <li>' +
	'      <feature-info ' +
	'        feature="Valence" ' +
	'        :value_text="valence"' +
	'        :value="valence"' +
	'        max="100"' +
	'      />' +
	'    </li>  ' +
	'  </ul>' +
	'</div>'
});