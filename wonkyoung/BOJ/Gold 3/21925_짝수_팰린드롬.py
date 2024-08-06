# 240806
# 31120 KB / 32 ms
def cnt_even_palindrome():

    N = int(input())
    arr = list(map(int, input().split()))
    cnt, start, end = 0, 0, 1
    can_make = False
    
    while end < N:
        i, j = start, end
        
        while i < j:
            if arr[i] != arr[j]:
                can_make = False
                break
            i += 1
            j -= 1
        else:
            cnt += 1
            start = end + 1
            can_make = True
        
        end += 2
    
    
    return cnt if can_make else -1

print(cnt_even_palindrome())
