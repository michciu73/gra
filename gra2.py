from random import randint
from time import sleep

# start zrób!!!!!!

print("START")
print("\n.\n.\n")
start = input()
print("Let's go")

#origin story 

enterr = input()
sum = 0

while sum >= 0 and sum <= 5:
    if sum == 0:
        enterr
        print("\n\nLong long time ago... \nWhen the Rose-merry Kingdom was ruled by cats and their allys, \na beautiful dynast, member of the royal family was born... \n\n")
        sum = sum+1

    enterr.replace(" ", ".")
    enterr = input()

    if sum == 1:
        enterr
        print("All the cats were stunned by the little kitty's beauty and wanted to see the baby.\nOffering them goods and gifting presents to welcome the representation\nof next generation of rulers.\n\n")
        sum = sum+1

    enterr.replace(" ", ".")
    enterr = input()

    if sum == 2:
        enterr
        print(" Years passed...\n\n")
        sum = sum+1
    
    enterr.replace(" ", ".")
    enterr = input()
    
    if sum == 3:
        enterr
        print("The kitty was growing strong,\ndiscovering their strengths and talents and eliminating their weaknesses.\nEveryone was happy that this cat, who was now training to become their sovereign \nwas healthy and becoming better week by week. ")
        sum = sum+1

    enterr.replace(" ", ".")
    enterr = input()

    if sum == 4:
        enterr
        print("The day of dynast's 15 birthday has come. That day was very special. \nToday, all the work and efforts they put in their destyny to become a great \nfuture representative should be reawrded, \nbecause that day one of the four Great Elements will be choosen \nand escort him throught the life.\n\n ")
        sum = sum+1

    enterr.replace(" ", ".")
    enterr = input()

    if sum == 5:
        enterr
        print("Ceremony started... ")
        sum = sum+1



# generator postaci

a = "o......o"
b = "^.....^"
c = "ⅇ.......ⅇ"
d = "∆......∆"
e = "|/#ⅇ-ⅇ#\|"
f = "|/#o-o#\|"
g = "/#^ - ^#\ "
h = " /#°^°#\ "
i = " / u.u \ "
j = "/. pq .\ "
k = "o\o..o/o"
l = "/. 00. \__.>"

def earss():
    if int(ears) == 1:
        print(a)
    elif int(ears) == 2:
        print(b)
    elif int(ears) == 3:
        print(c)
    else:
        print(d)
   
def eyess():
    if eyes == 1:
        print(f"{e}")
    elif eyes == 2:
        print(f"{f}")
    elif eyes == 3:
        print(f"{g}")
    else:
        print(f"{h}")
        
def bodyy():
    if body == 1:
        print(f"{i}")
    elif body == 2:
        print(f"{j}")
    elif body == 3:
        print(f"{k}")
    else:
        print(f"{l}")

def character():
    earss()
    eyess()
    bodyy()

def namedcharacter():
    print("\n.\n.\n.\n\n")
    earss()
    eyess()
    bodyy()
    if len(name) <= 7:
        print(f" {name}")
    else:
        print(name)


while enterr == " " and sum == 6:
    print (".\n\n\n.\n\n\n.\n\n\n")
    sum = sum+1

enterr.replace(" ", ".")
enterr = input()
sum = sum+1

if enterr == " " and sum == 8:
    print("\n\nchoose your character:\n")
    print(f"choose ears: \no......o           ^........^          ⅇ.......ⅇ      ∆......∆")
    ears = float(input("1-4\n"))

    print(f"choose your eyes: \n|/#ⅇ-ⅇ#\|          |#o-o#|        #^ - ^#     /#°^°#\ ")
    eyes = int(input("1-4\n"))


    print(f"choose your body: \n/ u.u \            /. pq .\        o\o .. o/o     /. 00. \__.>")
    body = int(input("1-4\n"))

    print("your character: \n")
    character()

    print("\nname your character:")
    name = input("name:")
    
    namedcharacter()


#atak - definicja :))

from random import randint

enemyhp = 100
strength = 13
life = 100                                           # pamietaj dodaj jeszcze strenght do definicji fight !!!!!!!!!
enemystrength = 10

def fight():

    global enemyhp
    global strength
    global life
    global enemystrength

    print("choose the element to fight")

    element = input(" a - fire, b - water, c - air, d - earth")

    def cat_lick():
        global life
        print("do you want a cat to lick away your wounds?")
        lick = int(input("1 - yes!      2 - no...      3 - i wanna end this game :')"))
        if lick == 1:
            life = 100
        elif lick == 2 or lick == 3:
            print("\n\n -------------------------- END :(( -------------------------")


    def enemy_attack():
        global life 
        global enemystrength 
        if enemystrength >= 10 and enemystrength < 20 and life > 0:
            x = randint(3, 5)
            life = life - x
        elif enemystrength >= 20 and enemystrength < 30 and life > 0:
            x = randint(5, 10)
            life = life - x
        elif enemystrength <= 30 and life > 0:
            x = randint(7, 13)
            life = life - x 
        elif life <= 0:
            print("you're dead")



    if element == "a":
        print("you chose fire")
        def attack_one():
            global enemyhp
            x = randint(1, 10)
            if enemyhp > 0:
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_two():
                global enemyhp
                x = randint(4, 14)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_three():
                global enemyhp
                x = randint(2, 8)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_four():
                global enemyhp
                x = randint(7, 16)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        atak = input()

        while enemyhp/1:
            if enemyhp > 0 and atak == "a" and life > 0:
                attack_one()
                enemy_attack()
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and life > 0:
                attack_two()
                enemy_attack()
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and life > 0:
                attack_three()
                enemy_attack()
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and life > 0:
                attack_four()
                enemy_attack()
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0:
                print("your dead")
                cat_lick()
                continue

            if enemyhp > 0 and atak == "a" and strength >= 20 and life > 0:
                attack_one()
                enemy_attack()
                enemyhp = enemyhp - 4
                life = life + 4
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and strength >= 20 and life > 0:
                attack_two()
                enemy_attack()
                enemyhp = enemyhp - 5
                life = life + 4
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and strength >= 20 and life > 0:
                attack_three()
                enemy_attack()
                enemyhp = enemyhp - 3
                life = life + 4
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and strength >= 20 and life > 0:
                attack_four()
                enemy_attack()
                enemyhp = enemyhp - 6
                life = life + 4
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0 and strength >= 20:
                print("your dead")
                cat_lick()
                continue


    if element == "b":
        print("you chose water")
        def attack_oneb():
            global enemyhp
            x = randint(1, 10)
            enemyhp = enemyhp - x
            if enemyhp > 0:
                print(enemyhp)
            
        def attack_twob():
                global enemyhp
                x = randint(4, 14)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_threeb():
                global enemyhp
                x = randint(2, 8)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_fourb():
                global enemyhp
                x = randint(7, 16)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        atak = input()

        while enemyhp/1:
            if enemyhp > 0 and atak == "a" and life > 0:
                attack_oneb()
                enemy_attack()
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and life > 0:
                attack_twob()
                enemy_attack()
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and life > 0:
                attack_threeb()
                enemy_attack()
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and life > 0:
                attack_fourb()
                enemy_attack()
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0:
                print("your dead :(")
                cat_lick()
                continue

            if enemyhp > 0 and atak == "a" and strength >= 20 and life > 0:
                attack_oneb()
                enemy_attack()
                enemyhp = enemyhp - 4
                life = life + 4
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and strength >= 20 and life > 0:
                attack_twob()
                enemy_attack()
                enemyhp = enemyhp - 5
                life - life + 4
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and strength >= 20 and life > 0:
                attack_threeb()
                enemy_attack()
                enemyhp = enemyhp - 3
                life = life + 4
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and strength >= 20 and life > 0:
                attack_fourb()
                enemy_attack()
                enemyhp = enemyhp - 6
                life = life + 4
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0 and strength >= 20:
                print("your dead")
                cat_lick()
                continue


    if element == "c":
        print("you chose air")
        def attack_onec():
            global enemyhp
            x = randint(1, 10)
            enemyhp = enemyhp - x
            if enemyhp > 0:
                print(enemyhp)
            
        def attack_twoc():
                global enemyhp
                x = randint(4, 14)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_threec():
                global enemyhp
                x = randint(2, 8)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_fourc():
                global enemyhp
                x = randint(7, 16)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        atak = input()

        while enemyhp/1:
            if enemyhp > 0 and atak == "a" and life > 0:
                attack_onec()
                enemy_attack()
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and life > 0:
                attack_twoc()
                enemy_attack()
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and life > 0:
                attack_threec()
                enemy_attack()
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and life > 0:
                attack_fourc()
                enemy_attack()
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0:
                print("your dead")
                cat_lick()
                continue

            if enemyhp > 0 and atak == "a" and strength >= 20 and life > 0:
                attack_onec()
                enemy_attack()
                enemyhp = enemyhp - 4
                life = life + 4
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and strength >= 20 and life > 0:
                attack_twoc()
                enemy_attack()
                enemyhp = enemyhp - 5
                life = life + 4
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and strength >= 20 and life > 0:
                attack_threec()
                enemy_attack()
                enemyhp = enemyhp - 3
                life = life + 4
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and strength >= 20 and life > 0:
                attack_fourc()
                enemy_attack()
                enemyhp = enemyhp - 6
                life = life + 4
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0 and strength >= 20:
                print("your dead :(")
                cat_lick()
                continue

    if element == "d":
        print("you chose earth")
        def attack_oned():
            global enemyhp
            x = randint(1, 10)
            enemyhp = enemyhp - x
            if enemyhp > 0:
                print(enemyhp)
            
        def attack_twod():
                global enemyhp
                x = randint(4, 14)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_threed():
                global enemyhp
                x = randint(2, 8)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        def attack_fourd():
                global enemyhp
                x = randint(7, 16)
                enemyhp = enemyhp - x
                if enemyhp > 0:
                    print(enemyhp)

        atak = input()

        while enemyhp/1:
            if enemyhp > 0 and atak == "a" and life > 0:
                attack_oned()
                enemy_attack()
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and life > 0:
                attack_twod()
                enemy_attack()
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and life > 0:
                attack_threed()
                enemy_attack()
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and life > 0:
                attack_fourd()
                enemy_attack()
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and life > 0:
                print("your enemy is dead")
                break
            if life <= 0:
                print("your dead")
                cat_lick()
                continue

            if enemyhp > 0 and atak == "a" and strength >= 20 and life > 0:
                attack_oned()
                enemy_attack()
                enemyhp = enemyhp - 4
                life = life + 4
                atak.replace("a", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "a" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "b" and strength >= 20 and life  > 0:
                attack_twod()
                enemy_attack()
                enemyhp = enemyhp - 5
                life = life + 4
                atak.replace("b", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "b" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "c" and strength >= 20 and life > 0:
                attack_threed()
                enemy_attack()
                enemyhp = enemyhp - 3
                life = life + 4
                atak.replace("c", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "c" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif enemyhp > 0 and atak == "d" and strength >= 20 and life > 0:
                attack_fourd()
                enemy_attack()
                enemyhp = enemyhp - 6
                life = life + 4
                atak.replace("d", ".")
                atak = input()
            elif enemyhp <= 0 and atak == "d" and strength >= 20 and life > 0:
                print("your enemy is dead")
                break
            elif life <= 0 and strength >= 20:
                print("your dead :(")
                cat_lick()
                continue



#1 ucieczka (tutorial)

from time import sleep

print("=--="*40)
print("All the cats were startled. Never in the houndreds of years there was such accident.\n\n")
sleep(1)
print("The new ruler must have run away...\n\n")
sleep(1)
print("=--="*40)
sleep(1)
print("Hint: click a number and press enter on your keyboard to choose an option\n\n")
question_1 = int(input("Come through the defence towers?\n 1 - yes\n"))

if question_1 == 1:
    print (f"\n\n{name} escaped... They wondered and wondered for so long, they started to get hungry.\n Suddenly, from the deep of the forest an evil troll jumpscared {name}.\n As scary as it was, this was still a great opportunity\n to gain something to eat.\n\n")

question_2 = int(input("Do you want to kill this evil troll?\n 1 - yes\n"))

if question_2 == 1:
    print("hint: to fight choose element you want to use\n and select it by typing one of options on your keyboard\n then keep choosing the attacks you want to use\ until your enemy is dead")
    enemyhp = 20
    enemystrength = 3
    fight()


print("congrats! You succesfully finished your tutorial! Good luck with your next tasks Adventurer!")

#lvl 1 

sleep(4)

print("\n\n\n ----------------------------------= LEVEL 1 == THE WITHERED TOWN =------------------------------------\n\n\n")

sleep(3)
print(f"Five years later...\n\n ")
sleep(2)

sth = 1

print("=--="*40)
sleep(1)
print(f"{name.upper()}: OH, what a priductive day!\n")
sleep(1)
print(f"{name.upper()}: I finally found theese mushrooms I was looking for!\n")
sleep(1)
print(f"{name.upper()}: It took me sooooooo loooong thogh...\n I should probably go back home.\n")
sleep(1)
print(f"{name.upper()} < chcecks map >\n")
sleep(1)
print(f"{name.upper()}: I don't recognize this path... I think I should turn... Left?\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_3 = int(input("Turn left?\n\n 1 - yes\n2 - i think no...\n"))
    if question_3 == 1:
        print(f"{name.upper()}: I suppose I go left...\n\n")
        break
    elif question_3 == 2:
        print("ERROR-"*27)
        continue

print("=--="*40)
sleep(1)
print(f"{name} followed the map and after a while found some signs of civilization\n\n")
sleep(1)
print("but, what shocked them a little, it wasn't their cozy house-\n\n")
sleep(2)
print(f"{name.upper()}: What is this town? I've never been there and I live here since...\n Seems like forever...")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1: 
    question_4 = int(input("Enter town? 1 = yes\n 2 = yes\n"))
    if question_4 == 1 or question_4 == 3:
        sleep(1)
        print(f"{name.upper()}: I feel like I want to investigate something. I'll... go in!\n\n")
        sleep(1)
        print(f"{name.upper()}: Oh.. It looks sad- Oh there's someone there\n\n")
        break


while sth/1:
    sleep(1)
    question_5 = int(input("Let's talk!\n1 - ofc B)\n 2 - I don't feel like talking though\n"))
    if question_5 == 1:
        sleep(1)
        print(f"{name.upper()}: He seems nice, maybe he knows what's going on\n\n")
        break
    elif question_5 == 2:
        print("OF COURSE YOU DOOO... RiGhT?")
        continue

sleep(2)
print("=--="*40)
sleep(1)
print("GUARD: Good evning fellow citizen! I've never seen you here, are you from Lilianshire?\n\n")
sleep(1)
print(f"{name.upper()}: No I'm not mr... Sir, what's your name? I can't read what's written on your tag\n\n")
sleep(1)
print("GUARD: Mr Junta! Junior police oficer of Lilianshire, how can I help you then? Are you lost?\n\n")
sleep(1)
print(f"{name.upper()}: I am, but that's not what I wanted to ask actually. This town seems a little off...\n\n")
sleep(1)
print("JUNTA: I'm sorry..?\n\n")
sleep(1)
print(f"{name.upper()}: Not that- I- I didn't mean to offend you in any way but- It's just- Unusuall, if that makes sense\n\n")
sleep(1)
print(f"{name.upper()}: I'm {name} by the way, nice to meet you\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_6 = int(input("Ask ...\n\n 1 - for his mom's phone number\n2 - what happend to the town\n"))
    if question_6 == 1:
        sleep(1)
        print(f"{name.upper()}: Sir, may I ask what's your mom's phone number? I'd love to...\n\n")
        sleep(1)
        print("JUNTA: I'M SORRY? What impudence! Tell me you're joking...\n\n")
        sleep(1)
        print(f"{name.upper()}: Yeah... Joking haha...\n\n")
        sleep(1)
        print("JUNTA: OH HAHA... You're funny my friend!\n\n")
        continue
    elif question_6 == 2:
        sleep(1)
        print(f"{name.upper()}: But.. What happend here? Based on your reaction you seem hurt... What's going on?\n\n")
        break

sleep(2)    
print("=--="*40)
sleep(1)
print("JUNTA: I've been observing the streets for a while.\n\n")
sleep(1)
print("JUNTA: and from my observation and the police records, someone keeps serving\nsleeping pills to the citizens\n\n")
sleep(1)
print("JUNTA: exept... They don't wake up. The're like in a trance... It never happened before\n\n")
sleep(1)
print(f"{name.upper()}: Oh...\n\n")
sleep(1)
print("JUNTA: Do you maybe... Want to help me find out what's going on?\n\n")
sleep(1)
print("JUNTA: I'm not really valued as a junior police officer, maybe that will be my\n ticket to apprication...\n\n")
sleep(1)
print("JUNTA: Sorry, I like daydreaming about this... So... Are you in?\n\n")

while sth/1:
    question_7 = int(input("Are you..?\n\n 1 - Of course, let's see what's up\n 2 - Nahhhh... Nah?\n"))
    if question_7 == 1:
        sleep(1)
        print("JUNTA: THANK YOU! Come on, I know where we should go!\n\n")
        break
    elif question_7 == 2:
        print("NAH."*30)
        sleep(0.5)
        print("\n\nNA- NA-\n\n")
        sleep(0.5)
        print("YES\n\n")
        sleep(0.5)
        print("YES."*30)
        break

sleep(3)
#lvl 2

print("\n\n\n ----------------------------------= LEVEL 2 = HIDDEN EVIL  =------------------------------------\n\n\n")


sleep(2)
print("While listening to interesting stories and legends about Lilianshire\n our new detectives arrived to The Falling Leaf pub\n\n\n")
sleep(2)
print("JUNTA: This is the best know pub in the town, if the cryminall strikes, he will do this here\n\n\n")
sleep(2)

print("They entered the pub and was hit with a worm air nad the noise of conversation muffled by the coffee machine.\n")
sleep(1)
print("Noone realy payed attention to the new visitors, exept for the bartener,\n a red cat with black patch on one eye\n\n\n")
sleep(2)
print("BARTENER: How can I help you gentelmen? Do you wish for any drinks?\n\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_8 = int(input("Do you want drinks?  (trust me, you do ;>)\n\n 1 - not really, I don't drink\n 2 - Honestly I'm in for a drink\n"))
    if question_8 == 1:
        break
    elif question_8 == 2:
        sleep(1)
        print("=--="*40)
        sleep(1)
        print("TASK: Guess the word from the mess\n\n")
        sleep(1)
        print("Hint: Write the correct word with capital letters\n\n")
        sleep(1)
        print("=--="*40)
        sleep(2)

        print("W O B R A Y R\n")
        answer_1 = input("")
        print("\n\n")
        if answer_1 == "BROWARY":
            sleep(1)
            print("correct!\n\n")
            sleep(1)
            print("BARTENER: Here's your drinks gents, enjoy\n\n")
            sleep(1)
            print(f"{name.upper()}: Thank you sir\n\n")
            break
        else:
            print("incorrect answer\n\n")
            continue

sleep(2)
print("=--="*40)
sleep(1)
print("Red cat, who was known to never leave his pub\n and - as rumours said - knows everything\n, was looking at them suspiciously\n\n\n")
sleep(1)
print("JUNTA: So my old friend, do you know what brings us here?\n\n")
sleep(1)
print("BARTENER: I suppose it's the sleeping pills? Am I right? Oh, of course I'm right\n\n")
sleep(1)
print("JUNTA: Yes you are, soo... Do you know something?\n\n")
sleep(1)
print(f"{name.upper()}: Yeah, do YOU know something?\n\n\n")
sleep(1)
print("=--="*40)
sleep(2)

print(f"{name} was sceptical about this cat's knowlage\n\n\n")
sleep(2)
print("They still decided to trust Junta, he knows better about the residents here\n\n")
sleep(1)
print("The bartener cast suspicion on the old sage, cat who was acused for keeping illigal plants.\n\n")
print(1)
print(f"Junta and {name} decided to go and find him.\n they wanted to ask some questions\n\n\n")
sleep(4)

#lvl 3

print("\n\n\n ----------------------------------= LEVEL 3 = HIDDEN EVIL  =------------------------------------\n\n\n")


sleep(2)
print("JUNTA: Do you know most common drink in...\n\n")
sleep(1)
print(f"{name.upper()}: WHAT was THAT-?\n\n")
sleep(2)

print("Cats looked arond in terror, as they were surrounded by five pickpockets...\n\n")
sleep(1)
print("The only way to escape from this sytuation...\n\n")
sleep(1)
print("=--="*40)

while sth/1:
    sleep(2)
    question_9 = int(input("FIGHT????????\n\n 1 - HELL YEAHHHH\n 2 - I GUESS SO?!?!?!?! \n"))
    if question_9 == 1 or question_9 == 2:
        print(f"\n\n PICKPOCKET 1 VS {name.upper()}\n\n")
        enemyhp = 30
        print(f"\n\nenemy hp = {enemyhp}\n")                                     
        enemystrength = 10
        print(f"enemy strength = {enemystrength}\n\n\n")
        sleep(1)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1)
        print("FIGHT\n\n\n")
        sleep(1)
        fight()
        break
        
while sth/1:
    enemyhp = 40                                      
    enemystrength = 14
    print(f"\n\n PICKPOCKET 1 VS {name.upper()}\n\n")
    print(f"\n\nenemy hp = {enemyhp}\n") 
    sleep(1)                                    
    print(f"enemy strength = {enemystrength}\n\n\n")
    sleep(1)
    print("3\n")
    sleep(1)
    print("2\n")
    sleep(1)
    print("1\n")
    sleep(1)
    print("FIGHT\n\n\n")
    sleep(1)
    fight()
    break

while sth/1:
    enemyhp = 25
    enemystrength = 17
    print(f"\n\n PICKPOCKET 1 VS {name.upper()}\n\n")
    print(f"\n\nenemy hp = {enemyhp}\n") 
    sleep(1)                                    
    print(f"enemy strength = {enemystrength}\n\n\n")
    sleep(1)
    print("3\n")
    sleep(1)
    print("2\n")
    sleep(1)
    print("1\n")
    sleep(1)
    print("FIGHT\n\n\n")
    sleep(1)
    fight()
    break

sleep(2)
print("=--="*40)
sleep(1)
print(f"{name.upper()}: WAIT! Why are we even fighting?! WE literally have NOTHING\n\n\n")
sleep(2)
print(f" After {name} screamed everyone stopped mid fight and looked at them\n\n")
sleep(2)
print(f"{name.upper()}: Why are you doing this guys, you literally attacked a cop!\n\n")
sleep(1)
print("PICKPOCKET 1: Why would we even tell you?!\n\n")
sleep(1)
print("PICKPOCKET 3: Yeah, why would we!\n\n")
sleep(1)
print("JUNTA: Maybeee because you just- attacked a cop?\n\n\n")
sleep(2)
print("Junta proudly aunnounced his status, and the rest of the cats took a step back\n\n\n")
sleep(2)
print("PICPOCKET 1: Our boss fell asleep one week ago, and we don't know what to do\n\n")
sleep(1)
print("PICKPOCKET 3: We don't know!\n\n")
sleep(1)
print(f"{name.upper()}: And this is the reason you say? Aren't there better ways to ern money? \n\n")
sleep(1)
print("JUNTA: Yeah, for example street shows are legal in Lilianshire, maybe try that?\n\n")
sleep(1)
print("PICKPOCKET 3: We should! We should!\n\n")
sleep(2)
print("A Picpocket smiled at a little one next to him and gave few pats on the head\n\n")
sleep(2)
print("PICPOCKET 1: If you say so little one, we'll try, thanks\n\n")
sleep(2)
print("Our detectives continued, arriving soon to the Sage's Hut")

sleep(4)


#lvl 4

print("\n\n\n ----------------------------------= LEVEL 4 = COLORED TEA  =------------------------------------\n\n\n")

sleep(3)

print("DOOR: <KnOCk kNOck>\n\n\n")
sleep(2)
print("SAGE: Hello wonderers, what brings you to my humble hut?\n\n")
sleep(1)
print("JUNTA: DON'T ACT SO NICE! YOU KNOW WHY WE'RE HERE!\n\n")
sleep(1)
print(f"{name.upper()}: Don't be rude Junta! So sorry for my friend sir, can we come in?\n\n")
sleep(1)
print(f"{name.upper()}: We have a few questions about the situation that's going on\n\n")
sleep(1)
print("SAGE: Of course gentelmen, let me have you, do you want some tea?\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_10 = int(input("Do you want tea?\n\n 1 - I'd love to, yes!\n  2 - I don't think I want tea from strengers...\n"))
    if question_10 == 1:
        sleep(1)
        print("\nSAGE: There you go gents, my own recepy\n\n")
        break
    elif question_10 == 2:
        break

sleep(2)
print("=--="*40)
sleep(1)
print("JUNTA: W'ere not here for this type od tea, what were you doing in the pub? Hmmm?\n\n")
sleep(1)
print("SAGE: What pub? The FAlling Leaf pub? I haven't been there for a month!\n\n")
sleep(1)
print("SAGE: I was working on mosaic for past weeks, I just finished it two hours ago\n\n")
sleep(1)
print("JUNTA: WHY is it that I DON'T believe you, hmmmmm? My COP intuituion...-\n\n")
sleep(1)
print(f"{name.upper()}: Junta calm down! I'm so sorry sir, can we se your work? It must be amazing\n\n")
sleep(1)
print("SAGE: Of course, It's upstairs\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_11 = int(input("Go and see artwork?\n\n 1 - Yes, there's not even another option\n"))
    if question_11 == 1:
        sleep(1)
        print("\nSAGE: Come with me\n\n\n")
        break

sleep(2)
print("=--="*40)
sleep(1) 
print("The two cats followed Sage upstairsn\n\n\n")
sleep(2)
print(f"{name.upper()}: OH MY CAT SIR, this mosaic is wonderfull\n\n")
sleep(1)
print(f"{name.upper()}: Junta he's telling the truth, it must have taken at least four weeks of solid work\n\n")
sleep(1)
print("JUNTA: Yeah, if you say so.. But that means... THE BARENER-\n\n")
sleep(1)
print(f"{name.upper()}: What do you- OH MY CATNESS THE BARENER! WE MUST GO!\n\n")
sleep(1)
print(f"{name.upper()}: THANK YOU SIR, WE'RE SO THANKFULL, HAVE A NICE DAY!\n\n\n")
sleep(2)
print(f"Junta and {name} went back to the pub. They were so close to finish that case\n\n")
sleep(4)

#lvl 5 

print("\n\n\n ----------------------------------= LEVEL 5 = =LEVER TO THE TRUTH  =------------------------------------\n\n\n")


sleep(2)
print("The cats runned back to the pub\n\n")
sleep(1)
print(f"{name.upper()}: STOP THE BARTENDER!\n\n")
sleep(1)
print("The cryminal jumped out of the bar and run towards the main square\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_12 = int(input("\nRun after him... or?\n\n 1 - stop and dance on a pipe\n  2 - run after him\n"))
    if question_12 == 1:
        dancepoints = 10
        while dancepoints > 0:
            print("DANCE!")
            sleep(1)
            dancepoints = dancepoints - 1
            if dancepoints == 5:
                print("SPECIAL DANCE!")
                dancepoints = dancepoints - 1
            if dancepoints == 0:
                print("you earned 5 pawlars")
                sleep(1)
        continue
    elif question_12 == 2:
        runpoints = 10
        while runpoints > 0:
            print("RUN")
            sleep(1)
            runpoints = runpoints - 1
            if runpoints == 0:
                print("YOU GOT HIM!!!")
        break
    break

sleep(2)
print("=--="*40)
sleep(1)
print(f"{name.upper()}: I GOT HIM I GOT HIM I- WHAT\n\n")
sleep(1)
print("JUNTA: WHAT THE ****?!\n\n\n")
sleep(2)
print("From the crowd emarged a whole lot of angry cats ready to fight\n\n\n")
sleep(2)
print("JUNTA: I'LL DEAL WITH THEM! Go and catch the bartender\n\n\n")
sleep(1)
print("TASK: Kill 3 enemies and fight the bartender\n\n")
sleep(1)
print("=--="*40)
sleep(2)

while sth/1:
    question_13 = int(input("Fight first enemy? 1 - yes 2 - i don't have a choise if i won't I'll be dead :>"))
    if question_13 == 1 or question_13 == 2:
        enemyhp = 50                                      
        enemystrength = 20
        print(f"\n\n ENEMY 1 VS {name.upper()}\n\n")
        print(f"\n\nenemy hp = {enemyhp}\n") 
        sleep(1)                                    
        print(f"enemy strength = {enemystrength}\n\n\n")
        sleep(1)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1)
        print("FIGHT\n\n\n")
        sleep(1)
        fight()
        break

sleep(2)
print("=--="*40)
sleep(2)

while sth/1:
    question_14 = int(input("Fight second enemy? 1 - actually i start to enjoy it... 2 - yes"))
    if question_14 == 1 or question_14 == 2:
        enemyhp = 40                                      
        enemystrength = 16
        print(f"\n\n ENEMY 2 VS {name.upper()}\n\n")
        print(f"\n\nenemy hp = {enemyhp}\n") 
        sleep(1)                                    
        print(f"enemy strength = {enemystrength}\n\n\n")
        sleep(1)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1)
        print("FIGHT\n\n\n")
        sleep(1)
        fight()
        break

sleep(2)
print("=--="*40)
sleep(2)

while sth/1:
    question_15 = int(input("Fight third enemy? 1 - YEAHH 2 - yes"))
    if question_15 == 1 or question_15 == 2:
        enemyhp = 55                                     
        enemystrength = 25
        print(f"\n\n ENEMY 3 VS {name.upper()}\n\n")
        print(f"\n\nenemy hp = {enemyhp}\n") 
        sleep(1)                                    
        print(f"enemy strength = {enemystrength}\n\n\n")
        sleep(1)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1)
        print("FIGHT\n\n\n")
        sleep(1)
        fight()
        break

sleep(2)
print("=--="*40)
sleep(2)

print(f"\nJUNTA: {name} are you alright?\n\n")
sleep(1)
print(f"c: Yeah, I have one enemy left...\n\n\n")

sleep(2)
print("=--="*40)
sleep(2)

while sth/1:
    question_16 = int(input("FIGHT BOSS? 1 - NEVER BEEN MORE READY 2 - YES LET'S GO"))
    if question_16 == 1 or question_16 == 2:
        enemyhp = 80                                  
        enemystrength = 30
        print(f"\n\n BOSS VS {name.upper()}\n\n")
        print(f"\n\nenemy hp = {enemyhp}\n") 
        sleep(1)                                    
        print(f"enemy strength = {enemystrength}\n\n\n")
        sleep(1)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1)
        print("FIGHT\n\n\n")
        sleep(1)
        fight()
        break

sleep(2)
print("=--="*40)
sleep(2)

sleep(2)
print(f"\n\n{name.upper()}: WE WON!\n\n")
sleep(1)
print("OFFICER: Junta... You're really brave and intelligent young men. Congratulations, you got a promotion\n\n")
sleep(1)
print("JUNTA: THANK YOU SIR-!\n\n")
sleep(1)
print("SAGE: OH so glad I came on time... Look, I have an antidote!\n\n")
sleep(1)

sleep(2)
print("=--="*40)
sleep(2)

print(f"\n\n\nAfter every cat in Llianshire was awake,\n the town started to look more vibrant.\n Flowers came back to life.\n Sage was more popular and opened a new teashop\n And {name} decided to go back to his kingdom...\n\n\n")

sleep(2)
print("=--="*40)
sleep(2)

print("\n\n\n TBC \n\n\n")
