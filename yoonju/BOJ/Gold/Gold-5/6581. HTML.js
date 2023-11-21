const fs = require("fs");
const [...lines] = fs.readFileSync("dev/stdin").toString().trim().split("\n");

let splitLines = [];

lines.forEach(
  (line) =>
    (splitLines = [...splitLines, ...line.split(/\s+/g).filter((word) => word)])
);

let count = 0;
let nowLine = [];
const result = [];
const hrLine = "-".repeat(80);

splitLines.forEach((word) => {
  if (word === "<br>") {
    if (count) {
      result.push(nowLine.join(" "));
    } else {
      result.push("");
    }
    nowLine = [];
    count = 0;
  } else if (word === "<hr>") {
    if (count) {
      result.push(nowLine.join(" "));
    }
    result.push(hrLine);
    nowLine = [];
    count = 0;
  } else {
    if (count + word.length <= 80) {
      nowLine.push(word);
      count += word.length + 1;
    } else {
      result.push(nowLine.join(" "));
      nowLine = [word];
      count = word.length + 1;
    }
  }
});

if (count) {
  result.push(nowLine.join(" "));
}

console.log(result.join("\n"));
