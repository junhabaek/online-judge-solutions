candidate_max = int(input())
votes_max = int(input())
votes = map(int, input().split())

# candidate_max = 3
# votes_max = 9
# votes = [2, 1, 4, 3, 5, 6, 2, 7, 2]

candidates = []
candidate_counts = 0
votes_per_all_students = [0]*101


for cur_vote in votes:
    # 사진틀에 없을 경우
    if cur_vote not in candidates:
        # 사진틀이 꽉찼을 경우
        if candidate_counts == candidate_max:
            # 최대 득표수는 vote_counts를 넘지 못한다.int.max의 대용으로 사용
            candidate_min_vote = votes_max
            candidate_min_id = -1

            # 리스트를 앞에서부터 순회하기 때문에, 같은 min value를 가진 index 중, 가장 오래된것이 min_index가 된다.
            for cur_candidate in candidates:
                if votes_per_all_students[cur_candidate] < candidate_min_vote:
                    candidate_min_id = cur_candidate
                    candidate_min_vote = votes_per_all_students[cur_candidate]

            candidates.remove(candidate_min_id)
            votes_per_all_students[candidate_min_id] = 0
        else:
            candidate_counts = candidate_counts + 1

        candidates.append(cur_vote)
        
    votes_per_all_students[cur_vote] = votes_per_all_students[cur_vote] + 1

# 정렬 출력하기
candidates.sort()
result_str = " ".join(str(candid_id) for candid_id in candidates)
print(result_str)

