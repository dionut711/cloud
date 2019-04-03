loadSubscribeButton = function(id) {
    document.getElementById("subscribe-button").innerHTML = "";

    var request = new XMLHttpRequest()

    request.open('GET', '/subscribed/' + id, true)

    request.onload = function () {
        button = document.getElementById("subscribe-button");
        console.log(request.responseText);
        var subscribed = JSON.parse(request.responseText).value;
        if (subscribed) 
            showUnsubscribeButton(id);
        else 
            showSubscribeButton(id);
    }
    
    request.send();
}

showUnsubscribeButton = function(id) {
    button.innerHTML = "Unsubscribe";
    button.onclick = () => unsubscribeOnClick(id);
}

showSubscribeButton = function(id) {
    button.innerHTML = "Subscribe";
    button.onclick = () => subscribeOnClick(id);
}

subscribeOnClick = function(id) {
    console.log(id);
    var request = new XMLHttpRequest()

    request.open('POST', '/subscribe/' + id, true)

    request.onload = function () {
        showUnsubscribeButton(id);
        //window.location.replace('/subscription/end');
    }
    
    request.send();
}

unsubscribeOnClick = function(id) {
    console.log(id);
    var request = new XMLHttpRequest()

    request.open('POST', '/unsubscribe/' + id, true)

    request.onload = function () {
        showSubscribeButton(id);
        //window.location.replace('/subscription/end');
    }
    
    request.send();
}