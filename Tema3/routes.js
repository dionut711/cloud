const express = require('express');
const youtubeVideos = require('./routes/youtubevideos');
const tokens = require('./routes/tokens');
const users = require('./routes/users');
const subscribe = require('./routes/subscribe');
const movies = require('./routes/movies');

const router = express.Router();

router.use('/youtubevideos', youtubeVideos);
router.use('/tokens', tokens);
router.use('/', subscribe);
router.use('/users', users);
router.use('/movies', movies);

router.get('/search' , (req, res) => {
    res.render('search');
});

router.get('/', (req, res) => {
    res.render('home', {authentificated: req.session.userid !== undefined});
});

module.exports = router;