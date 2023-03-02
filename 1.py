import re

text =input()
matching = re.search((r'^a(b*)$'), text)
if matching:
    print('yes')  # groups()
else:
    print('No')