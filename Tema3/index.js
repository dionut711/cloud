const express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var multer = require('multer');
var upload = multer();

const app = express();
const router = require('./routes');

app.set('view engine', 'pug');
app.set('views','./views');

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true })); 
app.use(upload.array()); 
app.use(express.static('public'));

app.use(session({
    'secret': '343ji43j4n3jn4jk3n',
    resave: true,
    saveUninitialized: true
}));

app.use('/', router);

app.listen(8080);