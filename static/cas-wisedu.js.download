(function($){
    $(document).ready(function() {
		if($("#username").val()!=""){
            $("#password").focus();
        }else{
            $("#username").focus();
        }
        $("#username").bind("blur",function(){
            getCaptcha();
        });
        $("#password").bind("blur",function(){
            getCaptcha();
        });
        var casLoginForm = $("#casLoginForm") ;
        casLoginForm.submit(doLogin);
        function getCaptcha(){
            if($.trim($("#username").val())!=""&&$("#captchaResponse").length==0){
                $.ajax("needCaptcha.html",{
                    data:{username:$("#username").val()},
                    cache:false,
                    dataType:"text",
                    success:function(data){
						if(data.indexOf("true")>-1){
							$(".last_ipt").removeClass("last_ipt");
                            var casCaptcha = $("#casCaptcha");
                            casCaptcha.empty();
							var chk_no = $("<label>").attr("for","chk_no").text("\u9a8c\u8bc1\u7801\uff1a");
							var captchaResponse = $("<input>").attr("type","text").attr("id","captchaResponse").attr("name","captchaResponse")
								.attr("data-osk-options","disableReturn").attr("class","input_medium validate[required] osk-trigger");
							var img = $("<img>").attr("id","captchaImg").attr("src","captcha.html");
							var changeCaptcha = $("<span>").attr("style","cursor: pointer;color: #1dadff;").attr("id","changeCaptcha").attr("class","chk_text").text("\u6362\u4e00\u5f20");
							casCaptcha.append($("<div>").attr("class","login_ipt_row last_ipt").append(chk_no).append(captchaResponse));
							casCaptcha.append($("<div>").attr("class","login_ipt_row last").append(img).append(changeCaptcha));			
                            $("#changeCaptcha").bind("click",function(){
                                $("#captchaImg").attr("src","captcha.html?ts="+new Date().getMilliseconds());
                            });
                            casCaptcha.fadeIn("slow");
                        }
                    }
                });
			}
        }
		function doLogin(){
            var username =$("#username");
            if(username.val()==""){
                username.addClass("form-error");
                $("#usernameError").addClass("errormsg").text("请输入您的用户名");
                username.focus();
                return false;
            }
            var password = $("#password");
            if(password.val()==""){
                password.addClass("form-error");
                $("#passwordError").addClass("errormsg").text("请输入您的密码");
                password.focus();
                return false;
            }
            var captchaResponse = $("#captchaResponse");
            if(captchaResponse.length>0 && captchaResponse.val()==""){
                captchaResponse.addClass("form-error");
                $("#captchaError").text("请输入验证码");
                captchaResponse.focus();
                return false;
            }
        }
    	
    	$("#language a").bind("click",function() {
    		var b = window.location.href;
    		var c = $(this).data("lang");
    		/\?/.test(b) ? /(\?|\&)locale=([^&]+)/.test(b) ? b = b.replace(
    				/(\?|\&)locale=([^&]+)/, "$1locale=" + c) : b = b + "&locale=" + c
    				: b = b + "?locale=" + c;
    		window.location.href = b;
    	});
    	
       
      
        $("#changeCaptcha").bind("click",function(){
            $("#captchaImg").attr("src","captcha.html?ts="+new Date().getMilliseconds());
        });
    });

})(jQuery);
function GetQueryString(name){
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r!=null) return unescape(r[2]); return null;
}