import random
import rulocal
from tkinter import *
import tkinter.font as fnt

def game():
    day_count = 1
    food = 10
    health = 10
    mind = 10
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
        print(rulocal.day_stat,day_count)
        print(rulocal.user_stat)
        print(rulocal.food, food)
        print(rulocal.health, health)
        print(rulocal.mind, mind)
        print()
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
        if food <= 0:
            print(rulocal.losefood)
        if health <= 0:
            print(rulocal.losehealth)
        if mind <= 0:
            print(rulocal.losemind)
            break
        if day_count == 15 :
            print(rulocal.congrats)
            break




root = Tk()
C = Canvas(root, bg="blue", height=600, width=600)
root.title('Bunker')
bg_img = PhotoImage(file='C://Users/Ангелина/PycharmProjects/game/image/BUNKER.png')

bg_label = Label(root, image = bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def rules_call() :
    b.destroy()
    l.destroy()

    def start_game():
        b_startgame.destroy()
        rules.destroy()
        cont = Label(root, text=rulocal.cont, font=fnt.Font(size=10), fg="red", bg="pink")
        cont.place(relx=0.5, rely=0.675, anchor="center")
        game()


    rules = Label(root,text = rulocal.start,font = fnt.Font(size = 10), fg = "red" , bg="pink" )
    b_startgame = Button(text = rulocal.btn_start_text,command = start_game, font = fnt.Font(size = 15), height= 1 , width= 12)

    b_startgame.place(relx = 0.5 , rely = 0.675 , anchor="center")
    rules.place(relx=0.5, rely=0.55, anchor="center")





l = Label(root, text = "BUNKER",font = fnt.Font(size = 35), fg = "red" , bg="pink")
b = Button(root, text="Start",command = rules_call, font = fnt.Font(size = 15), height= 1 , width= 12)

#b.grid(root, column= 200 ,row =200 )
C.pack()
b.place(relx = 0.5 , rely = 0.65 , anchor="center")
#b.pack()
l.place(relx = 0.5 , rely = 0.55 , anchor="center")

root.mainloop()





