#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', (err, res, body) => {
  if (err) return;
  const list = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
