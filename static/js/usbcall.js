/**
 * Created by Administrator on 2018/4/17.
 */

//        配置接口参数
        callnum=$("sendText");   //电话号码
        txtout=$("txtContent")   //状态输出
        call=$("btnCall");            //拨打
        answer=$("btnAnswer");//接听
        stop= $("btnStop");       //挂断
        signal=$('signal')          //信号
        mess=$('butmess')          //短信
        messinput=$("txtmess")       //输入短信

//响应事件！
        call.onclick=function(){socket.send("call"+callnum.value)};
        answer.onclick=function (){socket.send("answer")};
        stop.onclick=function (){socket.send("stop")};
        signal.onclick=function (){socket.send("signal")};
        mess.onclick=function (){socket.send("mess"+callnum.value+"|"+messinput.value)};
        var socket;

        function connect() {
            var host = "ws://127.0.0.1:9083/"
            try {
                socket = new WebSocket(host);
            }
            catch (ex) {
                alert("请确认本地服务是否正确打开！")
                return
            }

            try {
                socket.onopen = function (msg) {
                    displayContent("连接成功！")
                };

                socket.onmessage = function (msg) {
                    if (typeof msg.data == "string") {
                        if (msg.data=='0'){$("btnSend").disabled =true;displayContent('打开设备失败!')}
                        else{displayContent(msg.data);}
                    }
                    else {
                        displayContent("非文本消息");
                    }
                };
                socket.onclose = function (msg) { displayContent("本地服务关闭,刷新页面重新连接!"); call.disabled=true;answer.disabled=true;stop.disabled=true;signal.disabled=true;mess.disabled=true;};
            }
            catch (ex) {
                log(ex);
            }
        }


        window.onbeforeunload = function () {
            try {
                socket.close();
                socket = null;
            }
            catch (ex) {
            }
        };

        function $(id) { return document.getElementById(id); }

        function displayContent(msg) {
            txtout.value =  msg;
        }
        connect()