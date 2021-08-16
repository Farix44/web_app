var received_json;
var received_token;

function reqListener () {
      received_json = this.responseText;
    }

// Send GET request.
function send_request(req_data, _callback) {
    var token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';   // !!! TEMPORARY !!!
    // var token = received_token;
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", 'http://127.0.0.1:8000/'+req_data+'/');
    oReq.setRequestHeader('Authorization', 'Token ' + token);
    oReq.send();

    _callback;
}

// Display data from project.
function get_data(req_data) {
    send_request(req_data);
    console.log(received_json);
    document.getElementById("request_json").innerHTML = received_json;
}

// Display data from application kredyty.
function get_kredyty_data(req_data) {
    req_data = 'kredyty/' + req_data;
    send_request(req_data);
    console.log(received_json);
    document.getElementById("request_json").innerHTML = received_json;
}

// post test
function post_data() {
    var send_json = {
        "first_name": "Janek",
        "second_name": "Janecki",
        "amount": 4500,
        "period": 10
    };
    var token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';   // !!! TEMPORARY !!!
    //var token = received_token;
    var oReq = new XMLHttpRequest();
    oReq.open("POST", 'http://127.0.0.1:8000/kredyty/loans/');
    oReq.setRequestHeader('Authorization', 'Token ' + token);
    oReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    oReq.send(JSON.stringify(send_json));
}

// logowanie
function login(callback) {
    //var username = 'admin';
    //var password = 'admin';
    var send_json = {
        "username": "admin",
        "password": "admin"
    };

    var oReq = new XMLHttpRequest();
    oReq.onreadystatechange = function() {
        if (oReq.readyState == XMLHttpRequest.DONE) {
            //alert(oReq.responseText);
            //console.log(oReq.responseText);
            received_token = oReq.responseText;
        }
    }
    oReq.open("POST", 'http://127.0.0.1:8000/api-token-auth/');
    oReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    oReq.send(JSON.stringify(send_json));

    console.log(received_token);
}
