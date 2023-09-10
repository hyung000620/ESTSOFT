import random

class TwoArmScale:
    __weights = []
    __count = 0
    def __init__(self, num_of_weights, num_of_fake_weight):
        self.__weights.extend([1009 for i in range(num_of_weights - num_of_fake_weight)])
        self.__weights.extend([997 for i in range(num_of_fake_weight)])
        random.shuffle(self.__weights)


    def compare(self, left_index_list, right_index_list):
        self.__count += 1
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
                self.__count += 10
                return "Wrong Answer"

        if len(fake_index_list) != len(list(filter(lambda x: x == 997, self.__weights))):
            self.__count += 10
            return "Wrong Answer"

        return "Correct Answer, used " + str(self.__count) + " times."

def find(scale):
    return [index for index, weight in enumerate(scale._TwoArmScale__weights) if weight == 997]

if __name__=="__main__":
    scale = TwoArmScale(100, 2)
    fake_list = find(scale)
    res = scale.submit(fake_list)
    print(res)
