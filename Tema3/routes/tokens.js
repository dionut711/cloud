const express = require('express');
const tokens = require('../services/tokens');
const email = require('../services/email');
const users = require('../services/users');
const fs = require('fs');

const router = express.Router();

const contents = fs.readFileSync("./config/credentials.json");
const jsonContent = JSON.parse(contents);
const from_address = jsonContent.email;
const subject = 'Email confirmation';
const text = 'Click this to confirm {link}';
const token_confirm_url = require('../config/paths.js').token_confirm_url;

router.get('/send/:id', function(req, res) {
    users.getById(req.params.id, function(result) {
        if(result.length > 0) {
            tokens.insert(req.params.id, (tokenid) => {
                var final_text = text.replace("{link}", token_confirm_url + tokenid);
                email.send(result[0].Email, from_address, subject, final_text);
            });
            res.render('emailConfirmationSent', {email: result[0].Email});
        }
        else {
            res.render("useridNotFound", req.params.id);
        }
    });
});

router.get('/confirm/:token', function(req, res) {
    tokens.confirm(req.params.token,
    function(value) {
        if (value)
            res.render('tokenConfirmed');
        else
            res.render('tokenDeclined');
    });
});

router.get('/', function(req, res) {
    tokens.getAll(function(tokens) {
        res.set('Content-Type', 'application/json');
        res.send(tokens);
    })
});

module.exports = router;