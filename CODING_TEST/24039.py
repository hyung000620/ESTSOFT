
# def isPrime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# arr = list(filter(isPrime,[i for i in range(2,110)]));
li = [6, 15, 35, 77, 143, 221, 323, 437, 667, 899, 1147, 1517, 1763, 2021, 2491, 3127, 3599, 4087, 4757, 5183, 5767, 6557, 7387, 8633, 9797, 10403, 11021, 11663]

N = int(input())
for i in li:
    if N<i:
        print(i)
        break


