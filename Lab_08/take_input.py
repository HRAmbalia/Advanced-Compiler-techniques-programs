def take_input(length, flag):
    input_list = []
    length = 6
    for _ in range(length):
        temp_list = input("Enter a successor list (separated by spaces) : ").split()
        if flag:
            temp_list = [int(num) for num in temp_list]
        input_list.append(temp_list)
    print(input_list)

print(take_input(6, True))
