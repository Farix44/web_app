var received_json;
var rec_json_obj;
var received_token;
var url = ${BACKEND_HOST};

// przy wczytywaniu strony pobiera token i nastepnie z jego pomocaliste wnioskow
window.addEventListener( "load", function () {
    getToken();
} );

// wstawia id wnioskow do pola select
function setup_select() {
    var select = document.getElementById("select_loan");
    var options = [];
    for (let i=0; i<rec_json_obj.length; i++) {
        options.push(rec_json_obj[i]['id']);
    }
    for(var i = 0; i < options.length; i++) {
        var opt = options[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }
}

// wypelnia formularz danymi po wybranym id
function fillForm() {
    var selected_id = document.getElementById("select_loan").value;

    for (let i=0; i<rec_json_obj.length; i++) {
        if (selected_id == rec_json_obj[i]['id']) {
            document.getElementById('form_first_name').value = rec_json_obj[i]['first_name'];
            document.getElementById('form_second_name').value = rec_json_obj[i]['second_name'];
            document.getElementById('form_amount').value = rec_json_obj[i]['amount'];
            document.getElementById('form_period').value = rec_json_obj[i]['period'];
            document.getElementById('form_repayment_amount').value = rec_json_obj[i]['repayment_amount'];
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

// pobiera liste wnioskow
function getData(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url+'kredyty/loans/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + received_token);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                received_json = this.responseText;
                rec_json_obj = JSON.parse(received_json);
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
