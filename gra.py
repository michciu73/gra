from random import randint, random;
import copy
#------------------------------------Bohater
Name = input("Podaj imię swojego bohatera   ")
#0--imię  1--max_hp  2--hp  3--pd  4--poziom  5--coiny
Max_hp = 100
Hp = copy.copy(Max_hp)
Bohater = [Name,Max_hp,Hp,0,1,0]
Bohater[2] <= Bohater[1]
#------------------------------------przedmioty
Miecz = 'Miecz'
Zbroja = 'Zbroja'
Mała_potka = 'Mała potka'
Średnia_potka = 'Średnia potka'
Duża_potka = 'Duża potka'

Przedmioty = []
#-------------------------------------Sklep
def Sklep():
    print('Witaj w sklepie. Co chciałbyś kupić?    ')
    print(f'Masz {Bohater[5]} coinów\n')
    print('1 - Miecz: odblokowuje mocny atak  =  105 coinów')
    print('2 - Zbroja: +20 Max hp  =  200 coinów')
    print('3 - Mała potka: leczy 10 Hp  =  10 coinów')
    print('4 - Średnia potka: leczy 30 Hp  =  40 coinów')
    print('5 - Duża potka leczy: 100 Hp  =  100 coinów')
    print('-'*50)
    print(f'twoje przedmioty {Przedmioty}')
    while True:
        print('-'*50)
        gear = input()
        if gear == "1":
            if Miecz in Przedmioty:
                    print("Możesz mieć tylko jeden miecz!")
            elif Bohater[5] >= 105:
                Przedmioty.append(Miecz)
                print("Kupiłeś miecz!")
                Bohater[5] -= 105
            else:
                print("Nie stać cie biedaku!")
        elif gear == '2':
            if Zbroja in Przedmioty:
                print("Możesz mieć tylko jedną zbroję!")
            elif Bohater[5] >= 200:
                Przedmioty.append(Zbroja)
                Bohater[1] += 20
                print("Kupiłeś zbroję!")
                Bohater[5] -= 200
            else:
                print("Nie stać cie biedaku")
        elif gear == '3':
            if Bohater[5] >= 10:
                Przedmioty.append(Mała_potka)
                print('Kupiłeś małą potkę')
                Bohater[5] -= 10
            else:
                print('Nie stać cie biedaku!')
        elif gear == '4':
            if Bohater[5] >= 40:
                Przedmioty.append(Średnia_potka)
                print('Kupiłeś średnią potkę')
                Bohater[5] -= 40
            else:
                print('Nie stać cie biedaku!')
        elif gear == '5':
            if Bohater[5] >= 100:
                Przedmioty.append(Duża_potka)
                print('Kupiłeś dużą potkę')
                Bohater[5] -= 100
            else:
                print('Nie stać cie biedaku!')
        elif gear == 'nie':
            break
        print(f'Twoje przedmioty:    {Przedmioty}')
        print('nie - Wyjście')
        print('Czy chcesz kupić coś jeszcze?')
        print(f'Pozostałe coiny:    {Bohater[5]}')

#------------------------------------Atak
def Zwykły_atak():
    return randint(0,5)

Mocny_atak = [4]
#------------------------------------Leczenie
def leczenie_1():
    if Mała_potka in Przedmioty:
        Bohater[2] += 15
        print('Odzyskałeś 15 Hp\n')
        if Bohater[2] > Bohater[1]:
            rest = Bohater[1] - Bohater[2]
            Bohater[2] += rest
            print(f'Masz teraz {Bohater[2]} Hp')
        if wybierz_leczenie == '1':
            Przedmioty.remove(Mała_potka)
    else:
        print('Nie masz małej potki!!!\n')

def leczenie_2():
    if Średnia_potka in Przedmioty:
        Bohater[2] += 30
        print('Odzyskałeś 30 Hp\n')
        if Bohater[2] > Bohater[1]:
            rest1 = Bohater[1] - Bohater[2]
            Bohater[2] += rest1
            print(f'Masz teraz {Bohater[2]} Hp')
        if wybierz_leczenie == '2':
            Przedmioty.remove(Średnia_potka)
    else:
        print('Nie masz średniej potki!!!\n')
    
def leczenie_3():
    if Duża_potka in Przedmioty:
        Bohater[2] += 100
        print('Odzyskałeś 100 Hp\n')
        if Bohater[2] > Bohater[1]:
            rest2 = Bohater[1] - Bohater[2]
            Bohater[2] += rest2
            print(f'Masz teraz {Bohater[2]} Hp')
        if wybierz_leczenie == '3':
            Przedmioty.remove(Duża_potka)
    else:
        print('Nie masz dużej potki!!!\n')

def Wybierz_leczenie():
    print('1 - wypij małą potke')
    print('2 - wypij średnią potke')
    print('3 - wypij dużą potke')
    global wybierz_leczenie
    wybierz_leczenie = input()
    if wybierz_leczenie == '1':
        print('-'*50)
        return leczenie_1()
    elif wybierz_leczenie == '2':
        print('-'*50)
        return leczenie_2()
    elif wybierz_leczenie == '3':
        print('-'*50)
        return leczenie_3()

#------------------------------------Uplepszenia
def Ubgrade():
    print('Co chciałbyś ulepszyć?    ')
    print(f'Masz {Bohater[5]} coinów\n')
    print('1 - Miecz: + 2 Mocny atak  =  100 coinów')
    print('2 - Zbroja: + 15 Max Hp  =  175 coinów')
    while True:
        print('-'*50)
        gear_1 = input()
        if gear_1 == '1':
            if Miecz in Przedmioty:
                if Bohater[5] >= 100:
                    Mocny_atak[0] += 2
                    print('Ulepszyłeś miecz!')
                    Bohater[5] -= 100
                else:
                    print('Nie stać cie biedaku!')
            else:
                print('Mósisz kupić miecz aby ulepszyć!')
        elif gear_1 == "2":
            if Zbroja in Przedmioty:
                if Bohater[5] >= 175:
                    print('Ulepszyłeś zbroję!')
                    Bohater[5] -= 175
                    Bohater[1] += 15
                else:
                    print('Nie stać cie biedaku!')
            else:
                print('Musis kupić zbroję aby ulepszyć')
        elif gear_1 == 'nie':
            break
        print('nie - Wyjście')
        print('Czy chcesz Ulepszyć coś jeszcze?')
        print(f'Pozostałe coiny:    {Bohater[5]}')
#------------------------------------Przeciwnik
#0--nazwa  1--Hp  2--atak  3--coiny  4--Pd  5--level
Przeciwnik_Hp = 10
def Przeciwnik_atak():
    return randint(1,3)
def Przeciwnik_coiny():
    return randint(0,25)
def Przeciwnik_Pd():
    return randint(1,30)
def Przeciwnik():
    global list_Przeciwnik
    list_Przeciwnik = [f"Przeciwnik poz.{liczba_pokonanych_bossów}",Przeciwnik_Hp,Przeciwnik_atak(),Przeciwnik_coiny(),Przeciwnik_Pd(),]
    return list_Przeciwnik

def Boss_atak():
    return randint(7,24)
def Boss_coiny():
    return randint(50,100)
def Boss():
    global List_boss
    List_boss = ['Boss',60,Boss_atak(),Boss_coiny(),1]
    if liczba_pokonanych_bossów >= 1:
        List_boss[1] += 60
        List_boss[2] += Boss_atak()
    return List_boss
#------------------------------------Rozgrywka
liczba_pokonanych_przeciwników = 0
liczba_pokonanych_bossów = 0
input(f'\n{Bohater[0]} Zaczynasz swoją podróż')
print('1--imię  2--max_hp  3--hp  4--pd  5--poziom  6--coiny')
print(Bohater)
while Bohater[2] >= 0:
    Bohater[1] >= Bohater[2]
    if Bohater[2] <= 0:
        break
    print('-'*50)
    print(f'Twoje przedmioty:   {Przedmioty}')
    print(f'Twoje statystyki:    {Bohater}')
    rest_Pd = 125 - Bohater[3]
    print(f'Potrzebujesz {rest_Pd} Pd do kolejnego poziomu!')
    print('1 - walka')
    print('2 - sklep')
    inp = input('Co chcesz zrobić?   ')
    if inp == 'stop':
        break
    if inp == '1':
        if Bohater[4] % 5 == 0:
            print('!'*50)
            print('Nadszedł czas na walkę z Bossem!')
            Boss()
            while List_boss[1] >= 0:
                print(f"{Name} walczysz teraz z {List_boss[0]}")
                print(f"Przeciwnik ma {List_boss[1]} Hp i zadaje ci {List_boss[2]} obrażeń\n")
                Bohater[2] = Bohater[2] - List_boss[2]
                if Bohater[2] <= 0:
                    break
                print(f"Zostało ci {Bohater[2]} Hp")
                print(f"Twoje przedmioty    {Przedmioty}")
                print('1 - atak')
                print('2 - uleczyć')
                inp1 = input('Co chcesz zrobić?    ')
                if inp1 == 'stop':
                    break
                if inp1 == '1':
                    global wybierz_atak 
                    print('1 - wykonaj Zwykły atak')
                    print('2 - wykonaj Mocny atak')
                    wybierz_atak = input()
                    if wybierz_atak == '1':
                        atak = Zwykły_atak()
                        List_boss[1] = List_boss[1] - atak
                        print(f"Zadałeś {atak} obrażeń")
                        print("-"*50)
                    if wybierz_atak == '2':
                        if Miecz not in Przedmioty:
                            print('!'*50)
                            print("""Zadełeś 0 obrażeń.
Nie możesz tego zrobić!
Potrzebujesz 'Miecz' żeby użyć!""")
                        if Miecz in Przedmioty:
                            List_boss[1] = List_boss[1] - Mocny_atak[0]
                            print('-'*50)
                            print(f"Zadałeś {Mocny_atak[0]} obrażeń")
                            print('-'*50)
                elif inp1 == '2':
                    Wybierz_leczenie()
            if inp1 == 'stop':
                break
            if List_boss[1] <= 0:
                print('Brawo. Pokonałeś Bossa!!!!!!!!!!!!!!!!')
                global inp_b
                inp_b = input(f"Dostałeś {List_boss[3]} coinów i {List_boss[4]} Level")
                Bohater[5] += List_boss[3]
                Bohater[4] += List_boss[4]
                liczba_pokonanych_bossów += 1
        else:
            Przeciwnik()
            while list_Przeciwnik[1] >= 0:
                print(f"{Name} walczysz teraz z {list_Przeciwnik[0]}")
                print(f"Przeciwnik ma {list_Przeciwnik[1]} Hp i zadaje ci {list_Przeciwnik[2]} obrażeń\n")
                Bohater[2] = Bohater[2] - list_Przeciwnik[2]
                if Bohater[2] <= 0:
                    break
                print(f"Zostało ci {Bohater[2]} Hp")
                print(f"Twoje przedmioty    {Przedmioty}")
                print('1 - atak')
                print('2 - uleczyć')
                inp1 = input('Co chcesz zrobić?    ')
                if inp1 == 'stop':
                    break
                if inp1 == '1':
                    print('1 - wykonaj Zwykły atak')
                    print('2 - wykonaj Mocny atak')
                    wybierz_atak = input()
                    if wybierz_atak == '1':
                        atak = Zwykły_atak()
                        list_Przeciwnik[1] = list_Przeciwnik[1] - atak
                        print(f"Zadałeś {atak} obrażeń")
                        print("-"*50)
                    if wybierz_atak == '2':
                        if Miecz not in Przedmioty:
                            print('!'*50)
                            print("""Zadełeś 0 obrażeń.
Nie możesz tego zrobić!
Potrzebujesz 'Miecz' żeby użyć!""")
                        if Miecz in Przedmioty:
                            list_Przeciwnik[1] = list_Przeciwnik[1] - Mocny_atak[0]
                            print('-'*50)
                            print(f"Zadałeś {Mocny_atak[0]} obrażeń")
                            print('-'*50)
                elif inp1 == '2':
                    Wybierz_leczenie()
            if inp1 == 'stop':
                break
            if list_Przeciwnik[1] <= 0:
                print('Zabiłeś przeciwnika!!!!!!!!!!!!!!!!!!!')
                print(f"Dostałeś {list_Przeciwnik[3]} coinów i {list_Przeciwnik[4]} Pd")
                Bohater[5] += list_Przeciwnik[3]
                Bohater[3] += list_Przeciwnik[4]
                liczba_pokonanych_przeciwników += 1
    if inp == '2':
        print('-'*50)
        print('1 - Kupić')
        print('2 - Ulepszyć')
        inp2 = input('Co chcesz zrobić?    \n')
        if inp2 == '1':
            Sklep()
        if inp2 == '2':
            Ubgrade()
    if Bohater[3] >= 150:
        print('^'*50)
        inp_1 = input('Gratulecje, awansowałeś na kolejny poziom!')
        Bohater[4] += 1
        Bohater[3] -= Bohater[3]

print("="*50)
print("Umarłeś !!!!!!!!")
print(f'Zabiłeś {liczba_pokonanych_przeciwników} przeciwników')
print(f'Pokonałeś {liczba_pokonanych_bossów} Bossów')
print(f"Osiągnąłęś {Bohater[4]} poziom")
