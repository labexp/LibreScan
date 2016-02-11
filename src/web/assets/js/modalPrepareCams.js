var ready = function(){

    $('body').on("click", "#prepare-cam-continue-btn", function(e){
        e.preventDefault();
        $("#loading-div").css("display", "block");
        $.ajax({
            method: 'POST',
            url: '/camera/prepare'
        }).done(function(data) {
            $("#loading-div").css("display", "none");
            if(data.status == 1) {
                window.location.href = '/scan';
            }else{
                console.log(data);
                $('.modal-pcm-text').css('display', 'none');
                $('#modal-pcm-error').css('display', 'block');
            }
        });
    });

};

$(document).on('page:load', ready);
$(document).ready(ready);