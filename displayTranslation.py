def displayTranslationFunction(sourceFile,targetLanguage,sourceLanguage,name):
    print(" ")
    print(" ")
    print(sourceLanguage,"=>",targetLanguage)
    print(" ")
    print(" ")
    print(sourceLanguage,"-",sourceFile)
    print(" ")
    readSourceFile = open(sourceFile, "r")
    print(readSourceFile.read())
    readSourceFile.close()

    readTargetFile = open(name, "r")
    print(" ")
    print(" ")
    print(targetLanguage,"-",name)
    print(" ")
    print(readTargetFile.read())
    readTargetFile.close()
