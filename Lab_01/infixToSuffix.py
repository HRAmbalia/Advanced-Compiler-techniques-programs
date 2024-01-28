# Shunting Yard algorithm, which is used to convert infix expressions into postfix notation.

infix = list(input())
stk = ['#']
answer = []
precidence = {'#':0, '+':1, '-':1, '*':2, '/':2}
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(precidence['+'])
for j in infix:
    if(j in alphabets):
        answer.append(j)
    else:
        if(precidence[j] > precidence[stk[-1]]):
            stk.append(j)
        else:
            while(precidence[j] <= precidence[stk[-1]] and stk[-1]!='#'):
                p = stk.pop()
                answer.append(p)
            stk.append(j)
while(stk):
    p = stk.pop()
    answer.append(p)
answer.pop()
print(''.join(answer))
