const database = require('./database');
const https = require('http');
const movies = require('./movies');

var recommendations = {
    getByUserId: function (userId, callback) {
        con = database.getConnection();
        con.connect(function (err) {
            if (err) throw err;
            var query = "SELECT year, genreid, directorid, actorid, rating, liked FROM Movies JOIN WatchedMovies as wm ON Movies.id = wm.movieid WHERE wm.userid = ?";
            con.query(query, [userId], function (err, result, fields) {
                if (err) throw err;
                var query = "SELECT ID, Title, year, genreid, directorid, actorid, rating FROM Movies WHERE id NOT IN (SELECT movieid FROM WatchedMovies WHERE userid=?)";
                con.query(query, [userId], function (err, movies, fields) {
                    if (err) throw err;
                    con.end();

                    let data = {};
                    data.trainingData = result;
                    data.movies = [];
                    movies.forEach(element => {
                        data.movies.push({
                            year: element.year,
                            genreid: element.genreid,
                            directorid: element.directorid,
                            actorid: element.actorid,
                            rating: element.rating
                        })
                    });
                    let allMovies = movies;

                    data = JSON.stringify(data);
                    let options = {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    };
                    var request = require('request');
                    request.post({
                        headers: { 'content-type': 'application/json' },
                        url: 'http://europe-west1-cloudlab60000.cloudfunctions.net/MlFunction',
                        body: data
                    }, function (error, response, body) {
                        //console.log(response);
                        let result = JSON.parse(response.body);
                        result = result.results;
                        let movies = [];

                        movies.get
                        for (let index = 0; index < allMovies.length; index++) {
                            movies.push({
                                "movie": allMovies[index],
                                "score": result[index].result
                            });
                        }
                        movies.sort((m) => {
                            return m.score;
                        });
                        let finalData = [];
                        for (let i = 0; i < 5; i++) {
                            finalData.push(movies[i].movie);
                        }

                        callback(finalData);
                    });
                    // let req = https.request("http://europe-west1-cloudlab60000.cloudfunctions.net/MlFunction", options, function(res) {
                    //     let response = "";
                    //     res.on('data', (body) => {
                    //         response += body;
                    //     });
                    //     res.on('end', () => {
                    //         let result = JSON.parse(response);
                    //         result = result.results;
                    //         let movies = [];

                    //         movies.get
                    //         for (let index = 0; index < allMovies.length; index++) {
                    //             movies.push({
                    //                 "movie":allMovies[index],
                    //                 "score":result[index].result
                    //             });
                    //         }
                    //         movies.sort((m) => {
                    //             return m.score;
                    //         });
                    //         let finalData = [];
                    //         for(let i=0; i<5; i++) {
                    //             finalData.push(movies[i].movie);
                    //         }

                    //         callback(finalData);
                    //     })
                    // });
                    //req.write(data);
                    //req.end();
                    //callback([allMovies[1], allMovies[2]]);
                });
            });
        });
    }
};

module.exports = recommendations;