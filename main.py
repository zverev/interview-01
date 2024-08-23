from sys import *
from os import *


total_lines=0
total_empty=0
executables=0




def count_lines(file_name,file_lines,file_empty):
    file = open(file_name)
    for line in file:
        if line.strip():
            file_lines = file_lines + 1
            total_lines = total_lines + 1
        else:
            file_empty = file_empty + 1
            total_empty=total_lines+1
    print file_name,file_lines,file_empty


def CheckExecutable(file_name):
    import re
    global executables
    f = open(file_name, "r")
    S = f.read()
    x=re.search("^#!.*python[23]",S,re.MULTILINE)
    y = re.search("^\s*if.\s*__name__\s*==.*__main__.*:", S, re.MULTILINE)
    if x and y:
        executables+=1


#usage:
#./count.py path_to_project output.txt
result = open(argv[0],"w")
for path, dirs, files in walk(argv[1]):
    for name in files:
        if name.endswith('.py'):
            file_lines = 0
            file_empty = 0
            CheckExecutable(path+'/'+name)
            count_lines(path+name,file_lines,file_empty)
            result.write(path+name + " " + file_lines + "/" + file_empty)
result.write("Total:"+total_lines+" non empty lines, "+empty_lines+" empty  lines ")
print("Total:",total_lines," non empty lines, ",total_empty," empty lines ")
result.write("Executables:"+`executables`)
print("Executables:",executables)
result.close()
