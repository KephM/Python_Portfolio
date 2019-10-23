import  random

deff = 0
atk = 1
health = 100
mana = 50
inv = []
equp = []
max_inv = 10
        
chest_inv = ("gold", "gems", "sword", "armor", "shield", "healing potion",
             "mana potion", "arrows", "bow", "spear", "cross bow", "helm", "pants",
             "boots", "Doom Hammer", "orb of future telling", "gloves", "bracers")

max_chest = 5
items = random.randint(1,max_chest)
chest = []
for i in range(items):
             chest.append(random.choice(chest_inv))

if inv:
    print(inv)
else:
    print("you have nothing in your inventory")
    input("open the chest to get your items")
    for items in chest:
        inv.append(items)
        

print(chest)

for items in inv:
    if items == "healing potion":
        health += 50
        inv.remove("healing potion")
for i in inv:
    if i == "armor":
        print("you put on the armor")
        deff += 10
        equp.append("armor")
        inv.remove("armor")
        
print(health)
print(deff)
print(equp)
chest_inv = ("gold", "gems", "sword", "armor", "shield", "healing potion",
             "mana potion", "arrows", "bow", "spear", "cross bow", "helm", "pants",
             "boots", "Doom Hammer", "orb of future telling", "gloves", "bracers")

max_chest = 15
items = random.randint(1,max_chest)
chest = []
for i in range(items):
    chest.append(random.choice(chest_inv))

input ("press enter to open chest")
for i in chest:
    inv.append(i)

if len(inv) > max_inv:
    x = len(inv)- max_inv
    print(inv)
    print("you need to remove " +str(x)+" items")
    while x > 0:
        item = input("what item do you want to remove")
        inv.remove(item)
        x -=1
    print(inv)
