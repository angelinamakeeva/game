import random


def RandomEvent():
    with open("name.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        random_line = random.choice(lines)
    return random_line


random_line = RandomEvent()

hungry = 10
health = 10
mind = 10
day = 1


def Result(hungry, health, mind):
    output1 = "Итог: "
    output2 = ""
    if int(hungry) != 0:
        output2 += hungry + " голод "
    if int(health) != 0:
        output2 += health + " здоровье "
    if int(mind) != 0:
        output2 += mind + " рассудок "
    if output2 == "":
        output2 = "Ничего изменилось"
    return output1 + output2


while day <= 15:
    print("День", day)

    print("Голод", hungry)
    print("Здоровье", health)
    print("Рассудок", mind, "\n")

    if (day == 15):
        print("\nВы смогли выжить в бункере! Поздравляем!")
        break

    situation, act1, consequence1, change_hungry1, change_health1, change_mind1, act2, consequence2, change_hungry2, change_health2, change_mind2 = random_line.split(
        '*')

    print(situation)
    print("1. " + act1)
    print("2. " + act2)