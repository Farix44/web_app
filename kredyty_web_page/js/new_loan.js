var received_json;
var rec_json_obj;
// var admin_token = '8e1255930fd977816260fde8df8f27ca12249806';
var received_token;

// przy wczytywaniu strony pobiera token
window.addEventListener( "load", function () {
    getToken();
} );

// wysyłanie nowego wniosku (POST)
function submitNewLoan() {
    var data = getFormData();
    var json = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:8000/kredyty/loans/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + received_token);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
        if (xhr.readyState == 4 && xhr.status == "200") {
            //console.table(users);
        } else {
            //console.error(users);
        }
    }
    xhr.send(json);
}

// pobieranie danych z formularza do obiektu
function getFormData() {
    var elements = document.getElementById("add_new_loan_form").elements;
    var obj ={};
    for(var i = 0 ; i < elements.length ; i++){
        var item = elements.item(i);
        obj[item.name] = item.value;
    }
    // console.log(JSON.stringify(obj));
    return obj;
}

// pobieranie tokenu admina
function getToken(callback) {
    var send_json = {
        "username": "admin",
        "password": "admin"
    };
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:8000/api-token-auth/', true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                received_token = JSON.parse(xhr.responseText)['token']
            } else {
                console.error(xhr.statusText);
            }
        }
    };
    xhr.onerror = function (e) {
        console.error(xhr.statusText);
    };
    xhr.send(JSON.stringify(send_json));
}