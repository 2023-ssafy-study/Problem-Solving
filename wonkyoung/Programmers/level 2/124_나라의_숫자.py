# 240620

def solution(n):
    converted, answer = '124', ''
    while n:
        n -= 1
        answer += converted[n % 3]
        n //= 3
        
    return answer[::-1]
