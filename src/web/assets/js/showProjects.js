var ready = function(){

    $('body').on("click", ".remove-project-btn", function(e){
        e.preventDefault();
        var projectId = $(this).parent().attr("id");
        var $removedProject = $(".project-row-"+projectId);
        $removedProject.fadeOut("slow", function() {
            $removedProject.remove();
            if($(".projects-section").html().trim() == "") window.location.href = '/projects/show';;
        });
        $.ajax({
            method: 'DELETE',
            url: '/project',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({id: projectId})
        }).done(function() {
            console.log("We should show an alert, but the project was succesfully removed.");

        });
    });


    $('body').on("click", ".load-project-btn",function(e){
        e.preventDefault();
        var projectId = $(this).parent().attr("id");
        $.ajax({
            method: 'GET',
            url: '/project/' + projectId
        }).done(function(data) {
            if(data.status == 1){
                $('#prepare-cams-modal').modal('show');
                $('#modal-pcm-loaded').css('display', 'block');
                console.log("The project was successfully loaded.");
            }else{
                alert('Error cargando proyecto');
            }
        });
    });

};

$(document).on('page:load', ready);
$(document).ready(ready);