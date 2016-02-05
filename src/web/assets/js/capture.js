
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

        $.ajax({
            method: 'post',
            url: '/photo'
        }).done(function(response) {
            console.log('Done cap');
            $('#photo1').attr( "src", "/thumbnail/" + response.photo1);
            $('#photo2').attr( "src", "/thumbnail/"+ response.photo2);
            $('#photo1').attr( "name", response.photo1);
            $('#photo2').attr( "name", response.photo2);
        });
    });

    $('body').on('click', '#check-ocr-btn' ,function(){

        $.ajax({
            method: 'post',
            url: '/scan/halt'
        }).done(function(response) {
            if(response.ready) {
                window.location.href = '/ocrs';
            }
        });
    });

    $('body').on('click', '.recapture-btn' ,function(){
        if ($(this).hasClass('btn-disabled')){
            return;
        }
        $.ajax({
            method: 'PUT',
            url: '/photo'
        }).done(function(response) {
            console.log('Done recap');
            $('#photo1').attr( "src", "/thumbnail/" + response.photo1);
            $('#photo2').attr( "src", "/thumbnail/"+ response.photo2);
            $('#photo1').attr( "name", response.photo1);
            $('#photo2').attr( "name", response.photo2);
        });
   });

});