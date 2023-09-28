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


def find(scale, weight_cnt, fake_cnt):
    weight_list = [i for i in range(weight_cnt)]
    left_list, right_list = weight_list[:weight_cnt], weight_list[weight_cnt:]
    left_length, right_length = len(left_list), len(right_list)
    
    tmp = scale.compare(left_list, right_list)
    
    res = []
    if tmp == 1:
        res = find_compare(right_list, right_length)
        if len(res) == fake_cnt:
            return res
        else:
            return find_compare(left_list, left_length)
    elif tmp == -1:
        res = find_compare(left_list, left_length)
        if len(res) == fake_cnt:
            return res
        else:
            return find_compare(right_list, right_length)
    else:
        res = find_compare(weight_list, weight_cnt)
    
    
def find_compare(weight_list, length):
    res = []
    for i in range(length-1):
        tmp = scale.compare([weight_list[i]], [weight_list[i+1]])
        if tmp == 1:
            res.append(weight_list[i+1])
        elif tmp == -1:
            res.append(weight_list[i])
            
        if len(res)==fake_cnt:
            break
    
    return res        

if __name__ == "__main__":
    weight_cnt = 100
    fake_cnt = 1
    scale = TwoArmScale(weight_cnt, fake_cnt)
    fake_list = find(scale, weight_cnt,fake_cnt)
    res = scale.submit(fake_list)
    print(res)