import random

import rulocal

day_count = 1
food = 10
health = 10
mind = 10

while True:
    with open("name.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        randomnum = random.randint(0,len(lines)-1)
        event = lines[randomnum].split("/")[0]
        choise1 = lines[randomnum].split("/")[1]
        choise2 = lines[randomnum].split("/")[2]
        food_change1 = lines[randomnum].split("/")[3]
        health_change1 = lines[randomnum].split("/")[4]
        mind_change1 = lines[randomnum].split("/")[5]
        food_change2 = lines[randomnum].split("/")[6]
        health_change2 = lines[randomnum].split("/")[7]
        mind_change2 = lines[randomnum].split("/")[8]
    print(rulocal.day_stat,day_count)
    print(rulocal.user_stat)
    print(food)
    print(health)
    print(mind)
    print(event)
    print(rulocal.make_desision)
    print("1 ", choise1)
    print("2 ", choise2)
    user_choise = int(input())

    if user_choise == 1:
        food = food + int(food_change1)
        health = health + int(health_change1)
        mind = mind + int(mind_change1)
    if user_choise == 2:
        food = food + int(food_change2)
        health = health + int(health_change2)
        mind = mind + int(mind_change2)

    day_count += 1
    if food <= 0 or health <= 0 or mind <= 0:
        print(rulocal.lose)
        break
    if day_count == 15 :
        print(rulocal.congrats)
        break
