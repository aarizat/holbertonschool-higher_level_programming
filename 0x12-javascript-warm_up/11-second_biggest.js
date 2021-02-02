#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  arr.map(Number);
  arr.sort();
  console.log(arr[arr.length - 2]);
}
