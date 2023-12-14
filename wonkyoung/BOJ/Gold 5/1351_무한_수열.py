# 231214
# 31120 KB / 44 ms
N, P, Q = map(int, input().split())
arr = {0: 1}
def find_num(level):
    if arr.get(level):
        return arr[level]

    key1, key2 = level//P, level//Q
    num1, num2 = find_num(key1), find_num(key2)
    arr[key1], arr[key2] = num1, num2
    return num1+num2

print(find_num(N))



# 31120 KB / 44 ms
N, P, Q = map(int, input().split())
if N == 0:
    print(1)
else:
    arr = {0: 1}
    def find_num(level):
        key1, key2 = level//P, level//Q
        if arr.get(key1):
            num1 = arr[key1]
        else:
            num1 = find_num(key1)
            arr[key1] = num1

        if arr.get(key2):
            num2 = arr[key2]
        else:
            num2 = find_num(key2)
            arr[key2] = num2

        return num1+num2

    print(find_num(N))