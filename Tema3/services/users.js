const database = require('./database');
const crypto = require('crypto');
const tokens = require('./tokens');

var users = {
    hashedPassword: function(password) {
        var md5sum = crypto.createHash('md5');
        md5sum.update(password);
        return md5sum.digest('hex');
    },

    isValid: function(username, password, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Users WHERE Name = ?";
            con.query(query, [username], function (err, result, fields) {
                if (err) throw err;
                con.end();
                
                if (result.length > 0) {
                    if (users.hashedPassword(password) == result[0].Password) {
                        callback(true, result[0].ID);
                    }
                    else {
                        callback(false);
                    }
                }
                else {
                    callback(false);
                }
            });
        });
    },

    insert: function(name, password, email, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "INSERT INTO Users (Name, Password, Email, Verified) VALUES(?, ?, ?, 0)";
            var values = [name, users.hashedPassword(password), email];
            con.query(query, values, function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(err, result, fields);
                tokens.insert(result.insertId, function() {});
            });
        });
    },

    getAll: function(callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Users";
            con.query(query, function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    },

    getById: function(id, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Users WHERE id = ?";
            con.query(query, [id], function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    },
    
    verify: function(id) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "UPDATE Users SET verified = ? WHERE id = ?";
            con.query(query, [1, id], function (err, result, fields) {
                if (err) throw err;
                con.end();
            });
        });
    }
};

module.exports = users;