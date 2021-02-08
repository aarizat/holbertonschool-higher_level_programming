#!/usr/bin/node
const data = require('./100-data.js').list;
console.log(data);
console.log(data.map((val, idx) => val * idx));
