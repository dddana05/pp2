import re
text=input()
match=re.search((r"^[A-Z]+[a-z]+$"),text)
if match:
    print('yes')
else:
    print('no')