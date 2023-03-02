import re
text=input()
match=re.search((r"ab{2|3}"),text)
if match:
    print('yes')
else:
    print('no')