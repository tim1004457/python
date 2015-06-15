#-*-coding:utf-8-*-
__author__ = 'bj'
import string
import os
def createJava(file_name):
    file_obj = open(file_name)
    className = ""
    packageName = ""
    nameArray = []
    descArray = []
    try:
        list_content = file_obj.readlines()
        for content in list_content:
            content = content.replace("\n", "")
            content = content.replace("\t", "")
            content = content.replace(" ", "")
            idx = (content.index("="))
            name = content[0:idx]
            value = content[idx + 1:content.__len__()].replace("\n", "")
            if name == "className":
                className = value
            elif name == "packageName":
                packageName = value
            else:
                nameArray.append(name)
                descArray.append(value)
    finally:
        file_obj.close()

    fileContent = "package " + packageName + ";\n";
    fileContent += "public enum " + className + "{\n"
    for i in range(0, nameArray.__len__()):
        if i == nameArray.__len__() - 1:
            fileContent += (nameArray[i] + "(" + descArray[i] + ");\n")
        else:
            fileContent += (nameArray[i] + "(" + descArray[i] + "),\n")
    fileContent += "private String desc;\n"
    fileContent += className + '(String desc){this.desc=desc;'
    fileContent += '}\n';
    fileContent += "public String toString(){return desc;}\n"
    fileContent += "}\n"
    print(fileContent)
    outFile = open(className + ".java", "w")
    outFile.write(fileContent);
    outFile.flush()
    outFile.close()


dir = os.listdir("./")
for f in dir:
    print(f)