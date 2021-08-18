var received_json;
var received_token;
var admin_token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';

function reqListener () {
      received_json = this.responseText;
    }

// Send GET request.
function send_request(req_data, _callback) {
    // var token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';   // !!! TEMPORARY !!!
    // var token = received_token;
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", 'http://127.0.0.1:8000/'+req_data+'/');
    oReq.setRequestHeader('Authorization', 'Token ' + admin_token);
    oReq.send();

    _callback;
}

// Display data from project.
function get_data(req_data) {
    send_request(req_data);
    console.log(received_json);
    document.getElementById("request_json").innerHTML = received_json;
    //var jj = JSON.parse(received_json);
    //console.log(jj[0]['id']);
}

// Display data from application kredyty.
function get_kredyty_data(req_data) {
    req_data = 'kredyty/' + req_data;
    send_request(req_data);
    console.log(received_json);
    document.getElementById("request_json").innerHTML = received_json;

    // display data in form
    var rec_json_obj = JSON.parse(received_json);
    var loan_id = 0;
    document.getElementById('form_first_name').value = rec_json_obj[loan_id]['first_name'];
    document.getElementById('form_second_name').value = rec_json_obj[loan_id]['second_name'];
    document.getElementById('form_amount').value = rec_json_obj[loan_id]['amount'];
    document.getElementById('form_period').value = rec_json_obj[loan_id]['period'];
    document.getElementById('form_repayment_amount').value = rec_json_obj[loan_id]['repayment_amount'];

    // display data in loan list
    var loan_record = '';
    for (let i=0; i<rec_json_obj.length; i++) {
        loan_record += rec_json_obj[loan_id]['first_name']+' '+rec_json_obj[loan_id]['second_name']+'\n'+
        'pożyczył/a '+rec_json_obj[loan_id]['amount']+'zł, na okres: '+rec_json_obj[loan_id]['period']+' miesięcy.'+'\n'+
        'Do spłaty: '+rec_json_obj[loan_id]['repayment_amount']+'zł.'+'\n\n';
        loan_id++;
    }
    loan_record = loan_record.replace(/(\r\n|\n|\r)/gm, "<br>");
    document.getElementById('loan_list').innerHTML = loan_record;
}

// post test
function post_data() {
    var send_json = {
        "first_name": "Janek",
        "second_name": "Janecki",
        "amount": 4500,
        "period": 10
    };
    // var token = '7c374722bf776133c827a966f9fc9d89fbde7c6f';   // !!! TEMPORARY !!!
    // var token = received_token;
    var oReq = new XMLHttpRequest();
    oReq.open("POST", 'http://127.0.0.1:8000/kredyty/loans/');
    oReq.setRequestHeader('Authorization', 'Token ' + admin_token);
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


// ADD NEW LOAN:
window.addEventListener( "load", function () {
  function sendData() {
    const XHR = new XMLHttpRequest();

    // Bind the FormData object and the form element
    const FD = new FormData( form );

    // Define what happens on successful data submission
//    XHR.addEventListener( "load", function(event) {
//      alert( event.target.responseText );
//    } );

    // Define what happens in case of error
    XHR.addEventListener( "error", function( event ) {
      //alert( 'Oops! Something went wrong.' );
      console.log('Error');
    } );

    // Set up our request
    XHR.open( "POST", "http://127.0.0.1:8000/kredyty/loans/" );
    // XHR.setRequestHeader('Authorization', 'Token ' + '7c374722bf776133c827a966f9fc9d89fbde7c6f');
    XHR.setRequestHeader('Authorization', 'Token ' + admin_token);
    //XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    console.log(FD);
    // The data sent is what the user provided in the form
    XHR.send( FD );
  }

  // Access the form element...
  const form = document.getElementById( "add_new_loan_form" );

  // ...and take over its submit event.
  form.addEventListener( "submit", function ( event ) {
    event.preventDefault();

    sendData();
  } );
} );
