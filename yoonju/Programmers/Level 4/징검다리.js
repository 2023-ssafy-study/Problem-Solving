function solution(distance, rocks, n) {
  // dist : 최소 거리값이어야 하는 거리
  const removeRock = (dist) => {
    let prevRock = 0;
    let deleteRock = 0;
    rocks.forEach((rock) => {
      // 현재 바위와 이전 바위의 거리가 dist보다 적다면 => 바위 제거
      if (rock - prevRock < dist) {
        deleteRock += 1;
      } else {
        // 현재 바위와 이전 바위의 거리가 dist보다 크거나 같다면 => 이전 바위 교체
        prevRock = rock;
      }
      // 제거한 바위가 n보다 많다 => 더 확인할 필요 없음
      if (deleteRock > n) {
        return;
      }
    });
    // 제거한 바위가 n보다 많으면 false, 같거나 적으면 true
    return deleteRock > n ? false : true;
  };
  var answer = 0;

  rocks.push(distance);

  rocks.sort((a, b) => a - b);

  let [s, e] = [1, distance];

  while (s <= e) {
    const mid = Math.floor((s + e) / 2);
    if (removeRock(mid)) {
      answer = mid;
      s = mid + 1;
    } else {
      e = mid - 1;
    }
  }

  return answer;
}
