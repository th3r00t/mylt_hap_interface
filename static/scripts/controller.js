$(document).ready(function() {

    $("div#benchlight").click(function() {
        $.post('/controller') // , $(this).id)
    });

});