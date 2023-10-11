#231011
N = int(input()) # 단어 개수
words = [input() for _ in range(N)] # 단어 목록
alp_weight = {chr(ord('A')+i): 0 for i in range(26)} # 알파벳별 가중치

for word in words:
    length = len(word)
    weight = 1 # 가중치
    for i in range(length-1, -1, -1):
        alp_weight[word[i]] += weight
        weight *= 10

# 가중치가 높은 순으로 정렬
alp_keys = list(alp_weight)
alp_keys.sort(key= lambda key: -alp_weight[key])

number = 9 # 대응되는 숫자
total = 0 # 총합
for key in alp_keys:
    total += number * alp_weight[key]
    number -= 1

print(total)


#
N = int(input())
alp_weight = {chr(ord('A')+i): 0 for i in range(26)}

for _ in range(N):
    word = input()
    length = len(word)
    weight = 1
    for i in range(length-1, -1, -1):
        alp_weight[word[i]] += weight
        weight *= 10

alp_keys = list(alp_weight)
alp_keys.sort(key= lambda key: -alp_weight[key])

number = 9
total = 0
for key in alp_keys:
    total += number * alp_weight[key]
    number -= 1

print(total)



#
def return_total():
    N = int(input())
    alp_weight = {chr(ord('A') + i): 0 for i in range(26)}

    for _ in range(N):
        word = input()
        length = len(word)
        weight = 1
        for i in range(length - 1, -1, -1):
            alp_weight[word[i]] += weight
            weight *= 10

    alp_keys = list(alp_weight)
    alp_keys.sort(key=lambda key: -alp_weight[key])

    number = 9
    total = 0
    for key in alp_keys:
        total += number * alp_weight[key]
        number -= 1

    return total

print(return_total())