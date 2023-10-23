#231012
# 31120 KB / 40 ms
def calc_bracket_value():
    bracket_string = input()
    length = len(bracket_string)
    stack = []
    values = [0] * length
    result = 0
    close_to_open = {')':'(', ']':'['}

    for i in range(length):
        element = bracket_string[i]
        if element in {'(', '['}:
            stack.append((element, i))
        elif not stack:
            return 0
        else:
            last, j = stack.pop()
            number = 2 if element == ')' else 3
            if last == close_to_open[element]:
                if j == i-1:
                    if stack:
                        values[j] = number
                    else:
                        result += number
                else:
                    temp = 0
                    for k in range(j+1, i):
                        value = values[k]
                        if value:
                            temp += value
                            values[k] = 0
                    temp *= number
                    if stack:
                        values[j] = temp
                    else:
                        result += temp
            else:
                return 0
    if stack:
        return 0

    return result

print(calc_bracket_value())