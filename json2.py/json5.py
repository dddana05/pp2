import json

file= open('data.json', 'r')
data = json.load(file)

print("Interface Status\n\
================================================================================")
print("DN                                                 Description           Speed    MTU\n\
-------------------------------------------------- --------------------  ------  ------")

for i in data["imdata"]:
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed = i["l1PhysIf"]["attributes"]["speed"], MTU = i["l1PhysIf"]["attributes"]["mtu"]))
    