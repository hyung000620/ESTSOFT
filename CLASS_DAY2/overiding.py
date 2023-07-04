class Animal:
    def speak(self,name):
        print("동물이 소리를 냅니다.")


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        