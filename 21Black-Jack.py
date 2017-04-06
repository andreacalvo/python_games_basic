'''
Created on 2 de mar. de 2017

@author: andre_000
'''
'''
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
# Random Number
########################################

### CARTAS USER 
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier



########################################
########################################
# 09/03/2017
# 0.001 basic app working
# blacjack
# CARTAS CRUPIER
########################################

### CARTAS USER 
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier

### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA

while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"

'''
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  CARTAS USER  //PEDIR CARTA
########################################

### CARTAS USER 
'''
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier

### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA

while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"
### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS

sum_user=0
play = raw_input("Do you want to play? Y/N : ")
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ")
### PEDIR CARTA O NO
    if answer == 'Y':
        
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 
        #1 0 11
        
        
        for x in range(1):
            user_cards.append(card)   
            print "Your last card is : %d " %card 
        sum_user=0    
        for i in user_cards :
            sum_user = sum_user + i
        print "Your cards : " , user_cards
        print "Sum  your cards %d " %sum_user
       
 

        if card == 1:
            print"You've got an As "
            ask = raw_input ("Which value do you want for this card 1 or 11 : ")
            if ask =='1':
                card = 1
                print "1"
                print user_cards
                sum_user =sum_user - 1 
                print sum_user
            if ask== '11':
                print "11"
                card=11
                print user_cards
                sum_user =sum_user - 1 +11
                print sum_user
      
      
        if sum_user == 21:
            "You win!"
        if sum_user >1000:
            "You lose! "
    if answer == 'N':
        pass

### SI LA CARTA ES UN AS VALOR DE 1 O 11

    if card == 1:
        print"You've got an As "
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask =='1':
            card == 1
            print "1"
            print user_cards
            sum_user =sum_user - 1 
            print sum_user
        if ask== '11':
            print "11"
            card==11
            print user_cards
            sum_user =sum_user - 1 +11
            print sum_user
        for x in range(1):
            user_cards.append(card)  
         
### WIN OR LOSE
    for i in user_cards :
        sum_user = sum_user + i
    print "Suma user  %d " %sum_user
    if sum_user == 21:
        "You win!"
    if sum_user >21:
        "You lose! "
 
'''
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  CARTAS USER  //PEDIR CARTA
########################################

### CARTAS USER 
'''
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier

### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA

while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"
### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS

sum_user=0
play = raw_input("Do you want to play? Y/N : ")
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ")
### PEDIR CARTA O NO
    if answer == 'Y':
        
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 
        #1 0 11
        
        
        for x in range(1):
            user_cards.append(card)   
            print "Your last card is : %d " %card 
        sum_user=0    
        for i in user_cards :
            sum_user = sum_user + i
        print "Your cards : " , user_cards
        print "Sum your cards %d " %sum_user
'''        
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  CARTAS USER  //PEDIR CARTA
########################################

### CARTAS USER 
'''
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier
'''
### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA
'''
while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"
'''
### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS
'''
import random
sum_user=0
play = raw_input("Do you want to play? Y/N : ")
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ")
### PEDIR CARTA O NO
    if answer == 'Y':
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 

        for x in range(1):
            user_cards.append(card)   
            print "Your last card is : %d " %card 
    if card == 1:
        print"You've got an As "
   
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask =='1':
            pass
           
        if ask== '11':
            user_cards.pop()
            print "11"
            card = 11
            print user_cards
            for x in range(1):
                user_cards.append(card)  
            
    sum_user=0    
        
    for i in user_cards :
        sum_user = sum_user + i
    print "Your cards : " , user_cards
    print "Sum your cards %d " %sum_user
'''          
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  WIN//LOSE
########################################

### CARTAS USER 
'''
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier
'''
### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA
'''
while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"

### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS
import random
sum_user=0
play = raw_input("Do you want to play? Y/N : ")
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ")
### PEDIR CARTA O NO
    if answer == 'Y':
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 

        for x in range(1):
            user_cards.append(card)   
            print "Your last card is : %d " %card 
    if card == 1:
        print"You've got an As "
   
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask =='1':
            pass
           
        if ask== '11':
            user_cards.pop()
            print "11"
            card = 11
            print user_cards
            for x in range(1):
                user_cards.append(card)  
                
                
    sum_user=0    
    for i in user_cards :
        sum_user = sum_user + i
    if sum_user == 21:
        print "You win!"
        print sum_user
        break
    if sum_user >21:
        print "You lose, you've got more than 21! "
        print "You've got %d "%sum_user
        break
    print "Your cards : " , user_cards
    print "Sum your cards %d " %sum_user

########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  ALTERNAR CRUPIER Y USER
########################################

### CARTAS USER 

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER

sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier
'''
### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA
'''
while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card3 = random.choice(my_list)
    print "Card 3: %d" %card3
    if sum_crupier <11 and card3 == 1:
        card3 = 11
        print "Card 3 : %d"%card3
    
    for x in range(1):
        crupier_cards.append(card3)
    print crupier_cards
    sum_crupier=0
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    
    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"

### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS
import random
sum_user=0
play = raw_input("Do you want to play? Y/N : ").upper()
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ").upper()
    
### PEDIR CARTA O NO
    if answer == 'Y':
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 

        for x in range(1):
            user_cards.append(card)   
            print user_cards
            print "Your last card is : %d " %card 
    if card == 1:
        print"You've got an As "
   
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask == '1':
            print user_cards
            pass
        if ask== '11':
            user_cards.pop()
            print "11"
            card = 11
            user_cards.append(card) 
            print user_cards
        sum_user=0    
    for i in user_cards :
        sum_user = sum_user + i
    if sum_user == 21:
        print "You win!"
        print sum_user
        pass
    if sum_user >21:
        print "You lost, you've got more than 21! "
        print "You've got %d "%sum_user
        break
    print "Your cards : " , user_cards
    print "Sum your cards %d " %sum_user
    
if play =='Y':       
    pass       
'''   
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  ALTERNAR CRUPIER Y USER
########################################

### CARTAS USER 
'''
import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
card1 = random.choice(my_list)
card2 = random.choice(my_list)


user_cards = []
crupier_cards = []
 
for x in range(1):
    user_cards.append(card1)
    user_cards.append(card2)
print "Your cards : "
print user_cards

### CARTAS CRUPIER

import random
my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
card1 = random.choice(my_list)
card2 = random.choice(my_list)

for x in range(1):
    crupier_cards.append(card1)
    crupier_cards.append(card2)
  
print "Crupier's cards : "
print crupier_cards

### SUMA CARTAS CRUPIER
import random
user_cards = []
crupier_cards = []
sum_crupier=0
for i in crupier_cards :
    sum_crupier = sum_crupier + i
print "Suma crupier  %d " %sum_crupier

### CARTAS CRUPIER
### IF SUMA < 17 PEDIR CARTA

while sum_crupier <17:       
    
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card = random.choice(my_list)
    print "Last card's crupier : %d" %card
    if sum_crupier <11 and card == 1:
        print card
        card = 11
        print "Last card is an As the crupier chooses the value is 11: %d"%card
    
    for x in range(1):
        crupier_cards.append(card)
    print crupier_cards
    sum_crupier=0

    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Suma crupier  %d " %sum_crupier
    if card == '1':
            print user_cards
            pass


    if sum_crupier >=17:
       print "Crupier stops taking cards"
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier ==21:
        print "Crupier won"
    if card == '11':
        user_cards.pop()
        print "11"
        card = 11
        crupier_cards.append(card) 
        print crupier_cards

    

### CARTAS USER
### PREGUNTAR USUER SI QUIERE MAS CARTAS
import random
sum_user=0
play = raw_input("Do you want to play? Y/N : ").upper()
user_cards = [] 
while play =='Y':
### PREGUNTAR USER
    answer = raw_input("Do you want a card? Y/N : ").upper()
    
### PEDIR CARTA O NO
    if answer == 'Y':
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card = random.choice(my_list) 

        for x in range(1):
            user_cards.append(card)   
            print user_cards
            print "Your last card is : %d " %card 
    if card == 1:
        print"You've got an As "
   
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask == '1':
            print user_cards
            pass
        if ask== '11':
            user_cards.pop()
            print "11"
            card = 11
            user_cards.append(card) 
            print user_cards
        sum_user=0    
    for i in user_cards :
        sum_user = sum_user + i
    if sum_user == 21:
        print "You win!"
        print sum_user
        pass
    if sum_user >21:
        print "You lost, you've got more than 21! "
        print "You've got %d "%sum_user
        break
    print "Your cards : " , user_cards
    print "Sum your cards %d " %sum_user
    
if play =='Y':       
    pass       
               



########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  ALTERNAR CRUPIER Y USER
########################################

### CARTAS CRUPIER


### PREGUNTAR USER

   
    
### PEDIR CARTA O NO
import random
sum_user=0
sum_crupier = 0
cont = 0
play = raw_input("Do you want to play? Y/N : ").upper()
print "-"*8
user_cards = [] 
crupier_cards= []
while play =='Y':
    
################# --------- CRUPIER CARDS -------- #################

    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card_c = random.choice(my_list)
    #print "Card's crupier : %d" %card_c
    
                ######## SUMA CUPIER CARDS  #############
    #f#or i in crupier_cards :
       # sum_cupier = sum_crupier + i
        
        ####### 
    if cont >= 1:     
          
        print "-"*8
    cont = cont+1
    for x in range(1):
        crupier_cards.append(card_c)
        print "Crupier cards  :  " , crupier_cards 
        #yprint "Sum crupier", sum_crupier
    
        ############# CARD AS CRUPIER#########
     

    if sum_crupier <= 10 and card_c == 1:
        crupier_cards.pop()
        card_c = 11
        print "Last card is an As the crupier chooses the value is 11: %d"%card_c
        crupier_cards.append(card_c)
        print crupier_cards
    for i in crupier_cards :
        sum_crupier = sum_crupier + i
    print "Sum_crupier : %d" %sum_crupier
        
    
    if sum_crupier >=17:
        print "Crupier stops taking cards"
        print "You win"
        break
    if sum_crupier >22:
        print "Crupier lost"
    if sum_crupier == 21:
        print "Crupier wins"
################# ------- ASK USER FOR A CARD ------- ###############
    
        
    answer = raw_input("Do you want a card? Y/N : ").upper()
    if answer == 'Y':
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 4
        card_u = random.choice(my_list) 

        for x in range(1):
            user_cards.append(card_u)   
            
            #print "Your last card is : %d " %card_u
            print "User cards  :  " , user_cards
######  CARD  AS  USER#######
    if card_u == 1:
        print"You've got an As "
   
        ask = raw_input ("Which value do you want for this card 1 or 11 : ")
        if ask == '1':
            print user_cards
            pass
        if ask== '11':
            user_cards.pop()
            card_u = 11
            user_cards.append(card_u) 
            print user_cards
###### WIN / LOSE ######
    sum_user=0   
    sum_crupier = 0 
   

    for i in user_cards :
        sum_user = sum_user + i
    print "Sum_user : %d" %sum_user
        #print i,sum_user
        
    if sum_user == 21:
        print "You win!"
         
        break
    if sum_user >21:
        print "You lose, you've got more than 21! "
        print "You've got %d "%sum_user
        break
        
    
    
    
if play =='Y':       
    pass       
'''         
########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  MAKE DIFFERENT FUNCTIONS
########################################

## def ask_film_task1():

'''
global sum_user
global sum_crupier 
global cont
global user_cards 
global crupier_cards
global answer
sum_user=0
sum_crupier = 0
cont = 0      
user_cards = [] 
crupier_cards = []
answer = ""

### PEDIR CARTA O NO
def random_card():
    global sum_user
    global sum_crupier 
    global cont
    global user_cards 
    global crupier_cards
    global anwers 
    import random
    my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
    card = random.choice(my_list)
     
    return card    
#import random
def ask_card():
    global sum_user
    global sum_crupier 
    global cont
    global user_cards 
    global crupier_cards
    global anwers 
    
    answer = raw_input("Do you want a card? Y/N : ").upper()
    return answer
    

def sum_cards(cartas):
    global sum_user
    global sum_crupier 
    global cont
    global user_cards 
    global crupier_cards
    global anwers 
    suma = 0
    for i in cartas :
        suma= suma + i
    return suma
    
 
def game():
    global sum_user
    global sum_crupier 
    global cont
    global user_cards 
    global crupier_cards
    global answer 
    play = raw_input("Do you want to play? Y/N : ").upper()
    
    while play =='Y':
        print "-"*8
        answer=ask_card()
        if answer == 'Y':
            card_u = random_card()
            for x in range(1):
                user_cards.append(card_u)
            print "User cards  :  ", user_cards
            if card_u == 1:
                print"You've got an As "
           
                ask = raw_input ("Which value do you want for this card 1 or 11 : ")
                if ask == '1':
                    print user_cards
                    pass
                if ask== '11':
                    user_cards.pop()
                    card_u = 11
                    user_cards.append(card_u) 
                    print user_cards   
            sum_user = sum_cards(user_cards)
            print "Sum user cards  :  ", sum_user
            if sum_user >22:
                print "You lose"
            if sum_user == 21:
                print "You win"
                break
            
    
            
                ######### -- CRUPIER CARDS -- ############
                
            card_c = random_card()
            
            for x in range(1):
                crupier_cards.append(card_c)   
            print "Crupier cards  :  " ,crupier_cards
            if sum_crupier <= 10 and card_c == 1:
                crupier_cards.pop()
                card_c = 11
                print "Last card is an As the crupier chooses the value is 11: %d"%card_c
                crupier_cards.append(card_c)
                print crupier_cards
            sum_crupier = sum_cards(crupier_cards)
            print "Sum crupier cards  :  ", sum_crupier
            if sum_crupier >22:
                print "Crupier lose"
            
            
            if sum_crupier >=17:
                if sum_crupier == 21:
                    print "Crupier wins"
                    break
                else:
                    print "Crupier stops taking cards"
                    print "You win"
                    break
           
        if play =='Y':       
            pass
    
       
    
       
game()
'''

########################################
########################################
# guess_number
# 09/03/2017
# 0.001 basic app working
# blacjack
#  MAKE A CLASS
########################################

## def ask_film_task1():

 

 
class BlackJackTask3():  
   
    def __init__ (self):
             
             
        self.sum_user = 0
        self.sum_crupier =0
        self.cont = 0
        #self.user_cards = []
        #self.crupier_cards =[]
        self.answer = ""
      
      
    
    def randomCard(self):
        import random
        self.answer
        my_list = [1] * 4 + [2] * 4 + [3] * 4+ [4] * 4+ [5] * 4+ [6] * 4+[7] * 4+ [8] * 4+ [9] * 4+ [10] * 5
        card = random.choice(my_list)
         
        return card    
    
    
    def askCard(self):
        
        self.anwers = ""
        self.answer = raw_input("Do you want a card? Y/N : ").upper()
        return self.answer
        
    
    def sumCards(self,cartas):
         
        suma = 0
        for i in cartas :
            suma= suma + i
        return suma
        
     
    def game(self):
         
        play = raw_input("Do you want to play? Y/N : ").upper()
        user_cards = []
        crupier_cards =[]
        
        while play =='Y':
            print "-"*8
            self.answer= self.askCard()
            if self.answer == 'Y':
                card_u = self.randomCard()
                for x in range(1):
                    user_cards.append(card_u)
                print "User cards  :  ", user_cards
                if card_u == 1:
                    print"You've got an As "
               
                    ask = raw_input ("Which value do you want for this card 1 or 11 : ")
                    if ask == '1':
                        print user_cards
                        pass
                    if ask== '11':
                        user_cards.pop()
                        card_u = 11
                        user_cards.append(card_u) 
                        print user_cards   
                
                self.sum_user = self.sumCards(user_cards)
                print "Sum user cards  :  ", self.sum_user
                if self.sum_user >22:
                    print "You lose"
                if self.sum_user == 21:
                    print "You win"
                    break
                
        
                
        ######### -- CRUPIER CARDS -- ############
                    
                card_c = self.randomCard()
                
                for x in range(1):
                    crupier_cards.append(card_c)   
                print "Crupier cards  :  " ,crupier_cards
                if self.sum_crupier <= 10 and card_c == 1:
                    crupier_cards.pop()
                    card_c = 11
                    print "Last card is an As the crupier chooses the value is 11: %d"%card_c
                    crupier_cards.append(card_c)
                    print crupier_cards
                self.sum_crupier = self.sumCards(crupier_cards)
                print "Sum crupier cards  :  ", self.sum_crupier
                if self.sum_crupier >22:
                    print "Crupier lose"
                
                
                if self.sum_crupier >=17:
                    if self.sum_crupier == 21:
                        print "Crupier wins"
                        break
                    else:
                        print "Crupier stops taking cards"
                        print "You win"
                        break
               
            if play =='Y':       
                pass
        
           
    
bj = BlackJackTask3()       
bj.game()