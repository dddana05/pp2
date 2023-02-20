import json

file= open('data.json', 'r')
data = json.load(file)

print("Interface Status\n\
================================================================================")
print("DN                                                 Description           Speed    MTU\n\
-------------------------------------------------- --------------------  ------  ------")

for i in data["imdata"]:
    print(i)

