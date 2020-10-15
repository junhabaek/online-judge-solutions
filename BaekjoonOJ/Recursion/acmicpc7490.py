case_number = int(input())


class Find0:
    def __init__(self, length):
        self.cur_statements = list(','.join(map(str, range(1, length+1))))
        self.length = len(self.cur_statements)

    def start_find0(self):
        self.find0(1, '+')
        self.find0(1, '-')
        self.find0(1, ' ')

    def find0(self, cur_idx, cur_op):
        self.cur_statements[cur_idx] = cur_op
        if cur_idx + 2 == self.length:
            result = self.calculate_result()
            if result == 0:
                print(''.join(self.cur_statements))
        else:
            self.cur_statements[cur_idx] = cur_op
            self.find0(cur_idx+2, '+')
            self.find0(cur_idx+2, '-')
            self.find0(cur_idx+2, ' ')

    def calculate_result(self):
        cur_sum = 0
        before_number = "0"
        last_op = "+"
        is_extending = False

        for i in range(self.length):
            ## TODO commit하는걸 op index에서 했어야 했다.
            if i % 2 ==0: ## number idx
                if is_extending:
                    before_number += self.cur_statements[i]
                else:
                    before_number = self.cur_statements[i]
            else:  ## op idx
                cur_op = self.cur_statements[i]
                if cur_op == " ":
                    is_extending = True
                else:
                    if last_op == "+":
                        cur_sum += int(before_number)
                    else:
                        cur_sum -= int(before_number)

                    last_op = cur_op
                    is_extending = False

        if cur_sum == 0:
            return -500

        if last_op == "+":
            cur_sum += int(before_number)
        elif last_op == "-":
            cur_sum -= int(before_number)

        return cur_sum


for _ in range(case_number):
    cur_number = int(input())
    cur_case = Find0(cur_number)
    cur_case.start_find0()
    print()
