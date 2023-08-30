from sys import stdin
import heapq

input = stdin.readline
N = int(input())

heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
        
import sys
# sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush


def main():

    heap = []
    # 여러 줄에 있는 데이터를 한번에 입력받기 - sys.stdin.buffer.read()
    _, *nums = map(int, sys.stdin.buffer.read().split())

    for x in nums:
        if x == 0:
            if len(heap) == 0:
                temp = 0
            else:
                temp = heappop(heap)
            sys.stdout.write(str(temp)+'\n')
        else:
            heappush(heap, x)
            
            
if __name__ == '__main__':
    main()
        