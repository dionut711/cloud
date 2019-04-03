const database = require("./database");

const tokens = {
    getAll: function(callback) {
        con = database.getConnection();
    
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Tokens";
            con.query(query, function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    },

    insert: function(userid, callback) {
        con = database.getConnection();
    
        con.connect(function (err) {
            if (err) throw err;
            var query = "INSERT INTO Tokens (userid) VALUES(?)";
            con.query(query, [userid], function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result.insertId);
            });
        });
    },

    delete: function(id) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "DELETE FROM Tokens WHERE id=?";
            con.query(query, [id], function (err, result, fields) {
                if (err) throw err;
            });
        });
    },

    confirm: function(id, callback) {
        con = database.getConnection();
    
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Tokens WHERE id=?";
            con.query(query, [id], function (err, result, fields) {
                if (err) throw err;
                con.end();
                if(result.length > 0) {
                    const users = require("./users");
                    users.verify(result[0].userid);
                    tokens.delete(id);
                    callback(true);
                }
                else {
                    callback(false);
                }
            });
        });
    }
};

module.exports = tokens;