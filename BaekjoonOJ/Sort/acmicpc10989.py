from collections import defaultdict
import sys

number_counter = defaultdict(int)

number_counts = int(sys.stdin.readline())

for _ in range(number_counts):
    data = int(sys.stdin.readline())
    number_counter[data] += 1

for i in range(1, 10001):
    if number_counter[i] != 0:
        for j in range(number_counter[i]):
            print(i)
