#1번
number = input("숫자를 입력하세요: ")
length = len(number)
print("입력한 숫자는 %d자리입니다." % length)

#2번
date = input("날짜를 입력하세요 (yyyy-mm-dd): ")
year = date[:4]
month = date[5:7]
day = date[8:]
print("연도:", year)
print("월:", month)
print("일:", day)


#3번
number = int(input("정수를 입력하세요: "))

quotient = number // 2
remainder = number % 2

print("입력한 정수를 2로 나눈 몫은", quotient, "이고 나머지는", remainder, "입니다.")


# #4번
celsius = float(input("섭씨 온도를 입력하세요: "))

fahrenheit = celsius * 9/5 + 32

print("화씨 온도:", fahrenheit)

# #5번
filename = input("파일 이름을 입력하세요: ")
content = input("파일 내용을 입력하세요: ")

with open(filename, "w") as file: 
    file.write(content)

print("파일 생성 및 내용 저장이 완료되었습니다.")
print("파일을 열어 내용을 확인하는 동물이 있습니다...")
animal = "고양이"
print(animal, "가", filename, "파일을 열어 아래 내용을 확인합니다.")
with open(filename, "r") as file:
    file_content = file.read()
print("파일 내용:", file_content)