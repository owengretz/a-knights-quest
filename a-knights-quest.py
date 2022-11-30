import random


#game mechanic calculating functions

def calcStats():
    global atk, hp, evs
    stats = f"Your stats are: {hp} HP, {atk} atk, and {evs} evs.\n"
    return stats

def attack(enemyDef):
    global atk, xtratk
    attackValue = random.randint(round(atk / 2), atk)
    if xtratk == True:
        attackValue = attackValue + 25
        xtratk = False
    attackValue = (attackValue + 30) / 3
    failThreshold = random.randint(round(enemyDef / 3), enemyDef)
    print(f"Your strike had a power of {attackValue * 200:.0f}, and the enemy's defense had a power of {failThreshold * 200:.0f}.\n")
    if attackValue >= failThreshold:
        return True
    else:
        return False

def defend(enemyAtk):
    global exactWeaponName
    defendThreshold = random.randint(1, 100)
    #print(f'\n\n\n{defendThreshold}\n\n\n')
    if exactWeaponName == "daggers" or exactWeaponName == "light sword":
        defendThreshold += 15
    #print(f'\n\n\n{defendThreshold}\n\n\n')
    if defendThreshold > enemyAtk:
        return True
    else:
        return False

def evade():
    global evs
    evadeThreshold = random.randint(1, 100)
    if evs > evadeThreshold:
        return True
    else:
        return False

def dead():
    print("\n\n\n\n\nGAME OVER")

    
#actual story

def chooseWeapon():
    global atk, hp, evs, weapon, exactWeaponName
    weaponChoice = input("Enter 'h' to choose the heavy sword, 'l' to choose the light sword and shield, or 'd' to choose daggers.\n")
    if weaponChoice == "stats":
        print(calcStats())
        chooseWeapon()
    elif weaponChoice == "h":
        atk += 45
        evs -= 30
        weapon = "sword"
        exactWeaponName = "heavy sword"
        stats = calcStats
        print("\n" * 46)
        print("-" * 8)
        print("TUTORIAL")
        print("-" * 8 + "\n")
        print(f'So you chose the heavy sword, eh? This weapon packs a punch.\n\n{calcStats()}')
        choseHeavy()
    elif weaponChoice == "l":
        atk += 20
        hp += 50
        evs -= 15
        weapon = "sword"
        exactWeaponName = "light sword"
        stats = calcStats
        print("\n" * 46)
        print("-" * 8)
        print("TUTORIAL")
        print("-" * 8 + "\n")
        print(f'So you chose the light sword & shield, eh? You can never have enough HP.\n\n{calcStats()}')
        choseLight()
    elif weaponChoice == "d":
        atk += 15
        stats = calcStats
        weapon = "daggers"
        exactWeaponName = "daggers"
        print("\n" * 46)
        print("-" * 8)
        print("TUTORIAL")
        print("-" * 8 + "\n")
        print(f"So you chose the daggers, eh? You can't lose health if the enemies can't even hit you!\n\n{calcStats()}")
        choseDagg()
    else:
        print("Sorry, I didn't get that.\n")
        chooseWeapon()

def choseHeavy():
    global atk, hp, evs
    userInput = input('Here comes a pretty weak enemy goblin! Enter "attack" to strike it down with your powerful sword.\n')
    if userInput == "stats":
        print(calcStats())
        choseHeavy()
    elif userInput == "attack":
        print('See? Not much to it. In the future, consider defending first against stronger enemies though!\n\nSay, that goblin has some nice shoes! They fit comfortably.')
        print('+5 evs')
        evs += 5
        print('\nNow that you\'re a pro, where to?\nThe forest is the home of the goblins. You will surely find more there!\nThe city is full of other knights like yourself! They like to fight each other for fun sometimes.\nThe mountains contain many trolls. If you\'re looking for some variety head there.\n')
        forestCityOrMountains()
    else:
        print("Sorry, I didn't get that.\n")
        choseHeavy()

def choseLight():
    global atk, hp, evs
    userInput = input('Here comes a pretty weak enemy goblin! Enter "defend" to protect yourself! It will also leave the enemy more vulnerable, giving you +25 atk.\n')
    if userInput == "stats": 
        print(calcStats())
        choseLight()
    elif userInput == "defend":
        print('Nice job. The goblin\'s attack was successfully blocked. Now it\'s time to strike back with your temporarily increased attack!\n')
        choseLightpt2()
    else:
        print("Sorry, I didn't get that.\n")
        choseLight()

def choseLightpt2():
    global evs
    userInput = input('Enter "attack" again to kill the goblin!\n')
    if userInput == "stats":
        print(calcStats())
        choseLightpt2()
    elif userInput == "attack":
        print('Congratz, you killed the goblin.\n\nSay, that goblin has some nice shoes! They fit comfortably.')
        print('+5 evs')
        evs += 5
        print('\nNow that you\'re a pro, where to?\nThe forest is the home of the goblins. You will surely find more there!\nThe city is full of other knights like yourself! They like to fight each other for fun sometimes.\nThe mountains contain many trolls. If you\'re looking for some variety head there.\n')
        forestCityOrMountains()
    else:
        print("Sorry, I didn't get that.\n")
        choseLightpt2()
    
def choseDagg():
    global atk, hp, evs
    userInput = input('Here comes a pretty weak enemy goblin! Enter "attack" to stab it with your daggers!\n')
    if userInput == "stats":
        print(calcStats())
        choseDagg()
    elif userInput == "attack":
        print("Unfortuanately your attack wasn't strong enough. The goblin strikes back! Your high evasiveness allowed you to dodge the attack, though.\nLet's try something different. Instead of attacking, defend first. This will leave the opponent more vulnerable, giving you +25 atk temporarily!\n")
        choseDaggpt2()
    else:
        print("Sorry, I didn't get that.\n")
        choseDagg()

def choseDaggpt2():
    userInput = input('Enter "defend" to protect yourself!\n')
    if userInput == "stats":
        print(calcStats())
        choseDaggpt2()
    elif userInput == "defend":
        print("Nice! You blocked the goblin's attack without taking a scratch - and now the goblin is vulnerable!\n")
        choseDaggpt3()
    else:
        print("Sorry, I didn't get that.\n")
        choseDaggpt2()

def choseDaggpt3():
    global evs
    userInput = input('Now enter "attack" to kill the goblin!\n')
    if userInput == "stats":
        print(calcStats())
        choseDaggpt3()
    elif userInput == "attack":
        print('Congratz, you killed the goblin.\n\n\nSay, that goblin has some nice shoes! They fit comfortably.')
        print('+5 evs')
        evs += 5
        print('\nNow that you\'re a pro, where to?\nThe forest is the home of the goblins. You will surely find more there!\nThe city is full of other knights like yourself! They like to fight each other for fun sometimes.\nThe mountains contain many trolls. If you\'re looking for some variety head there.\n')
        forestCityOrMountains()
    else:
        print("Sorry, I didn't get that.\n")
        choseDaggpt3()

def forestCityOrMountains():
    global weapon, lookingForTooth
    userInput = input('Enter "forest" to go into the forest, "city" to go to the city, or "mountains" to go to the mountains.\n')
    if userInput == "stats":
        print(calcStats())
        forestCityOrMountains()
    if userInput == "forest":
        print("\n" * 46)
        print("-" * 17)
        print("THE FOREST PART 1")
        print("-" * 17 + "\n")
        print("So you chose the forest, huh. Well speaking of goblins, there seems to be one on the path right in front of you! And what's this? It's attacking something - or someone!\n")
        print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
        forest()
    elif userInput == "city":
        print("\n" * 46)
        print("-" * 15)
        print("THE CITY PART 1")
        print("-" * 15 + "\n")
        print('Well I did say that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
        print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
        city()
    elif userInput == "mountains":
        print("\n" * 46)
        print("-" * 20)
        print("THE MOUNTAINS PART 1")
        print("-" * 20 + "\n")
        print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
        print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
        print('Well... that\'s unfortuanate. Do you want to leave to look for a goblin tooth (or otherwise) or do you want to fight the troll? - I must warn you though, the troll is no easy opponent.')
        lookingForTooth = True
        mountains()
    else:
        print("Sorry, I didn't get that.\n")
        forestCityOrMountains()


#forest part 1

def forest():
    global weapon, helpingElf
    userInput = input('Enter "goblin" to help the mystery person out, or enter "person" to help the goblin kill them!\n')
    if userInput == "stats":
        print(calcStats())
        forest()
    elif userInput == "goblin":
        print('\nYou now see that the mystery person is an elf! That\'s not important right now though, you have a bigger task at hand.\n')
        helpingElf = True
        fightGoblin()
    elif userInput == "person":
        print(f"Merciless! It's obvious now that the mystery person is an elf. No matter! You plunge your {weapon} deep into their chest.\nIt looks as if the elf was wearing even nicer shoes than the ones you have, and light armor too!")
        killElf()
    else:
        print("Sorry, I didn't get that.\n")
        forest()

def fightGoblin():
    global hp, xtratk, helpingElf, lookingForTooth, hasTooth, hasCoin
    goblinAttack = 27
    goblinDefense = 35
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        fightGoblin()
    elif hp <= 0:
        dead()
    else:
        userInput = input('Enter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightGoblin()
        elif userInput == "attack":
            success = attack(goblinDefense)
            if success == True:
                print("Nice one! The goblin is dead.")
                if helpingElf == True:
                    username = input('\n???: "Thanks for saving me. My name is Anorlando. And you are?\n')
                    print(f'\nAnorlando: "Well thanks again for saving me, {username}. How could I ever repay you? - Oh, I know! You can have either my shoes or my light armor. Which one do you want?\n')
                    elfThanksYou()
                else:
                    if lookingForTooth == True:
                        print('You should steal one of those teeth. It may not be honest work, but it\'s good enough to pay the troll.')
                        print('Obtained goblin tooth!')
                        hasTooth = True
                    finishedForestPart1()
            else:
                print("The goblin avoided your attack and strikes back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the goblin's attack.")
                else:
                    print("Oh no! You were unable to avoid the goblin's attack.\n-25 HP")
                    hp = hp - 25
                fightGoblin()
        elif userInput == "defend":
            success = defend(goblinAttack)
            if success == True:
                xtratk = True
                print("You blocked the goblin's attack successfully! Your next attack will get a boost!")
            else:
                print("Oh no! Your block failed.\n-25HP")
                hp = hp - 25
            fightGoblin()
        else:
            print("Sorry, I didn't get that.\n")
            fightGoblin()
            
def killElf():
    global hp, evs
    userInput = input('\nEnter "take" to take the items, or enter "leave" to leave them.\n')
    if userInput == "stats":
        print(calcStats())
        killElf()
    elif userInput == "take":
        print("This is some nice loot!\n+25 HP\n+15 evs\nHowever, the goblin doesn't look too happy about you taking his prize! He's charging at you right now!")
        hp = hp + 25
        evs = evs - 5
        evs = evs + 15
        fightGoblin()
    elif userInput == "leave":
        print("You left the loot. The goblin seems to be trying to hand you a... a tooth!? Do you accept it?")
        acceptTooth()
    else:
        print("Sorry, I didn't get that.\n")
        killElf()

def acceptTooth():
    global hasTooth
    userInput = input('\nEnter "accept" to accept it or "decline" to decline the tooth.\n')
    if userInput == "stats":
        print(calcStats())
        acceptTooth()
    elif userInput == "accept":
        print('Obtained goblin tooth!')
        hasTooth = True
        finishedForestPart1()
    elif userInput == "decline":
        print("You declined the tooth. Was probably pretty important though not gonna lie.")
        finishedForestPart1()
    else:
        print("Sorry, I didn't get that.\n")
        acceptTooth()

def elfThanksYou():
    global evs, hp, hasTooth, lookingForTooth
    userInput = input('Enter "s" if you want the shoes, "a" if you want the armor, or enter "b" to demand for both!\n')
    if userInput == "stats":
        print(calcStats())
        elfThanksYou()
    elif userInput == "s":
        print('\nAnorlando: "The shoes? Great choice. I hope you don\'t mind if we just swap. Yours are all beaten up anyways. Goodluck on your travels!')
        print('-5 evs')
        print('+15 evs')
        evs = evs + 10
        if lookingForTooth == True:
            print('You should steal one of the goblin\'s teeth. It may not be honest work, but it\'s good enough to pay the troll.')
            print('Obtained goblin tooth!')
            hasTooth = True
        finishedForestPart1()
    elif userInput == "a":
        print('\nAnorlando: "The armor? Great choice. Take good care of it, and goodluck on your travels!')
        print('+30HP')
        hp = hp + 30
        if lookingForTooth == True:
            print('You should steal one of the goblin\'s teeth. It may not be honest work, but it\'s good enough to pay the troll.')
            print('Obtained goblin tooth!')
            hasTooth = True
        finishedForestPart1()
    elif userInput == "b":
        print('\nAnorlando: "What? That wasn\'t an option. It\'s either one or none buddy."\n')
        demandBoth()
    else:
        print("Sorry, I didn't get that.\n")
        elfThanksYou()

def demandBoth():
    global weapon, hp, hasTooth, lookingForTooth
    userInput = input('Enter "s" if you want the shoes, "a" if you want the armor, or enter "b" to demand for both again and are willing to fight for them.\n')
    if userInput == "stats":
        print(calcStats())
        demandBoth()
    elif userInput == "s":
        print('\nAnorlando: "The shoes? Great choice. I hope you don\'t mind if we just swap. Yours are all beaten up anyways. Goodluck on your travels!')
        print('-5 evs')
        print('+15 evs')
        evs = evs + 10
        if lookingForTooth == True:
            print('You should steal one of the goblin\'s teeth. It may not be honest work, but it\'s good enough to pay the troll.')
            print('Obtained goblin tooth!')
            hasTooth = True
        finishedForestPart1()
    elif userInput == "a":
        print('\nAnorlando: "The armor? Great choice. Take good care of it, and goodluck on your travels!')
        print('+30HP')
        hp = hp + 30
        if lookingForTooth == True:
            print('You should steal one of the goblin\'s teeth. It may not be honest work, but it\'s good enough to pay the troll.')
            print('Obtained goblin tooth!')
            hasTooth = True
        finishedForestPart1()
    elif userInput == "b":
        print(f'\nYou start to approach Anorlando, {weapon} drawn.')
        print('\nAnorlando: "You leave me no choice."')
        print('\nAnorlando shoots you with his bow!\n-20 HP.')
        hp = hp - 20
        fightAnorlando()
    else:
        print("Sorry, I didn't get that.\n")
        elfThanksYou()

def fightAnorlando():
    global hp, evs, xtratk, weapon, hasTooth, lookingForTooth, hasCoin
    anorlandoAttack = 23
    anorlandoDefense = 28
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        fightAnorlando()
    elif hp <= 0:
        dead()
    else:
        userInput = input('Enter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightAnorlando()
        elif userInput == "attack":
            success = attack(anorlandoDefense)
            if success == True:
                print(f"You successfully stab Anorlando with your {weapon}. You swap your shoes for his and equip his armor.")
                print('-5 evs')
                print('+15 evs')
                print('+30HP')
                evs = evs + 10
                hp = hp + 30
                if lookingForTooth == True:
                    print('You should steal one of the goblin\'s teeth. It may not be honest work, but it\'s good enough to pay the troll.')
                    print('Obtained goblin tooth!')
                    hasTooth = True
                finishedForestPart1()
            else:
                print("Anorlando avoided your attack and strikes back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided Anorlando's attack.")
                else:
                    print("Oh no! You were unable to avoid Anorlando's attack.\n-20 HP")
                    hp = hp - 20
                fightAnorlando()
        elif userInput == "defend":
            success = defend(anorlandoAttack)
            if success == True:
                xtratk = True
                print("You blocked Anorlando's attack successfully! Your next attack will get a boost!")
            else:
                print("Oh no! Your block failed.\n-20HP")
                hp = hp - 20
            fightAnorlando()
        else:
            print("Sorry, I didn't get that.\n")
            fightAnorlando()
            
def finishedForestPart1():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, hasTooth, visitedMountains, weapon
    doneForestP1 = True
    
    userInput = input('\n\nWell, you handled that... mediocrely at best.\nIf you would like to go deeper in the forest, enter "forest".\nIf you want to switch over to the city, enter "city".\nIf you\'d like to go to the mountains enter "mountains".\n')
    if userInput == "stats":
        print(calcStats())
        finishedForestPart1()
    elif userInput == "forest":
        print("\n" * 46)
        print("-" * 17)
        print("THE FOREST PART 2")
        print("-" * 17 + "\n")
        print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
        print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
        forestPart2()
    elif userInput == "city":
        if doneCityP1 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 1")
            print("-" * 15 + "\n")
            print('Well I did say earlier that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
            print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
            city()
        elif doneCityP2 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 2")
            print("-" * 15 + "\n")
            print("You've got some experience under your belt now. I think it's time to challenge the reigning champ, Sir William Marshal. What is there to lose anyways? Get right into it.")
            print('\nSir William Marshal: "Let\'s make this a good clean fight, I don\'t want no funny buisness."\n')
            fightBill()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedForestPart1()
    elif userInput == "mountains":
        if doneMountainsP1 == False:
            if hasTooth == True and visitedMountains == False:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Bridge Troll: "Now wait jusht a shecond whatsh that right there? YOU HAVE A GOBLIN TOOF? GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            elif hasTooth == True:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('And you\'re back. Now where did the troll g-')
                print('\nBridge Troll: "GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            else:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Well... that\'s unfortuanate. Do you want to leave to look for a goblin tooth (or otherwise) or do you want to fight the troll? - I must warn you though, the troll is no easy opponent.')
                lookingForTooth = True
                mountains()
        elif doneMountainsP2 == False:
            print("\n" * 46)
            print("-" * 20)
            print("THE MOUNTAINS PART 2")
            print("-" * 20 + "\n")
            print("Just beyond the bridge there's a cave! It looks like it could be really big on the inside and... there's something glinting... lets go check it out!")
            print("\nOk, we're entering the cave now. There seems to be a... oh! There's a massive cave troll right in front of you!")
            encounterCaveTroll()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedForestPart1()
    else:
        print("Sorry, I didn't get that.\n")
        finishedForestPart1()


#forest part 2
        
def forestPart2():
    global weapon, hp
    userInput = input('\nEnter "give" to give your weapon, enter "no" to refuse, or enter "run" to flee!\n')
    if userInput == "stats":
        print(calcStats())
        forestPart2()
    elif userInput == "give":
        print("I wouldn't do that if I were you. You wouldn't be able to defend yourself!")
        forestPart2()
    elif userInput == "no":
        print(f'\nWell this warlock seems extremely interested in your {weapon}!\nIt\'s sending its goblin underlings after you! There appears to be 5 in total.')
        fightUnderlings()
    elif userInput == "run":
        print(f'\nRunning away was a good try, but this warlock seems extremely interested in your {weapon}!\nIt\'s sending 5 goblin underlings after you, and they\'re very quick! One even managed to get a hit on you. There\'s no choice but to fight.\n-5 HP')
        hp -= 5
        fightUnderlings()
    else:
        print("Sorry, I didn't get that.\n")
        forestPart2()

def fightUnderlings():
    global hp, xtratk, underlingsAlive, hasCoin
    underlingAttack = 5
    underlingDefense = 15
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        fightUnderlings()
    elif hp <= 0:
        dead()
    else:
        userInput = input('\nEnter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightUnderlings()
        elif userInput == "attack":
            success = attack(underlingDefense)
            if success == True:
                underlingsAlive -= 1
                print(f'You got one. Now there\'s {underlingsAlive} underlings left.')
                if underlingsAlive == 0:
                    print("\nNice job on finishing off the underlings! You've still got the warlock to worry about though. Speaking of which, the warlock is about to strike you with a staff!")
                    fightWarlock()
                else:
                    print("\nThe other underling(s) are attacking!")
                    for x in range(underlingsAlive):
                        evadeSuccess = evade()
                        if evadeSuccess == True:
                            print(f"Luckily you avoided underling #{x + 1}'s attack.")
                        else:
                            print(f"Oh no! You were unable to avoid underling #{x + 1}'s attack.\n-5 HP")
                            hp -= 5
                    fightUnderlings()
            else:
                print("\nThe underling you attacked dodged the attack. Now all of the remaining underlings are striking back!")
                for x in range(underlingsAlive):
                    evadeSuccess = evade()
                    if evadeSuccess == True:
                        print(f"Luckily you avoided underling #{x + 1}'s attack.")
                    else:
                        print(f"Oh no! You were unable to avoid underling #{x + 1}'s attack.\n-5 HP")
                        hp -= 5
                fightUnderlings()
        elif userInput == "defend":
            blocks = 0
            fail = False
            for x in range(underlingsAlive):
                success = defend(underlingAttack)
                if success == True and fail == False:
                    print(f"You blocked underling #{x + 1}'s attack successfully!")
                    blocks += 1
                    if blocks == underlingsAlive:
                        print("Your next attack will get a boost!")
                        xtratk = True
                elif success == False and fail == False:
                    fail = True
                    print("Oh no! Your block failed.\n-5 HP")
                    hp -= 5
                else:
                    print("-5 HP")
                    hp -= 5
            fightUnderlings()
        else:
            print("Sorry, I didn't get that.\n")
            fightUnderlings()

def fightWarlock():
    global hp, xtratk, warlockHasHeal, hasCoin
    if warlockHasHeal:
        warlockAttack = 25
        warlockDefense = 30
        warlockDamage = 15
    else:
        warlockAttack = 30
        warlockDefense = 35
        warlockDamage = 25
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        fightWarlock()
    elif hp <= 0:
        dead()
    else:
        userInput = input('\nEnter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightWarlock()
        elif userInput == "attack":
            success = attack(warlockDefense)
            if success == True and warlockHasHeal == True:
                print("\nWhat a strike! The warlock will be dead within seconds.\n\nWait... what's this? The warlock is using a healing potion? And he looks even more angry than before!")
                warlockHasHeal = False
                fightWarlock()
            elif success == True:
                print("\nOk, that was another great hit. The warlock should be dead now.\nThe warlock was also carrying another healing potion it didn't get a chance to use! This is some seriously high tech stuff.\n+100 HP")
                hp += 100
                finishedForestPart2()
            else:
                print("\nThe warlock blocked your attack and strikes back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the warlock's attack.")
                else:
                    print(f"Oh no! You were unable to avoid the warlock's attack.\n-{warlockDamage} HP")
                    hp -= warlockDamage
                fightWarlock()
        elif userInput == "defend":
            success = defend(warlockAttack)
            if success == True:
                xtratk = True
                print("You blocked the warlock's attack successfully! Your next attack will get a boost!")
            else:
                print(f"Oh no! Your block failed.\n-{warlockDamage} HP")
                hp -= warlockDamage
            fightWarlock()
        else:
            print("Sorry, I didn't get that.\n")
            fightWarlock()

def finishedForestPart2():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, hasTooth, visitedMountains, weapon, finalBattleInForest
    doneForestP2 = True
    
    userInput = input('\n\nI\'ll admit, I\'m impressed with your progress.\nIf you would like to go into the goblin lair deep in the forest, enter "forest". I\'ve got a feeling in my gut that this will be one of your last decisions though.\nIf you want to switch over to the city, enter "city".\nIf you\'d like to go to the mountains enter "mountains".\n')
    if userInput == "stats":
        print(calcStats())
        finishedForestPart2()
    elif userInput == "forest":
        print("\n" * 46)
        print("-" * 16)
        print("THE FINAL BATTLE")
        print("-" * 16 + "\n")
        print("You venture into the deepest part of the woods, and there is a goblin lair! There\'s a throne but it\'s empty.\n\nOh wait someone is coming from the same direction you did!")
        print('\nGoblin King: "Well that was dissapointing trip to the city. The so called "champion" didn\'t even stand a chance. Maybe you will be a bigger challenge."')
        print('\nThe goblin king is charging at you, do something!')
        finalBattleInForest = True
        finalBattle()
    elif userInput == "city":
        if doneCityP1 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 1")
            print("-" * 15 + "\n")
            print('Well I did say earlier that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
            print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
            city()
        elif doneCityP2 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 2")
            print("-" * 15 + "\n")
            print("You've got some experience under your belt now. I think it's time to challenge the reigning champ, Sir William Marshal. What is there to lose anyways? Get right into it.")
            print('\nSir William Marshal: "Let\'s make this a good clean fight, I don\'t want no funny buisness."\n')
            fightBill()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedForestPart2()
    elif userInput == "mountains":
        if doneMountainsP1 == False:
            if hasTooth == True and visitedMountains == False:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Bridge Troll: "Now wait jusht a shecond whatsh that right there? YOU HAVE A GOBLIN TOOF? GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            elif hasTooth == True:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('And you\'re back. Now where did the troll g-')
                print('\nBridge Troll: "GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            else:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Well... that\'s unfortuanate. Do you want to leave to look for a goblin tooth (or otherwise) or do you want to fight the troll? - I must warn you though, the troll is no easy opponent.')
                lookingForTooth = True
                mountains()
        elif doneMountainsP2 == False:
            print("\n" * 46)
            print("-" * 20)
            print("THE MOUNTAINS PART 2")
            print("-" * 20 + "\n")
            print("Just beyond the bridge there's a cave! It looks like it could be really big on the inside and... there's something glinting... lets go check it out!")
            print("\nOk, we're entering the cave now. There seems to be a... oh! There's a massive cave troll right in front of you!")
            encounterCaveTroll()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedForestPart2()
    else:
        print("Sorry, I didn't get that.\n")
        finishedForestPart2()


#city part 1

def city():
    global hp, xtratk
    charlesAttack = 32
    charlesDefense = 37
    if hp <= 0:
        dead()
    else:
        userInput = input('Enter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            city()
        elif userInput == "attack":
            success = attack(charlesDefense)
            if success == True:
                print("\nNice moves! Sir Charles the Bald's sword just flew out of his hand in an attempt to block your strike.")
                print('\n"Sir Charles the Bald: "Now just hold on a second... I\'m sure we can come to some sort of agreement..."\n')
                killCharlesOrNot()
            else:
                print("Sir Charles the Bald blocked your attack and strikes back!\n")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided Sir Charles the Bald's attack.\n")
                else:
                    print("Oh no! You were unable to avoid Sir Charles the Bald's attack.\n-30 HP")
                    hp -= 30
                city()
        elif userInput == "defend":
            success = defend(charlesAttack)
            if success == True:
                xtratk = True
                print("You blocked Sir Charles the Bald's attack successfully! Your next attack will get a boost!\n")
            else:
                print("Oh no! Your block failed.\n-30HP\n")
                hp -= 30
            city()
        else:
            print("Sorry, I didn't get that.\n")
            city()

def killCharlesOrNot():
    global weapon, hp
    userInput = input('Enter "kill" to execute Sir Charles the Bald and steal his helmet, or enter "spare" to save him and walk away with only the prize money.\n')
    if userInput == "stats":
        print(calcStats())
        killCharlesOrNot()
    elif userInput == "kill":
        print('Gruesome. That\'s one way to do it I suppose. At least the helmet fits pretty well.\n+60 HP')
        hp += 60
        print(f'\nNow lets spend your prize money! No time like the present. Your best options are either:\n    - getting your {weapon} sharpened, which will net you +15 atk\n    - getting a cloak, giving +15 evs')
        challengedByCharlesFriends()
    elif userInput == "spare":
        print('Good choice. No one needs to see that gore.')
        print(f'\nNow lets spend your prize money! No time like the present. Your best options are either:\n    - getting your {weapon} sharpened, which will net you +15 atk\n    - getting a cloak, giving +15 evs')
        sharpenOrCloak()
    else:
        print("Sorry, I didn't get that.\n")
        killCharlesOrNot()

def challengedByCharlesFriends():
    global weapon
    userInput = input(f'Enter "sharpen" to sharpen your {weapon}, or enter "cloak" to buy the cloak!\n')
    if userInput == "stats":
        print(calcStats())
        challengedByCharlesFriends()
    elif userInput == "sharpen" or "cloak":
        print('\nOh shoot! Here come two intimidating men, and they look very angry!')
        print('\nMan #1: "That\'s the guy! That\'s the one that killed Charles!"')
        print('\nMan #2: "Get him!"\n')
        fightOrNot()
    else:
        print("Sorry, I didn't get that.\n")
        challengedByCharlesFriends()

def fightOrNot():
    userInput = input(f'Enter "fight" to try and fight the men off, or enter "bribe" to offer them your money!\n')
    if userInput == "stats":
        print(calcStats())
        fightOrNot()
    elif userInput == "fight":
        print('\nHere they come, do something quick!')
        fightCharlesFriends()
    elif userInput == "bribe":
        print('You hold out the bag of money. They take it, give you a scowl, and leave. That was a close one!')
        finishedCityPart1()
    else:
        print("Sorry, I didn't get that.\n")
        fightOrNot()

def fightCharlesFriends():
    global hp, xtratk, friendsAlive
    friendsAttack = 20
    friendsDefense = 27
    if hp <= 0:
        dead()
    else:
        userInput = input('\nEnter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightCharlesFriends()
        elif userInput == "attack":
            success = attack(friendsDefense)
            if success == True:
                if friendsAlive == 2:
                    print("Well played. One down, one to go!")
                    friendsAlive -= 1
                    print("\nThe second man is still alive and is striking!")
                    evadeSuccess = evade()
                    if evadeSuccess == True:
                        print("Luckily you avoided the second man's attack.")
                    else:
                        print("Oh no! You were unable to avoid the second man's attack.\n-20 HP")
                        hp -= 20
                    fightCharlesFriends()
                elif friendsAlive == 1:
                    print("Great work! They're both dead.\n\nNow we can actually spend the money.")
                    sharpenOrCloak()
            elif friendsAlive == 2:
                print("The man you attacked dodged the attack. Now they're both striking back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the first man's attack.")
                else:
                    print("Oh no! You were unable to avoid the first man's attack.\n-20 HP")
                    hp -= 20
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the second man's attack.")
                else:
                    print("Oh no! You were unable to avoid the second man's attack.\n-20 HP")
                    hp -= 20
                fightCharlesFriends()
            else:
                print("The man you attacked dodged the attack. Now he's striking back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the man's attack.")
                else:
                    print("Oh no! You were unable to avoid the man's attack.\n-20 HP")
                    hp -= 20
                fightCharlesFriends()
        elif userInput == "defend":
            if friendsAlive == 2:
                success = defend(friendsAttack)
                if success == True:
                    print("You blocked the first man's attack successfully!")
                    success = defend(friendsAttack)
                    if success == True:
                        xtratk = True
                        print("You blocked the second man's attack successfully! Your next attack will get a boost!")
                    else:
                        xtratk = False
                        print("Oh no! Your block against the second man failed.\n-20HP")
                        hp -= 20
                else:
                    print("Oh no! Your block failed.\n-20HP\n-20HP")
                    hp -= 40
                fightCharlesFriends()
            else:
                success = defend(friendsAttack)
                if success == True:
                    print("You blocked the man's attack successfully! Your next attack will get a boost!")
                    xtratk = True
                else:
                    print("Oh no! Your block failed.\n-20HP")
                    hp -= 20
                fightCharlesFriends()
        else:
            print("Sorry, I didn't get that.\n")
            fightCharlesFriends()

def sharpenOrCloak():
    global weapon, atk, evs, hasTooth
    userInput = input(f'Enter "sharpen" to sharpen your {weapon}, or enter "cloak" to buy the cloak!\n')
    if userInput == "stats":
        print(calcStats())
        sharpenOrCloak()
    elif userInput == "sharpen":
        print(f'\nAwesome. You\'ll be slicing through bad guys like butter with your {weapon} now.\n+15 atk')
        atk += 15
        finishedCityPart1()
    elif userInput == "cloak":
        print(f'\nAwesome. This should hopefully make it much harder for enemies to hit you!\n+15 evs')
        evs += 15
        finishedCityPart1()
    else:
        print("Sorry, I didn't get that.\n")
        sharpenOrCloak()

def finishedCityPart1():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, weapon
    doneCityP1 = True
    
    userInput = input('\n\nNot bad. Not bad at all.\nIf you would like to go stay in the city, enter "city". I hear the reigning champ is coming to town soon.\nIf you want to go to the forest, enter "forest".\nIf you\'d like to go to the mountains enter "mountains".\n')
    if userInput == "stats":
        print(calcStats())
        finishedCityPart1()
    elif userInput == "city":
        print("\n" * 46)
        print("-" * 15)
        print("THE CITY PART 2")
        print("-" * 15 + "\n")
        print("You've got some experience under your belt now. I think it's time to challenge the reigning champ, Sir William Marshal. What is there to lose anyways? Get right into it.")
        print('\nSir William Marshal: "Let\'s make this a good clean fight, I don\'t want no funny buisness."\n')
        fightBill()
    elif userInput == "forest":
        if doneForestP1 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 1")
            print("-" * 17 + "\n")
            print("So you chose the forest, huh. Say, there seems to be a goblin the path right in front of you! And what's this? It's attacking something - or someone!\n")
            print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
            forest()
        elif doneForestP2 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 2")
            print("-" * 17 + "\n")
            print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
            print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
            forestPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedCityPart1()
    elif userInput == "mountains":
        if doneMountainsP1 == False:
            if hasTooth == True and visitedMountains == False:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Bridge Troll: "Now wait jusht a shecond whatsh that right there? YOU HAVE A GOBLIN TOOF? GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth though, making it an easier opponent!')
                fightBridgeTroll()
            elif hasTooth == True:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('And you\'re back. Now where did the troll g-')
                print('\nBridge Troll: "GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth though, making it an easier opponent!')
                fightBridgeTroll()
            else:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Well... that\'s unfortuanate. Do you want to leave to look for a goblin tooth (or otherwise) or do you want to fight the troll? - I must warn you though, the troll is no easy opponent.')
                lookingForTooth = True
                mountains()
        elif doneMountainsP2 == False:
            print("\n" * 46)
            print("-" * 20)
            print("THE MOUNTAINS PART 2")
            print("-" * 20 + "\n")
            print("Just beyond the bridge there's a cave! It looks like it could be really big on the inside and... there's something glinting... lets go check it out!")
            print("\nOk, we're entering the cave now. There seems to be a... oh! There's a massive cave troll right in front of you!")
            encounterCaveTroll()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            finishedCityPart1()
    else:
        print("Sorry, I didn't get that.\n")
        finishedCityPart1()


#city part 2

def fightBill():
    global weapon
    userInput = input('Enter "attack" to go for the kill, or enter "defend" to go for a block!\n')
    if userInput == "stats":
        print(calcStats())
        fightBill()
    elif userInput == "attack" or "defend":
        print(f'\nSir William Marshal: "Yo chill! What\'s with the {weapon}? Are you trying to get someone killed? All I asked for was a clean game of rock paper scissors, best 2 out of 3!"\n')
        print("Oh... I'm sure you weren't expecting that... To be fair I wasn't either. Well, do your best!")
        billRPC()
    else:
        print("Sorry, I didn't get that.\n")
        fightBill()

def billRPC():
    global atk, hasCoin
    playerWins = 0
    billWins = 0
    while playerWins != 2 and billWins != 2:
        userInput = input('\nRock...\nPaper...\nScissors...\nShoot!\nEnter "rock", "paper", or "scissors"\n')
        billInput = random.randint(1, 3)
        if billInput == 1:
            billInput = "rock"
        elif billInput == 2:
            billInput = "paper"
        else:
            billInput = "scissors"
        print(f'\nYou chose {userInput} and Sir William Marshal chose {billInput}!')  
        if userInput == "stats":
            print(calcStats())
            billRPC()
        elif userInput == "rock" or "paper" or "scissors":
            if userInput == "rock" and billInput == "scissors" or userInput == "paper" and billInput == "rock" or userInput == "scissors" and billInput == "paper":
                playerWins += 1
                print(f'You got a point! The score is {playerWins} to {billWins}!')
            elif userInput == billInput:
                print(f'It\'s a draw! The score is {playerWins} to {billWins}!')
            else:
                billWins += 1
                print(f'Sir William Marshal got a point! The score is {playerWins} to {billWins}!')
        else:
            print("Sorry, I didn't get that.\n")
    if playerWins == 2:
        print('\nSir William Marshal: "Congratulations on your win. As a token of my thanks, I will give you this coin. It may come in handy later."')
        print('Obtained coin!')
        hasCoin = True
    else:
        print('\nSir William Marshal: "Wow, you REALLY suck at rock paper scissors. You should honestly just give up."\n')
        print('Ouch. That\'s gotta affect your confidence.\n-3 atk')
        atk -= 3
    doneCityPart2()

def doneCityPart2():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, hasTooth, visitedMountains, weapon, hasCoin
    doneCityP2 = True
    
    userInput = input('\n\nWhat an interesting turn of events.\nWell, If you\'d like to stick around here, enter "city". Something tells me it would be the last chapter in your tale.\nIf you want to go to the forest, enter "forest".\nIf you\'d like to go to the mountains enter "mountains".\n')
    if userInput == "stats":
        print(calcStats())
        doneCityPart2()
    elif userInput == "forest":
        if doneForestP1 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 1")
            print("-" * 17 + "\n")
            print("So you chose the forest, huh. Say, there seems to be a goblin the path right in front of you! And what's this? It's attacking something - or someone!\n")
            print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
            forest()
        elif doneForestP2 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 2")
            print("-" * 17 + "\n")
            print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
            print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
            forestPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneCityPart2()
    elif userInput == "city":
        print("\n" * 46)
        print("-" * 16)
        print("THE FINAL BATTLE")
        print("-" * 16 + "\n")
        print("You stay in the city to see what happens next...\n\nUh oh! A goblin decked out with fancy gear and crown just arrived! This is the goblin king... You may be in great danger, but if you defeat him you will surely become the champion!")
        print('\nGoblin King: "Alright who\'s the current champion? Who is it!?"')
        print('\nSir William Marshal: "It\'s him, right over there."')
        if hasCoin == False:
            print('\nUh oh! He\'s saying you won so that he doesn\'t have to fight the goblin king!')
        print('The goblin king is charging at you, do something!')
        finalBattle()
    elif userInput == "mountains":
        if doneMountainsP1 == False:
            if hasTooth == True and visitedMountains == False:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Bridge Troll: "Now wait jusht a shecond whatsh that right there? YOU HAVE A GOBLIN TOOF? GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            elif hasTooth == True:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('And you\'re back. Now where did the troll g-')
                print('\nBridge Troll: "GIMME THE GOBLIN TOOF. I NEEEED THE GOBLIN TOOF. GIMME NOW."\n')
                print('The troll is coming at you! You have no choice but to fight! The troll should hopefully be distracted by the tooth, making it an easier opponent though!')
                fightBridgeTroll()
            else:
                print("\n" * 46)
                print("-" * 20)
                print("THE MOUNTAINS PART 1")
                print("-" * 20 + "\n")
                print('The mountains are quite interesting, and you may agree once you visit. The trolls seem to have more personality than the goblins anyways.\nSpeaking of which - I should warn you. You won\'t get very far without confronting the bridge troll. Here he is now!')
                print('\nBridge Troll: "Well wadda\' we got \'ere? You\'s not croshin\' thish bridge here unlesh... Ah yesh! Gimme one of thoshe goblin\'s teef! Goblinsh \'ave been known to give em\' out people as a shign of thanksh! Don\'t come back until ye\'ve got one!"\n')
                print('Well... that\'s unfortuanate. Do you want to leave to look for a goblin tooth (or otherwise) or do you want to fight the troll? - I must warn you though, the troll is no easy opponent.')
                lookingForTooth = True
                mountains()
        elif doneMountainsP2 == False:
            print("\n" * 46)
            print("-" * 20)
            print("THE MOUNTAINS PART 2")
            print("-" * 20 + "\n")
            print("Just beyond the bridge there's a cave! It looks like it could be really big on the inside and... there's something glinting... lets go check it out!")
            print("\nOk, we're entering the cave now. There seems to be a... oh! There's a massive cave troll right in front of you!")
            encounterCaveTroll()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneCityPart2()
    else:
        print("Sorry, I didn't get that.\n")
        doneCityPart2()


#mountains part 1

def mountains():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, visitedMountains
    visitedMountains = True
    userInput = input('\nIf you want to go to the forest instead, enter "forest".\nIf you\'d like to go to the city enter "city",\nIf you\'d like to try your hand in combat, enter "fight".\n')
    if userInput == "stats":
        print(calcStats())
        mountains()
    elif userInput == "fight":
        print('This may be more than you bargained for! Goodluck!\n')
        fightBridgeTroll()
    elif userInput == "city":
        if doneCityP1 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 1")
            print("-" * 15 + "\n")
            print('Well I did say earlier that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
            print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
            city()
        elif doneCityP2 == False:
            cityPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            mountains()
    elif userInput == "forest":
        if doneForestP1 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 1")
            print("-" * 17 + "\n")
            print("So you chose the forest, huh. Say, there seems to be a goblin the path right in front of you! And what's this? It's attacking something - or someone!\n")
            print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
            forest()
        elif doneForestP2 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 2")
            print("-" * 17 + "\n")
            print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
            print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
            forestPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            mountains()
    else:
        print("Sorry, I didn't get that.\n")
        mountains()

def fightBridgeTroll():
    global hp, xtratk, helpingElf, hasTooth, exactWeaponName, atk, evs, hasCoin
    if hasTooth == True:
        bridgeTrollAttack = 25
        bridgeTrollDefense = 30
        bridgeTrollDamage = 25
    else:
        bridgeTrollAttack = 35
        bridgeTrollDefense = 40
        bridgeTrollDamage = 45
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        fightBridgeTroll()
    elif hp <= 0:
        dead()
    else:
        userInput = input('Enter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            fightBridgeTroll()
        elif userInput == "attack":
            success = attack(bridgeTrollDefense)
            if success == True:
                if exactWeaponName == "heavy sword":
                    print("Well you made it out alive.\n\nWait... what's that under the bridge? It looks like some sort of high quality weapon. Let's get a closer look.\n\nAh yes, it's a brilliant sword! One even bigger than the one you have now!\n+15 atk")
                    atk += 15
                elif exactWeaponName == "light sword":
                    print("Well you made it out alive.\n\nWait... what's that under the bridge? It looks like some sort of high quality weapon. Let's get a closer look.\n\nAh yes, it's a brilliant sword! One even sharper and lighter than the one you have now!\n+10 atk\n+5 evs")
                    atk += 10
                    evs += 5
                else:
                    print("Well you made it out alive.\n\nWait... what's that under the bridge? It looks like some sort of high quality weapon. Let's get a closer look.\n\nAh yes, a pair of brilliant daggers! They are even sharper than the ones you have now!\n+15 atk")
                    atk += 15
                doneMountainsPart1()
            else:
                print("The troll avoided your attack and strikes back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the troll's attack.")
                else:
                    print(f"Oh no! You were unable to avoid the troll's attack.\n-{bridgeTrollDamage} HP")
                    hp -= bridgeTrollDamage
                fightBridgeTroll()
        elif userInput == "defend":
            success = defend(bridgeTrollAttack)
            if success == True:
                xtratk = True
                print("You blocked the troll's attack successfully! Your next attack will get a boost!")
            else:
                print(f"Oh no! Your block failed.\n-{bridgeTrollDamage} HP")
                hp -= bridgeTrollDamage
            fightBridgeTroll()
        else:
            print("Sorry, I didn't get that.\n")
            fightBridgeTroll()

def doneMountainsPart1():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, visitedMountains, weapon
    doneMountainsP1 = True
    
    userInput = input(f'\n\nWhat a lovely surprise! The {weapon} will make a fine addition to your collection.\nIf you\'d like to explore the mountains more, enter "mountains".\nIf you want to go to the forest, enter "forest".\nIf you\'d like to check out what\'s going on in the city enter "city".\n')
    if userInput == "stats":
        print(calcStats())
        doneMountainsPart1()
    elif userInput == "forest":
        if doneForestP1 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 1")
            print("-" * 17 + "\n")
            print("So you chose the forest, huh. Say, there seems to be a goblin the path right in front of you! And what's this? It's attacking something - or someone!\n")
            print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
            forest()
        elif doneForestP2 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 2")
            print("-" * 17 + "\n")
            print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
            print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
            forestPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneMountainsPart1()
    elif userInput == "city":
        if doneCityP1 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 1")
            print("-" * 15 + "\n")
            print('Well I did say earlier that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
            print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
            city()
        elif doneCityP2 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 2")
            print("-" * 15 + "\n")
            print("You've got some experience under your belt now. I think it's time to challenge the reigning champ, Sir William Marshal. What is there to lose anyways? Get right into it.")
            print('\nSir William Marshal: "Let\'s make this a good clean fight, I don\'t want no funny buisness."\n')
            fightBill()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneMountainsPart1()
    elif userInput == "mountains":
        print("\n" * 46)
        print("-" * 20)
        print("THE MOUNTAINS PART 2")
        print("-" * 20 + "\n")
        print("Just beyond the bridge there's a cave! It looks like it could be really big on the inside and... there's something glinting... lets go check it out!")
        print("\nOk, we're entering the cave now. There seems to be a... oh! There's a massive cave troll right in front of you!")
        encounterCaveTroll()
    else:
        print("Sorry, I didn't get that.\n")
        doneMountainsPart1()
        

#mountains part 2

def encounterCaveTroll():
    userInput = input('Fight or flight! Enter "attack" to try to kill it or enter "run" to get out of here!\n')
    if userInput == "stats":
        print(calcStats())
        encounterCaveTroll()
    elif userInput == "attack":
        print("\nYou put all your might into a downwards strike, but the giant cave troll stopped you by grabbing your blade with it\'s bare hands, completely unharmed!")
        print('\nCave Troll: "Oh please, save the violence. Why don\'t we just sit down and have a cup of tea? Here."\n')
        smashOrDrinkTea()
    elif userInput == "run":
        print('\nCave Troll: "Wait! Don\'t run! Lets just have a cup of tea."\n')
        print('Well, you haven\'t had a drink in a while... it couldn\'t hurt right? Up to you though.')
        runOrDrinkTea()
    else:
        print("Sorry, I didn't get that.\n")
        encounterCaveTroll()

def smashOrDrinkTea():
    global hp
    userInput = input('Enter "tea" to calm down and drink with the cave troll, or enter "smash" to smash the teacup!\n')
    if userInput == "stats":
        print(calcStats())
        smashOrDrinkTea()
    elif userInput == "tea":
        print('\nCave Troll: "Thank you for giving me a chance. Most people just judge me for my scary appearance and won\'t sit down to have a cup o\' tea. This should help you rest up a bit."\n')
        print('This tea IS pretty delicious...\n+25 HP')
        hp += 25
        doneMountainsPart2()
    elif userInput == "smash":
        print('\nCave Troll: "YOU\'RE JUST LIKE THE REST. I TRY TO DO SOMETHING NICE AND YOU CAN\'T EVEN ACCEPT IT. YOU WILL REGRET THAT."\n')
        print(f'Oh no! The cave troll grabbed you! And... smashed your head against the wall, then threw you out of the cave!\n-{hp - 1}')
        hp -= (hp - 1)
        doneMountainsPart2()
    else:
        print("Sorry, I didn't get that.\n")
        smashOrDrinkTea()

def runOrDrinkTea():
    global hp
    userInput = input('Enter "tea" to calm down and drink with the cave troll, or enter "run" to get out of here!\n')
    if userInput == "stats":
        print(calcStats())
        runOrDrinkTea()
    elif userInput == "tea":
        print('\nCave Troll: "Thank you for giving me a chance. Most people just judge me for my scary appearance and won\'t sit down to have a cup o\' tea. This should help you rest up a bit."\n')
        print('This tea IS pretty delicious...\n+25 HP')
        hp += 25
        doneMountainsPart2()
    elif userInput == "run":
        print('\nWhat a shame... That troll seemed so friendly.')
        doneMountainsPart2()
    else:
        print("Sorry, I didn't get that.\n")
        runOrDrinkTea()

def doneMountainsPart2():
    global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, hasTooth, visitedMountains, weapon, finalBattleInMountains
    doneMountainsP2 = True
    userInput = input(f'\n\nWell that was an interesting turn of events.\nIf you\'d like to stay in the mountains, enter "mountains". My spidey senses are tingling though, your journey may be wrapping up!\nIf you want to go to the forest, enter "forest".\nIf you\'d like to check out what\'s going on in the city enter "city".\n')
    if userInput == "stats":
        print(calcStats())
        doneMountainsPart2()
    elif userInput == "forest":
        if doneForestP1 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 1")
            print("-" * 17 + "\n")
            print("So you chose the forest, huh. Say, there seems to be a goblin the path right in front of you! And what's this? It's attacking something - or someone!\n")
            print('???: "Help! I\'m being attacked! Get this goblin off of me!"\n')
            forest()
        elif doneForestP2 == False:
            print("\n" * 46)
            print("-" * 17)
            print("THE FOREST PART 2")
            print("-" * 17 + "\n")
            print("You venture deeper into the forest...\n\nThere seems to be some sort of hut. Upon looking inside it looks like there\'s... some sort of goblin warlock? You probably don\'t want to mess with-\nI think he saw you, watch out!")
            print(f"\nThe warlock is... pointing at your {weapon}? Yes, it appears like the warlock is motioning for you to hand it your {weapon}! What do you do?")
            forestPart2()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneMountainsPart2()
    elif userInput == "city":
        if doneCityP1 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 1")
            print("-" * 15 + "\n")
            print('Well I did say earlier that knights like to fight each other, and you chose to go to the city - I hope you were prepared!\nSir Charles the Bald has been making quite a sizeable sum of money lately. Say, why don\'t you put an end to his winning streak?')
            print(f'\nSir Charles the Bald: "You must be the new guy in town. Hah, nice {weapon} loser! Give me all you got! Although that won\'t be much from what I can tell."\n')
            city()
        elif doneCityP2 == False:
            print("\n" * 46)
            print("-" * 15)
            print("THE CITY PART 2")
            print("-" * 15 + "\n")
            print("You've got some experience under your belt now. I think it's time to challenge the reigning champ, Sir William Marshal. What is there to lose anyways? Get right into it.")
            print('\nSir William Marshal: "Let\'s make this a good clean fight, I don\'t want no funny buisness."\n')
            fightBill()
        else:
            print("But you've already explored that area pretty thoroughly... Try something else!")
            doneMountainsPart2()
    elif userInput == "mountains":
        print("\n" * 46)
        print("-" * 16)
        print("THE FINAL BATTLE")
        print("-" * 16 + "\n")
        print("Just as you were about to leave a goblin decked out with fancy armor and a crown walks into the cave! He must be a king or something!")
        print('\nGoblin King: "Babe? Who is this? Why are there 2 teacups set out?"')
        print('\nCave Troll: "It\'s not what it looks like, I swear! They\'re only teacups!"')
        print('\nGoblin King: "You\'ve used that excuse one too many times! I\'ll kill him! I\'ll kill him dead! I\'m tired of you having affairs with travelling knights!"')
        print('\nUh oh. This doesn\'t look good. The goblin king is charging at you, do something!')
        finalBattleInMountains = True
        finalBattle()
    else:
        print("Sorry, I didn't get that.\n")
        doneMountainsPart2()

def finalBattle():
    global hp, xtratk, goblinKingLives, finalBattleInMountains, finalBattleInForest, hasCoin
    goblinKingAttack = 30
    goblinKingDefense = 30
    goblinKingDamage = 30
    if hp <= 0 and hasCoin == True:
        print("\n\n\n\n\nGAME OV-")
        print('Wait... It seems as though the coin Sir William Marshal gave you is restoring your life force! Get back in the game!\n+100 HP')
        hp = 100
        finalBattle()
    elif hp <= 0:
        dead()
    else:
        userInput = input('\nEnter "attack" to go for the kill, or enter "defend" to go for a block!\n')
        if userInput == "stats":
            print(calcStats())
            finalBattle()
        elif userInput == "attack":
            success = attack(goblinKingDefense)
            if success == True and goblinKingLives == 3:
                print("Nice hit! That\'s definitely gonna leave a mark, but the goblin king is still very much capable of killing you, don\'t slow down the pace!")
                goblinKingLives -= 1
                print("\nThe goblin king is striking back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the goblin king's attack.")
                else:
                    print(f"Oh no! You were unable to avoid the goblin king's attack.\n-{goblinKingDamage} HP")
                    hp -= goblinKingDamage
                finalBattle()
            elif success == True and goblinKingLives == 2:
                print("\nAwesome! That\'s another great strike! Keep going though, one more strike should put him out for good!")
                goblinKingLives -= 1
                print("\nThe goblin king is striking back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the goblin king's attack.")
                else:
                    print(f"Oh no! You were unable to avoid the goblin king's attack.\n-{goblinKingDamage} HP")
                    hp -= goblinKingDamage
                finalBattle()
            elif success == True:
                print("That was a fatal blow! The goblin king fell over, dead.")
                if finalBattleInMountains == True:
                    print('\nCave Troll: "Wow, you are so strong! You managed to defeat the king!?"')
                    print('Obtained cave troll\'s love and affection!')
                elif finalBattleInForest == True:
                    print('\nAll of the goblins that watched the fight are... bowing down to you? It seems they are anointing you as their new king!')
                    print('Obtained crown!')
                    print("Obtained status: 'King of the Goblins'!")
                else:
                    print('\nAll the other knights and everyone else watching seem stunned at your epic victory! They crown you champion.')
                    print("Obtained status: 'Champion'!")
                print('\n\n\n\n\nCongratulations, player. You beat A Knight\'s Quest!')
            else:
                print("\nThe goblin king blocked your attack and strikes back!")
                evadeSuccess = evade()
                if evadeSuccess == True:
                    print("Luckily you avoided the goblin king's attack.")
                else:
                    print(f"Oh no! You were unable to avoid the goblin king's attack.\n-{goblinKingDamage} HP")
                    hp -= goblinKingDamage
                finalBattle()
        elif userInput == "defend":
            success = defend(goblinKingAttack)
            if success == True:
                xtratk = True
                print("You blocked the goblin king's attack successfully! Your next attack will get a boost!")
            else:
                print(f"Oh no! Your block failed.\n-{goblinKingDamage} HP")
                hp -= goblinKingDamage
            finalBattle()
        else:
            print("Sorry, I didn't get that.\n")
            finalBattle()


#variables

global atk, hp, evs, weapon, exactWeaponName, xtratk, helpingElf, hasTooth, lookingForTooth, friendsAlive, underlingsAlive, warlockHasHeal, goblinKingLives, hasCoin
atk = 0
hp = 100
evs = 50
friendsAlive = 2
underlingsAlive = 5
goblinKingLives = 3
weapon = "no weapon"
exactWeaponName = "no weapon"
xtratk = False
helpingElf = False
hasTooth = False
lookingForTooth = False
warlockHasHeal = True
hasCoin = False

global doneForestP1, doneForestP2, doneCityP1, doneCityP2, doneMountainsP1, doneMountainsP2, visitedMountains, finalBattleInMountains, finalBattleInForest
doneForestP1 = False
doneForestP2 = False
doneCityP1 = False
doneCityP2 = False
doneMountainsP1 = False
doneMountainsP2 = False
visitedMountains = False
finalBattleInMountains = False
finalBattleInForest = False


#introduction

print('Welcome to A Knight\'s Quest. In this choose your own adventure text game you will play as a knight.\nYou have 3 different stats:\n    - Health\n    - Attack\n    - Evasiveness/Speed\n\nYour base stats are:\n    - 100 HP (health)\n    - 0 atk (attack)\n    - 50 evs (evasiveness)\n\nIMPORTANT:You can check your stats anytime by entering "stats".')
print("\nHP is how much damage you can take before it's gameover. atk is the probability of landing your hits, and evs is the probability of dodging hits.\n")
print('COMBAT: Throughout the game, there will be many battles. You will have the option to either "attack" or "defend":')
print('    - Choosing "attack" will run your atk stat through a formula and come up with how much attack power your strike has, which will be compared to the defense power of the enemy.\n      If your number is higher, the strike succeeds! These numbers will always be displayed.')
print('    - Choosing "defend" will calculate if your defence succeeds. You have a smaller chance of succeeding against stronger enemies!      If it succeeds, your atk stat is TEMPORARILY increased by 25, so that your next attack is stronger.\n      As you will find out, there are different weapons, and this defend feature helps you defeat stronger enemies when using a weapon with a smaller atk stat!\n')
print("Speaking of which, I think it's time to choose your weapon!\n    Heavy Sword:\n        +45atk\n        -30evs\n    Light Sword & Shield:\n        +20atk\n        +50HP\n        -15evs\n    Daggers:\n        +15atk\n")

chooseWeapon()
