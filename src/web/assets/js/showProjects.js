var ready = function(){

    $('body').on("click", ".remove-project-btn", function(e){
        e.preventDefault();
        var projectId = $(this).parent().attr("id");
        var $removedProject = $(".project-row-"+projectId);
        $removedProject.fadeOut("slow", function() {
            $removedProject.remove();
            if($(".main-container").html().trim() == "") window.location.href = '/projects/show';;
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


    $('body').on("click", ".load-project-btn", function(e){
        e.preventDefault();
        var projectId = $(this).parent().attr("id");
        //$("#loading-cams").css("display", "block");
        $.ajax({
            method: 'GET',
            url: '/project/' + projectId
        }).done(function(data) {
            $("#loading-cams").css("display", "none");
            window.location.href = '/scan';
            console.log("We should show an alert, but the project was loaded.");
            console.log(data);
        });
    });


};

$(document).on('page:load', ready);
$(document).ready(ready);