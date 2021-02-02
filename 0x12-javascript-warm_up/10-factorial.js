#!/usr/bin/node
function fact (n) {
  if (n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else if (num > 0) {
  console.log(fact(num));
}
