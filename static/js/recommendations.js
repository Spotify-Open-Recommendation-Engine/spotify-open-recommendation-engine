// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};


// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = (app) => {

    // This is the Vue data.
    app.data = {
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
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => {e._idx = k++;});
        return a;
    };


    // This contains all the methods.
    app.methods = {
        // Complete as you see fit.
    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    // And this initializes it.
    app.init = () => {
        // Put here any initialization code.
        // Typically this is a server GET call to load the data.
    };

    app.init();
};

init(app);