import os
file1 = open("students1.txt","r")
file2 = open("students2.txt","r")
file3 = open("students3.txt","w")
lines1 = file1.readlines()
lines2 = file2.readlines()
if len(lines1)>len(lines2):
    for i in range(len(lines2)):
        file3.write(lines1[i]+lines2[i])
    for i in range(len(lines1)-len(lines2)):
        file3.write(lines1[len(lines2)+i])
elif len(lines1)<len(lines2):
    for i in range(len(lines1)):
        file3.write(lines1[i]+lines2[i])
    for i in range(len(lines2)-len(lines1)):
        file3.write(lines2[len(lines1)+i])
else:
    for i in range(len(lines1)-1):
        file3.write(lines1[i]+lines2[i])
    file3.write(lines1[-1]+"\n"+lines2[-1])