$(document).ready(function() {

    $("div#benchlight").click(function() {
        console.log('toggle')
        $.ajax({
            type: "POST",
            url: '/controller',
            data: '',
            success: '',
            dataType: 'json'
        });
        // rt = $.post('/controller') // , $(this).id)
        // console.log(rt.responseText)
    });
});