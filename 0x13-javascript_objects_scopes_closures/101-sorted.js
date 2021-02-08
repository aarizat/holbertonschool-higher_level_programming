#!/usr/bin/node
const data = require('./101-data.js').dict;
const newData = {};
for (const key in data) {
  if (newData[data[key]] === undefined) {
    newData[data[key]] = [key];
  } else {
    newData[data[key]].push(key);
  }
}
console.log(newData);
