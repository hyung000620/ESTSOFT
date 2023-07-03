# import random

# player_name = "지삐"
# player_health = 100
# player_attack = 10

# enemy_name = "별이"
# enemy_health = 50
# enemy_attack = 5

# def player_turn():
#     global enemy_health

#     action = input("어떤 행동을 하겠습니까? (1: 건초어택/2: 사료스킬)")

#     if action == "1":
#         attack_damage = random.randint(1, player_attack)
#         attack(player_name, attack_damage)
#         enemy_health -= attack_damage

#     elif action == "2":
#         skill_damage = random.randint(1, player_attack + 5)
#         attack(player_name, skill_damage)
#         enemy_health -= skill_damage

#     else:
#         print("잘못된 입력입니다. 다시 입력해주세요!")
#         player_turn()

# def enemy_turn():
#     global player_health
#     enemy_attack_damage = random.randint(1, enemy_attack)
#     attack(enemy_name, enemy_attack_damage)
#     player_health -= enemy_attack_damage

# def attack(character_name, attack_damge):
#     print(f"{character_name}의 공격! 적에게 {attack_damge}의 피해를 입혔습니다!")

# while player_health > 0 and enemy_health > 0:
#     print(f"{player_name}의 차례입니다.")
#     player_turn()

#     print(f"{enemy_name}의 차례입니다.")
#     enemy_turn()

# if player_health > 0:
#     print("승리하였습니다!")
# else:
#     print("패배하였습니다ㅠㅠ")

class HealthCheck:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def check_health(self):
        bmi = self.calculate_bmi()
        result = self.get_result(bmi)

        return f"""=== 건강검진 결과 ===
        이름: {self.name}
        나이: {self.age}
        신장: {self.height}cm
        체중: {self.weight}kg
        BMI: {bmi:.2f}
        f"결과: {result}"""

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"
        
    def backup_records(self):
        with open("result.txt","w",encoding="utf-8") as f:
            f.write(self.check_health())
    def getAge(self):
        return self.age

person1 = HealthCheck(name="이준형", age=28, height=180,weight=80)
person2 = HealthCheck(name="이예원", age=21, height=160,weight=50)

li = [person1,person2]

li = list(map(lambda x: x.getAge(),li))
# print(sum(li)/len(li))