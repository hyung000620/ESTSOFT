# data = """
# B5    111    12.7%
# B4    131    15.0%
# B3    210    24.1%
# B2    145    16.6%
# B1    60    6.9%
# S5    87    10.0%
# S4    61    7.0%
# S3    33    3.8%
# S2    15    1.7%
# S1    7    0.8%
# G5    3    0.3%
# G4    3    0.3%
# G3    0    0.0%
# G2    1    0.1%
# G1    0 ss
# """

# # 빈 딕셔너리 생성
# result_dict = {}

# # 줄 단위로 데이터를 처리하고 딕셔너리에 추가
# for line in data.strip().split('\n'):
#     key, value, _ = line.split()  # 공백을 구분자로 사용하여 데이터 추출
#     result_dict[key] = int(value)

# print(result_dict)

res = {'B5': 111, 'B4': 131, 'B3': 210, 'B2': 145, 'B1': 60, 'S5': 87, 'S4': 61, 'S3': 33, 'S2': 15, 'S1': 7, 'G5': 3, 'G4': 3, 'G3': 0, 'G2': 1, 'G1': 0}

li = []
study = 0
for k,v in res.items():
    if v <100:
        li.append(f"{k}: {100-v}")
        study += (100-v)
        
        
print(*li,sep='\n')
print(study)