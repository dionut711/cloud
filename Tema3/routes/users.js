const users = require('../services/users');
const express = require('express');
const recommendations = require('../services/recommendations');

const router = express.Router();

router.get('/', function (req, res) {
    users.getAll(function (result) {
        res.set('Content-Type', 'application/json');
        res.send(result);
    });
});

router.get('/signup', function (req, res) {
    if (req.session.userid === undefined) {
        res.render('signup', {
            authentificated: false
        });
    }
    else {
        res.redirect('/users/account');
    }
});

router.get('/signout', function (req, res) {
    req.session.userid = undefined;
    res.redirect('/');
});

router.get('/signin', function (req, res) {
    if (req.session.userid === undefined) {
        res.render('signin', {
            authentificated: false
        });
    }
    else {
        res.redirect('/users/account');
    }
});

router.post('/signup', function (req, res) {
    users.insert(req.body.Name, req.body.Password, req.body.Email, function (err, result, field) {
        res.render("signupConfirmed");
    });
});

router.post('/signin', function (req, res) {
    if (req.session.userid === undefined) {
        users.isValid(req.body.Name, req.body.Password, function (value, userid) {
            if (value) {
                req.session.userid = userid;
                res.redirect('/users/account');
            }
            else {
                res.redirect('/users/signin');
            }
        });
    }
    else {
        res.redirect('/users/account');
    }
});

router.get('/account', function (req, res) {
    if (req.session.userid === undefined) {
        res.redirect('/users/signin');
    }
    else {
        recommendations.getByUserId(req.session.userid, function (result) {
            console.log(result.recommendations);
            res.render('account', {
                userid: req.session.userid,
                authentificated: req.session.userid !== undefined,
                recommendations: result
            });
        });
    }
});

module.exports = router;