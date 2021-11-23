<template>
  <div>
    <h5>{{ artist }}</h5>
    <h5>{{ album }}</h5>
    <h5>Tempo: {{ tempo }}</h5>
    <h5>Key: {{ key }}</h5>
    <h5>Popularity: {{ popularity }}</h5>
    <h5>Acousticness: {{ acustic }}</h5>
    <h5>Dancability: {{ dance }}</h5>
    <h5>Acousticness: {{ acusticness }}</h5>
    <h5>Energy: {{ energy }}</h5>
    <h5>Instrumentalness: {{ instrumentralness }}</h5>
    <h5>Liveness: {{Liveness }}</h5>
    <h5>Speechiness: {{ speechiness }}</h5>
    <h5>Valences: {{ valences }}</h5>
  </div>
</template>



<script>

export default {
  props: {
    artist: { required: true, type: String },
    ablum: { required: true, type: String },
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
  }
};

</script>

