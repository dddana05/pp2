import re
text=input()
match=re.search((r"^a.*?b$"),text)
if match:
    print('yes')
else:
    print('no')