const youtube = require('../services/youtube.js');
const express = require('express');
const router = express.Router();

router.get('/:query', (req, res) => {
    youtube.get_iframes(req.params.query, (iframes) => {
        res.set('Content-Type', 'text/html');
        let html = ""
        iframes.forEach(element => {
            html += element;
        });
        res.send(html);
    });
});

module.exports = router;