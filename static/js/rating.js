function rate() {
    if ($('#ratep').valid()) {
        alert("hello");
        var email = $('#email').val();
        var business = $('#business').val();
        var description = $('#description').val();
        var rating = $('#rating').val();
        var formdata = new FormData();
        formdata.append('email', email);
        formdata.append('business', business);
        formdata.append('description', description);
        formdata.append('rating', rating);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.status == 200 && this.readyState == 4) {
                var output = this.response;
                if (output == "fail") {
                    window.location.href="login"
                } else {
                    alert(output);
                }
            }
        };
        xml.open('POST', 'rating', true);
        xml.send(formdata);
    }
}

// function viewallrating(email) {
//     var xml = new XMLHttpRequest();
//     xml.onreadystatechange = function () {
//         if (this.status == 200 && this.readyState == 4) {
//             var output = JSON.parse(this.response);
//             alert(output);
//             document.getElementById('Customerreviews').innerHTML='<div class="rating text-warning"></div>'
//         }
//     };
//     xml.open('GET', 'viewallrating?email='+email, true);
//     xml.send();
// }