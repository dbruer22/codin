from math import pow
x = 1
y = 0
math = 0
answer = 0
answerList = []
final = ""

while True:
    if x < 10:
        math = pow(x,x)
        answer += y + math
        y = answer
        x += 1
    elif x == 10:
        for digit in double(answer):
            answerList.append(digit)
            x += 1
    else:
        final += answerList[range(-1,-11)]
        print(final)
