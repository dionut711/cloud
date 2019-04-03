const fs = require("fs");
const sgMail = require('@sendgrid/mail');

const contents = fs.readFileSync("./config/credentials.json");
const jsonContent = JSON.parse(contents);
sgMail.setApiKey(jsonContent.sendgrid_api_key);

const email = {
    send: function(to, from, subject, text) {
        const msg = {
            to: to,
            from: from,
            subject: subject,
            text: text
        };
        sgMail.send(msg);
        console.log('sent mail: ' + msg);
    }
}

module.exports = email;
