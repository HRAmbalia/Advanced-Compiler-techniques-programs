
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
			stack.pop() #to remove '('
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

state = 'a*(b+c)/d-e'
# state = input()
print(infix_to_suffix(state))