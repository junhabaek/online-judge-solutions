test_case_counts = int(input())

for i in range(test_case_counts):
    cur_test_case = input()
    result_list = []
    result_index = 0
    for char in cur_test_case:
        if char == '-':
            if result_index != 0:
                result_index = result_index-1
                del result_list[result_index]
        elif char == '<':
            if result_index != 0:
                result_index = result_index-1
        elif char == '>':
            if result_index != len(result_list):
                result_index = result_index+1
        else:
            result_list.insert(result_index, char)
            result_index = result_index+1

        # print("".join(result_list))
    print("".join(result_list))
