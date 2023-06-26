with open("PYTHON_1/a.txt", "r") as f:
    content = f.read()
    print(id(content))
print(id(content)) 