#!/usr/bin/node
const req = require('request');
req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, body) => {
  if (!err) {
    const urls = JSON.parse(body).characters;
    for (const url of urls) {
      req(url, (e, r, b) => {
        if (!e) {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
