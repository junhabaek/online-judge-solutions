## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    n_of_jobs = len(jobs)
    expected_jobs = sorted(jobs, key=lambda x: -x[0])
    waiting_jobs = []
    cur_time = 0
    answer = 0

    while expected_jobs or waiting_jobs:
        while expected_jobs and expected_jobs[-1][0] <= cur_time:
            target = expected_jobs.pop()
            heapq.heappush(waiting_jobs, (target[1], target[0]))

        if waiting_jobs:
            cur_job = heapq.heappop(waiting_jobs)
            cur_time += cur_job[0]
            answer += cur_time - cur_job[1]
        else:
            cur_time = expected_jobs[-1][0]

    return answer // n_of_jobs
