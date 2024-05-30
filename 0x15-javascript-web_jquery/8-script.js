const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const name  = [];

$.ajax(url, {
    success: function (data, status, xhr) {
        const movies =  data.results;
        movies.forEach(movie => {
            $('UL#list_movies').append('<li>' + movie.title + '</li>');
        });   
}})