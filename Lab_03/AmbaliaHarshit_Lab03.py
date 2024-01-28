## LAB - 03

# NAME : AMBALIA HARSHIT
# SUBJECT : ACT
# ROLL NO. : MT001
# AIM : VALIDATE FINITE AUTOMETA FOR GIVEN INPUT

# Input : Number of nodes, Starting node, Transation Matrix & input string
# Output : Result string

def create_mapping(nodes):
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    mapping = {}
    for i in range(nodes):
        mapping.update({names[i]:i})
    return mapping

def check_autometa(strg, start, arr, end_nodes, nodes):
    mapping = create_mapping(nodes)
    current = mapping[start]
    for i in strg:
        i = int(i)
        current = mapping[arr[current][i]]

    flag = False
    for i in end_nodes:
        if(mapping[i]==current):
            flag = True
            break

    return flag


if __name__=="__main__":
    nodes = int(input("Enter number of nodes : "))

    start = input("Enter Start node : ")
    
    end_node_count = int(input("Enter number of End nodes : "))
    end_nodes = []
    for i in range(end_node_count):
        end_nodes.append(input(f'Enter {i+1}th end node : '))

    print("Enter Array : ")
    arr = []
    for i in range(nodes):
        a = []
        for j in range(2):
            a.append(input(f'Enter {i+1}th row, {j+1}th column element : '))
        arr.append(a)

    strg = input("Enter string : ")

    flag = check_autometa(strg, start, arr, end_nodes, nodes)

    if flag:
        print(f'String {strg} is ACCEPTED')
    else:
        print(f'String {strg} is NOT ACCEPTED')
