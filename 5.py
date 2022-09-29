import re

data = ["DEXTER <dexter@hotmail.com>","VIRUS <virus!@variable.:p>"]

pattern = r"\<[A-Za-z0-9]+\@[a-z]*mail.com\>"

for i in data:

    mail = i.split()

    x = re.findall(pattern,mail[1])

    if x:

        print(mail[0]+" "+mail[1][1:-1])