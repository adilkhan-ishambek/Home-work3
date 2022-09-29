import re

data  = ["Feb 1 2019","Janjhhh.  3     1290","Feb.23  2017 ","JAhnuary 01 15"]

mp = {"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12,"jan":1}

pattern1 = r"(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)|(jan)\w*"

for i in data:
  
    i = i.lower()
    i = re.sub("\."," ",i)
    i = re.sub("\s+"," ",i)

    x = re.findall(pattern1,i)
    
    if x:

        i = i.split()
       
        print("{}/{}/{}".format(mp[i[0][0:3]],i[1],i[2][-2:]))