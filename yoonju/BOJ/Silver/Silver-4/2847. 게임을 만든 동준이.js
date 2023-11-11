const fs = require("fs");

const [N, ...scores] = fs
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let prev = 20001;

const answer = scores.reverse().reduce((acc, cur) => {
  if (prev <= cur) {
    const change_count = cur - prev + 1;
    prev = prev - 1;
    return acc + change_count;
  }
  prev = cur;
  return acc;
}, 0);

console.log(answer);
