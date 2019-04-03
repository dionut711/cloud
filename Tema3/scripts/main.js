onClickLike = function(id) {
    var request = new XMLHttpRequest()

    request.open('POST', '/movies/' + id + '/like', true)

    request.onload = function () {
    }
    
    request.send()
}

onClickDislike = function(id) {
    var request = new XMLHttpRequest()

    request.open('POST', '/movies/' + id + '/dislike', true)

    request.onload = function () {
    }
    
    request.send()
}