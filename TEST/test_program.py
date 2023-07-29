from datetime import datetime, time
from PIL import Image

class Oreumi:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
                
class Teacher(Oreumi):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
    
    def say(self):
        return f"({self.grade}){self.name} 수업시작하겠습니다."
    
class Mentor(Oreumi):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
    
    def say(self):
        return f"({self.grade}){self.name} 오르미 여러분 QR 찍으셔야 합니다."
        
class Student(Oreumi):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        
    def say(self):
        return "음소거 되었습니다."
    
def msg(mentor, teacher):
    now = datetime.now()
    
    time1 = time(now.hour, 50, 0)
    time2 = time(now.hour, 0 ,0)
    
    if now.time() == time1:
        print(mentor.say())
        
        image_path = "qr.png"
        try:
            img = Image.open(image_path)
            img.show()
        except:
            print("이미지 파일을 찾을 수 없습니다.")
            
    elif now.time() == time2:
        print(teacher.say())
        
mentor1 = Mentor("이예원",20,"멘토")
teacher1 = Teacher("김도언",20, "강사")

while 8< datetime.now().hour <18:
    msg(mentor1,teacher1)
