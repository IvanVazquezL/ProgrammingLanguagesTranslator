def javaProcessor(file,targetLanguage,newFileName):
    if targetLanguage == "python":
        name = newFileName + ".py"
        newTargetFile = open(name, "w")

        listLines = file.readlines()

        print(listLines)


        for line in listLines:
            print("hello")
            if "public class" in line:
                print("hi")
            if "static" in line:
                func = list(line.split(" "))
                print(func)


        newTargetFile.write("print()")
        newTargetFile.close()

    elif targetLanguage == "c++":
        print("c++")
    elif targetLanguage == "c#":
        print("c#")
    elif targetLanguage == "javascript":
        print("javascript")
    else:
        print("Target language is not available")
