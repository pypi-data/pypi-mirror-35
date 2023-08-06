var urlParams = new URLSearchParams(window.location.search);
var page_num = urlParams.get('page');

function next_page(subnet_id){
    var last_page = Number(page_num) + 1;
    location.href = '/subnet/view/' + subnet_id + '/?page=' + last_page
}

function back_page(subnet_id){
    var next_page = Number(page_num) - 1;
    location.href = '/subnet/view/' + subnet_id + '/?page=' + next_page
}