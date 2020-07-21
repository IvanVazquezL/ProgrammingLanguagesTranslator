from javascriptParser import parserFile


def javascriptProcessor(file, targetLanguage, newFileName):
    if targetLanguage == "python":
        name = newFileName + ".py"
        newTargetFile = open(name, "w")

        listLines = file.readlines()
        pythonLine = ""

        for line in listLines:
            elementChecker = line.split(" ")
            for word in elementChecker:
                    pythonLine = ""
                    #print("**",word,"**")
                    if word == "function":
                        functionName = elementChecker[1].replace("{", ":")
                        functionBoiler = "def " + functionName
                        pythonLine += functionBoiler
                        newTargetFile.write(pythonLine)
                    if word.find("main();") !=-1:
                        pythonLine = "if __name__ == \"__main__\": "
                        newTargetFile.write(pythonLine)
                        newTargetFile.write("\n")
                        pythonLine = "  main()"
                        newTargetFile.write(pythonLine)
                    if word.find("}") !=-1:
                        newTargetFile.write("\n")
                    if word=="return":
                        indexWord = elementChecker.index("return")
                        returnLine = "  return "+elementChecker[indexWord+1].replace(";","")
                        newTargetFile.write(returnLine)
                    if word.find("alert") !=-1:
                        print("line",line)
                        printLine = line.replace("alert","print")
                        finalPrint = printLine.replace(";","")
                        newTargetFile.write(finalPrint)

        newTargetFile.close()

    elif targetLanguage == "c++":
        print("c++")
    elif targetLanguage == "c#":
        print("c#")
    elif targetLanguage == "java":
        print("java")
    else:
        print("Target language is not available")
