num_of_cases = int(input())


def travel(_key, _relations, _nodes_passed):
    _nodes_passed[_key] = True
    num_of_passed = 1
    nodes_to_be_passed = [_key]
    while nodes_to_be_passed:
        cur_node = nodes_to_be_passed.pop()
        for key in _relations[cur_node]:
            if not _nodes_passed[key]:
                num_of_passed = num_of_passed + 1
                nodes_to_be_passed.append(key)
                _nodes_passed[key] = True

    return num_of_passed


for _ in range(num_of_cases):
    relations = {}
    nodes_passed = {}

    num_of_relations = int(input())

    for _ in range(num_of_relations):
        cur_relation = tuple(input().split())

        relations[cur_relation[0]] = relations.get(cur_relation[0], set())
        first_relations = relations[cur_relation[0]]
        first_relations.add(cur_relation[1])
        nodes_passed[cur_relation[0]] = nodes_passed.get(cur_relation[0], False)

        relations[cur_relation[1]] = relations.get(cur_relation[1], set())
        second_relations = relations[cur_relation[1]]
        second_relations.add(cur_relation[0])
        nodes_passed[cur_relation[1]] = nodes_passed.get(cur_relation[1], False)

        for k in nodes_passed:
            nodes_passed[k] = False

        friends = travel(cur_relation[0], relations, nodes_passed)
        print(friends)
