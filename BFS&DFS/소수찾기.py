from itertools import permutations

numbers = input()

def prime(n):
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    li = []
    for i in range(1,len(numbers)+1):
        li += list(permutations(numbers,i))
    li = [int("".join(i)) for i in li]    
    li = list(filter(prime, li))
    return len(set(li))

print(solution(numbers))