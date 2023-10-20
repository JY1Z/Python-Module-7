#1
spr = (3,4,5)
sum = (6,7,8)
aut = (9,10,11)
win = (12,1,2)
season = ("spring","summer","autumn","winter")
num = int(input("month:"))
if num in spr:
    print(season[0])
if num in sum:
    print(season[1])
if num in aut:
    print(season[2])
if num in win:
    print(season[3])

#2
name = input("name:")
names = set()
while name != " ":
    a = len(names)
    names.add(name)
    b = len(names)
    if a != b:
        print("New")
        name = input("name:")
    if a == b:
        print("Existing")
        name = input("name:")
print(names)


#3
ICAO = {"EFHK":"Helsinki-Vantaa Airport","BJJC":"Beijing airport"}
a = input("enter?fetch?quit?")
while a != "quit":
  if a == "enter":
    icao = input("icao")
    name = input("name")
    ICAO[icao] = name
    a = input("enter?fetch?quit?")
  if a == "fetch":
    icao = str(input("ICAO"))
    if icao in ICAO:
        print(ICAO[icao])
    a = input("enter?fetch?quit?")
else:
    print("ends")