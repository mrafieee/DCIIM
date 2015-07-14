var java_script_language_bidi = ""

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


$(function(){

    var signup = signup || {};
    java_script_language_bidi = getDirection(document.body); // Detect if language is persian or english
    $.backstretch("/static/images/bg.jpg");

    // Password Visibility
    signup.$passwordInput = $('#id_password');
    signup.$passwordToggleBtn = $('#password-toggle-btn');
    signup.$passwordToggleIcon = signup.$passwordToggleBtn.find('.icon');
    signup.$passwordToggleBtn.data('visible', false);
    signup.$passwordToggleBtn.click(function(){
        if( $(this).data('visible') ){
            signup.$passwordToggleIcon.attr('class', 'icon icon-eye');
            signup.$passwordInput.attr('type', 'password');
            signup.$passwordToggleBtn.data('visible', false);
        }else{
            signup.$passwordToggleIcon.attr('class', 'icon icon-eye-blocked');
            signup.$passwordInput.attr('type', 'text');
            signup.$passwordToggleBtn.data('visible', true);
        }
    });

    var cpu_array = [1, 2, 3, 4, 5];
    var memory_array = [256, 512, 1024, 2048, 4096, 6144];
    var storage_array = [1, 2, 5, 10];


    // Sliders
    $('#slider-cpu').slider({animate: true, min: 0, max: 4, step: 1, value: 1, change: function(e, ui){ $('#id_cpu').val(cpu_array[ui.value]) }});
    $('#slider-memory').slider({animate: true, min: 0, max: 5, step: 1, value: 2, change: function(e, ui){ $('#id_memory').val(memory_array[ui.value]) }});
    $('#slider-storage').slider({animate: true, min: 0, max: 3, step: 1, value: 1, change: function(e, ui){ $('#id_storage').val(storage_array[ui.value]) }});
    //$('#slider-instances').slider({animate: true, min: 0, max: 3, step: 1, change: function(e, ui){ $('#id_instances').val(ui.value) }});


    // Form submission
    signup.$formDialog = $('.form-dialog');
    signup.$form = $('#signup-form');
    signup.$form.submit(function(e){
        e.preventDefault();
        hideErrors($(this));
//        var data = {"username": signup.$emailInput.val(), "pass": signup.$passwordInput.val(), "project": "demo"}
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            dataType: 'json',
            data: $(this).serialize(),
            beforeSend: $.proxy(function(xhr, settings){
                addToXhrPool(xhr, settings, this.$element);
            }, this),
            success: $.proxy(function(json){
                clearXhrPool();
                if(json.errors) {
                    // Form errors
                    showErrors(json.errors)
                    try{
                    showUserInfoForm();
                    $('.captcha-refresh').click()
                    }
                    catch(err){
                    showUserInfoFormVPS();
                    }
                }else if( !json.success ){
                    if(json.lang=='en')
                    {
                        signup.$formDialog.empty().append('' +
                            '   <h2>An Error occurred while creating your service</h2>' +
                            '   <p>'+ json.message +'</p>' +
                            '');

                    }
                    else
                    {
                        signup.$formDialog.empty().append('' +
                            '   <h1>خطا در ساخت سرویس</h1>' +
                            '   <p>'+ json.message +'</p>' +
                            '');
                    }
                }else if(json.success){
                    if(json.type=='vpc') {
                        var i = 10;
                        if(json.lang=='fa')
                        {
                            signup.$formDialog.empty().append('<h1>حساب کاربری آزمایشی شما با موفقیت ایجاد شد</h1>' +
                            '<!--<p>اطلاعات دسترسی به سرویس ابر آزمایشی شما به صورت زیر می‌باشد: </p>' +
                            '   <ul>' +
                            '      <li>آدرس وب سایت سرویس انتخابی شما: <a href='+ json.subdomain +'>' + json.subdomain + '</a></li>' +
                            '      <li>خط فرمان برای اتصال به سرور مجازی: ' + json.sshaccesslink + '</li>' +
                            '      <li>حساب کاربری سرور: <strong>root</strong></li>' +
                            '      <li>رمز عبور سرور: <strong>xamin@passwd</strong></li></ul>-->' +
                            '<p>لینک فعال‌سازی حساب‌کاربری به ایمیل شما اراسال شد. لطفا برای تکمیل مراحل ثبت نام بر روی این لینک کلیک نمایید.</p>' +
                            '   <hr>');
                        }
                        else
                        {
                            signup.$formDialog.empty().append('<h2>Your trial account has been successfully created</h2>' +

                            '   <!--<ul>' +
                            '      <li>Your Demo Service: <a href='+ json.subdomain +'>' + json.subdomain + '</a></li>' +
                            '      <li>Your ssh command: ' + json.sshaccesslink + '</li>' +
                            '      <li>Server Username: <strong>root</strong></li>' +
                            '      <li>Server Password: <strong>xamin@passwd</strong></li></ul>-->' +
                            '      <p>An activation link has been sent to your email. Please check your emails and click on the confirmation link to finish the registration.</p>' +
                            '   ');
                        }

                       // '   ' +
                        //'   );
                        //var data_from_django = credentials ;
                        //var $seconds = signup.$formDialog.find('#seconds');
                        //var inter = setInterval(function () {
                         //   $seconds.text(--i);
                         //   if (i <= 0) {
                          //      clearInterval(inter);
                          //      window.location = json.redirect;
                           // }
                        //}, 1000)
                    }else if(json.type=='vps'){
                        if(json.lang=='en')
                        {
                            if (!json.message)
                             {
                               signup.$formDialog.empty().append('' +
                            '   <h1>Your VPS is not created.</h1>' +
                            '<p>You requested more than your quota. No resource available to create your VPS.</p>' +
                            '');
                             }
                             else
                             {
                                signup.$formDialog.empty().append('' +
                                '   <h1>Your private server has been successfully created.</h1>' +
                                '   <p>You can access your virtual private server using the following credentials:</p>' +
                                '   <ul>' +
                                '      <li>Address: <stong>'+ json.message +'</strong></li>' +
                                '      <li>Username: <strong>root</strong></li>' +
                                '      <li>Password: <strong>xamin@passwd</strong></li></ul>' +
                                '   <p>DO NOT FORGET TO CHANGE THE DEFAULT PASSWORD AS SOON AS POSSIBLE.</p>' +
                                '   <hr>' +
                                '   <a href="/" class="btn btn-primary">Back to Home</button>' +
                                '');
                            }
                        }
                        else
                        {
                        if (!json.message)
                         {
                           signup.$formDialog.empty().append('' +
                        '   <h1>سرور مجازی شما ساخته نشد</h1>' +
                        '<p>منابع انتخابی شما بیش از حد مجاز بوده است.</p>' +
                        '');
                         }
                         else
                         {
                                 signup.$formDialog.empty().append('' +
                            '   <h1>سرور درخواستی شما با موفقیت ساخته شد</h1>' +
                            '   <p>اطلاعات مورد نیاز برای دسترسی به سرور درخواستی شما به صورت زیر می‌باشد:</p>' +
                            '   <ul>' +
                            '      <li>آدرس: <stong>'+ json.message +'</strong></li>' +
                            '      <li>نام کاربری <strong>root</strong></li>' +
                            '      <li>رمز عبور: <strong>xamin@passwd</strong></li></ul>' +
                            '   <p><strong>برای اطمینان بیشتر، رمز عبور سرور خود را به‌روزرسانی نمایید.</strong></p>' +
                            '   <hr>' +
                            '   <a href="/" class="btn btn-primary">بازگشت به صفحه اصلی</button>' +
                            '');
                         }

                        }
                    }
                }

            }, this),
            error: $.proxy(function(xhr, ajaxOptions, thrownError){
                clearXhrPool();

            }, this)
        });
    });

    function showErrors(errors){
        for(var i=0; i<errors.length; i++){
            var $field = $('#id_'+errors[i].field);
            if(! $field.length ) $field = $('[id^=\'id_'+errors[i].field+'\']');
            $field.parents('.form-group').addClass('error');
            var $error = $(errors[i].error).insertBefore($field).addClass('help-block error').hide();
            $error.slideDown('500');
        }
    }
    function hideErrors($form){
        $form.find('ul.errorlist').remove();
        $form.find('.error').removeClass('error');
    }

});


//add referesh button to captcha.
$(function() {
    // Add refresh button after field (this can be done in the template as well)
    if (java_script_language_bidi != 'rtl')
    {
        $('img.captcha').after(
                $('<a href="#void" class="captcha-refresh"><img class="my-captcha-referesh" height="28px" src="/static/images/captcha-referesh-icon.png" alt="Referesh"></a>')
                );
    }
    else
    {
        $('img.captcha').after(
            $('<a href="#void" class="captcha-refresh"><img height="28px" class="my-captcha-referesh" src="/static/images/captcha-referesh-icon.png" alt="Referesh"></a>')
            );
    }

    // Click-handler for the refresh-link
    $('.captcha-refresh').click(function(){
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":"
                  + location.port + "/captcha/refresh/";

        // Make the AJAX-call
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});


function showImageTemplateForm(){
 document.getElementById('demo_form_id').hidden = true;
 document.getElementById('demo_form_id').style.display = "none";
 document.getElementById('image_template_frm_id').style.display = "inline";
 document.getElementById('signup_btn').style.display = "inline";
 document.getElementById('next_btn').style.display = "none";
 $('#signup_btn').css('display', 'inline');
}


function showUserInfoForm(){
 document.getElementById('demo_form_id').hidden = false;
 document.getElementById('demo_form_id').style.display = "block";
 document.getElementById('image_template_frm_id').style.display = "none";
 document.getElementById('signup_btn').style.display = "none";
 document.getElementById('next_btn').style.display = "inline";
 $('#loading_page_id').css('display', 'none');

 // Remove second captcha error message.
 if ($('ul:contains(Captcha)').length)
 {
     $('ul:contains(Captcha)')[0].style.display = "none"
 }

 if ($('ul:contains(Math result)').length)
 {
     $('ul:contains(Math result)')[0].style.display = "none"
 }

 if ($('ul:contains(نتیجه محاسبه عبارت)').length)
 {
  $('ul:contains(نتیجه محاسبه عبارت)')[0].style.display = "none"
 }

 if ($('ul:contains(نتیجه محاسبه اشتباه است)').length)
 {
   $('ul:contains(نتیجه محاسبه اشتباه است)')[0].style.display = "none"
 }
}

function change_image_template_id_value(value){
document.getElementById('signup-form')['image_template'].value = value;
}

function please_wait_message(language_code)
{
  $('#loading_page_id').css('display', 'block');
   document.getElementById('demo_form_id').style.display = "none";
   document.getElementById('image_template_frm_id').style.display = "none";
   $('#signup_btn').css('display', 'none');
}


function please_wait_message_for_vps(){
    document.getElementById('server-details-form').style.display = "none";
    $('#loading_page_id_vps').css('display', 'block');
    document.getElementById('vps_submit_btn').style.display = "none";
}

function showUserInfoFormVPS(){
document.getElementById('vps_submit_btn').style.display = "inline";
document.getElementById('server-details-form').style.display = "inline";
$('#loading_page_id_vps').css('display', 'none');
}

function update_uuid_fields()
{
    uuid_value = $('#id_uuid').val()
    var uuid_array = uuid_value.split('-');
    // Sample: 0-C2-R01G-S2G--825c-1541e2d4fd91
    if (uuid_value != "" && uuid_array.length == 7)
     {

        cpu_limit = parseInt(uuid_array[1].split('C')[1]) - 1
        if (uuid_array[2].indexOf('G')!=-1)
        {
            mem_limit = parseInt(uuid_array[2].split('R')[1].split('G')[0])
        }
        else
        {
            mem_limit = parseInt(uuid_array[2].split('R')[1].split('M')[0])
        }

        storage_limit = parseInt(uuid_array[3].split('S')[1].split('G')[0])
        CPU_LIMIT = cpu_limit
        MEM_LIMIT = mem_limit
        STORAGE_LIMIT = storage_limit
        // alert(MEM_LIMIT)
        // alert('cpu: ' + cpu_limit + "  mem: " + mem_limit + "   storage: " + storage_limit)
        $('#slider-cpu').slider({value:cpu_limit})
        $('#slider-memory').slider({value:mem_to_index(mem_limit)})
        $('#slider-storage').slider({value:storage_to_index(storage_limit)})
        // alert(mem_to_index(storage_limit))
     }
     else
     {
        CPU_LIMIT = 0
        MEM_LIMIT = 0
        STORAGE_LIMIT = 0
     }

}

function index_to_mem(index)
{
    switch(index) {
    case 0:
        return 256;
    case 1:
        return 512;
    case 2:
        return 1024;
    case 3:
        return 2048;
    case 4:
        return 4096;
    case 5:
        return 6144;
    default:
        return null;
    }
}

function mem_to_index(value)
{
    switch(value) {
    case 256:
        return 0;
    case 512:
        return 1;
    case 1:
        return 2;
    case 2:
        return 3;
    case 4:
        return 4;
    case 6:
        return 5;
    default:
        return null;
    }
}

function index_to_storage(index)
{
    switch(index) {
    case 0:
        return 1;
    case 1:
        return 2;
    case 2:
        return 5;
    case 3:
        return 10;
    default:
        return null;
    }
}

function mem_to_MB(value)
{
    switch(value) {
    case 256:
        return 256;
    case 512:
        return 512;
    case 1:
        return 1024;
    case 2:
        return 2048;
    case 4:
        return 4096;
    case 6:
        return 6144;
    default:
        return 256;
    }
}

function storage_to_index(value)
{
    switch(value) {
    case 1:
        return 0;
    case 2:
        return 1;
    case 5:
        return 2;
    case 10:
        return 3;
    default:
        return null;
    }
}

CPU_LIMIT = 0
MEM_LIMIT = 0
STORAGE_LIMIT = 0

function set_limit_drag()
{
      if ((CPU_LIMIT + MEM_LIMIT + STORAGE_LIMIT)!=0)
      {
            if ($('#id_cpu').val() - 1 > CPU_LIMIT)
            {
                $('#slider-cpu').slider({value:CPU_LIMIT})
                $('#quota-exceed-error').velocity({ opacity: 1 }, 0);
            }
            if ($('#id_memory').val() > mem_to_MB(MEM_LIMIT))
            {
                $('#slider-memory').slider({value:mem_to_index(MEM_LIMIT)})
                $('#quota-exceed-error').velocity({ opacity: 1 }, 0);

            }
            if ($('#id_storage').val() > STORAGE_LIMIT)
            {
                $('#slider-storage').slider({value:storage_to_index(STORAGE_LIMIT)})
                //console.log("value of storage: " + $('#id_storage').val() + " Storage Limit = " + STORAGE_LIMIT)
                $('#quota-exceed-error').velocity({ opacity: 1 }, 0);

            }

      }
}

jQuery.fn.onPositionChanged = function (trigger, millis) {
    if (millis == null) millis = 10;
    var o = $(this[0]); // our jquery object
    if (o.length < 1) return o;

    var lastPos = null;
    var lastOff = null;
    setInterval(function () {
        if (o == null || o.length < 1) return o; // abort if element is non existend eny more
        if (lastPos == null) lastPos = o.position();
        if (lastOff == null) lastOff = o.offset();
        var newPos = o.position();
        var newOff = o.offset();
        if (lastPos.top != newPos.top || lastPos.left != newPos.left) {
            $(this).trigger('onPositionChanged', { lastPos: lastPos, newPos: newPos });
            if (typeof (trigger) == "function") trigger(lastPos, newPos);
            lastPos = o.position();
        }
        if (lastOff.top != newOff.top || lastOff.left != newOff.left) {
            $(this).trigger('onOffsetChanged', { lastOff: lastOff, newOff: newOff});
            if (typeof (trigger) == "function") trigger(lastOff, newOff);
            lastOff= o.offset();
        }
    }, millis);

    return o;
};


$(document).ready(function(){
    $('#id_uuid').bind('input propertychange', function() {
        update_uuid_fields()
    })
    var cpu_slider = $(".ui-slider-handle")[0]
    var mem_slider = $(".ui-slider-handle")[1]
    var storage_slider = $(".ui-slider-handle")[2]
    cpu_slider.id = "cpu_slider_id"
    mem_slider.id = "mem_slider_id"
    storage_slider.id = "storage_slider_id"
    // $('#cpu_slider_id').onPositionChanged(function(){set_limit_drag()});
    // $('#mem_slider_id').onPositionChanged(function(){set_limit_drag()});
    // $('#storage_slider_id').onPositionChanged(function(){set_limit_drag()});
    window.setInterval(function(){
     $('#quota-exceed-error').velocity({ opacity: 0 }, 0);
     set_limit_drag()
}, 1000);
})