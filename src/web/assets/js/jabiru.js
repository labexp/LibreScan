
var ready = function() {
	var page = 0;
	var final_page = 0;

	$.get('/images/last/id', function(data){
		final_page = data.last_id;
	});

	$.get('/texts/0', function(data){
		text = data.text;
		$('#page-text').val(text);
	});


	
	$('#back-btn').hide();

	// Manage when the next button is pressed
	$('#next-btn').click(function(){
		page++;
		if(page === final_page)
			$('#next-btn').hide();
		if(page > 0)
			$('#back-btn').show();
		$('#page-image').attr("src", "/images/" + page);
		$.get('/texts/'+ page, function(data){
			text = data.text;
			$('#page-text').val(text);
		});
	});

	// Manage when the back button is pressed
	$('#back-btn').click(function(){
		page--;
		if(page === 0)
			$('#back-btn').hide();
		if(page < final_page)
			$('#next-btn').show();
		$('#page-image').attr("src", "/images/" + page);
		$.get('/texts/'+ page, function(data){
			text = data.text;
			$('#page-text').val(text);
		});
	});

	// Manage when the save button is pressed
	$('#save-btn').click(function(){
		text = $('#page-text').val();
		$.ajax({
            method: 'POST',
            url: '/saves/' + page,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({"text" : text})
        })
	});

};

$(document).on('page:load', ready);
$(document).ready(ready);
