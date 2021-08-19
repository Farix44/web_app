var received_json;
var rec_json_obj;
var admin_token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';

// wysyłanie nowego wniosku (POST)
function submitNewLoan() {
    var data = getFormData();
    var json = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:8000/kredyty/loans/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + admin_token);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
        if (xhr.readyState == 4 && xhr.status == "200") {
            console.table(users);
        } else {
            console.error(users);
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


