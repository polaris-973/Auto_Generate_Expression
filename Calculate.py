def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '×':
        return num1 * num2
    elif operator == '÷':
        return num1 / num2


def get_result(expression):
    stack = []
    for item in expression:
        if item in ['+', '-', '×', '÷']:
            num2 = stack.pop()
            num1 = stack.pop()
            result = calculate(num1, num2, item)
            if result < 0:
                return -1
            stack.append(result)
        else:
            stack.append(item)
    return stack[0]

