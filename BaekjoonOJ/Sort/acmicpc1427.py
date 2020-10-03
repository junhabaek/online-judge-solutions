from collections import Counter

target_number = input()

number_counter = Counter()
number_counter.update(target_number)

result_str = ""
for number in sorted(number_counter.keys(), reverse=True):
    result_str = result_str + number * number_counter[number]

print(result_str)