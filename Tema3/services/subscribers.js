const database = require('./database.js');

var subscribers = {
    isVerified: function(userid, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT verified FROM Users WHERE id=?";
            con.query(query, [userid], function (err, result, fields) {
                if (err) throw err;
                callback(result[0].verified);
            });
        });
    },

    isSubscribed: function(userid, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Subscriptions WHERE userid=?";
            con.query(query, [userid], function (err, result, fields) {
                if (err) throw err;
                callback(result.length > 0);
            });
        });
    },

    insert: function(userid) {
        if (subscribers.isVerified(userid, function(value) {
            if (value == 1) {
                if(subscribers.isSubscribed(userid, function(value) {
                    if (value == false) {
                        con = database.getConnection();
                        con.connect(function (err) {
                            var query = "INSERT INTO Subscriptions (Userid) VALUES(?)";
                            con.query(query, [userid], function (err, result, fields) {
                                con.end();
                            });
                        });
                    }
                    else {
                        con.end();
                    }
                }));
            }
            else {
                con.end();
            }
        }));
    },

    delete: function(userid) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "DELETE FROM Subscriptions WHERE userid=?";
            console.log(query);
            console.log(userid);
            con.query(query, [userid], function (err, result, fields) {
                if (err) throw err;
            });
        });
    },

    getAll: function(callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Users WHERE id IN (SELECT userid FROM Subscriptions)";
            con.query(query, function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    }
};

module.exports = subscribers;