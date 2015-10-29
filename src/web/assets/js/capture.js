
$(document).ready(function(){



   $('.photo').on('click', function(){


        var src = $(this).attr('src');
        var img = '<img src="' + src + '" class="img-responsive"/>';

        $('#photo-modal').on('shown.bs.modal', function(){
            $('#photo-modal .modal-body').html(img);
        });

        $('#photo-modal').on('hidden.bs.modal', function(){
            $('#photo-modal .modal-body').html('');
        });

       $('#photo-modal').modal();
   });
})