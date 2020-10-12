from fractions import Fraction


class infix2postfix:  # 将中缀表达式转换为后缀表达式
    def __init__(self):
        self.operators = ["+", "-", "×", "÷", "(", ")", "="]
        self.pri_operators = {"+": 0, "-": 0, "×": 1, "÷": 1}

    def to_postfix_expression(self, expression):  # 生成逆波兰表达式即后缀表达式
        operator_stack = []  # 运算符栈
        postfix_expression = []  # 运算表达式结果
        temp = []
        for item in expression:
            if item not in self.operators:  # 数字则放进暂时结果列表
                temp.append(item)
            elif item == '=':  # 遇到等号时将临时结果列表输出到结果列表
                if len(temp) != 0:
                    str_temp = ''
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
                    if operator_stack[-1] != '(' and self.pri_operators[item] > self.pri_operators[
                        operator_stack[-1]]:  # 当栈顶不是左括号且当前不是’+/-‘时，入栈
                        operator_stack.append(item)
                    else:  # 当当前运算符是’+/-‘且栈顶是’×/÷‘时，将栈中的运算符弹出直到左括号停止
                        while True:
                            if operator_stack[-1] == '(':  # 当栈顶是左括号时，运算符入栈
                                operator_stack.append(item)
                                break
                            elif self.pri_operators[item] < self.pri_operators[operator_stack[-1]]:
                                while len(operator_stack) != 0 and True:
                                    operator_str = operator_stack[-1]
                                    if operator_str == '(' or self.pri_operators[operator_str] < self.pri_operators[
                                        item]:
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

    def numStr2fraction(self, postfix):  # 将字符形式的分数转换为 Fraction 形式
        for i in range(len(postfix)):
            if postfix[i] not in self.operators:
                postfix_item = postfix[i].strip()
                if postfix_item.find('’') == -1:
                    if postfix_item.find('/') == -1:
                        numerator = int(postfix_item)
                        denominator = 1
                    else:
                        a = postfix_item.split('/')
                        numerator = int(a[0])
                        denominator = int(a[1])
                else:
                    a = postfix_item.split('’')
                    integer = int(a[0])
                    b = a[1].split('/')
                    denominator = int(b[1])
                    numerator = integer * denominator + int(b[0])
                res_num = Fraction(numerator, denominator)
                postfix[i] = res_num
        return postfix

