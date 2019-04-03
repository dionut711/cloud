window.onload = function() {
    var request = new XMLHttpRequest();
    request.open('GET', '/logs', true);

    request.onload = function () {
        document.getElementById('loading').style.visibility = "hidden";
        document.getElementById('metrics').innerHTML = request.responseText;
    }

    request.send();
    document.getElementById('loading').style.visibility = "visible";
}