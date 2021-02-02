#!/usr/bin/node
const arr = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  arr.map(Number);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
