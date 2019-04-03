window.onload = function() {
    var request = new XMLHttpRequest();
    request.open('GET', '/entries', true);

    request.onload = function () {
        document.getElementById("dropdown").innerHTML = request.responseText;
        document.getElementById("dropdown").value = "-1";
    }

    request.send();
}

function onAPISelect() {
    selectedValue = document.getElementById("dropdown").value
    var request = new XMLHttpRequest();
    request.open('GET', '/location?url={url}'.replace('{url}', selectedValue), true);

    request.onload = function () {
        let jsonObject = JSON.parse(request.responseText.replace(/'/g, '"'));
        document.getElementById("country").innerHTML = jsonObject.country;
        document.getElementById("city").innerHTML = jsonObject.city;
        document.getElementById("address").innerHTML = jsonObject.as;
        document.getElementById("lat").innerHTML = jsonObject.lat;
        document.getElementById("lon").innerHTML = jsonObject.lon;

        document.getElementById("distance").innerHTML = jsonObject.distance;
        document.getElementById("duration").innerHTML = jsonObject.duration;
        // document.getElementById("location-data").innerHTML = request.responseText;
        document.getElementById("loading").style.visibility = "hidden";
    }

    request.send();
    document.getElementById("loading").style.visibility = "visible";
}