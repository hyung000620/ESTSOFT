import random

class TwoArmScale:
    __weights = []
    __count = 0
    
    def __init__(self, num_of_weights, num_of_fake_weight):
        self.__weights.extend([1009 for i in range(num_of_weights - num_of_fake_weight)])
        self.__weights.extend([997 for i in range(num_of_fake_weight)])
        random.shuffle(self.__weights)

    def compare(self, left_index_list, right_index_list):
        left_weights = sum([self.__weights[i] for i in left_index_list])
        right_weights = sum([self.__weights[i] for i in right_index_list])

        if left_weights > right_weights:
            return 1
        elif left_weights < right_weights:
            return -1
        else:
            return 0

    def submit(self, fake_index_list):
        for i in fake_index_list:
            if self.__weights[i] != 997:
                return "Wrong Answer"

        if len(fake_index_list) != len([x for x in self.__weights if x == 997]):
            return "Wrong Answer"

        return "Correct Answer, used " + str(self.__count) + " times."

def find_fake_weight(scale, left, right, max_count):
    mid = (left + right) // 2
    if left == right:
        return left

    left_group = list(range(left, mid + 1))
    right_group = list(range(mid + 1, right + 1))
    
    result = scale.compare(left_group, right_group)
    max_count -= 1  # 비교 횟수를 하나 감소시킴

    if result == 0:
        return find_fake_weight(scale, mid + 1, right, max_count)
    else:
        return find_fake_weight(scale, left, mid, max_count)

# 예제로 100개의 추 중에서 1개가 잘못 생산되었다고 가정합니다.
test1 = TwoArmScale(100, 1)
fake_index = find_fake_weight(test1, 0, 99, 10)
result = test1.submit([fake_index])

print("잘못 생산된 추의 인덱스:", fake_index)
print(result)