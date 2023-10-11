'''
문제 조건 :
1. 순서대로 => 정렬을 통해

2. 모음이 한개이상,
3. 자음이 두개이상 => check라는 함수를 통해서 구현

4. 단어만들기 => 백트래킹을 통해,
    생각해야할 것 : 이미 앞에서 본 건 볼 필요없기 때문에, s라는 변수를 두고 반복문 조건만들기.
5. 출력 => 리스트를 문자열 형식으로 붙여 출력하기 ''.join(password)
'''
L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
def check(pw):
    # 모음 1개 이상
    check1, check2 = 0, 0
    for i in range(L):
        if pw[i] in {'a', 'e', 'i', 'o', 'u'}:
            check1 += 1
        else:
            check2 += 1
    if check1 >= 1 and check2 >= 2:
        return True
    else:
        return False

def solve(pw, s):
    if len(pw) == L:
        if check(pw):
            print(''.join(pw))
        return
    for i in range(s, C):
        pw.append(lst[i])
        solve(pw, i+1)
        pw.pop()
solve([], 0)