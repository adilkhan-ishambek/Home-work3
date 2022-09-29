import os
import re

pattern1 = r".*(ime)$"
pattern2 = r".ave.*"
pattern3 = r".*[rstlne].*"
pattern4 = r".*[rstln].*"
pattern5 = r"^[^aeiou]+$"

endime = []
inave = []
cnt_rstlne = 0
cnt_rstln = 0
cnt_words = 0
no_vowels = []
all_vowels = []

with open("students3.txt") as infile:
    
    for line in infile:

        words = line.split()
    
        cnt_words+=len(words)
        
        for word in words:
          
            ime = re.findall(pattern1,word)
            ave = re.findall(pattern2,word)
            rstlne = re.findall(pattern3,word)
            rstln = re.findall(pattern4,word)
            no_vowel = re.findall(pattern5,word)
            
            if ime:
                endime.append(word)
            if ave:
                inave.append(word)
            if rstlne:
                cnt_rstlne+=1
            if rstln:
                cnt_rstln+=1
            if no_vowel:
                no_vowels.append(word)
            if re.search(r"a",word) and  re.search(r"e",word) and  re.search(r"i",word) and  re.search(r"o",word) and  re.search(r"y",word) and  re.search(r"u",word):
                all_vowels.append(word)

print(endime,inave,cnt_rstlne*100/cnt_words,cnt_rstln,no_vowels,all_vowels)
