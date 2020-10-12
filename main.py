from Generate_Expression import GenerateExpression
from To_Postfix import infix2postfix
import Calculate
import argparse
import linecache


def main():
    parser = argparse.ArgumentParser(description='一个自动生成小学四则运算题目的命令行程序')
    parser.add_argument('-n', dest='number', type=int, help='使用 -n 参数控制生成题目的个数')
    parser.add_argument('-r', dest='range', type=int, help='使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围')
    parser.add_argument('-e', dest='exercise', type=str, help='给定题目文件路径')
    parser.add_argument('-a', dest='answer', type=str, help='给定答案文件路径')
    i = 1
    args = parser.parse_args()
    try:
        res_exercise = '练习题目如下，共有' + str(args.number) + '道，开始练习吧！'
        res_answer = '对应题目的答案如下，开始校对吧！'
        f_exercise = open('Exercise.txt', 'w+', encoding='utf-8')
        f_answer = open('Answer.txt', 'w+', encoding='utf-8')
        while i <= args.number:
            get_exp = GenerateExpression(args.range)
            to_postfix = infix2postfix()
            get_exp.get_expression()
            res_exercise += '\n' + str(i) + '. ' + get_exp.expression
            answer_item = Calculate.get_result(
                to_postfix.numStr2fraction(to_postfix.to_postfix_expression(get_exp.expression)))
            res_answer += '\n' + str(i) + '. ' + str(answer_item)
            i += 1
        f_exercise.write(res_exercise)
        f_exercise.close()
        f_answer.write(res_answer)
        f_answer.close()
    except:
        correct = []
        wrong = []
        to_postfix = infix2postfix()
        f_score = open('Score.txt', 'w+', encoding='utf-8')
        f_exercise = open(args.exercise, 'r+', encoding='utf-8')
        f_uanswer = open(args.answer, 'r+', encoding='utf-8')
        c_num = 0
        w_num = 0
        exercises = f_exercise.read()
        for i in range(len(exercises)):
            answer_item = Calculate.get_result(to_postfix.numStr2fraction(to_postfix.to_postfix_expression(exercises[i + 1])))
            uanswer = linecache.getline(str(args.answer), i)
            if answer_item == uanswer:
                correct.append(i + 1)
                c_num += 1
            else:
                wrong.append(i)
                w_num += 1
        f_score.write('Correct:' + str(c_num) + '(')
        for x in correct:
            f_score.write(str(x) + ', ')
        f_score.write(')\n')
        f_score.write('Wrong:' + str(w_num) + '(')
        for x in wrong:
            f_score.write(str(x) + ', ')
        f_score.write(')\n')
        f_score.close()
        f_uanswer.close()


if __name__ == '__main__':
    main()
