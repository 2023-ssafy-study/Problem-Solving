# 240523
def return_remain(a, b):
    return a % b

def solution(data, col, row_begin, row_end):
    data.sort(key= lambda each: (each[col-1], -each[0]))
    n, m = len(data), len(data[0])
    sum_remain = [0] * row_end
    for i in range(row_begin-1, row_end):
        sum_remain[i] = sum(map(return_remain, data[i], [i+1]*m))
    
    hash_val = sum_remain[row_begin-1]
    for i in range(row_begin, row_end):
        hash_val ^= sum_remain[i]
    
    return hash_val

'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.20ms, 10.2MB)
테스트 5 〉	통과 (1.37ms, 12MB)
테스트 6 〉	통과 (25.95ms, 57.9MB)
테스트 7 〉	통과 (37.33ms, 64.4MB)
테스트 8 〉	통과 (47.61ms, 64.4MB)
테스트 9 〉	통과 (53.33ms, 64.5MB)
테스트 10 〉	통과 (58.06ms, 64MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
'''



# 
def solution(data, col, row_begin, row_end):
    data.sort(key= lambda each: (each[col-1], -each[0]))
    n, m = len(data), len(data[0])
    sum_remain = [0] * row_end
    for i in range(row_begin-1, row_end):
        for j in range(m):
            sum_remain[i] += data[i][j] % (i+1)
    
    hash_val = sum_remain[row_begin-1]
    for i in range(row_begin, row_end):
        hash_val ^= sum_remain[i]
    
    return hash_val


'''
테스트 1 〉	통과 (0.03ms, 10MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.34ms, 10.3MB)
테스트 5 〉	통과 (2.71ms, 12.3MB)
테스트 6 〉	통과 (45.63ms, 57.8MB)
테스트 7 〉	통과 (76.70ms, 64.3MB)
테스트 8 〉	통과 (94.92ms, 64.4MB)
테스트 9 〉	통과 (99.94ms, 64.5MB)
테스트 10 〉	통과 (100.78ms, 64.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''


#
def return_remain(a, b):
    return a % b

def solution(data, col, row_begin, row_end):
    
    data.sort(key= lambda each: (each[col-1], -each[0]))
    n, m = len(data), len(data[0])
    hash_val = sum(map(return_remain, data[row_begin-1], [row_begin]*m))
    
    for i in range(row_begin, row_end):
        hash_val ^= sum(map(return_remain, data[i], [i+1]*m))
    
    return hash_val


'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.19ms, 10.3MB)
테스트 5 〉	통과 (1.34ms, 12.2MB)
테스트 6 〉	통과 (25.85ms, 57.8MB)
테스트 7 〉	통과 (37.93ms, 64.4MB)
테스트 8 〉	통과 (48.69ms, 64.5MB)
테스트 9 〉	통과 (51.82ms, 64.5MB)
테스트 10 〉	통과 (59.43ms, 64.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''
