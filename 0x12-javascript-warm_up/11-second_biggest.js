#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  arr.map(Number);
  const uniq = [...new Set(arr)];
  uniq.sort();
  console.log(uniq[uniq.length - 2]);
}
