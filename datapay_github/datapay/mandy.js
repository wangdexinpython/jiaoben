// 补充包
var http = require('http');
var querystring = require('querystring');
var CryptoJS = require('crypto-js')
//补充运行的变量
var SSlocalhostPaht="https://www.chinadatapay.com:443";

//json2.js开始 使Json兼容ie6 7 8
var JSON;
if (!JSON) {
    JSON = {};
}
(function () {
    'use strict';
    function f(n) {
        return n < 10 ? '0' + n : n;
    }

    if (typeof Date.prototype.toJSON !== 'function') {
        Date.prototype.toJSON = function (key) {
            return isFinite(this.valueOf())
                ? this.getUTCFullYear() + '-' +
            f(this.getUTCMonth() + 1) + '-' +
            f(this.getUTCDate()) + 'T' +
            f(this.getUTCHours()) + ':' +
            f(this.getUTCMinutes()) + ':' +
            f(this.getUTCSeconds()) + 'Z'
                : null;
        };
        String.prototype.toJSON =
            Number.prototype.toJSON =
                Boolean.prototype.toJSON = function (key) {
                    return this.valueOf();
                };
    }
    var cx = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        escapable = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        gap = "",
        indent = "",
        meta = {    // table of character substitutions
            '\b': '\\b',
            '\t': '\\t',
            '\n': '\\n',
            '\f': '\\f',
            '\r': '\\r',
            '"': '\\"',
            '\\': '\\\\'
        },
        rep = "";

    function quote(string) {
        escapable.lastIndex = 0;
        return escapable.test(string) ? '"' + string.replace(escapable, function (a) {
            var c = meta[a];
            return typeof c === 'string'
                ? c
                : '\\u' + ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
        }) + '"' : '"' + string + '"';
    }

    function str(key, holder) {
        var i,          // The loop counter.
            k,          // The member key.
            v,          // The member value.
            length,
            mind = gap,
            partial,
            value = holder[key];
        if (value && typeof value === 'object' &&
            typeof value.toJSON === 'function') {
            value = value.toJSON(key);
        }
        if (typeof rep === 'function') {
            value = rep.call(holder, key, value);
        }
        switch (typeof value) {
            case 'string':
                return quote(value);

            case 'number':
                return isFinite(value) ? String(value) : 'null';

            case 'boolean':
            case 'null':
                return String(value);
            case 'object':
                if (!value) {
                    return 'null';
                }
                gap += indent;
                partial = [];
                if (Object.prototype.toString.apply(value) === '[object Array]') {
                    length = value.length;
                    for (i = 0; i < length; i += 1) {
                        partial[i] = str(i, value) || 'null';
                    }
                    v = partial.length === 0
                        ? '[]'
                        : gap
                        ? '[\n' + gap + partial.join(',\n' + gap) + '\n' + mind + ']'
                        : '[' + partial.join(',') + ']';
                    gap = mind;
                    return v;
                }
                if (rep && typeof rep === 'object') {
                    length = rep.length;
                    for (i = 0; i < length; i += 1) {
                        if (typeof rep[i] === 'string') {
                            k = rep[i];
                            v = str(k, value);
                            if (v) {
                                partial.push(quote(k) + (gap ? ': ' : ':') + v);
                            }
                        }
                    }
                } else {
                    for (k in value) {
                        if (Object.prototype.hasOwnProperty.call(value, k)) {
                            v = str(k, value);
                            if (v) {
                                partial.push(quote(k) + (gap ? ': ' : ':') + v);
                            }
                        }
                    }
                }
                v = partial.length === 0
                    ? '{}'
                    : gap
                    ? '{\n' + gap + partial.join(',\n' + gap) + '\n' + mind + '}'
                    : '{' + partial.join(',') + '}';
                gap = mind;
                return v;
        }
    }

    if (typeof JSON.stringify !== 'function') {
        JSON.stringify = function (value, replacer, space) {
            var i;
            gap = '';
            indent = '';
            if (typeof space === 'number') {
                for (i = 0; i < space; i += 1) {
                    indent += ' ';
                }
            } else if (typeof space === 'string') {
                indent = space;
            }
            rep = replacer;
            if (replacer && typeof replacer !== 'function' &&
                (typeof replacer !== 'object' ||
                typeof replacer.length !== 'number')) {
                throw new Error('JSON.stringify');
            }
            return str('', {'': value});
        };
    }
    if (typeof JSON.parse !== 'function') {
        JSON.parse = function (text, reviver) {
            var j;

            function walk(holder, key) {
                var k = "", v, value = holder[key];
                if (value && typeof value === 'object') {
                    for (k in value) {
                        if (Object.prototype.hasOwnProperty.call(value, k)) {
                            v = walk(value, k);
                            if (v !== undefined) {
                                value[k] = v;
                            } else {
                                delete value[k];
                            }
                        }
                    }
                }
                return reviver.call(holder, key, value);
            }

            text = String(text);
            cx.lastIndex = 0;
            if (cx.test(text)) {
                text = text.replace(cx, function (a) {
                    return '\\u' +
                        ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
                });
            }
            if (/^[\],:{}\s]*$/
                    .test(text.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, '@')
                        .replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']')
                        .replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {
                j = eval('(' + text + ')');
                return typeof reviver === 'function'
                    ? walk({'': j}, '')
                    : j;
            }
            throw new SyntaxError('JSON.parse');
        };
    }
}());
//json2.js结束
//原生ajax
//创建http
function createXMLHTTPRequest() {
    //1.创建XMLHttpRequest对象
    //这是XMLHttpReuquest对象无部使用中最复杂的一步
    //需要针对IE和其他类型的浏览器建立这个对象的不同方式写不同的代码
    var xmlHttpRequest;
    if (window.XMLHttpRequest) {
        //针对FireFox，Mozillar，Opera，Safari，IE7，IE8
        xmlHttpRequest = new XMLHttpRequest();
        //针对某些特定版本的mozillar浏览器的BUG进行修正
        if (xmlHttpRequest.overrideMimeType) {
            xmlHttpRequest.overrideMimeType("text/xml");
        }
    } else if (window.ActiveXObject) {
        //针对IE6，IE5.5，IE5
        //两个可以用于创建XMLHTTPRequest对象的控件名称，保存在一个js的数组中
        //排在前面的版本较新
        var activexName = ["MSXML2.XMLHTTP", "Microsoft.XMLHTTP"];
        for (var i = 0; i < activexName.length; i++) {
            try {
                //取出一个控件名进行创建，如果创建成功就终止循环
                //如果创建失败，回抛出异常，然后可以继续循环，继续尝试创建
                xmlHttpRequest = new ActiveXObject(activexName[i]);
                if (xmlHttpRequest) {
                    break;
                }
            } catch (e) {
            }
        }
    }
    return xmlHttpRequest;
}
//原生ajax结束
function getParameter(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return decodeURI(r[2]);
    }
    return null;
}
function changeURLArg(url, arg, arg_val) {
    var pattern = arg + "=([^&]*)";
    var replaceText = arg + "=" + arg_val;
    if (url.match(pattern)) {
        var tmp = "/(" + arg + "=)([^&]*)/gi";
        tmp = url.replace(eval(tmp), replaceText);
        return tmp;
    } else {
        if (url.match("[?]")) {
            return url + "&" + replaceText;
        } else {
            return url + "?" + replaceText;
        }
    }
    return url + "\n" + arg + "\n" + arg_val;
}
//替换或增加URL中的参数
function changeURLPar(destiny, par, par_value) {
    var pattern = par + '=([^&]*)';
    var replaceText = par + '=' + par_value;
    if (destiny.match(pattern)) {
        var tmp = '/\\' + par + '=[^&]*/';
        tmp = destiny.replace(eval(tmp), replaceText);
        return (tmp);
    }
    else {
        if (destiny.match('[\?]')) {
            return destiny + '&' + replaceText;
        }
        else {
            return destiny + '?' + replaceText;
        }
    }
    return destiny + '\n' + par + '\n' + par_value;
}
// 设置json参数
// jsonStr:原先json的数据
// name:需要设置的参数
// value:所需设置参数的属性
function setJson(jsonStr, name, value) {
    // if (!jsonStr) jsonStr = "{}";
    // var jsonObj = JSON.parse(jsonStr);
    jsonStr[name] = value;
    return JSON.stringify(jsonStr);
}

//获取table表格 里面的数据转成json对象
//labels为table里的标签数组
function countApi_table(id, labels) {
    var trList = $("#" + id).find("tr:has(td)");
    var tdList, tdValue;
    var tdListValue = {};
    var list = [];
    for (var i = 0; i < trList.length; i++) {
        tdList = trList.eq(i).find("td");
        for (var m = 0; m < labels.length; m++) {
            tdValue = tdList.eq(m).text();
            tdListValue = $.parseJSON(setJson(tdListValue, labels[m], tdValue));
        }
        list.push(tdListValue);
        tdListValue = {};
    }
    //console.log(list);
    return list;
}

function isPhone2(str) {
    var reg = /(^13\d{9}$)|(^14)[5,7]\d{8}$|(^15\d{9}$)|(^17)[0,3,5,6,7,8]\d{8}$|(^18\d{9}$)/g ;
    return reg.test(str);
}
function isPhone(str) {
    var reg = /^1([34689][0-9]|5[0-35-9]|7[1-9])\d{8}$/g;
    return reg.test(str);
}
function isEmail(str) {
    var reg = /^([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/gi;
    return reg.test(str);
}
function isUserName(str) {
    var _result;
    if (str.length < 6) {
        _result = false;
    } else {
        var reg = /^[A-Za-z]([A-Za-z].*[0-9]|[0-9].*[A-Za-z]|[0-9])/;
        _result = reg.test(str);
    }
    return _result;
}
//验证密码 6-16位字母数字组合
function isPsw(str) {
    var _result;
    if (str.length < 6 || str.length > 16) {
        _result = false;
    } else {
        var reg = /[A-Za-z].*[0-9]|[0-9].*[A-Za-z]|[0-9]/;
        _result = reg.test(str);
    }
    return _result;
}

function validPsw(id) {
    var num = 0;
    var number = 0;
    var letter = 0;
    var bigLetter = 0;
    var chars = 0;
    var tips = "";
    var password = $.trim($(id).val());
    if (password.search(/[0-9]/) != -1) {
        num += 1;
        number = 1;
    }
    if (password.search(/[A-Z]/) != -1) {
        num += 1;
        bigLetter = 1;
    }
    if (password.search(/[a-z]/) != -1) {
        num += 1;
        letter = 1;
    }
    if (password.search(/[^A-Za-z0-9]/) != -1) {
        num += 1;
        chars = 1;
    }
    if (num >= 2 && (password.length >= 6 && password.length <= 16)) {
        tips = "ok";
    } else if (password.length < 6 || password.length > 16) {
        tips = "密码由6-16个字符组成!";
    } else if (num == 1) {
        if (number == 1) {
            tips = "密码不能全为数字!";
        }
        if (letter == 1) {
            tips = "密码不能全为字母!";
        }
        if (bigLetter == 1) {
            tips = "密码不能全为字母!";
        }
        if (chars == 1) {
            tips = "密码不能全为字符!";
        }
    }
    return tips;
}
//验证事件
//time:2016-09-18
//输入框事例：<input type="password" id="comPwd" name="pwd" data-tip="确认密码" required="required" data-options="required:required,equal:newPwd">
//data-tip：当前输入框的名称，起到弹出层提示具体某个字段用途
//required="required"：需要验证的标识符，起到检索的用途
//data-options：包含了所有需要验证的属性
//data-options——required:required：验证是否为空
//data-options——equal:newPwd：验证是否一致，事例newPwd为某个输入框的属性id，通过此id可进行2个输入框的一致验证
function submitCheck(e) {
    var input = $(e).find(".form-control[required='required']");//获取所有需要验证的输入框
    for (var i = 0; i < input.length; i++) {//循环所有需要验证的输入框
        //获取当前验证框的验证属性对象
        //属性事例:["required:required","equal:newPwd"]
        for (var k = 0; k < input[i].attributes.length; k++) {
            switch (input[i].attributes[k].name) {
                case "dataoptions":
                    var option = input[i].attributes[k].value.split(",")//切割data-options的验证属性
                    break;
                case "datatip":
                    var tip = input[i].attributes[k].nodeValue;//当前验证框的焦点名称，弹出层提示需用到，例如：账户名，密码
                    break;
                case "id":
                    var node = input[i].attributes[k].nodeValue;//当前验证框的属性id，通过id来将弹出层定位在当前验证框后面
                    break;
            }
        }

        //var option = input[i].attributes[1].value.split(",")
        for (var j = 0; j < option.length; j++) {
            //var tip = input[i].attributes[3].nodeValue;//当前验证框的焦点名称，弹出层提示需用到，例如：账户名，密码
            //var node = input[i].attributes[7].nodeValue;//当前验证框的属性id，通过id来将弹出层定位在当前验证框后面
            var val = input[i].value;//当前验证框的值
            //获取验证框属性，通过:切割，获取第一位参数，即实现的验证方法
            //required：验证是否为空
            //type：验证某个类型,mobile,email,PositiveNum
            //equal：验证是否和某个字段参数相同
            switch (option[j].split(":")[0]) {
                case "required":
                    if (val == "") {
                        layer.alert(tip + '不能为空！');
                        return false;
                    }
                    break;
                case "type":
                    var tpNode = option[j].split(":")[1];//获取需要验证的类型
                    if (tpNode == "mobile") {
                        if (!isMobile(val)) {//调用验证手机号码方法，如果不符合，!isMobile(val)为true，进入验证提示
                            layer.alert('手机号码不合法！');
                            return false;
                        }
                    } else if (tpNode == "PositiveNum") {
                        if (!isPositiveNum(val)) {//调用验证正整数方法，如果不符合，!isPositiveNum(val)为true，进入验证提示
                            layer.alert(tip + '请填写正整数');
                            return false;
                        }
                    }
                    break;
                case "equal":
                    var eqNode = option[j].split(":")[1];//获取需要验证是否一致的输入框的属性id

                    if (val != document.getElementById(eqNode).value) {//$("#"+eqNode).val().trim()：jquery写法，获取验证一致的输入框的值
                        layer.alert(tip + '不相同！');
                        return false;
                    }
                    break;
            }
        }
    }
    return true;
}
function isPositiveNum(s) {//是否为正整数
    var re = /^[0-9]*[1-9][0-9]*$/;
    return re.test(s);
}
function isCardNo(s) {
    // 身份证号码为15位或者18位，15位时全为数字，18位前17位为数字，最后一位是校验位，可能为数字或字符X
    var re = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
    return re.test(s);
}

function isLegal(s) {//是否含<>号 防脚本注入
    var re = /<[^<]+>/;
    return re.test(s);
}

function getTime(t) {
    //var time = parseInt(t.substring(6, 19));
    var date = new Date(t);
    Y = date.getFullYear() + '-';
    M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
    D = (date.getDate() < 10 ? "0" + date.getDate() : date.getDate()) + " ";
    h = (date.getHours() < 10 ? "0" + date.getHours() : date.getHours()) + ':';
    m = (date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes()) + ':';
    s = (date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds());
    return Y + M + D + h + m + s;
}

function getTimeDay(t) {
    //var time = parseInt(t.substring(6, 19));
    var date = new Date(t);
    Y = date.getFullYear() + '-';
    M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
    D = (date.getDate() < 10 ? "0" + date.getDate() : date.getDate()) + " ";
    return Y + M + D;
}
//md5加密
function mandy_md5(string) {
    function md5_RotateLeft(lValue, iShiftBits) {
        return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits));
    }

    function md5_AddUnsigned(lX, lY) {
        var lX4, lY4, lX8, lY8, lResult;
        lX8 = (lX & 0x80000000);
        lY8 = (lY & 0x80000000);
        lX4 = (lX & 0x40000000);
        lY4 = (lY & 0x40000000);
        lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
        if (lX4 & lY4) {
            return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
        }
        if (lX4 | lY4) {
            if (lResult & 0x40000000) {
                return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
            } else {
                return (lResult ^ 0x40000000 ^ lX8 ^ lY8);
            }
        } else {
            return (lResult ^ lX8 ^ lY8);
        }
    }

    function md5_F(x, y, z) {
        return (x & y) | ((~x) & z);
    }

    function md5_G(x, y, z) {
        return (x & z) | (y & (~z));
    }

    function md5_H(x, y, z) {
        return (x ^ y ^ z);
    }

    function md5_I(x, y, z) {
        return (y ^ (x | (~z)));
    }

    function md5_FF(a, b, c, d, x, s, ac) {
        a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_F(b, c, d), x), ac));
        return md5_AddUnsigned(md5_RotateLeft(a, s), b);
    };
    function md5_GG(a, b, c, d, x, s, ac) {
        a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_G(b, c, d), x), ac));
        return md5_AddUnsigned(md5_RotateLeft(a, s), b);
    };
    function md5_HH(a, b, c, d, x, s, ac) {
        a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_H(b, c, d), x), ac));
        return md5_AddUnsigned(md5_RotateLeft(a, s), b);
    };
    function md5_II(a, b, c, d, x, s, ac) {
        a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_I(b, c, d), x), ac));
        return md5_AddUnsigned(md5_RotateLeft(a, s), b);
    };
    function md5_ConvertToWordArray(string) {
        var lWordCount;
        var lMessageLength = string.length;
        var lNumberOfWords_temp1 = lMessageLength + 8;
        var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
        var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
        var lWordArray = Array(lNumberOfWords - 1);
        var lBytePosition = 0;
        var lByteCount = 0;
        while (lByteCount < lMessageLength) {
            lWordCount = (lByteCount - (lByteCount % 4)) / 4;
            lBytePosition = (lByteCount % 4) * 8;
            lWordArray[lWordCount] = (lWordArray[lWordCount] | (string.charCodeAt(lByteCount) << lBytePosition));
            lByteCount++;
        }
        lWordCount = (lByteCount - (lByteCount % 4)) / 4;
        lBytePosition = (lByteCount % 4) * 8;
        lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition);
        lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
        lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
        return lWordArray;
    };
    function md5_WordToHex(lValue) {
        var WordToHexValue = "", WordToHexValue_temp = "", lByte, lCount;
        for (lCount = 0; lCount <= 3; lCount++) {
            lByte = (lValue >>> (lCount * 8)) & 255;
            WordToHexValue_temp = "0" + lByte.toString(16);
            WordToHexValue = WordToHexValue + WordToHexValue_temp.substr(WordToHexValue_temp.length - 2, 2);
        }
        return WordToHexValue;
    };
    function md5_Utf8Encode(string) {
        string = string.replace(/\r\n/g, "\n");
        var utftext = "";
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else if ((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            } else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }
        }
        return utftext;
    };
    var x = Array();
    var k, AA, BB, CC, DD, a, b, c, d;
    var S11 = 7, S12 = 12, S13 = 17, S14 = 22;
    var S21 = 5, S22 = 9, S23 = 14, S24 = 20;
    var S31 = 4, S32 = 11, S33 = 16, S34 = 23;
    var S41 = 6, S42 = 10, S43 = 15, S44 = 21;
    string = md5_Utf8Encode(string);
    x = md5_ConvertToWordArray(string);
    a = 0x67452301;
    b = 0xEFCDAB89;
    c = 0x98BADCFE;
    d = 0x10325476;
    for (k = 0; k < x.length; k += 16) {
        AA = a;
        BB = b;
        CC = c;
        DD = d;
        a = md5_FF(a, b, c, d, x[k + 0], S11, 0xD76AA478);
        d = md5_FF(d, a, b, c, x[k + 1], S12, 0xE8C7B756);
        c = md5_FF(c, d, a, b, x[k + 2], S13, 0x242070DB);
        b = md5_FF(b, c, d, a, x[k + 3], S14, 0xC1BDCEEE);
        a = md5_FF(a, b, c, d, x[k + 4], S11, 0xF57C0FAF);
        d = md5_FF(d, a, b, c, x[k + 5], S12, 0x4787C62A);
        c = md5_FF(c, d, a, b, x[k + 6], S13, 0xA8304613);
        b = md5_FF(b, c, d, a, x[k + 7], S14, 0xFD469501);
        a = md5_FF(a, b, c, d, x[k + 8], S11, 0x698098D8);
        d = md5_FF(d, a, b, c, x[k + 9], S12, 0x8B44F7AF);
        c = md5_FF(c, d, a, b, x[k + 10], S13, 0xFFFF5BB1);
        b = md5_FF(b, c, d, a, x[k + 11], S14, 0x895CD7BE);
        a = md5_FF(a, b, c, d, x[k + 12], S11, 0x6B901122);
        d = md5_FF(d, a, b, c, x[k + 13], S12, 0xFD987193);
        c = md5_FF(c, d, a, b, x[k + 14], S13, 0xA679438E);
        b = md5_FF(b, c, d, a, x[k + 15], S14, 0x49B40821);
        a = md5_GG(a, b, c, d, x[k + 1], S21, 0xF61E2562);
        d = md5_GG(d, a, b, c, x[k + 6], S22, 0xC040B340);
        c = md5_GG(c, d, a, b, x[k + 11], S23, 0x265E5A51);
        b = md5_GG(b, c, d, a, x[k + 0], S24, 0xE9B6C7AA);
        a = md5_GG(a, b, c, d, x[k + 5], S21, 0xD62F105D);
        d = md5_GG(d, a, b, c, x[k + 10], S22, 0x2441453);
        c = md5_GG(c, d, a, b, x[k + 15], S23, 0xD8A1E681);
        b = md5_GG(b, c, d, a, x[k + 4], S24, 0xE7D3FBC8);
        a = md5_GG(a, b, c, d, x[k + 9], S21, 0x21E1CDE6);
        d = md5_GG(d, a, b, c, x[k + 14], S22, 0xC33707D6);
        c = md5_GG(c, d, a, b, x[k + 3], S23, 0xF4D50D87);
        b = md5_GG(b, c, d, a, x[k + 8], S24, 0x455A14ED);
        a = md5_GG(a, b, c, d, x[k + 13], S21, 0xA9E3E905);
        d = md5_GG(d, a, b, c, x[k + 2], S22, 0xFCEFA3F8);
        c = md5_GG(c, d, a, b, x[k + 7], S23, 0x676F02D9);
        b = md5_GG(b, c, d, a, x[k + 12], S24, 0x8D2A4C8A);
        a = md5_HH(a, b, c, d, x[k + 5], S31, 0xFFFA3942);
        d = md5_HH(d, a, b, c, x[k + 8], S32, 0x8771F681);
        c = md5_HH(c, d, a, b, x[k + 11], S33, 0x6D9D6122);
        b = md5_HH(b, c, d, a, x[k + 14], S34, 0xFDE5380C);
        a = md5_HH(a, b, c, d, x[k + 1], S31, 0xA4BEEA44);
        d = md5_HH(d, a, b, c, x[k + 4], S32, 0x4BDECFA9);
        c = md5_HH(c, d, a, b, x[k + 7], S33, 0xF6BB4B60);
        b = md5_HH(b, c, d, a, x[k + 10], S34, 0xBEBFBC70);
        a = md5_HH(a, b, c, d, x[k + 13], S31, 0x289B7EC6);
        d = md5_HH(d, a, b, c, x[k + 0], S32, 0xEAA127FA);
        c = md5_HH(c, d, a, b, x[k + 3], S33, 0xD4EF3085);
        b = md5_HH(b, c, d, a, x[k + 6], S34, 0x4881D05);
        a = md5_HH(a, b, c, d, x[k + 9], S31, 0xD9D4D039);
        d = md5_HH(d, a, b, c, x[k + 12], S32, 0xE6DB99E5);
        c = md5_HH(c, d, a, b, x[k + 15], S33, 0x1FA27CF8);
        b = md5_HH(b, c, d, a, x[k + 2], S34, 0xC4AC5665);
        a = md5_II(a, b, c, d, x[k + 0], S41, 0xF4292244);
        d = md5_II(d, a, b, c, x[k + 7], S42, 0x432AFF97);
        c = md5_II(c, d, a, b, x[k + 14], S43, 0xAB9423A7);
        b = md5_II(b, c, d, a, x[k + 5], S44, 0xFC93A039);
        a = md5_II(a, b, c, d, x[k + 12], S41, 0x655B59C3);
        d = md5_II(d, a, b, c, x[k + 3], S42, 0x8F0CCC92);
        c = md5_II(c, d, a, b, x[k + 10], S43, 0xFFEFF47D);
        b = md5_II(b, c, d, a, x[k + 1], S44, 0x85845DD1);
        a = md5_II(a, b, c, d, x[k + 8], S41, 0x6FA87E4F);
        d = md5_II(d, a, b, c, x[k + 15], S42, 0xFE2CE6E0);
        c = md5_II(c, d, a, b, x[k + 6], S43, 0xA3014314);
        b = md5_II(b, c, d, a, x[k + 13], S44, 0x4E0811A1);
        a = md5_II(a, b, c, d, x[k + 4], S41, 0xF7537E82);
        d = md5_II(d, a, b, c, x[k + 11], S42, 0xBD3AF235);
        c = md5_II(c, d, a, b, x[k + 2], S43, 0x2AD7D2BB);
        b = md5_II(b, c, d, a, x[k + 9], S44, 0xEB86D391);
        a = md5_AddUnsigned(a, AA);
        b = md5_AddUnsigned(b, BB);
        c = md5_AddUnsigned(c, CC);
        d = md5_AddUnsigned(d, DD);
    }
    return (md5_WordToHex(a) + md5_WordToHex(b) + md5_WordToHex(c) + md5_WordToHex(d)).toLowerCase();
}
function md_setCookie(name, value, time) {
    if (md_getCookie(name)) {
        md_delCookie(name)
    }//如果已经存在，就删除之后再设置
    var strsec = md_getsec(time);
    var exp = new Date();
    exp.setTime(exp.getTime() + strsec * 1);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString() + "; path=/";
    //document.cookie=c_name+ "=" +escape(value)+ (expiredays==null) ? "" : ";expires="+exdate.toGMTString())+"; path=/";
}
function md_getsec(str) {

    var str1 = str.substring(1, str.length) * 1;
    var str2 = str.substring(0, 1);
    if (str2 == "s") {
        return str1 * 1000;
    }
    else if (str2 == "h") {
        return str1 * 60 * 60 * 1000;
    }
    else if (str2 == "d") {
        return str1 * 24 * 60 * 60 * 1000;
    }
}
//这是有设定过期时间的使用示例：
//s20是代表20秒
//h是指小时，如12小时则是：h12
//d是天数，30天则：d30
//md_setCookie("name","hayden","s20");
//读取cookies
function md_getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

    //if (arr = document.cookie.match(reg))

      //  return (arr[2]);
    //else
    //    return null;
    return null
}

//删除cookies
function md_delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = md_getCookie(name);
    if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}
//时间戳转化为日期
function getLocalTime(nS) {
    var str = "";
    var time = new Date(parseInt(nS));
    str = time.getFullYear() + '年' + (parseInt(time.getMonth()) + 1) + '月' + time.getDate() + '日';
    return str;
}
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
function mandyAjax(jsonData, url, style) {
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

        console.log(mySign);
        console.log(myToken);
        console.log(newUrl);
        console.log(jsonstring);

    } else {
        var jsonstring = '';
        var myToken = md_getCookie("myToken");
        var data = new Date().getTime();
        var mySign = mandy_md5(myToken + data + "dac203b84f1c11e7a4dbd43d7e0f045c");
        var newUrl = SSlocalhostPaht + url + "?cdpDate=" + data + "&token=" + myToken + "&sign=" + mySign;
        console.log(data);
        console.log(mySign);
        console.log(newUrl);
    }

   /*$.ajax({
        type: style,
        async: false,
        url: newUrl,
        data: jsonstring,
        success: function (res) {
            if(res.code=="ALL_0024"){
                window.location.href=SSlocalhostPaht+'/viewJsp/login.jsp'
            }else{
                backJson = res;
            }
            backJson = res;
        }
    }
  );*/
    //return backJson;
}
//页面购买弹出框
function openBuyBox(interfaceId, apiName) {
    layer.open({
        type: 2,
        title: [apiName, 'font-size:18px;'],
        shadeClose: true,
        shade: 0.8,
        area: ['800px', '500px'],
        content: SSlocalhostPaht + '/userCenter/buyBox.jsp?interfaceId=' + interfaceId
    })
}
function md_isLogin() {
    var str = mandyAjax({}, "/memberShip/isLoginState", "post");
    return str;
}

//去空  例：$.trim(str)
String.prototype.trim = function () {
    return this.replace(/(^\s*)|(\s*$)/g, "");
}

//获取select下拉框值
function getList(idName, industryId) {
    var res = mandyAjax({industryId: industryId}, "/dataApi/audit/industry", "post");
    if (res.success) {
        var nameOpt = document.getElementById(idName);
        for (i in res.industrys) {
            nameOpt[i] = new Option(res.industrys[i].industryName, res.industrys[i].industryId)
        }
    }
}

//获取图形验证码 getCode("identycode")
function getCode(ID) {
    $("#" + ID).attr("src", SSlocalhostPaht + "/memberShip/code?" + Math.random());
}

//页面登录
function LoinPage() {
    layer.confirm("请先登录", {btn: ['确定', '取消']}, function () {
        layer.open({
            type: 2,
            title: '数据宝登录',
            shadeClose: true,
            shade: 0.8,
            area: ['450px', '520px'],
            content: SSlocalhostPaht + '/viewJsp/pageLogin.jsp?v='+SSversion
        });
    });
}
//layer插件页面登录后重新加载
function reLoadPage() {
    window.location.reload();
}

// 向外暴露函数
module.exports = mandyAjax;
