var received_json;

function reqListener () {
      received_json = this.responseText;
    }

// Send GET request.
function send_request(req_data, _callback) {
    var token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';   // !!! TEMPORARY !!!
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", 'http://127.0.0.1:8000/'+req_data+'/');
    oReq.setRequestHeader('Authorization', 'Token ' + token);
    console.log(token);
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
