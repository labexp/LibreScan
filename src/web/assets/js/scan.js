
$(document).ready(function(){


   $('body').on('click', '.photo' ,function(){
       var name = $(this).attr('name');
       if (!name) return;
        var src = '/photo/'+name;
        var img = '<img src="' + src + '" class="img-responsive"/>';

        $('#photo-modal').on('shown.bs.modal', function(){
            $('#photo-modal .modal-body').html(img);
        });
        $('#photo-modal').on('hidden.bs.modal', function(){
            $('#photo-modal .modal-body').html('');
        });
       $('#photo-modal').modal();
    });

    $('body').on('click', '.capture-btn' ,function(){
        if ($('.recapture-btn').hasClass('btn-disabled')) {
            $('.recapture-btn').removeClass('btn-disabled');
        }
        $("#loading-div").css("display", "block");
        $(".loading-text").css("display", "none");
        $.ajax({
            method: 'post',
            url: '/photo'
        }).done(function(response) {
            $("#loading-cams-msg").css("display", "block");
            $("#loading-div").css("display", "none");
            if(response.status == -1) {
                $('#prepare-cams-modal').modal('show');
                $('#modal-pcm-capture-error').css('display', 'block');
            }else {
                console.log('Done cap');
                $('#photo1').attr( "src", "/thumbnail/" + response.photo1);
                $('#photo2').attr( "src", "/thumbnail/"+ response.photo2);
                $('#photo1').attr( "name", response.photo1);
                $('#photo2').attr( "name", response.photo2);
            }
        });
    });

    $('body').on('click', '#check-ocr-btn' ,function(e){
        e.preventDefault();
        $(".loading-text").css("display", "none");
        $("#loading-process-msg").css("display", "block");
        $("#loading-div").css("display", "block");
        $.ajax({
            method: 'post',
            url: '/scan/halt'
        }).done(function(response) {
            if(response.status == -1) {
                alert("Error al procesar imagenes");
            }else {
                checkProgress(-1);
            }
        });
    });

    function checkProgress(itemsLeft) {
        if(itemsLeft == 0) progressCompleted();
        setTimeout(function() {
            $.ajax({
                method: 'get',
                url: '/progress'
            }).done(function(data){
                itemsLeft = data.itemsLeft;
                $("#left-items-span").html(itemsLeft);
                checkProgress(itemsLeft);
            });
        }, 2000);
    }

    function progressCompleted() {
        $(".loading-text").css("display", "none");
        $("#loading-cams-msg").css("display", "block");
        $("#loading-div").css("display", "none");
        window.location.href = '/ocrs';
    }

    $('body').on('click', '.recapture-btn' ,function(){
        if ($(this).hasClass('btn-disabled')){
            return;
        }
        $("#loading-div").css("display", "block");
        $(".loading-text").css("display", "none");
        $.ajax({
            method: 'PUT',
            url: '/photo'
        }).done(function(response) {
            $("#loading-cams-msg").css("display", "block");
            $("#loading-div").css("display", "none");
            if(response.status == -1) {
                $('#prepare-cams-modal').modal('show');
                $('#modal-pcm-capture-error').css('display', 'block');
            }else {
                console.log('Done recap');
                $('#photo1').attr( "src", "/thumbnail/" + response.photo1);
                $('#photo2').attr( "src", "/thumbnail/"+ response.photo2);
                $('#photo1').attr( "name", response.photo1);
                $('#photo2').attr( "name", response.photo2);
            }
        });
   });

    $('body').on('click', '#calibrate-btn' ,function(e){
        e.preventDefault();
        $.ajax({
            method: 'POST',
            url: '/camera/calibrate'
        }).done(function(response){
            if(response.status == -1) {
                $('#prepare-cams-modal').modal('show');
                $('#modal-pcm-capture-error').css('display', 'block');
            }else{
                var message = $('#calibrate-success-message').text()
                generateNotification('success', message, 'topRight', 2000);
            }
        });

    });

    $('#calibrate-btn').hover(function(){
        var message = $('#calibrate-message').text();
        generateNotification('information', message, 'topCenter', 6000);
    });



});