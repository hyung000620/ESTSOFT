encoding_text = b'\xbc\xd3\xd3\xcd'

with open("input.txt","r") as f:
    li = f.read().replace(",","").replace("\n"," ").split()
    arr = []
    
    for i in li:
        try:
            text = encoding_text.decode(i)
            arr.append(text)
        except:
            pass

print(arr)