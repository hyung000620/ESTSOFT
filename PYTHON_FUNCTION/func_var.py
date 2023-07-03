global_var = 100

def my_func(global_var=global_var):
    # global global_var
    
    local_var =50
    global_var += 50 # global 변수 선언 없이 사용하면 UnboundLocalError
    print("전역변수: ",global_var) 
    print("지역변수: ",local_var)

# my_func()
# print("전역변수: ",global_var)
# print("지역변수: ",local_var) #NameError

# def get_person():
#     return "김도언",20,"4_2@naver.com"

# name, age, email = get_person()
# print(f"이름 {name}, 나이 {age}, 이메일 {email}")

def add(a:int, b:int)->int:
    """
    Description:
        두 수를 입력받아 합을 리턴한다.
    Args:
        a`int: 정수
        b`int: 정수
    Returns:
        result `int`:합한 값
    """
    return a+b

print(add(3,5))