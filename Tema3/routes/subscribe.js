const subscribers = require('../services/subscribers');
const express = require('express');

const router = express.Router();

router.get('/subscribed/:user', function (req, res) {
    subscribers.isSubscribed(req.params.user, function (value) {
        res.set("Content-Type", 'application/json');
        res.send({ 'value': value });
        console.log("called " + value);
    });
});

router.post('/subscribe/:user', function (req, res) {
    subscribers.insert(req.params.user);
    res.render('subscriptionAccepted');
});

router.post('/unsubscribe/:user', function (req, res) {
    subscribers.delete(req.params.user);
    res.render('subscriptionAccepted');
});

router.get('/subscribers', function (req, res) {
    subscribers.getAll(function (result) {
        res.set('Content-Type', 'application/json');
        res.send(result);
    });
});

router.get('/subscription/start', function(req, res) {
    res.render('subscriptionStart');
});

router.get('/subscription/end', function(req, res) {
    res.render('subscriptionEnd');
});

module.exports = router;