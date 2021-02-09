#!/usr/bin/node
const req = require('request');
const completed = {};
req(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const list = JSON.parse(body);
  for (const item of list) {
    if (completed[item.userId] === undefined) {
      completed[item.userId] = 0;
    }
    if (item.completed) {
      completed[item.userId]++;
    }
  }
  console.log(completed);
});
