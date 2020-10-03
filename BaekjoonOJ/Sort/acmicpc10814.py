from operator import itemgetter

member_max = int(input())

member_datas = []
member_counts = 0

for _ in range(member_max):
    age, name = input().split()
    member_datas.append((int(age), name, member_counts))
    member_counts = member_counts + 1

member_datas.sort(key=itemgetter(0,2))

for member in member_datas:
    print(member[0], member[1])
