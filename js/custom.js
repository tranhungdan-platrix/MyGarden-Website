/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Menu
4. Init Home Slider
5. Init Date Picker
6. Init SVG
7. Init Gallery
8. Init Testimonials Slider
9. Init Booking Slider
10. Init Blog Slider


******************************/
function topFunciton() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var header = $('.header');

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();

		setTimeout(function()
		{
			$(window).trigger('resize.px.parallax');
		}, 375);
	});

	$(document).on('scroll', function()
	{
		setHeader();
		const mybutton = $("#scrollToTop");

		if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
			mybutton.css("display", "flex");
		} else {
			mybutton.css("display", "none");
		}
	});

	initMenu();
	initHomeSlider();
	initSvg();
	initBlogSlider();

	/* 

	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 91)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/* 

	3. Init Menu

	*/

	function initMenu()
	{
		if($('.menu').length)
		{
			var menu = $('.menu');
			var hamburger = $('.hamburger');
			var navLinks = $(`.menu_nav ul`).find('li');
			var close = $('.menu_close');
			// console.log("🚀 ~ navLinks:", navLinks)

			hamburger.on('click', function()
			{
				menu.toggleClass('active');
			});

			navLinks.each(function(index, element) {
				$(element).on('click', function() {
					menu.toggleClass('active');
				})
			});

			close.on('click', function()
			{
				menu.toggleClass('active');
			});
		}
	}

	/* 

	4. Init Home Slider

	*/

	function initHomeSlider()
	{
		if($('.home_slider').length)
		{
			var homeSlider = $('.home_slider');
			homeSlider.owlCarousel(
			{
				items:1,
				autoplay:true,
				loop:true,
				nav:false,
				smartSpeed:1200
			});

			/* Custom dots events */
			if($('.home_slider_custom_dot').length)
			{
				$('.home_slider_custom_dot').on('click', function()
				{
					$('.home_slider_custom_dot').removeClass('active');
					$(this).addClass('active');
					homeSlider.trigger('to.owl.carousel', [$(this).index(), 1200]);
				});
			}

			/* Change active class for dots when slide changes by nav or touch */
			homeSlider.on('changed.owl.carousel', function(event)
			{
				$('.home_slider_custom_dot').removeClass('active');
				$('.home_description').css("animation", "none");
				$('.home_slider_custom_dots li').eq(event.page.index).addClass('active');
				setTimeout(function() {
					$('.home_description').css("animation", "fadeInDown 2s ease-out forwards");
				}, 100);
			});
		}
	}

	/* 

	6. Init SVG

	*/

	function initSvg()
	{
		if($('img.svg').length)
		{
			jQuery('img.svg').each(function()
			{
				var $img = jQuery(this);
				var imgID = $img.attr('id');
				var imgClass = $img.attr('class');
				var imgURL = $img.attr('src');

				jQuery.get(imgURL, function(data)
				{
					// Get the SVG tag, ignore the rest
					var $svg = jQuery(data).find('svg');

					// Add replaced image's ID to the new SVG
					if(typeof imgID !== 'undefined') {
					$svg = $svg.attr('id', imgID);
					}
					// Add replaced image's classes to the new SVG
					if(typeof imgClass !== 'undefined') {
					$svg = $svg.attr('class', imgClass+' replaced-svg');
					}

					// Remove any invalid XML tags as per http://validator.w3.org
					$svg = $svg.removeAttr('xmlns:a');

					// Replace image with new SVG
					$img.replaceWith($svg);
				}, 'xml');
			});
		}	
	}

	/* 

	10. Init Blog Slider

	*/

	function initBlogSlider()
	{
		if($('.blog_slider').length)
		{
			var blogSlider = $('.blog_slider');
			blogSlider.owlCarousel(
			{
				items:3,
				autoplay:true,
				loop:true,
				smartSpeed:1200,
				dots:false,
				nav:false,
				margin:20,
				responsive:
				{
					0:{items:1},
					768:{items:2},
					992:{items:3}
				}
			});
		}
	}

});

function openPopup(src) {
    var popup = document.getElementById("popup");
    var popupImg = document.getElementById("popup-img");
    popup.style.display = "flex";
    popupImg.src = src;
}

function closePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "none";
}

document.addEventListener('DOMContentLoaded', () => {
	const sections = document.querySelectorAll('.section-tag');
	const navLinks = document.querySelectorAll('.nav-group li a');	

	const options = {
		root: null,
		rootMargin: '0px',
		threshold: 0.2
	};

	const callback = (entries, observer) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				const navLink = $(`.nav-group li a[href="#${entry.target.id}"]`);
				navLinks.forEach(link => $(link).removeClass('active'));
				$(navLink).addClass('active');
			}
		});
	};

	const observer = new IntersectionObserver(callback, options);

	sections.forEach(section => {
		observer.observe(section);
	});
});