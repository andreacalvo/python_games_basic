'''
Created on 8 de mar. de 2017

@author: andre_000
'''
########################################
# guess_number
# 06/03/2017
# 0.001 basic app working
# Generate a random list 1-6

########################################
'''
list_random=[]
cont_random = 4
from random import randint

for num_random in range(4):
    
        num_random = (randint(1,6))
        list_random.append(num_random)
        
print list_random
'''
########################################
# guess_number
# 06/03/2017
# 0.001 basic app working
# The user chooses their list with 4 numbers (1-6)

########################################
'''
list_random=[]
cont_random = 4
from random import randint

for num_random in range(4):
    
        num_random = (randint(1,6))
        list_random.append(num_random)
        
print list_random

list_chosen = []


for number_chosen in range (4):
    numbers_chosen = raw_input("Choose a number")
    list_chosen.append(numbers_chosen)
print list_chosen

'''
########################################
# guess_number
# 06/03/2017
# 0.001 basic app working
# game

########################################
'''
list_random=[]
cont_random = 4
from random import randint

for num_random in range(4):
    
        num_random = (randint(1,6))
        list_random.append(num_random)
        
print list_random


cont_game = 8
while cont_game != 0:
    cont_game -= 1
    list_chosen = []
    print "Yoy've got %i chances" %cont_game
    
    for number_chosen in range (4):
        numbers_chosen = int(raw_input("Choose a number : "))
        if 0<numbers_chosen <7:
            list_chosen.append(numbers_chosen)
        else:
            print "You must chose numbers between 1 and 6"
            break
    print list_chosen
    
    
    num_cont = 0
    num_pos = 0
    cont_wrong_num = 0
    cont = 0
    for number_r in list_random:
        for number_c in list_chosen: 
            if number_r == number_c and num_cont<5:
                num_cont+=1         
                break    
         
    
    for pos in range(len(list_chosen)):
        if list_random[pos] == list_chosen[pos]:
            num_pos+=1
    #         print list_chosen.index(number_r)    
    if cont_game == 0:
        print "You lost"
    if numbers_chosen == num_random:
        print "You won!"
        break
                     
    print "%i correct numbers and %i correct position"%(num_cont,num_pos)
    
'''
########################################
# guess_number
# 06/03/2017
# 0.001 basic app working
# function

########################################
'''
from random import randint

def num_random():
    global list_random
    global num_random
    list_random=[]
    
    for num_random in range(4):
        num_random = (randint(1,6))
        list_random.append(num_random)
            
    print list_random

def number_chosen():
    global list_chosen 
    global numbers_chosen
    list_chosen = []
        
    for number_chosen in range (4):
        numbers_chosen = int(raw_input("Choose a number : "))
        if 0<numbers_chosen <7:
            list_chosen.append(numbers_chosen)
        else:
            print "You must chose numbers between 1 and 6"
            break
    print list_chosen
    return numbers_chosen

def game():
        
    global list_random
    global numbers_chosen
    global list_chosen
    num_cont = 0
    num_pos = 0  
    cont_game = 8
    
    num_random()
    
    
    while cont_game != 0:
        number_chosen()
        cont_game -= 1
        num_cont = 0
        num_pos = 0
         
        
       
        for number_r in list_random:
            for number_c in list_chosen: 
                if number_r == number_c:
                    num_cont+=1       
                   
                    break    
             
        
        for pos in range(len(list_chosen)):
            if list_random[pos] == list_chosen[pos]:
                num_pos+=1
         
        if cont_game == 0:
            print "You lost"
            break
        if num_pos == 4:
            print "You won!"
            break
        print "Yoy've got %i chances" %cont_game     
        print "%i correct numbers and %i correct position"%(num_cont,num_pos)
        
game()
'''
########################################
# guess_number
# 06/03/2017
# 0.001 basic app working
# class guess_numbers

########################################
from random import randint
class GuessNumbersTask2():
    
     
    def __init__ (self):
         
        self.list_random = []
         
        self.list_random = []
         
        self.list_chosen = []
    
    def numRandom(self):
         
         
        
        for num_random in range(4):
            num_random = (randint(1,6))
            self.list_random.append(num_random)
                
        print self.list_random
    
    def numberChosen(self):
       
        self.list_chosen = []
        # maybe use number _chosen   
        for numbers_chosen in range (4):
            numbers_chosen = int(raw_input("Choose a number : "))
            if 0<numbers_chosen <7:
                self.list_chosen.append(numbers_chosen)
            else:
                print "You must chose numbers between 1 and 6"
                break
        print self.list_chosen
        return numbers_chosen
    
    def gamePlay(self):
            
        
        num_cont = 0
        num_pos = 0  
        cont_game = 8
        
        self.numRandom()
        
        
        while cont_game != 0:
            self.numberChosen()
            cont_game -= 1
            num_cont = 0
            num_pos = 0
             
            
           
            for number_r in self.list_random:
                for number_c in self.list_chosen: 
                    if number_r == number_c:
                        num_cont+=1       
                       
                        break    
                 
            
            for pos in range(len(self.list_chosen)):
                if self.list_random[pos] == self.list_chosen[pos]:
                    num_pos+=1
             
            if cont_game == 0:
                print "You lost"
                break
            if num_pos == 4:
                print "You won!"
                break
            print "Yoy've got %i chances" %cont_game     
            print "%i correct numbers and %i correct position"%(num_cont,num_pos)

gn = GuessNumbersTask2() 
gn.gamePlay()    




