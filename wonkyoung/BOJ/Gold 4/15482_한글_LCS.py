# 231120
# 38300 KB / 680 ms
str1 = input()
str2 = input()
len1, len2 = len(str1), len(str2)
check = [[0] * (len1+1) for _ in range(len2+1)]
for i in range(1, len2+1):
    for j in range(1, len1+1):
        if str2[i-1] == str1[j-1]:
            check[i][j] = check[i-1][j-1]+1
        else:
            check[i][j] = max(check[i][j-1], check[i-1][j])

print(check[-1][-1])


# 38300 KB / 664 ms
str1 = input()
str2 = input()
len1, len2 = len(str1), len(str2)
check = [[0] * (len1+1) for _ in range(len2+1)]
for i in range(len2):
    for j in range(len1):
        if str2[i] == str1[j]:
            check[i+1][j+1] = check[i][j]+1
        else:
            check[i+1][j+1] = max(check[i+1][j], check[i][j+1])

print(check[-1][-1])

# 31120 KB / 544 ms
str1 = input()
str2 = input()
len1, len2 = len(str1), len(str2)
check = [0] * (len1+1)
temp = check[:]
for i in range(len2):
    for j in range(len1):
        if str2[i] == str1[j]:
            temp[j+1] = check[j]+1
        else:
            temp[j+1] = max(temp[j], check[j+1])

    check = temp[:]

print(check[-1])


# 31120 KB / 708 ms
str1 = input()
str2 = input()
len1, len2 = len(str1), len(str2)
check = [0] * (len1+1)
temp = check[:]
for i in range(len2):
    for j in range(len1):
        if ord(str2[i]) == ord(str1[j]):
            temp[j+1] = check[j]+1
        else:
            temp[j+1] = max(temp[j], check[j+1])

    check = temp[:]

print(check[-1])