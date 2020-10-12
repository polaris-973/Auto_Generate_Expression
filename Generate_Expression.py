import random
from fractions import Fraction


class GenerateExpression():
    def __init__(self, max_value):
        self.get_operator()
        self.get_nums(max_value)
        self.get_expression()
    def get_num(self, max_value):
        return Fraction(random.randint(0, max_value), random.randint(1,max_value))
    def get_nums(self, max_value):
        self.nums = []
        self.nums.append(self.get_num(max_value))
        for x in range(len(self.operators)):
            y = self.get_num(max_value)
            if self.operators[x] == '÷':
                while y.numerator == 0:
                    y = self.get_num(max_value)
            self.nums.append(y)
        if len(self.nums) >= 5: # 当有括号时，不因括号产生多余的数
            del self.nums[-2:]


    def get_operator(self):  # 随机生成一个运算符并随机插入括号
        self.operators = []
        operator = ['+', '-', '×', '÷']
        for x in range(3):
            i = random.randint(0,2)
            if x != i:
                self.operators.append(random.choice(operator))
            if self.operators == []:
                self.operators.append(random.choice(operator))
        self.insert_bracket()


    def insert_bracket(self):
        if len(self.operators) > 1:
            x = random.randint(0, len(self.operators))
            while x < len(self.operators):
                y = random.randint(x, len(self.operators))
                flag_bracket = 0
                for a in self.operators[x:y+1]:
                     if a in ['+', '-']:
                         flag_bracket= 1
                         break
                try:
                    if self.operators[y+1] in ['×', '÷'] and flag_bracket:
                        self.operators.insert(x, '(')
                        self.operators.insert(y+2, ')')
                except IndexError:
                    pass
                x = y+2


    def num_change_str(self, num):
        x = num.numerator
        y = num.denominator
        if x % y == 0:  # num 为整数
            return '%d' % (x / y)
        elif x < y:  # num 为真分数
            return '%d%s%d' % (x, '/', y)
        else:
            z = int(x / y)
            x -= y * z
            return '%d%s%d%s%d' % (z, '’', x, '/', y)


    def get_expression(self):
        self.expression = ''
        right_bracket_flag = 0
        i = 0
        for operator in self.operators:
            if right_bracket_flag or operator == '(':
                self.expression += operator + ' '
            elif operator == ')':
                self.expression += self.num_change_str(self.nums[i]) + ' '
                self.expression += operator + ' '
                i += 1
                right_bracket_flag = 1
            else:
                self.expression += self.num_change_str(self.nums[i]) + ' '
                self.expression += operator + ' '
                i += 1
        self.expression += self.num_change_str(self.nums[-1]) + ' = ?'


i = GenerateExpression(20)
i.get_expression()
print(i.expression)
