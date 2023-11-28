// 231117
// 17092 KB / 912 ms
const input = require("fs").readFileSync("dev/stdin").toString().split("\n");
const N = parseInt(input[0]);
const words = {};
const length = input.length;
for (let i = 1; i < N + 1; i += 1) {
  const word = input[i];
  const word_length = word.length;
  const key = word_length > 1 ? word[0] + word[word_length - 1] : word[0];
  const value = word.slice(1, word_length - 1).split("");
  value.sort();
  const sorted_value = value.join("");
  if (key in words) {
    if (sorted_value in words[key]) {
      words[key][sorted_value] += 1;
    } else {
      words[key][sorted_value] = 1;
    }
  } else {
    words[key] = { [sorted_value]: 1 };
  }
}

const M = parseInt(input[N + 1]);
if (M !== 0) {
  const answer = Array.from({ length: M }, () => (N !== 0 ? 1 : 0));
  for (let i = N + 2; i < length; i += 1) {
    let non_exist_all = true;
    const sentence = input[i].split(" ");
    for (let j = 0; j < sentence.length; j += 1) {
      const word = sentence[j];
      const word_length = word.length;
      const key = word_length > 1 ? word[0] + word[word_length - 1] : word[0];
      const value = word.slice(1, word_length - 1).split("");
      value.sort();
      const sorted_value = value.join("");

      if (key in words && sorted_value in words[key]) {
        answer[i - N - 2] *= words[key][sorted_value];
        non_exist_all = false;
      }
    }
    if (non_exist_all === true) {
      answer[i - N - 2] = 0;
    }
  }

  for (let i = 0; i < M; i += 1) {
    console.log(answer[i]);
  }
}
