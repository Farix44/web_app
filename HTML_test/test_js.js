var received_json;

function reqListener () {
      received_json = this.responseText;
    }

function send_request(req_data, _callback) {
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", 'http://127.0.0.1:8000/'+req_data+'/');
    oReq.send();

    _callback;
}

function get_data(req_data) {
    send_request(req_data);

    console.log(received_json)
    document.getElementById("request_json").innerHTML = received_json;
}
