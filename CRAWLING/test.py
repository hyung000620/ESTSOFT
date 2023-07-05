from datetime import datetime
import re
import sys

now = datetime.now()
now = now.strftime("%Y년 %m월 %d일")

while True:
    name = input("이름을 입력해주세요:")
    if not re.search(r"^[가-힣]+$",name):
        print("이름은 한글로만 입력해주세요.")
        continue
    
    user_id = input("아이디를 입력해주세요:")
    
    
    break

pw = ""
while True:
    pw = input("비밀번호를 입력하세요: ")

    #8자리 이상으로 제한
    if len(pw)<8:print("비밀번호는 8자리 이상이어야 합니다.");continue
    
    #2자리이상 반복되는 구간 없도록(aa같은) 제한
    if re.search(r"(.)\1{1,}",pw):print("2자리이상 반복되는 구간 없도록(aa같은) 제한");continue
    
    #영문대소문자/숫자/특수문자 포함여부 확인
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).+$",pw):print("영문대소문자/숫자/특수문자 포함여부 확인");continue
    
    if " " in pw:print("비밀번호에 공백이 포함되어 있습니다.");continue
    
    print("강력한 비밀번호 입니다.")
    break

cnt = 1
while True:
    pw2 = input("비밀번호를 한번 더 입력하세요:")

    if cnt ==3:break

    if pw != pw2:
        print("비밀번호를 다시입력해주세요.")
        cnt +=1
    else:
        print("비밀번호 확인이 완료되었습니다")
        break
        

gender = input("주민등록번호를 입력하세요(-포함):")
gender = gender.split("-")[1]
st = "남성"
if gender[0] == 2 or gender[0] == 4: st="여성"

print(f'{st}회원입니다.')
print(f"가입일은 {now} 입니다")