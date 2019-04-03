const database = require('./database');
const pageSize = 20;

var movies = {
    getUnwatched: function(id, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Movies";
            con.query(query, function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    },

    getPage: function(page, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT * FROM Movies WHERE ? < id AND id < ?";
            con.query(query, [(page - 1) * pageSize, page * pageSize], function (err, result, fields) {
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
            var query = "SELECT * FROM Movies WHERE id = ?";
            con.query(query, [id], function (err, result, fields) {
                if (err) throw err;
                con.end();
                callback(result);
            });
        });
    },
};

module.exports = movies;