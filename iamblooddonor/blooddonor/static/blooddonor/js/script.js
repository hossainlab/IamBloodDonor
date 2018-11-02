$(function ($) {
    "use strict";

    // testimonial_slider

    $('.testimonial_slider').slick({
        fade: false,
        arrows: true,
        dots: false,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 2000,
        speed: 1500,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: '.service_part .next',
        nextArrow: '.service_part .prev',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1
                }
            },

            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 320,
                settings: {
                    slidesToShow: 1
                }
            }
          ]
    });



    $('.gallery_slider').slick({
        fade: false,
        arrows: true,
        dots: false,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 2000,
        speed: 1500,
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: '.service_part .next',
        nextArrow: '.service_part .prev',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2
                }
            },

            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 320,
                settings: {
                    slidesToShow: 1
                }
            }
          ]
    });


    $('.gallery_slider_s').slick({
        fade: false,
        arrows: true,
        dots: false,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 2000,
        speed: 1500,
        slidesToShow: 5,
        slidesToScroll: 1,
        prevArrow: '.service_part .next',
        nextArrow: '.service_part .prev',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2
                }
            },

            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 320,
                settings: {
                    slidesToShow: 1
                }
            }
          ]
    });

    $('.team_slider').slick({
        fade: false,
        arrows: true,
        dots: false,
        infinite: true,
        //        autoplay: true,
        autoplaySpeed: 2000,
        speed: 1500,
        slidesToShow: 2,
        slidesToScroll: 1,
        prevArrow: '.service_part .next',
        nextArrow: '.service_part .prev',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2
                }
            },

            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 320,
                settings: {
                    slidesToShow: 1
                }
            }
          ]
    });



    $('#navbar_toggoler').on('click', function () {
        $('#navber_toggler').animate({
            'left': '0'
        }, 500);
    });

    $('.cross_sign').on('click', function () {
        $('#navber_toggler').animate({
            'left': '100%'
        }, 500);
    });

    //preloader js
    $(window).on('load', function () {
        $(".Pre_loader").delay(500).fadeOut(1000);
        $(".load").delay(1000).fadeOut(1000);
    });
    



    // menufix start....

    var menutop = $(".navber_part").offset().top;

    $(window).scroll(function () {

        var scrollto = $(window).scrollTop();

        if (scrollto > menutop) {
            $(".navber_part").addClass("menufix");
        } else {
            $(".navber_part").removeClass("menufix");
        }
        if (scrollto > 200) {
            $('.button').fadeIn(1000);
        } else {
            $('.button').fadeOut(1000);
        }

    });



    // scrolling system....

    $('a[href*="#"]:not([href="#').on('click', function () {

        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('a[href*="#"]:not([href="#').removeClass('active_class');
                $(this).addClass('active_class');
                $('html, body').animate({
                    scrollTop: target.offset().top - 70
                }, 1000);
                return false;
            }
        }

    });
    
    
    
    var $window = $(window);		//Window object
	
	var scrollTime = 1.2;			//Scroll time
	var scrollDistance = 180;		//Distance. Use smaller value for shorter scroll and greater value for longer scroll
		
	$window.on("mousewheel DOMMouseScroll", function(event){
		
		event.preventDefault();	
										
		var delta = event.originalEvent.wheelDelta/120 || -event.originalEvent.detail/3;
		var scrollTop = $window.scrollTop();
		var finalScroll = scrollTop - parseInt(delta*scrollDistance);
			
		TweenMax.to($window, scrollTime, {
			scrollTo : { y: finalScroll, autoKill:true },
				ease: Power1.easeOut,	//For more easing functions see https://api.greensock.com/js/com/greensock/easing/package-detail.html
				autoKill: true,
				overwrite: 5							
			});
					
	});

	$('#logout').on('click',function(){
	    $('#message').animate({
	        'height':'100%'

	    });

	});



	





})
