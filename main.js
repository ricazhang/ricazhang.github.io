$('#expand-courses').click(function(event) {
	event.preventDefault();
	$(this).find('span').each(function() { $(this).toggle(); });
	$('#relevant-courses').slideToggle();
});

function get_type(thing){
    if(thing===null)return "[object Null]"; // special case
    return Object.prototype.toString.call(thing);
}

function capture(elemId) {
	console.log(event);
	var scrollToId = "#" + elemId.replace("menu-","");
	console.log(scrollToId);
	//console.log($(this).firstChild.data('id'));
	$('#resume-center-box').scrollTo(scrollToId);
}

for (var i = 0; i < $('.resume-menu-item').length; i++) {
  $('.resume-menu-item')[i].addEventListener('click', function(event) {
  	//event.preventDefault();
  	var elemId = this.id;
		var scrollToId = "#" + elemId.replace("menu-","");
		$('#resume-center-box').scrollTo(scrollToId, 500, { offset:-25, easing:'swing' });
  }, true);
}

for (var i = 0; i < $('.square').length; i++) {
  $('.square')[i].addEventListener('click', function(event) {
  	//event.preventDefault();
  	var elemId = this.id;
		var imageLocation = "images/" + elemId + ".jpg";
		console.log(imageLocation);
		$('#photo-background-dim').css("z-index","15");
		$('#photo-background-dim').fadeTo(400, .9);
		$('#image-viewer img').attr('src', imageLocation);
		$('#image-viewer img').fadeIn();
		$('#image-viewer').fadeIn();
  }, true);
}

$('#photo-background-dim').click(function() {
	$('#image-viewer img').fadeOut();
	$('#image-viewer img').fadeOut();
	$('#photo-background-dim').css("z-index","0");
	$('#photo-background-dim').fadeTo(400, 0);
});