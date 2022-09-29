import re
pattern = r"\+7|8\s?\-?7(05|07|71|47|75|78)\s?[0-9]{3}\s?\-?[0-9]{2}\s?\-?[0-9]{2}"
nums = ["87054185571","8-771 449 88-29","+7 705 418-55-71"]
for i in nums:
    x = re.findall(pattern,i)
    if x:
        print(i)
