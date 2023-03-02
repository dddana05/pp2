import re
text=input()
words=re.findall("[A-Z][a-z]*", text)
print(' '.join((words)))