from javaTranslator import javaProcessor

sourceFile = input("Source File: ")
targetLanguage = input("Target Language: ").lower()

file = open(sourceFile, "r")
#print(file.read())

nameAndType = sourceFile.split(".")
newFileName = nameAndType[0]
typeFile = nameAndType[1]

if typeFile == "java":
    print("Java")
    javaProcessor(file,targetLanguage,newFileName)

elif typeFile == "py":
    print("Python")

elif typeFile == "cs":
    print("C#")

elif typeFile == "js":
    print("JavaScript")

elif typeFile == "cpp":
    print("C++")

else:
    print("Not able to convert that type of file")

file.close()
