A,P = map(int, input().split())

numbers = [A]
while True:
    tmp = 0
    for s in str(numbers[-1]):
        tmp += int(s)**P
    
    if tmp in numbers:
        break
    
    numbers.append(tmp)

print(numbers.index(tmp))