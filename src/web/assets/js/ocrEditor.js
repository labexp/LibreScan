var ready = function(){

    $('body').on('click', '#process-btn', function() {
        $.ajax({
            method: 'post',
            url: '/output'
        }).done(function(output) {
            $("#show-output").removeClass('disabled');
        }).fail(function(){
            alert("Algo no salio bien");
        });
    });

    //OCR Editor is not implemented yet, so when the page loads it clicks the process button.
    //$("#process-btn").trigger("click");

};

$(document).on('page:load', ready);
$(document).ready(ready);