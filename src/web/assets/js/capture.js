
$(document).ready(function(){


   $('body').on('click', '.photo' ,function(){
       var name = $(this).attr('name');
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

    $('body').on('click', '.recapture-btn' ,function(){
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