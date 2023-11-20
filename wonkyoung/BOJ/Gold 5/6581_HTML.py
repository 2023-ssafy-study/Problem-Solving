# 231115
# 31120 KB / 48 ms
arr = []
line_length = 0

while True:
    try:
        line = input()
        if len(line.rstrip()) > 0:
            line = line.split()
            for element in line:
                if element == '<br>':
                    arr.append('\n')
                elif element == '<hr>':
                    arr.append('-'*80)
                else:
                    arr.append(element)

    except Exception:
        break

line = ''
for element in arr:
    length = len(element)
    if element == '\n':
        print(line)
        line_length = 0
        line = ''
    elif line_length + length >= 80:
        if line_length == 0:
            print(element)
            line_length = 0
            line = ''
        else:
            print(line)
            line_length = length
            line = element
    elif line:
        line_length += length+1
        line += f' {element}'
    else:
        line_length = length
        line = element

print(line)


# 31120 KB / 40 ms
arr = []
line_length = 0

while True:
    try:
        line = input()
        if len(line.rstrip()) > 0:
            line = line.split()
            for element in line:
                if element == '<br>':
                    arr.append('\n')
                elif element == '<hr>':
                    arr.append('-'*80)
                else:
                    arr.append(element)

    except EOFError:
        break

line = ''
for element in arr:
    length = len(element)
    if element == '\n':
        print(line)
        line_length = 0
        line = ''
    elif line_length + length >= 80:
        if line_length == 0:
            print(element)
            line_length = 0
            line = ''
        else:
            print(line)
            line_length = length
            line = element
    elif line:
        line_length += length+1
        line += f' {element}'
    else:
        line_length = length
        line = element

print(line)



# 31120 KB / 40 ms
from sys import stdin
arr = []
line_length = 0

for line in stdin:
    if len(line.rstrip()) > 0:
        line = line.split()
        for element in line:
            if element == '<br>':
                arr.append('\n')
            elif element == '<hr>':
                arr.append('-'*80)
            else:
                arr.append(element)

line = ''
for element in arr:
    length = len(element)
    if element == '\n':
        print(line)
        line_length = 0
        line = ''
    elif line_length + length >= 80:
        if line_length == 0:
            print(element)
            line_length = 0
            line = ''
        else:
            print(line)
            line_length = length
            line = element
    elif line:
        line_length += length+1
        line += f' {element}'
    else:
        line_length = length
        line = element

print(line)