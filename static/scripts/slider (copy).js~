;(function($, window, document, undefined){

	var pluginName = 'slider';

	function Plugin(element, options){
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

	Plugin.prototype = {
		add: function(html){
			var $li = $('<li>'+ html +'</li>').appendTo(this.$ul)
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
            this.$ul.velocity('stop').velocity(animation, {duration: this.options.transitionSpeed * 1000, easing: this.options.transitionEffect, complete: $.proxy(function(){
				this.$element.trigger('stop', [this.prev, index]);
			}, this)});

		},
        resize: function($slide){
            this.$element.velocity('stop').velocity({'height': $slide.outerHeight()}, {duration: this.options.transitionSpeed * 1000, easing: this.options.transitionEffect});
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

	$.fn[pluginName] = function(options){

		if( typeof options == 'string'){
			var plugin = this.data(pluginName);
			if(plugin){
				var r = plugin[options].apply(plugin, Array.prototype.slice.call( arguments, 1 ) );
				if(r) return r;
			}
			return this
		}

		options = $.extend({}, $.fn[pluginName].defaults, options);

		return this.each(function(){
			var plugin = $.data(this, pluginName);
			if( ! plugin ){
				plugin = new Plugin(this, options);
				$.data(this, pluginName, plugin);
			}
		});
	};
	$.fn[pluginName].defaults = {
		speed:3,
		transitionSpeed:.7,
		directionSensitive:true,
		autoAnimate:true,
		transitionEffect:'easeInOutCubic',
		start:function(){},
		stop:function(){}
	};

})(jQuery, window, document);