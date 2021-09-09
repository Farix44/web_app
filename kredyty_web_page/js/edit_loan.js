var received_json;
var rec_json_obj;
var received_token;
var url = 'http://127.0.0.1:8000/api/';

// przy wczytywaniu strony pobiera token i nastepnie z jego pomocaliste wnioskow
window.addEventListener( "load", function () {
    getToken();
} );

function test() {
    console.log(document.getElementById("select_client").value);
}

// wstawia id i nazwe klientow do pola select_client
function setup_select_client() {
    var select = document.getElementById("select_client");
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

// wstawia id wniosku do pola select_loan
function setup_select_loan() {
    var select = document.getElementById("select_loan");
    var selected_client_id = document.getElementById("select_client").value;
    var options = [];

    // wyczyszczenie pol select
    for (i = select.options.length-1; i >= 0; i--) {
      select.options[i] = null;
    }

    for (let i=0; i<rec_json_obj[selected_client_id-1]['loans'].length; i++) {
        options.push(rec_json_obj[selected_client_id-1]['loans'][i]['id']);
    }

    for(var i = 0; i < options.length; i++) {
        var opt = options[i];
        var el = document.createElement("option");
        el.textContent = '(' + rec_json_obj[selected_client_id-1]['loans'][i]['id'] + ') ' +
                         rec_json_obj[selected_client_id-1]['loans'][i]['amount'];
        el.value = opt;
        select.appendChild(el);
    }
    fillForm();
}

// wypelnia formularz danymi po wybranym id
function fillForm() {
    var selected_client_id = document.getElementById("select_client").value;
    var selected_loan_id = document.getElementById("select_loan").value;
//    console.log('===== ' + selected_client_id + '  ' + selected_loan_id + ' =====');

    for (let i=0; i<rec_json_obj.length; i++) {
        if (selected_client_id == rec_json_obj[i]['id']) {
            for (let j=0; j<rec_json_obj[i]['loans'].length; j++) {
                if (selected_loan_id == rec_json_obj[i]['loans'][j]['id']) {
                    document.getElementById("client_name").innerHTML = rec_json_obj[i]['first_name'] + ' ' + rec_json_obj[i]['second_name'];
                    //document.getElementById('form_first_name').value = rec_json_obj[i]['first_name'];
                    //document.getElementById('form_second_name').value = rec_json_obj[i]['second_name'];
                    document.getElementById('form_amount').value = rec_json_obj[i]['loans'][j]['amount'];
                    document.getElementById('form_period').value = rec_json_obj[i]['loans'][j]['period'];
                    document.getElementById('form_repayment_amount').value = rec_json_obj[i]['loans'][j]['repayment_amount'];
                }
            }
        }
    }

}

// wysyłanie PUT zedytowanych danych z formularza
function submitEdit() {
    var data = getFormData();
    var json = JSON.stringify(data);
    var loan_id = document.getElementById("select_loan").value;

    var xhr = new XMLHttpRequest();
    xhr.open("PUT", url+'kredyty/loans/'+loan_id+'/', true);
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

// usuniecie wybranego kredytu (DELETE)
function submitDelete() {
    var loan_id = document.getElementById("select_loan").value;

    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", url+'kredyty/loans/'+loan_id+'/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + received_token);
    xhr.onload = function () {
        if (xhr.readyState == 4 && xhr.status == "200") {
            console.table(users);
        } else {
            console.error(users);
        }
    }
    xhr.send(null);
    return false;
}


// pobieranie danych z formularza do obiektu
function getFormData() {
    var elements = document.getElementById("edit_loan_form").elements;
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
                setup_select_client();
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
