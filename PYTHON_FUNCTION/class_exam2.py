class Estsoft:
    
    work_in = 9
    work_out = 18
    company = "이스트소프트"
        
    def __init__(self,name,age:int):
        self.name = name
    
    def getJob(self):
        pass
    def go_to_work(self):
        return f"{self.work_in}시에 출근합니다."
    def go_to_home(self):
        return f"{self.work_out}시에 퇴근합니다."
        
class Developer(Estsoft):
    job = "개발자"
    def __init__(self,name,age:int):
        self.name = name
        self.age = age
        
    def getJob(self):
        return f"저는 {self.company} 에서 {self.job}로 일하고 있습니다."
    
    def night_shift(self,time:int):
        work_out = self.work_out +time
        return f"{time}시간 야근으로 인하여 {work_out}시에 퇴근합니다."
    
    def getName(self):
        return self.name

    def setNick(self,nick):
        self.name = nick
    def aboutMe(self):
        return f"제 이름은 {self.name}이고,\n나이는 {self.age} 입니다.\n현재 저는 {self.getJob()}"
        
class Pm(Estsoft):
    job = "프로젝트매니저"
    
    def __init__(self,name,age:int):
        self.name = name
        self.age = age
        
    def getJob(self):
        return f"저는 {self.company} 에서 {self.job}로 일하고 있습니다."
    
    def night_shift(self,time:int):
        work_out = self.work_out +time
        return f"{time}시간 야근으로 인하여 {work_out}시에 퇴근합니다."
    
    def getName(self):
        return self.name
    
    def setNick(self,nick):
        self.name = nick
    def aboutMe(self):
        return f"제 이름은 {self.name}이고,\n나이는 {self.age} 입니다.\n현재 저는 {self.getJob()}"


class Designer(Estsoft):
    job = "디자이너"
    
    def __init__(self,name,age:int):
        self.name = name
        self.age = age
        
    def getJob(self):
        return f"저는 {self.company} 에서 {self.job}로 일하고 있습니다."
    
    def night_shift(self,time:int):
        work_out = self.work_out +time
        return f"{time}시간 야근으로 인하여 {work_out}시에 퇴근합니다."
    
    def getName(self):
        return self.name
    
    def setNick(self,nick):
        self.name = nick
    
    def aboutMe(self):
        return f"제 이름은 {self.name}이고,\n나이는 {self.age} 입니다.\n현재 저는 {self.getJob()}"
    
     
    
est1 = Developer(name="지삐",age=26)
est2 = Designer(name="별이",age=32)
est3 = Pm(name="정하영",age=35)

est2.setNick("토깽이")
team1 = [est1,est2,est3]

for i in team1:
    print(i.aboutMe())
    if i.getName() == "별이":
        print(i.night_shift(3))
    else:
        print(i.go_to_home())
    print("=====================================")
    print()