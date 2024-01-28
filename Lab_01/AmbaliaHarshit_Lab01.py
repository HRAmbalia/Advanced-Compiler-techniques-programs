## LAB - 01

# NAME : AMBALIA HARSHIT
# SUBJECT : ACT
# ROLL NO. : -----
# AIM : INFIX -> POSTFIX -> 3 ADDRESS CODE

# Shunting Yard algorithm, which is used to convert infix expressions to 3 address code

def infix_to_suffix(infix):
    # suffix and postfix is same.
	stack = ['#']
	answer = []
	precidence = {'#':0, '(':1, '+':2, '-':2, '*':3, '/':3, '^':4}
	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for j in infix:
		if(j=='('):
			stack.append(j)
		elif(j in alphabets):
			answer.append(j)
		elif(j==')'):
			while(stack[-1]!='('):
				p = stack.pop()
				answer.append(p)
			stack.pop()
		else:
			while(precidence[j]<=precidence[stack[-1]] and stack[-1]!='#'):
				p = stack.pop()
				answer.append(p)
			stack.append(j)
	while(stack):
		p = stack.pop()
		answer.append(p)
	answer.pop()
	return answer

def get_operations(suffix):
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
    return answer
    # assumptions.pop()
    # print(assumptions)

def main():
    infix = list('a*(b+c)/d-e')
    suffix = infix_to_suffix(infix)
    print(get_operations(suffix))

if __name__ == "__main__":
    main()