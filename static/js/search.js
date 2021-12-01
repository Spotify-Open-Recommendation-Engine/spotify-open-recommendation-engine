// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};


// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = (app) => {

    // This is the Vue data.
    app.data = {
        search_query: '',
        loading_search: false,
        results: [],
        feature_cache: {}
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => {e._idx = k++;});
        return a;
    };

    app.methods = {
        search: function() {
            app.data.loading_search = true;
            let search_endpoint = document.location.origin + "/spotify-open-recommendation-engine/sp_search"
            let features_endpoint = document.location.origin + "/spotify-open-recommendation-engine/song_features"
            fetch(search_endpoint + "?q=" + app.data.search_query)
                .then(response => response.json())
                .then(data => {
                    for(let i=0;i<data.length;i++) {
                        if(data[i].track_id in app.data.feature_cache) {
                            data[i].features = app.data.feature_cache[data[i].track_id];
                            data[i].has_features = true;
                        } else {
                            data[i].has_features = false;
                        }
                    }
                    app.data.results = data;
                    app.data.loading_search = false;
                    for(let i=0;i<app.data.results.length;i++) {
                        if(app.data.results[i].track_id in app.data.feature_cache) {
                            app.data.results[i].features = app.data.feature_cache[app.data.results[i].track_id];
                        }
                        if(!("features" in app.data.results[i])) {
                            let track_index = i;
                            fetch(features_endpoint + "?tid=" + app.data.results[track_index].track_id)
                                .then(response => response.json())
                                .then(features_data => {
                                    app.data.feature_cache[app.data.results[track_index].track_id] = features_data;
                                    app.data.results[track_index].features = features_data;
                                    app.data.results[track_index].has_features = true;
                                });
                        }
                    }
                });

        },
        int_to_music_key: function(val) {
            let keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            return keys[val];
            //convert spotify key to music key
            
        },
        open_in_spotify: function(id) {
            window.open("https://open.spotify.com/track/" + id, '_blank');
        },
        format_percent: function(val) {
            return (val * 100).toFixed(0);
        }
    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    // And this initializes it.
    app.init = () => { };

    app.init();
};

init(app);