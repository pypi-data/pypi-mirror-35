function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds){
            break;
        }
    }
}

function enableEdit(subnet_id, ip_id, field, value){
    // View and edit objects
    var view = document.querySelector('#' + field + '_' + ip_id);
    var edit = document.createElement('input');

    // Set required attributes
    edit.setAttribute('id', field + '_' + ip_id);
    view.setAttribute('name', field + '_' + ip_id);
    edit.setAttribute('type', 'text');
    edit.setAttribute('tabindex', '0');
    edit.setAttribute("onfocusout", "saveEdit('" + subnet_id + "','" + ip_id + "', '" + field + "')");

    // Replace the view with the edit object
    edit.value = value;
    view.parentNode.replaceChild(edit, view);

    edit.focus();
}

function saveEdit(subnet_id, ip_id, field){
    // Submit AJAX POST request
    var xhttp = new XMLHttpRequest();
    var value = document.getElementById(field + '_' + ip_id).value;
    var json_data = JSON.stringify({id: ip_id, field: field, value: value});

    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            console.log('INFO: Data submitted');
        }
    };

    xhttp.open('POST', '/subnet/update/' + subnet_id + '/', true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(json_data);

    // Reload view
    sleep(500);
    window.location.reload();
}