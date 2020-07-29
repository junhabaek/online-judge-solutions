n = int(input())
expected_numbers = []

for i in range(n):
    expected_numbers.append(int(input()))

## test cases ##
# n = 8
# expected_numbers = [4, 3, 6, 8, 7, 5, 2, 1]
#
# n = 5
# expected_numbers = [1, 2, 5, 3, 4]

cur_expected_idx = 0
cur_expected_number = expected_numbers[cur_expected_idx]

simulated_numbers = []
simulated_operators = []

for i in range(1, n+1):
    simulated_numbers.append(i)
    simulated_operators.append("+")

    while cur_expected_number <= i:
        popped_number = simulated_numbers.pop()
        simulated_operators.append("-")

        if popped_number != cur_expected_number:
            print("NO")
            exit(0)
        if cur_expected_idx == n-1:
            for op in simulated_operators:
                print(op)

            exit(0)
        cur_expected_idx = cur_expected_idx+1
        cur_expected_number = expected_numbers[cur_expected_idx]
