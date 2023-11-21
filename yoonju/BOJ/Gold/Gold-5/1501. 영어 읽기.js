const fs = require("fs");
const inputs = fs.readFileSync("dev/stdin").toString().trim().split("\n");

/**
 * 단어의 앞과 뒤, 중간을 분리
 * 단, 중간은 정렬함
 * word => w / or / d
 * @param {string} word
 * @returns [string, string]
 */
const getPartOfWord = (word) => {
  const length = word.length;
  const key = length > 1 ? [word[0], word[length - 1]] : [word[0]];
  const middle = Array.from(word.slice(1, length - 1)).sort();
  return [key, middle];
};

/**
 * 사전에 저장
 * 첫번째 key (단어의 앞과 뒤)가 사전에 있는지 확인
 * 두번째 middle (단어의 중간)이 사전의 key에 있는지 확인
 * @param {string} word
 */
const splitDictWords = (word) => {
  const [key, middle] = getPartOfWord(word);

  if (!dictionaryCount.hasOwnProperty(key)) {
    dictionaryCount[key] = {};
  }
  if (!dictionaryCount[key].hasOwnProperty(middle)) {
    dictionaryCount[key][middle] = 0;
  }

  dictionaryCount[key][middle] += 1;
};

/**
 * 문장을 분리, 해석할 수 있는 경우의 수 구하기
 * 문장의 단어 모두가 해석 불가능 => 경우의 수 0
 * 문장의 단어 중 하나라도 해석 가능 => 경우의 수 1 이상
 * @param {string} sentence
 * @returns 0 || number
 */
const getSentenceTranslateCount = (sentence) => {
  let count = 1;
  let isWeird = true;
  sentence.split(" ").forEach((word) => {
    const [key, middle] = getPartOfWord(word);
    if (
      dictionaryCount.hasOwnProperty(key) &&
      dictionaryCount[key].hasOwnProperty(middle)
    ) {
      isWeird = false;
      count *= dictionaryCount[key][middle];
    }
  });

  if (isWeird) {
    return 0;
  }
  return count;
};

const N = Number(inputs[0]);
const dictionary = inputs.slice(1, N + 1);
const M = Number(inputs[N + 1]);
const sentences = inputs.slice(N + 2);
const dictionaryCount = {};

dictionary.forEach(splitDictWords);
const answer = sentences.map(getSentenceTranslateCount);

console.log(answer.join("\n"));
