window.onload = function() {
    var rows = document.getElementById('ip_addresses').getElementsByTagName('tbody')[0].getElementsByTagName('tr');

    // Loop through each row and change cell colour accordingly
    for (i = 0; i < rows.length; i++) {
        cells = rows[i].getElementsByTagName('td');

        if (cells[1].innerHTML == 'Online'){
            cells[1].className = 'online';
        } else {
            cells[1].className = 'offline';
        }
    }
}