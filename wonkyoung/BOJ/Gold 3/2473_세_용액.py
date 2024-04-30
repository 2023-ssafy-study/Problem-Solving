# 240430
# 111520 KB / 1364 ms (pypy3)
def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end)//2
        mid_val = arr[mid]
        if mid_val < target:
            start = mid + 1
        elif mid_val > target:
            end = mid - 1
        else:
            return (mid,)

    return (start, end)

def mix_solutions(N, solutions):

    plus_i, minus_i = binary_search(0, N-1, solutions, 0)

    # 양 양 양
    answer = solutions[plus_i:plus_i + 3][:]
    min_val = sum(answer)

    # 음 음 음 / 음 음 양 / 음 양 양
    for i in range(plus_i):
        solution1 = solutions[i]
        for j in range(i+1, N-1):
            solution2 = solutions[j]
            total = solution1 + solution2
            if total >= 0:
                new_answer = [solution1, solution2, solutions[j+1]]
                new_val = abs(sum(new_answer))
            else:
                result = binary_search(i+2, N-1, solutions, -total)
                if len(result) == 1:
                    return [solution1, solution2, solutions[result[0]]]

                right, left = result


                if right == N:
                    new_answer = [solution1, solution2, solutions[left]]
                    new_val = abs(sum(new_answer))
                elif left == j or right <= minus_i:
                    new_answer = [solution1, solution2, solutions[right]]
                    new_val = abs(sum(new_answer))
                else:
                    solution_r, solution_l = solutions[right], solutions[left]
                    total_r, total_l = abs(total + solution_r), abs(total + solution_l)

                    if total_r <= total_l:
                        new_answer = [solution1, solution2, solution_r]
                        new_val = total_r
                    else:
                        new_answer = [solution1, solution2, solution_l]
                        new_val = total_l

            if new_val < min_val:
                min_val = new_val
                answer = new_answer[:]

    return answer

def main():
    N = int(input())
    solutions = list(map(int, input().split()))
    solutions.sort()
    last_three, first_three = solutions[-3:], solutions[:3]

    if solutions[-1] < 0:
        return last_three

    if solutions[0] > 0:
        return first_three

    return mix_solutions(N, solutions)

print(*main())