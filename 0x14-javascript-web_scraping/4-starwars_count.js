#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) return;
  const list = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list[i].characters.length; j++) {
      if (list[i].characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
