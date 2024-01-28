number_of_blocks = 4
number_of_variables = 7

generate_matrix = [
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
]
kill_matrix = [
    [0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
]
predecessors_matrix = [
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
]

gen_set = []
for i in range(number_of_blocks):
    temp = []
    for j in range(number_of_variables):
        if(generate_matrix[i][j]==1):
            temp.append(j+1)
    gen_set.append(temp)
print(gen_set)

kill_set = []
for i in range(number_of_blocks):
    temp = []
    for j in range(number_of_variables):
        if(kill_matrix[i][j]==1):
            temp.append(j+1)
    kill_set.append(temp)
print(kill_set)

predecessors_set = []
for i in range(number_of_blocks):
    temp = []
    for j in range(number_of_blocks):
        if(predecessors_matrix[i][j]==1):
            temp.append(j+1)
    predecessors_set.append(temp)
print(predecessors_set)

reach_in_set = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
reach_out_set = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

reach_in_set_previous = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
reach_out_set_previous = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

def find_union(list_of_lists):
    result = []
    if(list_of_lists):
        for i in range(len(list_of_lists[0])):
            max_value = max([list_of_lists[j][i] for j in range(len(list_of_lists))])
            result.append(max_value)
    else:
        result = [0]*number_of_variables
    return result

def find_difference(reach_in_list, kill_list):
    result = []
    for i in range(len(reach_in_list)):
        if(reach_in_list[i]==1):
            result.append(reach_in_list[i] - kill_list[i])
        else:
            result.append(0)
    return result

var = 1
while(True):
    for i in range(number_of_blocks):
        temp_reachin = []
        for j in range(len(predecessors_set[i])):
            temp_reachin.append(reach_out_set[predecessors_set[i][j]-1])
        reach_in_set[i] = find_union(temp_reachin)

        temp_reachout = []
        temp_reachout.append(generate_matrix[i])
        temp_reachout.append(find_difference(reach_in_set[i], kill_matrix[i]))
        reach_out_set[i] = find_union(temp_reachout)

    if((reach_in_set_previous == reach_in_set) and (reach_out_set_previous == reach_out_set)):
        print(var)
        var = var +1
        print(reach_in_set)
        print(reach_out_set)
        exit(0)
    else:
        reach_in_set_previous = reach_in_set
        reach_out_set_previous = reach_out_set