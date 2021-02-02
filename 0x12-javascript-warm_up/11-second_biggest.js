#!/usr/bin/node
let arr = process.argv.slice(2);
arr = arr.map(Number);
arr.sort();
console.log(arr[arr.length - 2]);
