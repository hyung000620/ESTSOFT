"""
실버1 추월
car_dict에 index 값을 넣고, 터널에서 나온 차량들을 따로 배열에 추가한 다음에
먼저 나온 차들 중에서 나중에 나온 차량들의 인덱스보다 큰 경우가 
하나라도 있으면 cnt 값으 1증가시켜서 문제를 해결하였습니다.
"""
import sys
input = sys.stdin.readline
N = int(input())

car_dict,out = dict(),[]
for i in range(N):
    car_dict[input().rstrip()]=i
for j in range(N):
    out.append(input().rstrip())
cnt = 0
for i in range(N-1):
	for j in range(i+1, N):
		if car_dict[out[i]] > car_dict[out[j]]:
			cnt += 1
			break
print(cnt)
