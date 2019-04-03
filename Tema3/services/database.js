const mysql = require('mysql');

var database = {
    getConnection: function() {
        const fs = require('fs');
        const contents = fs.readFileSync("./config/db.json");
        const jsonContent = JSON.parse(contents);

        var con = mysql.createConnection({
            host: jsonContent.host,
            //socketPath: jsonContent.socketPath,
            user: jsonContent.user,
            password: jsonContent.password,
            database: jsonContent.database,
        });
        return con;
    } 
};

module.exports = database;