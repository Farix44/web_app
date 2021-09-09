var received_json;
var rec_json_obj;
var received_token;
var url = 'http://127.0.0.1:8000/api/';

// przy wczytywaniu strony pobiera token i nastepnie z jego pomocaliste wnioskow
window.addEventListener( "load", function () {
    getToken();
} );

// Display data from application kredyty.
function displayData() {
//    document.getElementById("request_json").innerHTML = received_json;
//    console.log('===== '+rec_json_obj[0]['loans'][0]['amount']+' =====');

    var client_id = 0;
    var client_record = [];
    for (let i=0; i<rec_json_obj.length; i++) {
        client_record[i] = '';
        client_record[i] += '(' + rec_json_obj[i]['id'] + ') ';
        client_record[i] += rec_json_obj[i]['first_name'] + ' ';
        client_record[i] += rec_json_obj[i]['second_name'] + '<br>';
        for (let j=0; j<rec_json_obj[i]['loans'].length; j++) {
            client_record[i] += '&nbsp;&nbsp;&nbsp;&nbsp;  (' + rec_json_obj[i]['loans'][j]['id'] + ') ';
            client_record[i] += 'pożyczył/a ';
            client_record[i] += rec_json_obj[i]['loans'][j]['amount'] + 'zł ';
            client_record[i] += 'na okres ';
            client_record[i] += rec_json_obj[i]['loans'][j]['period'] + ' miesięcy, ';
            client_record[i] += 'do spłaty: ';
            client_record[i] += rec_json_obj[i]['loans'][j]['repayment_amount'] + '<br>';
        }
        client_record[i] += '<br>';
    }

    var display_record = '';
    for (let i=0; i<client_record.length; i++) {
        console.log(client_record[i]);
        display_record += client_record[i];
    }
    document.getElementById('loan_list').innerHTML = display_record;

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
    xhr.open("GET", url+'kredyty/clients/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + received_token);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                received_json = this.responseText;
                rec_json_obj = JSON.parse(received_json);
                displayData();
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
