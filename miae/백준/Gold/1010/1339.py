'''
수학적 지식 - 결합법칙
AB + BB
= (10 * A + B) + (10 * B + B)
= (10 * A) + (12 * B)
= (12 * B) + (10 * A)
계수가 큰 수부터 내림차순으로 더해주면 가장 큰 값이 나온다.

필요한 자료구조
1. 단어를 넣을 리스트
2. 계수 딕셔너리
3. 계수값 내림차순 정렬
'''

N = int(input())
words = []
for _ in range(N):
    words.append(list(map(str, input().rstrip())))
coef = {}
for word in words:
    for i in range(len(word)):
        l = len(word) - 1 - i # 자릿수
        if word[i] not in coef:
            coef[word[i]] = 10 ** l
        else:
            coef[word[i]] += 10 ** l

# key * value 를 다 더하면된다.
nums = list(coef.values())
nums.sort(reverse=True)
#print(alpha_cnt)
#print(nums)
ans = 0
t = 9
for num in nums:
    ans += num * t
    t -= 1
print(ans)