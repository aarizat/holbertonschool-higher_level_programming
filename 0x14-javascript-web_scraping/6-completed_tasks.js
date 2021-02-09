#!/usr/bin/node
const req = require('request');
const completed = {};
req(process.argv[2], (err, res, body) => {
  if (!err) {
    const list = JSON.parse(body);
    for (const item of list) {
      if (item.completed && completed[item.userId] === undefined) {
        completed[item.userId] = 1;
      } else if (item.completed) {
        completed[item.userId] += 1;
      }
    }
  }
  console.log(completed);
});
