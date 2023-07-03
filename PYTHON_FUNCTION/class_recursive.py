company = ["사장","부장","차장","과장","대리","나"]

def recursive(n):
    if n<1:
        print(company[n])
    else:
        recursive(n-1) # 위에 사람이 호출
        print(company[n]) # 일을 하려고 하는데
        

recursive(5)
"""
==== print result ====

사장
부장
차장
과장
대리
나
"""