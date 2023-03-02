import re
text=input()
match=re.search((r"^[a-z]+_[a-z]+$"),text)
if match:
    print('yes')
else:
    print('no')