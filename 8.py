import re

import os

initials = input("Enter initials: ")

file1 =open("names.txt","r")

lines = file1.readlines()

for i in lines:
            
    if len(initials) == 2:

        name,surname = initials[0],initials[1]

        pattern1,pattern2  = r"{}[a-z]+\s{}[a-z]+".format(name,surname),r"{}[a-z]+\s[A-Z][a-z]+\s{}[a-z]+".format(name,surname)
            
        x, y = re.findall(pattern1,i), re.findall(pattern2,i)

        if y:

            print(y[0])
        
        elif x:

            print(x[0])

    else:

        name, middle, surname = initials[0], initials[1], initials[2]

        pattern = r"{}[a-z]+\s{}[a-z]+\s{}[a-z]+".format(name,middle,surname)

        x = re.findall(pattern,i)

        if x:

            print(x[0])