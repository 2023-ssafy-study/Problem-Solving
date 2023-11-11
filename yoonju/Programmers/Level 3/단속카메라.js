function solution(routes) {
  let answer = 0;
  let lastCamera = -2e9;

  routes.sort((a, b) => a[1] - b[1]);

  routes.forEach(([start, end]) => {
    if (start > lastCamera) {
      answer += 1;
      lastCamera = end;
    }
  });

  return answer;
}
