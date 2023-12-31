$(document).ready(function(){
    $("#LogoutForm").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/api/v1/logout/",
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
            url: "/api/v1/token/",
            data: {},
            success: function(data){
                window.location.reload();
            }
        });
    });

    $("#messageFormSend").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/api/v1/message/",
            headers: {
                'HTTP-X-CSRFToken': getCookie('csrftoken')
            },
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
    
    $("#getMessages").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/api/v1/message/history/",
            data: {},
            success: function(data){
                console.log(data);
                $("#messagesHistory").html("");
                for (var i = 0; i < data.length; i++){
                    $("#messagesHistory").append("<p>" + data[i].message + "\t::\t" + data[i].date + "</p>");
                }
            },
            error: function(data){
                console.log("Cant get messages")
            }
        })});
});