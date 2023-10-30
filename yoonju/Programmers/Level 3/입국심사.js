function solution(n, times) {
  const calTime = (value) => {
    return times.reduce((acc, cur) => acc + Math.floor(value / cur), 0);
  };

  var answer = Number(Infinity);

  times.sort((a, b) => a - b);

  const maxTime = times.at(-1);

  let [s, e] = [0, maxTime * n];

  while (s <= e) {
    const mid = Math.ceil((s + e) / 2);
    if (calTime(mid) >= n) {
      answer = Math.min(answer, mid);
      e = mid - 1;
    } else {
      s = mid + 1;
    }
  }
  return answer;
}
