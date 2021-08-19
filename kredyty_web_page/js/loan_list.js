var received_json;
var rec_json_obj;
var admin_token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';

// przy wczytywaniu strony pobiera liste wnioskow
window.addEventListener( "load", function () {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", 'http://127.0.0.1:8000/kredyty/loans/', true);
    xhr.setRequestHeader('Authorization', 'Token ' + admin_token);
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
} );


// Display data from application kredyty.
function displayData() {
    // document.getElementById("request_json").innerHTML = received_json;

    // display data in loan list
    var loan_id=0;
    var loan_record = '';
    for (let i=0; i<rec_json_obj.length; i++) {
        loan_record += rec_json_obj[loan_id]['first_name']+' '+rec_json_obj[loan_id]['second_name']+'\n'+
        'pożyczył/a '+rec_json_obj[loan_id]['amount']+'zł, na okres: '+rec_json_obj[loan_id]['period']+' miesięcy.'+'\n'+
        'Do spłaty: '+rec_json_obj[loan_id]['repayment_amount']+'zł.'+'\n'+
        '( id wniosku = '+rec_json_obj[loan_id]['id']+' )\n\n';
        loan_id++;
    }
    loan_record = loan_record.replace(/(\r\n|\n|\r)/gm, "<br>");
    document.getElementById('loan_list').innerHTML = loan_record;
}
