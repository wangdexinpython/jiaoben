import execjs


resp = ''' function mandyAjax(jsonData, url, style) {
    var backJson;
    if (JSON.stringify(jsonData) != "{}") {
        var myToken = md_getCookie("myToken");
        if (!myToken) {
            myToken = "null"
        }
        var data = new Date().getTime()
        var mySign = mandy_md5(myToken + data + "dac203b84f1c11e7a4dbd43d7e0f045c");
        var newUrl = SSlocalhostPaht + url;
        var jsonstring = '{"encrypt":"1","cdpDate":"' + md_Encrypt(data) + '","token":"' + md_Encrypt(myToken) + '","sign":"' + md_Encrypt(mySign) + '"';
        for (var i in jsonData) {
            if (jsonData[i] != null || jsonData[i] != undefined) {
                jsonstring += ',"' + i + '":"' + md_Encrypt(jsonData[i]) + '"'
            }
        }
        jsonstring += '}';
        jsonstring = JSON.parse(jsonstring);
    } else {
        var jsonstring = '';
        var myToken = md_getCookie("myToken");
        var data = new Date().getTime()
        var mySign = mandy_md5(myToken + data + "dac203b84f1c11e7a4dbd43d7e0f045c");
        var newUrl = SSlocalhostPaht + url + "?cdpDate=" + data + "&token=" + myToken + "&sign=" + mySign;
    }
    $.ajax({
        type: style,
        async: false,
        url: newUrl,
        data: jsonstring,
        success: function (res) {
            /*if(res.code=="ALL_0024"){
                window.location.href=SSlocalhostPaht+'/viewJsp/login.jsp'
            }else{
                backJson = res;
            }*/
            backJson = res;
        }
    });
    return backJson;

}
'''

content = execjs.eval(resp)
# status = content['status']
print(content)


'''
encrypt:1 解决


cdpDate:uv0XlMGBtx/mYSxIrs+JPg==

var data = new Date().getTime()
"cdpDate":"' + md_Encrypt(data) + 

function md_Encrypt(word) {
    word = word + "";
    var key = CryptoJS.enc.Latin1.parse('h8mlhE538fmao8Np');
    var iv = CryptoJS.enc.Latin1.parse('h8mlhE538fmao8Np');
    var encrypted = CryptoJS.AES.encrypt(word, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return encrypted.toString();
}






token:NWuPw+1kpuAOLk5ufIwB3A==

function md_getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

    if (arr = document.cookie.match(reg))

        return (arr[2]);
    else
        return null;
}
var myToken = md_getCookie("myToken");

"token":"' + md_Encrypt(myToken) + '
function md_Encrypt(word) {
    word = word + "";
    var key = CryptoJS.enc.Latin1.parse('h8mlhE538fmao8Np');
    var iv = CryptoJS.enc.Latin1.parse('h8mlhE538fmao8Np');
    var encrypted = CryptoJS.AES.encrypt(word, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return encrypted.toString();
}


sign:OSrDOREe0zo65rDZI3JLuNLuPUWwaWeZHnz2sWMIhPE=
page:gjGIigAEqLMxUHJsQsDIww==
pageSize:ORYL5P5EIJpP6rXsw8AG7Q==

'''










'''
RegExp("(^| )" + name + "=([^;]*)(;|$)");


'''