function solution(operations) {
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
      while (index > 0 && this.heap[parentIndex] > this.heap[index]) {
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
          if (this.heap[index] > this.heap[leftChildIndex]) {
            smallestChildIndex = leftChildIndex;
          }
        }

        if (rightChildIndex < this.heap.length) {
          // smallestChildIndex가 null => 현재 위치와 오른쪽 자식 비교
          if (smallestChildIndex === null) {
            if (this.heap[index] > this.heap[rightChildIndex]) {
              smallestChildIndex = rightChildIndex;
            }
          } else {
            // smallestChildIndex가 null X => smallestChildIndex와 오른쪽 자식 비교
            if (this.heap[smallestChildIndex] > this.heap[rightChildIndex]) {
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

  var answer = [];
  const check = {};
  const minHeap = new Heap();
  const maxHeap = new Heap();

  operations.forEach((item) => {
    const [type, num] = item.split(" ");
    if (type === "I") {
      minHeap.insert(Number(num));
      maxHeap.insert(-Number(num));
      check[num] = true;
    } else {
      if (num === "1") {
        while (true && !maxHeap.isEmpty()) {
          const maxValue = maxHeap.pop();
          if (check[maxValue * -1]) {
            check[maxValue * -1] = false;
            break;
          }
        }
      } else if (num === "-1") {
        while (true && !minHeap.isEmpty()) {
          const minValue = minHeap.pop();
          if (check[minValue]) {
            check[minValue] = false;
            break;
          }
        }
      }
    }
  });

  const checkTrue = Object.keys(check)
    .filter((item) => check[item] === true)
    .map(Number)
    .sort((a, b) => a - b);

  if (!checkTrue.length) {
    return [0, 0];
  }

  return [Number(checkTrue.at(-1)), Number(checkTrue[0])];
}
