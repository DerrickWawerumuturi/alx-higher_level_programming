const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.ajax(URL, {
    success: function (data, status, xhr) {
        console.log(data);
        $('#character').text(data.name)
    }
})