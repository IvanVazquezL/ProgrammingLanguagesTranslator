from displayTranslation import displayTranslationFunction

def pythonProcessor(file, targetLanguage, newFileName,sourceFile):
    if targetLanguage == "javascript":
        name = newFileName + ".js"
        newTargetFile = open(name, "w")

        listLines = file.readlines()
        javascriptLine = ""
        firstFunction = bool(False)


        for line in listLines:
            #print(line)
            elementChecker = line.split(" ")
            for word in elementChecker:
                    javascriptLine = ""
                    #print(elementChecker)
                    #print("**",word,"**")
                    if word == "def":
                        #print(firstFunction)
                        if firstFunction:
                            newTargetFile.write("}")
                            newTargetFile.write("\n")
                            newTargetFile.write("\n")

                        functionName = elementChecker[1].replace(":", "{")
                        functionBoiler = "function " + functionName
                        javascriptLine += functionBoiler
                        newTargetFile.write(javascriptLine)
                    if word.find("print") !=-1:
                        printLine = line.replace("print","alert")
                        finalPrint = printLine.replace("))","));")
                        newTargetFile.write(finalPrint)
                    if word == "main()":
                        newTargetFile.write("}")
                        newTargetFile.write("\n")
                        newTargetFile.write("\n")
                        newTargetFile.write("main();")
                    if word=="return":
                        javascriptLine = line.replace("\n",";")
                        newTargetFile.write(javascriptLine)
                        newTargetFile.write("\n")
                    if word=="\n":
                        firstFunction = bool(True);


        newTargetFile.close()
        file.close()

        targetLanguage = "JavaScript"
        sourceLanguage = "Python"

    elif targetLanguage == "c++":
        print("c++")
    elif targetLanguage == "c#":
        print("c#")
    elif targetLanguage == "java":
        print("java")
    else:
        print("Target language is not available")

    displayTranslationFunction(sourceFile,targetLanguage,sourceLanguage,name)
