from javaTranslator import javaProcessor
from javascriptTranslator import javascriptProcessor
from pythonTranslator import pythonProcessor

sourceFile = input("Source File: ")
targetLanguage = input("Target Language: ").lower()

file = open(sourceFile, "r")
#print(file.read())

#We split the sourceFile in two, the name of the file and its type
nameAndType = sourceFile.split(".")
newFileName = nameAndType[0]
typeFile = nameAndType[1]

if typeFile == "java":
    print("Java")
    javaProcessor(file,targetLanguage,newFileName)

elif typeFile == "py":
    print("Python")
    pythonProcessor(file,targetLanguage,newFileName)

elif typeFile == "cs":
    print("C#")

elif typeFile == "js":
    print("JavaScript")
    javascriptProcessor(file,targetLanguage,newFileName)

elif typeFile == "cpp":
    print("C++")

else:
    print("Not able to convert that type of file")

file.close()
