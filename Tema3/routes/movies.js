const movies = require('../services/movies');
const express = require('express');
const youtube = require('../services/youtube');

const router = express.Router();

router.get('/page/:page', function (req, res) {
    movies.getPage(req.params.page, function (result) {
        let elements = []
        result.forEach(element => {
            elements.push(element);
        });
        res.render('movies', {
            authentificated: req.session.userid !== undefined,
            movies: elements,
            nextPage: parseInt(req.params.page) + 1,
            prevPage: parseInt(req.params.page) - 1,
            firstpage: req.params.page == 1,
            lastpage: req.params.page == 100
        });
    });
});

router.get('/:id', function (req, res) {
    movies.getById(req.params.id, function (result) {
        youtube.get_iframes(result[0].Title + " trailer", (iframes) => {
            let html = ""
            iframes.forEach(element => {
                html += element + "\n";
            });
            res.render('movie', {
                authentificated: req.session.userid !== undefined,
                movie: result[0],
                youtubevideos: html
            });
        });
    });
});

router.post('/:id/like', function(req, res) {
    console.log('you just liked me');
    res.send('like');
});

router.post('/:id/dislike', function(req, res) {
    console.log('you just disliked me');
    res.send('dislike');
});

module.exports = router;