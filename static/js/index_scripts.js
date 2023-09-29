$(document).ready(function(){
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