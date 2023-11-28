N, M = map(int, input().split())
books = map(int, input().split())
max_abs = 0  # 가장 먼 거리
p_li, n_li = [], []

for book in books:
    max_abs = max(max_abs, abs(book))
    if book > 0:
        p_li.append(book)
    else:
        n_li.append(-book)
p_li.sort(reverse=True)
n_li.sort(reverse=True)

result = 0
# 먼 곳부터 M권씩 반납해야 최소 걸음 보장
for i in range(0, len(p_li), M):
    result += p_li[i] * 2
for i in range(0, len(n_li), M):
    result += n_li[i] * 2
print(result - max_abs)  # 다시 0으로 돌아가지 않아도 됨
