var ready = function(){

    $('body').on('click', '#process-btn', function() {
        $.ajax({
            method: 'get',
            url: '/output'
        }).done(function(output) {
            localStorage.setItem('output', output);
            $("#show-output").removeClass('disabled');
        }).fail(function(){
            alert("Algo no salio bien");
        });

    });

};

$(document).on('page:load', ready);
$(document).ready(ready);