$(document).ready(function(){
    let resp = $("#messageForm").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "api/v1/message/",
            // headers: {
            //     'X-CSRFToken': getCookie('csrftoken')
            // },
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                message: $("textarea[name='message']").val()
            },
            success: function(data){
                alert("Message sent");
            },
            error: function(data){
                alert("Error");
            }
        });
    });


    $("#LogoutForm").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "api/v1/logout/",
            data: {},
            success: function(data){
                window.location.reload();
            }
        });
    });

    $("#getToken").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "api/v1/token/",
            data: {},
            success: function(data){
                window.location.reload();
            }
        });
    });
});