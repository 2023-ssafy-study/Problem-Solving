def find_blood(name):
    global blood
    if name in blood.keys():
        return
    if name not in parent.keys():
        blood[name] = 0
        return
    p1, p2 = parent[name]
    find_blood(p1)
    find_blood(p2)
    blood[name] = (blood[p1] + blood[p2]) / 2


N, M = map(int, input().split())
b = input()  # 유토피아를 세운 사람
parent = {}  # 자식: (부모)
for _ in range(N):
    child, p1, p2 = input().split()
    parent[child] = (p1, p2)

answer = ''
blood = {b: 1}  # 혈통
for _ in range(M):
    name = input()
    if name not in blood.keys():
        find_blood(name)
    if not answer or blood[answer] < blood[name]:
        answer = name

print(answer)
