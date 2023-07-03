# class Rectangle:
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height
    
    
# rec = Rectangle(width=4, height=5)
# print(rec.area())

class Animal:
    def sound_play(self):
        pass

class Cat(Animal):
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f"{self.name}:" +  f"{self.sound}" * 2 

class Dog(Animal):
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f"{self.name}:" +  f"{self.sound}" * 3

animals = [Cat(name="르미", sound="Meow"), Dog(name="스트", sound="Bark")]
for animal in animals:
    print(animal.sound_play())