
var ready = function() {

	var output = localStorage.getItem('output');
    $('#pdf-preview').attr( "src", "data:application/pdf;base64," + output);

};

$(document).on('page:load', ready);
$(document).ready(ready);
