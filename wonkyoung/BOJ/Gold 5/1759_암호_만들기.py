#231005
L, C = map(int, input().split())
alp_list = input().split()
alp_list.sort()
def print_password(level=0, vowel=0, consonant=0, password='', start=0):
    if level == L:
        if vowel >= 1 and consonant >= 2:
            print(password)
        return
    for i in range(start, C):
        alp = alp_list[i]
        if alp in {'a', 'e', 'i', 'o', 'u'}:
            print_password(level+1, vowel+1, consonant, password+alp, i+1)
        else:
            print_password(level+1, vowel, consonant+1, password+alp, i+1)

print_password()


#
L, C = map(int, input().split())
alp_list = input().split()
alp_list.sort()
def print_password(vowel=0, consonant=0, password='', start=0):
    if vowel + consonant == L:
        if vowel >= 1 and consonant >= 2:
            print(password)
        return
    for i in range(start, C):
        alp = alp_list[i]
        if alp in {'a', 'e', 'i', 'o', 'u'}:
            print_password(vowel+1, consonant, password+alp, i+1)
        else:
            print_password(vowel, consonant+1, password+alp, i+1)

print_password()
