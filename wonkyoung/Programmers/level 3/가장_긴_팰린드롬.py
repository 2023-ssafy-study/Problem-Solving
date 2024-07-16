# 240715
def solution(input_s):
    max_len, n = 1, len(input_s)
    if n == 1:
        return 1
    
    def find_max_len(s, e):
        while 0 <= s and e < n:
            if input_s[s] != input_s[e]:
                return e-s-1
            s -= 1
            e += 1
        return e-s-1
    
    for i in range(1, n-1):
        max_len = max(find_max_len(i-1, i+1), find_max_len(i-1, i), max_len)
    
    if input_s[-1] == input_s[-2] and max_len == 1:
        return 2

    return max_len



#
def solution(input_s):
    n = len(input_s)
    
    def find_max_len(s, e):
        while 0 <= s and e < n:
            if input_s[s] != input_s[e]:
                return e-s-1
            s -= 1
            e += 1
        return e-s-1

    len_list = [1]
    for i in range(1, n-1):
        len_list.append(find_max_len(i-1, i+1))
        
    for i in range(1, n):
        len_list.append(find_max_len(i-1, i))

    return max(len_list)
