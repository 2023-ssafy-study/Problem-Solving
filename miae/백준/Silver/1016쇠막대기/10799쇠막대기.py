lst = list(map(str,input().strip()))
lazer = False
bar = 0
ans = 0
for i in lst:
    if i == '(':
        if not lazer:
            lazer = True
        else:
            bar += 1
    else:
        if lazer:
            ans += bar
            lazer = False
        else:
            bar -= 1
            ans += 1
print(ans)