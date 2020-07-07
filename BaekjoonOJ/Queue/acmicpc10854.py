from collections import deque

number_of_commands = int(input())
queue = deque()
input_list = []
for i in range(number_of_commands):
    input_list.append(input().split())

for cur_input in input_list:
    cur_command = cur_input[0]
    cur_command_start_letter = cur_command[0]

    queue_length = len(queue)

    if cur_command_start_letter == 'f':
        if queue_length != 0:
            print(queue[-1])
        else:
            print(-1)
    elif cur_command_start_letter == 's':
        print(queue_length)
    elif cur_command_start_letter == 'e':
        if queue_length == 0:
            print(1)
        else:
            print(0)
    elif cur_command_start_letter == 'b':
        if queue_length != 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(cur_input) == 2:
            queue.appendleft(int(cur_input[1]))
        else:
            if queue_length != 0:
                print(queue.pop())
            else:
                print(-1)
