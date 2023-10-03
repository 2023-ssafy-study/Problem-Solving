#230605
str1 = input()
str2 = input()
len_1, len_2 = len(str1), len(str2)
length_list = [0] * (len_2+1)
for i in range(len_1):
    temp = length_list[:]
    for j in range(len_2):
        if str1[i] == str2[j]:
            temp[j+1] = max(length_list[j]+1, length_list[j+1])
        else:
            temp[j+1] = max(temp[j], length_list[j], length_list[j+1])
    length_list = temp[:]
print(max(length_list))


#
str1 = input()
str2 = input()
len_1, len_2 = len(str1), len(str2)
length_list = [0] * (len_2+1)
for i in range(len_1):
    temp = length_list[:]
    for j in range(len_2):
        if str1[i] == str2[j]:
            temp[j+1] = length_list[j]+1
        else:
            temp[j+1] = max(temp[j], length_list[j+1])
    length_list = temp[:]
print(max(length_list))


#
def lcs():
    str1 = input()
    str2 = input()
    len_1, len_2 = len(str1), len(str2)
    length_list = [0] * (len_2+1)
    for i in range(len_1):
        temp = length_list[:]
        for j in range(len_2):
            if str1[i] == str2[j]:
                temp[j+1] = length_list[j]+1
            else:
                temp[j+1] = max(temp[j], length_list[j+1])
        length_list = temp[:]
    return length_list[-1]
print(lcs())


#
def lcs():
    str1 = input()
    str2 = input()
    len_1, len_2 = len(str1), len(str2)
    length_list = [0] * (len_2+1)
    for i in range(len_1):
        temp = length_list[:]
        for j in range(len_2):
            if str1[i] == str2[j]:
                temp[j+1] = length_list[j]+1
            else:
                temp[j+1] = max(temp[j], length_list[j+1])
        for j in range(1, len_2+1):
            length_list[j] = temp[j]
    return length_list[-1]
print(lcs())