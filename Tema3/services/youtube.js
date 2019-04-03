const https = require("https");
const fs = require("fs");

const contents = fs.readFileSync("./config/credentials.json");
const jsonContent = JSON.parse(contents);
const api_key = jsonContent.youtube_api_key;

let search_url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&key=${api_key}&q={}`;
let video_url = `https://www.googleapis.com/youtube/v3/videos?part=player&key=${api_key}&id={}`;

var youtube = {
    request: function(url, callback) {
        https.get(url, (resp) => {
            let data = '';
        
            resp.on('data', (chunk) => {
                data += chunk;
            });
        
            resp.on('end', () => {
                callback(JSON.parse(data));
            });
        
            }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    },
    
    search: function(query, callback) {
        final_url = search_url.replace("{}", query)
        youtube.request(final_url, (resp) => {
            callback(resp.items);
        });
    },
    
    get_iframes: function(query, callback) {
        youtube.search(query, function(items) {
            var iframes = [];
            items.forEach(element => {
                var final_url = video_url.replace('{}', element.id.videoId);
                youtube.request(final_url, (resp) => {
                    frame = resp.items[0].player.embedHtml.replace("//www", "https://www");
                    iframes.push(frame);
                    if (iframes.length >= 5) {
                        callback(iframes)
                    }
                });
            });
        });
    }
};

module.exports = youtube;
