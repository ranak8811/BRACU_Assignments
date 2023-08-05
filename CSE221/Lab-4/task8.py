from collections import defaultdict

def find_maximum_members(T, cases):
    for case_num in range(1, T + 1):
        n = cases[case_num]['n']
        fights = cases[case_num]['fights']

        rivals = defaultdict(set)

        for fight in fights:
            u, v = fight
            rivals[u].add(v)
            rivals[v].add(u)

        max_members = max(len(rivals[rival]) for rival in rivals)

        print(f"Case {case_num}: {max_members}")

T = int(input())

cases = {}

for case_num in range(1, T + 1):
    n = int(input())
    fights = []
    for _ in range(n):
        u, v = map(int, input().split())
        fights.append((u, v))
    
    cases[case_num] = {'n': n, 'fights': fights}

find_maximum_members(T, cases)
