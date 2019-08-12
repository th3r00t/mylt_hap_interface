$(document).ready(function(){
    
    $("div#benchlight").click(function(){
        $.ajax({
            url: 'controller/',
            type: 'POST',
            data: JSON.stringify($(this).id),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            async: false,
            success: function(msg) {
                alert(msg);
            }
        });
    });

});