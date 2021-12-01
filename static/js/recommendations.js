// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};


// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = (app) => {

    // This is the Vue data.
    app.data = {
        valid_genres: ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop', 'turkish', 'work-out', 'world-music'],
        genres: [],
        enabled_filters: [],
        filters: {
		    tempo: [20, 300],
		    key: [1, 12],
		    popularity: [0, 100],
		    acousticness: [0, 1],
		    danceability: [0, 1],
		    energy: [0, 1],
		    instrumentalness: [0, 1],
		    liveness: [0, 1],
		    loudness: [0, 1],
		    speechiness: [0, 1],
		    valence: [0, 1]
        },
        recommendations: [],
        limit: 10,
        not_found: false,
        show_recommendation_modal: false,
        playlist_name: '',
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => {e._idx = k++;});
        return a;
    };


    app.methods = {
        filters_changed: function() {
            app.data.not_found = false;
        },
        int_to_music_key: function(val) {
            let keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            return keys[val];
        },
        generate: function () {
            let recs_endpoint = document.location.origin + "/spotify-open-recommendation-engine/recs"
            let genre_string = ""
            for(const genre of this.genres) {
                genre_string += genre + ",";
            }
            genre_string = genre_string.slice(0, -1);
            recs_endpoint += "?sgenres=" + genre_string + "&";
            for(const [parameter, range] of Object.entries(app.data.filters)) {
                if(!app.data.enabled_filters.includes(parameter)) continue;
                recs_endpoint += parameter + "=" + range[0] + "," + range[1] + "&";
            }
            recs_endpoint = recs_endpoint.slice(0, -1);
            app.data.recommendations = [];
            app.data.show_recommendation_modal = true;
            fetch(recs_endpoint)
            .then(response => response.json())
            .then(data => {
                if(data.tracks.length == 0) {
                    app.data.not_found = true;
                    app.data.show_recommendation_modal = false;
                } else {
                    app.data.recommendations = data.tracks;
                    app.data.recommendations.forEach(element => {
                        element.include_in_playlist = true;
                    });
                    app.data.playlist_name = '';
                }
            });
        },
        make_playlist: function() {   
            playlist_tracks = [];
            app.data.recommendations.forEach(element => {
                if(element.include_in_playlist) {
                    playlist_tracks.push(element.id);
                }
            });
            if(playlist_tracks.length == 0) {
                app.data.show_recommendation_modal = false;
            } else {
                playlist_name = app.data.playlist_name === '' ? 'My New Recommendations!' : app.data.playlist_name;
                fetch(document.location.origin + "/spotify-open-recommendation-engine/create_playlist?songs=" + playlist_tracks.join(",") + "&name=" + playlist_name).then(response => response.text()).then(data => {
                    window.open("https://open.spotify.com/playlist/" + data, '_blank');
                });
            }
        },
        open_in_spotify: function(id) {
            window.open("https://open.spotify.com/track/" + id, '_blank');
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