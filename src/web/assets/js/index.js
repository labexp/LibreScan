$(document).ready(function() {
	var navsHeight = $(".header-navbar").height() + $(".footer-nav").height();
	$(".main-container").css("min-height", $(window).height() - navsHeight);
});

// Shows notification on the top right of the screen.
 function generateNotification(notificationType, message, position, timeout) {
  notyObject = noty({
   text        : message,
   type        : notificationType,
   theme       : 'relax',
   dismissQueue: true,
   layout      : position,
   timeout   : false,
   maxVisible  : 1,
   killer   : true,
   animation   : {
    open  : 'animated flipInX',
    close : 'animated flipOutX'
   }
  });
  notyObject.setTimeout(timeout);
 }