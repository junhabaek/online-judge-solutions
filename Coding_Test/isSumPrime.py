## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12977

def find_prime(max_number):
    prime_list = []
    eratos = [0 for _ in range(max_number + 1)]
    eratos_length = len(eratos)

    for i in range(2, eratos_length):
        if eratos[i] == 0:
            prime_list.append(i)
            for j in range(i * i, eratos_length, i):
                eratos[j] = 1
    return prime_list

def split_odd_even(full_list):
    odd_nums, even_nums = [], []
    for i in full_list:
        even_nums.append(i) if i % 2 == 0 else odd_nums.append(i)
    return odd_nums, even_nums

def get_n_of_ooo_cases(prime_list, odd_list):
    odd_length = len(odd_list)
    n_of_cases = 0
    cumul = 0

    for i in range(odd_length):
        cumul += odd_list[i]
        for j in range(i + 1, odd_length):
            cumul += odd_list[j]
            for k in range(j + 1, odd_length):
                cumul += odd_list[k]
                if cumul in prime_list:
                    n_of_cases += 1
                cumul -= odd_list[k]
            cumul -= odd_list[j]
        cumul -= odd_list[i]

    return n_of_cases

def get_n_of_oee_cases(prime_list, odd_list, even_list):
    odd_length = len(odd_list)
    even_length = len(even_list)
    n_of_cases = 0
    cumul = 0

    for i in range(odd_length):
        cumul += odd_list[i]
        for j in range(even_length):
            cumul += even_list[j]
            for k in range(j + 1, even_length):
                cumul += even_list[k]
                print(cumul)
                if cumul in prime_list:
                    n_of_cases += 1
                cumul -= even_list[k]
            cumul -= even_list[j]
        cumul -= odd_list[i]

    return n_of_cases

def solution(nums):
    nums.sort()
    max_sum = sum(nums[-3:])

    odd_nums, even_nums = split_odd_even(nums)

    prime_nums = find_prime(max_sum)

    ooo_cases = get_n_of_ooo_cases(prime_nums, odd_nums)
    oee_cases = get_n_of_oee_cases(prime_nums, odd_nums, even_nums)

    return ooo_cases + oee_cases

