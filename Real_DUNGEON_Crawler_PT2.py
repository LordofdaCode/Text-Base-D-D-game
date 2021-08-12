import random
import time

print('Welcome to my Dungeon Crawler game!')

#Slow_scroll
def slow_scroll(Char):
  for Char in Char:
    print(Char, end='')
    time.sleep(0.10)


#Hero select
print()

Choose_Character = input('Choose a character:\n1.Warrior\n2.Wizard\n3.Elf\n')

if Choose_Character == '1':
    hero = {'HP':140,'AP':23,'Class':'Warrior'} 

if Choose_Character == '2':
    hero = {'HP':123,'AP':12,'Class':'Wizard'} 

if Choose_Character == '3':
    hero = {'HP':123,'AP':12,'Class':'Elf'} 

print(f"Here are your {hero['Class']} stats:\nHit Points: {str(hero['HP'])} \nMagic Points: {str(hero['AP'])}")



print('\n')


#Monster List
monster1 = {'HP':123,'AP':25, 'Name': 'Fox'}
monster2 = {'HP':123,'AP':12, 'Name': 'Orc'}
monster3 = {'HP':123,'AP':12, 'Name': 'Mage'}
monster4 = {'HP':123,'AP':12, 'Name': 'Deranged_druid'}


#Start of quest
intro =(f'''After a long journey you find your self at a small village.You are thirsty so you decide
to get a drink at the local pub. As you enter you notice the Townspeople seem scared and nervous.
As you order your drink you ask the bar keep why people are so scared. He tells you of a ancient Dungeon
in the local forest that harbors strange monsters and a Dragon who terrorizes the Townspeople.
Legend has it that the Dragon hoards a treasure of gold and precious gems and metals. Being the
brave {hero['Class']} that you are you tell the Townspeople you will rid them of this Dragon and
split the treasure with the community!''')

slow_scroll(intro)


print('\n')
time.sleep(1.5)

#dungeon entrance
Dungeon_Entrance =('''As you enter the ancient Dungeon you notice two doors in front of you.
Which door will you enter?: 1 or 2\n''')

print(Dungeon_Entrance)


Dungeon_Entrance = input()


if Dungeon_Entrance == '1':
  boobyTrap = (f'''As you open the door and enter the room, a poison dart shoots from the wall.
You have been hit!You loose 10 hit points.\nYou now have {hero['HP']-10} hit points.''')
  slow_scroll(boobyTrap)
elif Dungeon_Entrance == '2':
  print(f"You encounter a {monster1['Name']}")
  dice_roll = 5
  M_Attack = random.randint(1,11)
  if M_Attack < dice_roll:
    print(f"The {monster1['Name']} attacks you causing you to loose 25 HP")
    hero['HP'] = hero['HP'] - 25
    print(f"You now have {hero['HP']} hit points.")
  elif M_Attack > dice_roll:
    print('You slash at the fox and kill him.')


time.sleep(2)
print()
print()

 
slow_scroll('''As you continue your journey down a dark corridor you see a entracne to a large temple room.
You enter and notice a large shrine straight ahead of you dedicated to the Dragon God Zantar!To the right,
you see a large bowl full of gold, and rare gems! You also notice the Dragon God Zantar holding a extremly
large diamond.''')

print('\n')
time.sleep(1.5)


temple_room = input('Do you take the large Diamond from the Dragon, or grab the bowl full of gold?:(1 for Diamond, 2 for Gold)')


print('\n')

for temple in temple_room:
  if temple_room == '1':
    slow_scroll('As you grab the diamond a secret door opens up behind the dragon leading into a secret chamber!')
  elif temple_room == '2':
    slow_scroll('''As you grab the gold you fall through a trap door and into a pit full of snakes. 
unfortunately your journey ends here!''')
    print('Thanks for playing!')
    exit()
    
  
      
print('\n')

secret_room = ('''once inside the secret chamber you notice some writing on the wall,
It looks some type of riddle.''')

slow_scroll(secret_room)

print('\n')


count = 0
while count < 3:
    guess = input('What goes through a door but never goes in or comes out?')
    answer = 'a keyhole'
    if guess == answer:
        print('A hiden door slides open and reveals the Dragon Treaure room!')
        break
    else:
        print('Wrong, try again.')
        count += 1
else:
        print('No more attemps!Your game is over...')
              
              
print('\n')


slow_scroll('You enter the treaure room and the Dragon Zantar is waiting for your arrival....')
slow_scroll('\nIf you defeat the Dragon you get the treaure, otherwise,well you know what happens...')

print('\n')


diceRoll = 6

# if 1 the game still in progress. if 0 it ended
gameStatus = 1 # will check game status. For while loop


while gameStatus:
    hero_attack = random.randint(1,10) # inside loop, because it makes more sense to get a new value each time.
    
    if hero_attack > diceRoll:
        monster4['HP'] = monster4['HP']-hero['AP']  # Attack dmage ['AP'] from source            
        print(f'''You slash at the Dragon and hurt him. The Dragon has {monster4['HP']} hit points left''')
        print(monster4["HP"])

    if hero_attack < diceRoll:
        hero['HP'] = hero['HP']-monster4['AP']  # Attack dmage ['AP'] from source
        print(f'''The Dragon claws at you and hurts you badly,you now have {hero['HP']} hit points.''')
         
         
    gameStatus = (monster4['HP']>=0 and hero['HP']>=0) and 1 or 0

    



if monster4['HP']<0:
        slow_scroll('You slayed the Dragon!You return to the Townspeople and share the Dragon\'s treaure!You are a true hero!')
elif hero['HP']<0:
        slow_scroll('The Dragon eat\'s you and you are never to be heard of again...')

        
    

