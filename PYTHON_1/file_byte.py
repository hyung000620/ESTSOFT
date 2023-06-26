file = open("PYTHON_1/byte.txt", "rb")
context = file.read()
print(context)
file.close()

file = open("PYTHON_1/byte.txt", "rw")
file.write(b'hello')
file.close()