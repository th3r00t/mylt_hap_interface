$(document).ready(function() {

    $("div#benchlight").click(function() {
        console.log('toggle')
        rt = $.post('/controller') // , $(this).id)
        console.log(rt.responseText)
    });
});