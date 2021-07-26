# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:46:06 2021

@author: Pimchanok Duang-In 640631125
"""

name = input('What is your name: ')
print('There are 20 sticks in the pile')
total_pile = 20
i = 1
player1 = True
player2 = True
while total_pile > 0:
    if player1 == True:
        if total_pile == 1:
            pick = 1
            print('I, smart computer, takes the last stick.')
            break
        elif total_pile%3 == 0:
            pick = 2
            print('I take %d stick, there are %d sticks in the pile.' %(pick,total_pile-pick))
        elif total_pile == 2:
            pick = 1
            print('I take %d stick, there are %d sticks in the pile.' %(pick,total_pile-pick))
        else:
            import random
            pick = random.randint(1,2)
            print('I take %d stick, there are %d sticks in the pile.' %(pick,total_pile-pick))
        total_pile = total_pile - pick
    player1 = not player1
        
    if player2 == True:
        pick = int(input('How many you will take (1 or 2): '))
        if 0 < pick <= 2:
            if total_pile - pick < 0:
                print('There are no enough sticks to take')
            else:
                if total_pile == 1:
                    print('You take the last stick,')
                    break
                else:
                    print('There are %d sticks in the pile' %(total_pile-pick))
                    print()
                total_pile = total_pile - pick
        elif pick > 2:
            print('No you cannot take more than 2 sticks!')
        elif pick < 1:
            print('No you cannot take more less than 1 sticks!')
    player2 = not player2
    i = i + 1

if player1 == False:
    print('I WON (Python WON)')
else:
    print('%s win (I, smart computer, am sad T_T)' %name)