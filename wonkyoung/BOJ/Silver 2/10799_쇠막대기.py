#231016
# 31120 KB / 60 ms
arrange = input()
now = total = 0
before = ''
for element in arrange:
    if element == '(':
        now += 1
    else:
        now -= 1
        if before == '(':
            total += now
        else:
            total += 1

    before = element

print(total)


# 31552 KB / 56 ms
arrange = input()
total = 0
stack = []
open = True
for element in arrange:
    if element == '(':
        stack.append(element)
        open = True
    else:
        stack.pop()
        if open:
            total += len(stack)
        else:
            total += 1
        open = False

print(total)


# 31120 KB / 52 ms
def cut_iron():
    arrange = input()
    now = total = 0
    before = ''
    for element in arrange:
        if element == '(':
            now += 1
        else:
            now -= 1
            if before == '(':
                total += now
            else:
                total += 1

        before = element

    return total

print(cut_iron())


# 31552 KB / 48 ms
def cut_iron():
    arrange = input()
    total = 0
    stack = []
    open = True
    for element in arrange:
        if element == '(':
            stack.append(element)
            open = True
        else:
            stack.pop()
            if open:
                total += len(stack)
            else:
                total += 1
            open = False

    return total

print(cut_iron())


# 31552 KB / 52 ms
def cut_iron():
    arrange = input()
    total = 0
    stack = []
    open = True
    for element in arrange:
        if element == '(':
            stack.append(element)
            open = True
        else:
            stack.pop()
            if open:
                total += len(stack)
                open = False
            else:
                total += 1

    return total

print(cut_iron())


# 31552 KB / 48 ms
def cut_iron():
    arrange = input()
    total, stack, open = 0, [], True
    for element in arrange:
        if element == '(':
            stack.append(element)
            open = True
        else:
            stack.pop()
            total += len(stack) if open else 1
            open = False

    return total

print(cut_iron())