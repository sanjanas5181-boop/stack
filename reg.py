import re
text="hello,my name is sriram and my email is sriram@example.com"
pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match=re.search(pattern,text)
if match:
    print("email found:",match.group())
else:
    print("email not found")


text1="there are 26 students in class 10A and 25 in 10B"
pattern="[0-9]+"
matches=re.findall(pattern,text1)
print("numbers found:",matches)
data_string="2026-05-16"
data_pattern=r"\d{4}-\d{2}-\d{2}"
if re.match(data_pattern,data_string):
   print("valid date")
else:
    print("invalid data")   
