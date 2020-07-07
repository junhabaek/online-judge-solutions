from collections import deque

num_of_cases = int(input())

input_queue = deque()
for i in range(num_of_cases):
    temp_list = []
    temp_list.append(input())
    temp_list.append(input())
    input_queue.appendleft(temp_list)

for i in range(num_of_cases):
    cur_input = input_queue.pop()
    num_of_documents, target_index = map(int, cur_input[0].split())
    documents = list(map(int, cur_input[1].split()))
    document_queue = deque(documents)
    isTarget_queue = deque([i == target_index for i in range(num_of_documents)])

    order = 1
    while True:
        cur_max = max(document_queue)
        cur_value = document_queue.popleft()
        isTarget = isTarget_queue.popleft()
        if cur_value >= cur_max:

            if isTarget:
                print(order)
                break
            else:
                order = order+1
        else:
            document_queue.append(cur_value)
            isTarget_queue.append(isTarget)

