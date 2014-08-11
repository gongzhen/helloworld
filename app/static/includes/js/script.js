/*

My Custom JS
============

Author:  Brad Hussey
Updated: August 2013
Notes:	 Hand coded for Udemy.com

*/
// Test javascript works
// $(document).ready(function ()
// {
//     window.alert("function started");
// });

$(document).ready(function() {
	$('.carousel').carousel({
			interval: 3000
	})
});

$(function(){
	$('#alertMe').click(function(e){
		e.preventDefault(); //prevent the default alert
		$('#successAlert').slideDown(); 
	});
});

