from itertools import permutations,combinations

"""
permutations(순열)
n개의 원소들 중에서 r개의 원소를 뽑는 경우의 수 (순서 상관 있음)
ex) ('A','B') != ('B','A')

combinations(조합)
n개의 원소들 중에서 r개의 원소를 뽑는 경우의 수 (순서 상관 없음)
ex) ('A','B') = ('B','A')
"""
arr = ['A','B','C']

nPr = list(permutations(arr,2))
nCr = list(combinations(arr,2))

print(nPr) # 출력: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(nCr) # 출력: [('A', 'B'), ('A', 'C'), ('B', 'C')]
