class Car:
    wheel = 4
    window = 2
    
    def __init__(self, people):
        self.people = people
        
    def brake(self):
        print(f"{self.people}(이)가 brake!")
        
    def accel(self):
        print("accel!!")
    

my_car = Car("김도언")
my_car.brake()