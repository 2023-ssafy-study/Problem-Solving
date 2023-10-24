function solution(jobs) {
  class Heap {
    constructor() {
      this.heap = [];
    }
    size() {
      return this.heap.length;
    }
    getMin() {
      return this.heap[0];
    }
    getParentIndex(index) {
      return Math.floor((index - 1) / 2);
    }
    swap(first, second) {
      const temp = this.heap[first];
      this.heap[first] = this.heap[second];
      this.heap[second] = temp;
    }
    isEmpty() {
      return this.heap.length === 0;
    }
    insert(value) {
      this.heap.push(value);
      this.heapifyUp();
    }
    pop() {
      if (this.heap.length === 0) {
        return null;
      }
      if (this.heap.length === 1) {
        return this.heap.pop();
      }
      const minValue = this.heap[0];
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
      return minValue;
    }
    heapifyUp() {
      let index = this.heap.length - 1;
      let parentIndex = this.getParentIndex(index);
      // 부모 인덱스의 값이 자식 인덱스의 값보다 크면 swap
      while (index > 0 && this.heap[parentIndex][1] > this.heap[index][1]) {
        this.swap(parentIndex, index);
        index = parentIndex;
        parentIndex = this.getParentIndex(index);
      }
    }
    heapifyDown() {
      let index = 0;
      while (true) {
        const leftChildIndex = 2 * index + 1;
        const rightChildIndex = 2 * index + 2;
        let smallestChildIndex = null;

        if (leftChildIndex < this.heap.length) {
          // 왼쪽 자식과 비교
          if (this.heap[index][1] > this.heap[leftChildIndex][1]) {
            smallestChildIndex = leftChildIndex;
          }
        }

        if (rightChildIndex < this.heap.length) {
          // smallestChildIndex가 null => 현재 위치와 오른쪽 자식 비교
          if (smallestChildIndex === null) {
            if (this.heap[index][1] > this.heap[rightChildIndex][1]) {
              smallestChildIndex = rightChildIndex;
            }
          } else {
            // smallestChildIndex가 null X => smallestChildIndex와 오른쪽 자식 비교
            if (
              this.heap[smallestChildIndex][1] > this.heap[rightChildIndex][1]
            ) {
              smallestChildIndex = rightChildIndex;
            }
          }
        }

        if (smallestChildIndex !== null) {
          this.swap(index, smallestChildIndex);
          index = smallestChildIndex;
        } else {
          break;
        }
      }
    }
  }

  var answer = 0;

  const heap = new Heap();

  let time = 0;
  let j = 0;

  jobs.sort((a, b) => a[0] - b[0]);

  while (jobs.length > j || heap.size() !== 0) {
    // 현재 진행 중인 작업의 끝나는 시간보다 빨리 요청된 작업이 있으면 heap에 넣기
    if (jobs.length > j && time >= jobs[j][0]) {
      heap.insert(jobs[j]);
      j += 1;
      // // 종료까지 걸리는 시간을 기준으로 오름차순
      // heap.sort((a, b) => a[1] - b[1]);
      continue;
    }
    // 종료까지 걸리는 시간이 적은 것부터 꺼내서 실행
    if (heap.size() > 0) {
      const minItem = heap.getMin();
      time += minItem[1];
      answer += time - minItem[0];
      heap.pop();
    } else {
      time = jobs[j][0];
    }
  }

  return Math.floor(answer / jobs.length);
}
