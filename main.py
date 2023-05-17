import random

import rulocal

day_count = 1
food = 10
health = 10
mind = 10

print(rulocal.start)

while True:
    with open("name.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        L = random.sample(range(0, len(lines)), k=1)
        randomnum = int(''.join(str(i) for i in L))
        event = lines[randomnum].split("/")[0]
        choise1 = lines[randomnum].split("/")[1]
        choise2 = lines[randomnum].split("/")[2]
        food_change1 = lines[randomnum].split("/")[3]
        health_change1 = lines[randomnum].split("/")[4]
        mind_change1 = lines[randomnum].split("/")[5]
        food_change2 = lines[randomnum].split("/")[6]
        health_change2 = lines[randomnum].split("/")[7]
        mind_change2 = lines[randomnum].split("/")[8]
        consequence1 = lines[randomnum].split("/")[9]
        consequence2 = lines[randomnum].split("/")[10]
    print(rulocal.day_stat,day_count)

    print(rulocal.user_stat)
    print(rulocal.food,food)
    print(rulocal.health,health)
    print(rulocal.mind,mind)
    print()
    print(event)
    print(rulocal.make_desision)
    print("1 ", choise1)
    print("2 ", choise2)
    user_choise = int(input())

    if user_choise == 1:
        print()
        print(consequence1)
    if user_choise == 2:
        print()
        print(consequence2)
    if user_choise == 1:
        food = food + int(food_change1)
        health = health + int(health_change1)
        mind = mind + int(mind_change1)
    if user_choise == 2:
        food = food + int(food_change2)
        health = health + int(health_change2)
        mind = mind + int(mind_change2)


    day_count += 1
    if food <= 0:
        print(rulocal.losefood)
    if health <= 0:
        print(rulocal.losehealth)
    if mind <= 0:
        print(rulocal.losemind)
        break
    if day_count == 16 :
        print(rulocal.congrats)
        break
