function createXhr() {
    //判断是否有XMLHttpRequest
    if (window.XMLHttpRequest) {
        var xhr = new XMLHttpRequest();
        // console.log(xhr);
    }
    else {
        var xhr = new ActiveXObjecxt("Microsoft.XMLHTTP");
        // console.log(xhr);
    }
    return xhr;
}

function getXhr() {
    // 创建xhr对象
    var xhr = createXhr();
    // 创建get请求
    // true代表异步
    xhr.open("GET", "/test_xhr_get_server", true);
    // 3.设置回调函数
    xhr.onreadystatechange = function () {
        // 代表xhr对象响应成功,并且服务器端响应正常
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("show").innerHTML = xhr.responseText;
        }
    };
    // 4 发送get请求
    xhr.send(null);
}

//外层函数的作用:保证代码在文档dom元素全部加载完成以后再执行
$(function () {
    $("#btn").click(function () {
        console.log("jQuery发送ajax请求");
        $.ajax({
            url: "/test_xhr_get_server",
            type: "get",
            //res表示服务端返回的数据
            success: function (res) {
                $("#show").html(res);
            }
        })
    })
})



$(function () {
    $("#btn").click(function () {
        console.log("json");
    });
    var json_obj = {
        "username": "aid2010",
        "age": "18",
    };
    console.log(json_obj.username, json_obj.age);
    console.log(json_obj);
    // json数组
    var json_arr = [
        { "name": "tedu", "age": 20, },
        { "name": "tedu", "age": 18, },
    ];
    console.log(json_arr);
    console.log("jQuery遍历json");
    console.log("遍历1");
    $(json_arr).each(function (index, obj) {
        console.log(index, obj.name, obj.age);
    });
    console.log("遍历2");
    $.each(json_arr, function (i, o) {
        console.log(i, o.name, o.age);
    });
});


$(function () {
    $("#btn").click(function () {
        console.log("ajax的post提交")
        var uname = $("#uname").val();
        var pwd = $("#pwd").val();
        var csrf = $("[name='csrfmiddlewaretoken']").val();
        var params = "uname=" + uname + "&pwd=" + pwd + "&csrfmiddlewaretoken=" + csrf;
        console.log(params);
        $.ajax({
            url: "/register",
            type: "post",
            data: params,
            success: function (res) {
                console.log(res);
            }
        });
    });
});