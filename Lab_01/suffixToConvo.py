suffix = list(input())
precidence = {'#':0, '+':1, '-':1, '*':2, '/':2}
alphabetCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stak = []
answer = []
# assumptions = []
for j in suffix:
    if(j in alphabets):
        stak.append(j)
    else:
        tmp1 = stak.pop()
        tmp2 = stak.pop()
        answer.append([j, tmp2, tmp1])
        temp = alphabetCap[0]
        alphabetCap.remove(temp)
        # assumptions.append([temp, answer[-1]])
        stak.append(temp)
print(answer)
# assumptions.pop()
# print(assumptions)
