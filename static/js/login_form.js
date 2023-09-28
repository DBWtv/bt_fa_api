$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "api/v1/login/",
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                login: $('input[name=login]').val(),
                password: $('input[name=password]').val(),
                from_site: true
            },
            success: function(response)
            {
                console.log(response);
                if (response.message == 'Authentication successful') {
                    window.location.reload()
                } else {
                    alert(response);
                }
            }
        });
    });
});