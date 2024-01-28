no_of_stat = int(input("Enter number of statements : "))
statements = []
for i in range(no_of_stat):
    statements.append(input("Enter Expression : "))

my_dict = {}
answer = []
for i,stmt in enumerate(statements):
    if(len(stmt)==3):
        # Check if RHS is in dictionary if not add it. if yes use it.
        if(stmt[2] in my_dict):
            answer.append(stmt[0]+"="+my_dict[stmt[2]])
            my_dict[stmt[0]] = my_dict[stmt[2]]
        else:
            answer.append(stmt)
            my_dict[stmt[0]] = stmt[2]
    if(len(stmt)==5):
        if(stmt[2] in my_dict and stmt[4] in my_dict):
            answer.append(stmt[0]+"="+my_dict[stmt[2]]+stmt[3]+my_dict[stmt[4]])
        else:
            if(stmt[2] in my_dict):
                answer.append(stmt[0]+"="+my_dict[stmt[2]]+stmt[3]+stmt[4])
            if(stmt[4] in my_dict):
                answer.append(stmt[0]+"="+stmt[2]+stmt[3]+my_dict[stmt[4]])  
        if(stmt[0] in my_dict):
            my_dict.pop(stmt[0])
    print(stmt, my_dict, answer) 

