def take_input(length, flag, strng):
    input_list = []
    for i in range(length):
        temp_list = input(f'Enter a {strng} for Block-{i} (separated by spaces) : ').split()
        if flag:
            temp_list = [int(num) for num in temp_list]
        input_list.append(temp_list)
    return input_list

def find_union(list_of_lists):
    union_result = set()
    for inner_list in list_of_lists:
        union_result = union_result.union(set(inner_list))
    union_list = list(union_result)
    return union_list

def find_difference(live_in_list, definition_list):
    set1 = set(live_in_list)
    set2 = set(definition_list)
    difference = set1.difference(set2)
    result_list = list(difference)
    return result_list

def live_variable_analysis(order_list, successor_set, use_dict, definition_dict):
    live_in_set = {}
    live_out_set = {}
    live_in_set_previous = {}
    live_out_set_previous = {}
    for i in range(len(order_list)):
        live_in_set[i] = []
        live_out_set[i] = []
        live_in_set_previous[i] = []
        live_out_set_previous[i] = []

    while(1):
        for i in order_list:
            temp_liveout = []
            for j in successor_set[i]:
                temp_liveout.append(live_in_set[j])
            live_out_set[i] = find_union(temp_liveout)

            temp_livein = []
            temp_livein.append(use_dict[i])
            temp_livein.append(find_difference(live_out_set[i], definition_dict[i]))
            live_in_set[i] = find_union(temp_livein)

        if((live_in_set_previous == live_in_set) and (live_out_set_previous == live_out_set)):
                return live_out_set, live_in_set
        else:
            live_in_set_previous = live_in_set
            live_out_set_previous = live_out_set

def main():
    number_of_blocks = int(input("Enter number of blocks : "))
    successor_set = take_input(number_of_blocks, True, "Successor set")
    use_dict = take_input(number_of_blocks, False, "Use dictionary set")
    definition_dict = take_input(number_of_blocks, False, "Defition dictionary set")
    order_list = list(map(int, input("Enter Order list sequence : ").split()))
    live_out_set, live_in_set = live_variable_analysis(order_list, successor_set, use_dict, definition_dict)
    print(f'Live out Set : {live_out_set}')
    print(f'Live in Set : {live_in_set}')

if __name__=="__main__":
    main()
