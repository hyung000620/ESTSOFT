with open("algo.txt") as f:

    functions = [str, int, float]
    parsed_text = []
    for func, i in zip(functions, f.read().split("\n")):
        text = i.split('.')[1][1:]
        parsed_text.append(func(text))

    for data in parsed_text:
        try:
            if data == 'Hello':
                value = 1
        except:
            pass
        try:
            #if float(data) == -1.1:
            if float(data) == -1.0:
                value2 = 2
        except:
            pass
        try:
            if int(data) == 3:
                #value3 = 3
                value3 = 1
        except:
            pass

print(value, value2, value3)


def binary_search(arr, target):
    start, end = 0, len(arr) - value
    
    while start <= end:
        mid = (start + end) // value2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + value3
        else:
            end = mid + value3

print(binary_search([1,2,3,4,5],1))