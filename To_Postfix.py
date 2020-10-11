class infix2postfix:  # 将中缀表达式转换为后缀表达式
    def __init__(self):
        self.operators = ["+", "-", "×", "÷", "(", ")", "="]

    def to_postfix_expression(self, expression):  # 生成逆波兰表达式即后缀表达式
        operator_stack = []  # 运算符栈
        postfix_expression = []  # 运算表达式结果
        temp = []
        for item in expression:
            if item not in self.operators:  # 数字则放进暂时结果列表
                temp.append(item)
            elif item == '=':  # 遇到等号时将临时结果列表输出到结果列表
                if len(temp) != 0:
                    str_temp = ""
                    for i in range(0, len(temp)):
                        str_temp = str_temp + temp.pop(0)
                    postfix_expression.append(str_temp)
            else:
                if len(temp) != 0:
                    str_temp = ''
                    for i in range(len(temp)):
                        str_temp += temp.pop(0)
                    postfix_expression.append(str_temp)
                if len(operator_stack) == 0 or item == '(':  # 左括号直接入栈
                    operator_stack.append(item)
                elif item != '(' and item != ')':
                    if operator_stack[-1] != '(' and item in '×÷' and item not in '+-':  # 当栈顶不是左括号且当前不是’+/-‘时，入栈
                        operator_stack.append(item)
                    else:  # 当当前运算符是’+/-‘且栈顶是’×/÷‘时，将栈中的运算符弹出直到左括号停止
                        while True:
                            if operator_stack[-1] == '(':  # 当栈顶是左括号时，运算符入栈
                                operator_stack.append(item)
                                break
                            elif item not in '×÷' and item in '+-':
                                while len(operator_stack) != 0 and True:
                                    operator_str = operator_stack[-1]
                                    if operator_str == '(' or item not in '×÷' and operator_stack[-1] in '+-':
                                        break
                                    else:
                                        operator_stack.pop()
                                        postfix_expression.append(operator_str)
                            else:
                                postfix_expression.append(operator_stack.pop())
                            if len(operator_stack) == 0:
                                operator_stack.append(item)
                                break
                elif item == ')':  # 当前为右括号时，运算符出栈输出到表达式列表直到左括号停止
                    while True:
                        if operator_stack[-1] != '(':
                            postfix_expression.append(operator_stack.pop())
                        else:
                            operator_stack.pop()
                            break
                else:
                    operator_stack.append(item)
        if len(operator_stack) != 0:
            while len(operator_stack) != 0:
                postfix_expression.append(operator_stack.pop())
        return postfix_expression
