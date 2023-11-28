const fs = require("fs");
const [...lines] = fs.readFileSync("dev/stdin").toString().trim().split("\n");

const firstArr = [...lines[0]];
const secondArr = [...lines[1]];

const firstArrLength = firstArr.length;
const secondArrLength = secondArr.length;

const check = Array.from(Array(firstArrLength + 1), () =>
  Array(secondArrLength + 1).fill(0)
);

check.forEach((row, i) => {
  row.forEach((item, j) => {
    if (i === 0 || j === 0) {
      return;
    }
    if (firstArr[i - 1] === secondArr[j - 1]) {
      check[i][j] = check[i - 1][j - 1] + 1;
    } else {
      let maxLCS = 0;
      maxLCS = Math.max(maxLCS, check[i - 1][j]);
      maxLCS = Math.max(maxLCS, check[i][j - 1]);
      check[i][j] = maxLCS;
    }
  });
});

console.log(check[firstArrLength][secondArrLength]);
