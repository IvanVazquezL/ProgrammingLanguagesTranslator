s = input("Enter name \n")
file = open(s, "r")
code = ""

for line in file:
    try:
        code += line
    except EOFError:
        break

print(code)
