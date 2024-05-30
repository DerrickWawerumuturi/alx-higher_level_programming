const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.ajax(url,
    {
        success: function(data, status, xhr) {
            $('#hello').text(data.hello)
    }
})