$(function() {
    var intro = {};
    intro.$carousel = $('#home-intro');
    intro.$settingsBtn = $('#home-intro-settings-btn');
    intro.$backBtn = $('.home-intro-back-btn');

    intro.$carousel.carousel({
        easing: 'easeInOutQuint',
        autoAnimate: false
    });


function getDirection(element){
    var result = null;
    if (element){
        if (window.getComputedStyle){
            result = window.getComputedStyle(element,null).direction;
        } else if (element.currentStyle){
            result = element.currentStyle.direction;
        }
    }

    return result;
}


var java_script_language_bidi = "";
$(document).ready(function(){
  java_script_language_bidi = getDirection(document.body); // Detect if language is persian or english
  $('.bxslider').bxSlider();
  $('.bx-next').text('');
  $('.bx-prev').text('')
});




var visibleBranding=false;
$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    // Do something
    $('#xaas-nav-bar').addClass("colored-nav-bar-menu");
    $('#xaasMenu').css('padding-top', '0px')
    $('#lan-tray-en').css('margin-top', '10px')
    $('#lan-tray-pr').css('margin-top', '10px')
    $('#xaas-brand-img').css('height', '30px')
    $('#nav-bar-header-id').css('padding-top', '10px')

    if(!visibleBranding)
    {
        visibleBranding = true;
        if (java_script_language_bidi != 'rtl')
        {
          $(".moving-beta")
      .velocity({ left:0 }, 500)
      .delay(51)
      }
      else
      {
       $(".moving-beta")
      .velocity({ right:0 }, 300)
      .delay(51)
      }
    }

    if ($(window).scrollTop() ==0)
    {
        visibleBranding = false;
        if (java_script_language_bidi != 'rtl')
        {
       $(".moving-beta")
      .velocity({ left:-100 }, 400)
      .delay(10)
      }
      else
      {
             $(".moving-beta")
      .velocity({ right:-100 }, 300)
      .delay(10)
      }
        $('#xaas-nav-bar').removeClass("colored-nav-bar-menu");
        $('#xaasMenu').css('padding-top', '25px')
        $('#lan-tray-en').css('margin-top', '35px')
        $('#lan-tray-pr').css('margin-top', '35px')
        $('#xaas-brand-img').css('height', '40px')
        $('#nav-bar-header-id').css('padding-top', '25px')
    }
});


function set_home_banner_height(){
 //$('#home-banner').height($(window).height());
}

$(window).resize(function() {
 set_home_banner_height();
});

$(document).ready(set_home_banner_height());




    intro.$settingsBtn.click(function(e){e.preventDefault(); intro.$carousel.carousel('next'); });
    intro.$backBtn.click(function(e){ e.preventDefault();  intro.$carousel.carousel('previous'); });

//    $('#slider-cpu').slider({min: 0, max: 4, step: 1, value: 1});
//    $('#slider-memory').slider({min: 0, max: 5, step: 1, value: 2});
//    $('#slider-storage').slider({min: 0, max: 3, step: 1, value: 1});
//    $('#slider-instance').slider({min: 1, max: 5, step: 1});

//    intro.$emailInput = $('#email-input');
//    intro.$passwordInput = $('#password-input');
//    intro.$passwordToggleBtn = $('#password-toggle-btn');
//    intro.$passwordToggleIcon = intro.$passwordToggleBtn.find('.icon');
//    intro.$passwordToggleBtn.data('visible', false);
//    intro.$passwordToggleBtn.click(function(){
//        if( $(this).data('visible') ){
//            intro.$passwordToggleIcon.attr('class', 'icon icon-eye');
//            intro.$passwordInput.attr('type', 'password');
//            intro.$passwordToggleBtn.data('visible', false);
//        }else{
//            intro.$passwordToggleIcon.attr('class', 'icon icon-eye-blocked');
//            intro.$passwordInput.attr('type', 'text');
//            intro.$passwordToggleBtn.data('visible', true);
//        }
//    });

//    intro.$form = $('#home-intro-signup-form');
//    intro.$form.submit(function(e){
//        e.preventDefault();
////        var data = {"username": intro.$emailInput.val(), "pass": intro.$passwordInput.val(), "project": "demo"}
//        $.ajax({
//            url: '/api/users/',
//            type: 'POST',
//            dataType: 'json',
//            data: $(this).serialize(),
//            beforeSend: $.proxy(function(xhr, settings){
//                addToXhrPool(xhr, settings, this.$element);
//            }, this),
//            success: $.proxy(function(json){
//                clearXhrPool();
//                if( json === 'false'){
//
//                }else{
//                    intro.$carousel.carousel('next');
//                }
//
//            }, this),
//            error: $.proxy(function(xhr, ajaxOptions, thrownError){
//                clearXhrPool();
//
//            }, this)
//        });
//    });

});

//--- Carousel ---//
(function($, window, document, undefined){

    function Carousel(element, options){
        this.$element = $(element);
        this.options = options;

        this.$element.bind('start', this.options.start);
		this.$element.bind('stop', this.options.stop);

		this.$ul = this.$element.find('>ul');
		this.$lis = this.$ul.find('>li');
		this.index = 0;
		this.prev = 0;
		this.length = this.$lis.length;

		this.bidi = this.options.directionSensitive && this.$element.css('direction' ) === 'rtl';

		this._configureStyles();
		$(window).resize($.proxy(function(){ this._configureStyles(); }, this));

		if(this.options.autoAnimate)
			this.inter = setInterval($.proxy(function(){ this.next() }, this), this.options.speed*1000);

    }

    Carousel.prototype = {
        add: function(html){
			var $li = $('<li>'+ html +'</li>').appendTo(this.$ul);
			this.length++;
			this._configureStyles();
			this.next();
			return $li
		},
		next: function(){
			this.prev = this.index;
			this.index++;
			if(this.index >= this.length) this.index=0;
			this.goto(this.index)
		},
        previous: function(){
			this.prev = this.index;
			this.index--;
			if(this.index < 0) this.index=this.length - 1;
			this.goto(this.index)
		},
		goto: function(index){
			var animation = {};
            var $slide = $(this.$lis[index]);
			var offset = - this.$element.width() * index;
			if(this.bidi) animation = {right:offset};
			else animation = {left:offset};

			this.$element.trigger('start', [this.prev, index]);
			this.resize($slide);
            this.$ul.velocity('stop').velocity(animation, {duration: this.options.transitionSpeed * 1000, easing: this.options.easing, complete: $.proxy(function(){
				this.$element.trigger('stop', [this.prev, index]);
			}, this)});

		},
        resize: function($slide){
            this.$element.velocity('stop').velocity({'height': $slide.outerHeight()}, {duration: this.options.transitionSpeed * 1000, easing: this.options.easing});
        },
		_configureStyles:function(){
			this.$element.css({overflow:'hidden'});
			if( this.$element.css('position') === 'static') this.$element.css('position', 'relative');

            var $slide = $(this.$lis[this.index]);

            this.$element.css({height: $slide.outerHeight(true)});
			this.$ul.css({position:'absolute', left:-(this.$element.width() * this.index), top:0, width:(this.$element.width() * this.length)});
			this.$lis = this.$ul.find('>li');
			this.$lis.css({float:'left', width:this.$element.width()});
//			this.$lis.css({float:'left', width:this.$element.width(), height:this.$element.height()});
			if(this.bidi) this.$lis.css({float:'right'});
		}
    };
    // Plugin Definition //
    $.fn.carousel = function(options){
        if( typeof options == 'string'){
            var plugin = this.data('carousel');
            if(plugin){
                var r = plugin[options].apply(plugin, Array.prototype.slice.call( arguments, 1 ) );
                if(r) return r
            }
            return this
        }

        options = $.extend({}, $.fn.carousel.defaults, options);

        return this.each(function(){
            var plugin = $.data(this, 'carousel');
            if( ! plugin ){
                plugin = new Carousel(this, options);
                $.data(this, 'carousel', plugin);
            }
        });
    };
    $.fn.carousel.defaults = {
        speed:3,
		transitionSpeed:.7,
		directionSensitive:true,
		autoAnimate:true,
		easing:'easeInOutCubic',
		start:function(){},
		stop:function(){}
    };

})(jQuery, window, document);

//--- FullScreen ---//
(function($, window, document, undefined){

    function FullScreen(element, options){
        this.$element = $(element);
        this.options = options;

        this.$image = this.$element.find('img');
        this.originalRatio = this.$image.width() / this.$image.height();

        this.$element.css({
            overflow: 'hidden',
            position: 'fixed', 'z-index': '-1',
            top: 0, right: 0, bottom: 0, left: 0
        });
        this.$image.css({
            position: 'absolute'
        });

        this.$image.one('load', $.proxy(function(){
            this._setSize();
            $(window).resize($.proxy(function(){ this._setSize();}, this));
        }, this));
    }

    FullScreen.prototype = {
        _setSize: function(){
            this.heightOfWidthMatch = this.$element.width() / this.originalRatio; // if the widths would be matched this would be the height
            this.widthOfHeightMatch = this.$element.height() * this.originalRatio; // if the heights would be matched this would be the width

            if(this.heightOfWidthMatch >= this.$element.height()){
                // Go for width match
                this.$image.css({
                    width: this.$element.width(),
                    height: this.heightOfWidthMatch,
                    top: (this.$element.height() - this.heightOfWidthMatch)/2
                });
            }else{
                // Go for height match
                this.$image.css({
                    width: this.widthOfHeightMatch,
                    height: this.$element.height(),
                    left: (this.$element.width() - this.widthOfHeightMatch)/2
                });
            }
        }
    };
    // Plugin Definition //
    $.fn.fullscreen = function(options){
        if( typeof options == 'string'){
            var plugin = this.data('fullscreen');
            if(plugin){
                var r = plugin[options].apply(plugin, Array.prototype.slice.call( arguments, 1 ) );
                if(r) return r
            }
            return this
        }

        options = $.extend({}, $.fn.fullscreen.defaults, options);

        return this.each(function(){
            var plugin = $.data(this, 'fullscreen');
            if( ! plugin ){
                plugin = new FullScreen(this, options);
                $.data(this, 'fullscreen', plugin);
            }
        });
    };
    $.fn.fullscreen.defaults = {

    };

})(jQuery, window, document);

$.xhrPool = []; // array of uncompleted requests
function clearXhrPool(){
	for(var i=0; i<$.xhrPool.length; i++){
		var jqXHR = $.xhrPool[i];
		if(jqXHR && jqXHR.readystate != 4)
			jqXHR.abort();
//		if(jqXHR['element']) {
//            jqXHR.element.removeClass('sug-waiting-icon');
//        }
	}
	$.xhrPool = [];
}

function addToXhrPool(xhr, settings, $element){
	this.clearXhrPool();
//	if( $element ){
//		xhr.element = $element;
////		$element.addClass('sug-waiting-icon');
//	}
	$.xhrPool.push(xhr);
	if (!csrfSafeMethod(settings.type)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
}

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// using jQuery
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}


function showxaasclip(){
$('#element_to_pop_up').bPopup({
            onOpen: function() {
            },
            onClose: function() {
                $('#clip-id').attr('src', $('iframe').attr('src'));
            }
        });


}
