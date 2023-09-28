$(document).ready(function() {
    $('#registerForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/api/v1/register/",
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                login: $('input[name=login]').val(),
                password: $('input[name=password]').val(),
                name: $('input[name=password]').val(),
                from_site: true
            },
            success: function(response)
            {
                console.log(response);
                if (response.info == 'success') {
                    window.location.href = "/";
                } else {
                    alert(response);
                }
            },
            error: function(response)
            {
                alert("User with this login already exists");
            }
        });
    });
});