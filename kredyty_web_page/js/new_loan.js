var received_json;
var rec_json_obj;
var received_token;
var url = 'http://127.0.0.1:8000/api/';

// przy wczytywaniu strony pobiera token
window.addEventListener( "load", function () {
    getToken();
} );

// wysyłanie nowego wniosku (POST)
function submitNewLoan() {
    var data = getFormData();
    var json = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url+'kredyty/loans/', true);
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
    return false;
}

// pobieranie danych z formularza do obiektu
function getFormData() {
    var elements = document.getElementById("add_new_loan_form").elements;
    var obj ={};
    for(var i = 0 ; i < elements.length ; i++){
        var item = elements.item(i);
        obj[item.name] = item.value;
    }
     console.log(JSON.stringify(obj));
    return obj;
}

// pobieranie tokenu admina
function getToken(callback) {
    var send_json = {
        "username": "admin",
        "password": "admin"
    };
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url+'api-token-auth/', true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                received_token = JSON.parse(xhr.responseText)['token']
                getData();
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

// pobiera liste klientow
function getData(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url+'kredyty/clients/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + received_token);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                received_json = this.responseText;
                rec_json_obj = JSON.parse(received_json);
//                displayData();
                setup_select();
            } else {
                console.error(xhr.statusText);
            }
        }
    };
    xhr.onerror = function (e) {
        console.error(xhr.statusText);
    };
    xhr.send(null);
}

// wstawia id klientow do pola select
function setup_select() {
    var select = document.getElementById("form_client");
    var options = [];
    for (let i=0; i<rec_json_obj.length; i++) {
        options.push(rec_json_obj[i]['id']);
    }

    for(var i = 0; i < options.length; i++) {
        var opt = options[i];
        var el = document.createElement("option");
        el.textContent = '('+rec_json_obj[i]['id']+') '+rec_json_obj[i]['first_name']+' '+rec_json_obj[i]['second_name'];
        el.value = opt;
        select.appendChild(el);
    }
}
