'''
Created on 2 de mar. de 2017

@author: andre_000
'''
########################################
# hangman
# 02/03/2017
# 0.001 basic app working
########################################

# def ask_film():
#     frase=(raw_input("Choose a film "))
#     len_frase = len(frase)
#     board = []
#    
#     for a in range(len_frase):
#         a = "_" #* len_frase
#         board.append(a)
#     print " ".join(board)
# 
#    
#     cont = 11
#     while cont>=0:  
#         letter = str(raw_input("Choose a letter ")) 
#         print "You've got %d chances" %cont
#         
#         for letter_pos in range (0, len(frase)):
#             if frase[letter_pos] == letter :
#                 board[letter_pos] = letter 
#                 print " ".join(board)
#         
#         if cont == 0:
#             print "You lost!"
#         cont = cont-1
    
# ask_film()

########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Check if the user won
########################################
'''
def ask_film_task1():
    frase=(raw_input("Choose a film "))
    len_frase = len(frase)
    board = []
    cont2=1
    for a in range(len_frase):
        a = "_" #* len_frase
        board.append(a)
        cont2= len_frase
    print " ".join(board)     
    cont = 11
    while cont>=0:  
        letter = str(raw_input("Choose a letter ")) 
        print "You've got %d chances" %cont
        
        
        for letter_pos in range (0, len(frase)):
            if frase[letter_pos] == letter :
               
                board[letter_pos] = letter 
                print " ".join(board)
                cont2 = cont2 - 1
        if cont == 0:
            print "You lost!"
        cont = cont-1
        if cont2 ==0:
            print "You win!"
        
ask_film_task1()
'''


########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Check the film only has letters and numbers
########################################

#def special_match(strg, search = re.compile(r'[^a-z0-9.]').search):
#   return not bool(search(strg))
#     
#special_match(raw_input("Choose a film ")
 
'''              
a = "hola"    

for i in range(len(a)): 
    if  123<ord(a[i])>96 or 58<ord(a[i])>47:
        print a
 
'''     
'''         
def ask_film_task1():
    global frase
    frase=(raw_input("Choose a film "))
    len_frase = len(frase)
    board = []
    cont2=1  
    #frase.split()     
    for a in range(len_frase):
        if 123<ord(frase[a])>96 or 58<ord(frase[a])>47:
            a = "_" #* len_frase
            board.append(a)
            cont2= len_frase
        else:
            print"Only numbers and letters!"
            quit()
    print " ".join(board)     
    cont = 11
     while cont>=0:  
        letter = str(raw_input("Choose a letter "))
        if 123<ord(letter)>96 or 58<ord(letter)>47: 
            for letter_pos in range (0, len(frase)):
            
                if frase[letter_pos] == letter() :
                
                    board[letter_pos] = letter 
                    print " ".join(board)
                    cont2 = cont2 - 1
            
        else:
            print("Only numbers and letters!")
        print "You've got %d chances" %cont     
            
        if cont == 0:
            print "You lost!"
        cont = cont-1
        if cont2 ==0:
            print "You win!"
            quit()
        
        
ask_film_task1()
'''

########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Accept lowercase and capitalcase
########################################
 
'''   
def ask_film_task1():
    global frase
    frase=(raw_input("Choose a film "))
    frase=frase.lower()
    len_frase = len(frase)
    board = []
    cont2=1  
    #frase.split()     
    for a in range(len_frase):
        if 123<ord(frase[a])>96 or 58<ord(frase[a])>47:
            a = "_" #* len_frase
            board.append(a)
            cont2= len_frase
        else:
            print"Only numbers and letters!"
            quit()
    print " ".join(board)     
    cont = 11
   while cont>=0:  
        letter = str(raw_input("Choose a letter "))
        if 123<ord(letter)>96 or 58<ord(letter)>47: 
            for letter_pos in range (0, len(frase)):
            
                if frase[letter_pos] == letter.lower() :
                
                    board[letter_pos] = letter 
                    print " ".join(board)
                    cont2 = cont2 - 1
            
        else:
            print("Only numbers and letters!")
        print "You've got %d chances" %cont
             
           
        if cont == 0:
            print "You lost!"
        cont = cont-1
        if cont2 ==0:
            print "You win!"
            quit()
        
        
ask_film_task1()
'''  
########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Check repeated letters
########################################
'''
def ask_film_task1():
    frase=(raw_input("Choose a film "))
    len_frase = len(frase)
    board = []
    cont2=1
    for a in range(len_frase):
        a = "_" #* len_frase
        board.append(a)
        cont2= len_frase
    print " ".join(board)     
    cont = 11
    while cont>=0:  
        ask_letter()
        
        letter_alpha_num(letter)
        for letter_pos in range (0, len(frase)):
            if frase[letter_pos] == letter.lower() and board[letter_pos]=="_" :
                board[letter_pos] = letter
                print " ".join(board)
                cont2 = cont2 - 1
            elif  board[letter_pos]!="_" and frase[letter_pos] == letter.lower():
                print("Yoe've alredy choosen that one")
        print "You've got %d chances" %cont       
        if cont == 0:
            print "You lost!"
        cont = cont-1
        if cont2 ==0:
            print "You win!"
            quit()
ask_film_task1()
'''
########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Make different functions

########################################
 
'''  
def ask_film_task1():
    
    global frase
    global board
    global len_frase
    frase=(raw_input("Choose a film "))
    frase=frase.lower()
    len_frase = len(frase)
    board = []
    
    film_alpha_num(frase)
    
      
    
def ask_letter():
   
    global frase 
    global board
    global len_frase
    global letter    
    
    letter = str(raw_input("Choose a letter "))
    
    
    
    
def win_lose_11():
    
    global frase
    global board
    global len_frase
    global letter
    cont2=len_frase 
    cont = 11
    
    while cont>=0:  
        ask_letter()
        
        letter_alpha_num(letter)
        for letter_pos in range (0, len(frase)):
            if frase[letter_pos] == letter.lower() and board[letter_pos]=="_" :
                board[letter_pos] = letter
                print " ".join(board)
                cont2 = cont2 - 1
            elif  board[letter_pos]!="_" and frase[letter_pos] == letter.lower():
                print("Yoe've alredy choosen that one")
        print "You've got %d chances" %cont       
        if cont == 0:
            print "You lost!"
        cont = cont-1
        if cont2 ==0:
            print "You win!"
            quit()

def film_alpha_num(film):
    #### the film only with num and letters####
    global frase 
    global board
    global len_frase
    global cont2
    
    for a in range(len_frase):
        if 123<ord(film[a])>96 or 58<ord(film[a])>47:
            a = "_" #* len_frase
            board.append(a)
            cont2= len_frase
        else:
            print"Only numbers and letters!"
            quit()
    print " ".join(board)

def letter_alpha_num(letra):
    #### the letra only nums or letters####   
    global cont2
    if 123<ord(letra)>96 or 58<ord(letra)>47:
        #print ord('a')
        pass
    else:
        print"Only numbers and letters!"
        

 
        
 
#print letter_alpha_num('b')

ask_film_task1()
win_lose_11()
'''
########################################
# hangman
# 03/03/2017
# 0.001 basic app working
# Make a class

########################################

class HangmanTask1():  
   
    def __init__ (self, frase):
        self.frase = frase
        self.board = []
        #self.letter= ''
        self.len_frase = 0
    
    def askFilmTask1(self, user_film=str(raw_input("Choose a film "))):
        self.frase = user_film.lower()
        self.len_frase = len(self.frase)
  
        
        self.filmAlphaNum(self.frase)
        """ 
        Description : Ask user to insert a film
        Params IN   :    user_film = film desired by user                
        Params OUT  : None
        """   
        
          
        
    def askLetter(self):
        #comprobar solo una letra
        return str(raw_input("Choose a letter "))
          """ 
        Description : Ask user to insert a letter
        Params IN   :    film = film desired by user
        Params OUT  : None
        """   
        
    def winLose11(self):
          """ 
        Description : 11 chances to find out the film            
        Params IN   :    letter = letter disired by user
        Params OUT  : None
        """   
                
        cont2 = self.len_frase 
        cont  = 11
        
        while cont>=0:  
            letter = self.askLetter()
            
            self.letterAlphaNum(letter)
            for letter_pos in range (0, self.len_frase):
                if self.frase[letter_pos] == letter.lower() :
                    self.board[letter_pos] = letter
                    print " ".join(self.board)
                    cont2 = cont2 - 1
            print "You've got %d chances" %cont       
            if cont == 0:
                print "You lost!"
            cont = cont-1
            if cont2 ==0:
                print "You win!"
                quit()
    
    def filmAlphaNum(self, film):
        """ 
        Description : Only let the user insert a film with
                      numbers and letters. Print board.
        Params IN   :    film = film desired by user
                         blas = asdasd
        Params OUT  : None
        """     
        
        for a in range(self.len_frase):
            if ord('z') < ord(film[a]) > ord('a') or ord('9')<ord(film[a])>ord('0'):
                a = "_" #* len_frase
                self.board.append(a)
                
            else:
                print"Only numbers and letters!"
                quit()
        print " ".join(self.board)
    
    def letterAlphaNum(self, letra):
          """ 
        Description : Only let the user insert numbers and letters 
        Params IN   :    letra = letra desired by user
        Params OUT  : None
        """   
        #### the letra only nums or letters####   
         
        if 123<ord(letra)>96 or 58<ord(letra)>47:
            #print ord('a')
            pass
        else:
            print"Only numbers and letters!"
    
#     def isAlpha(self, letter):
#         
#     def isNumber(self, letter):        
 
hm = HangmanTask1('lacasa') 
hm.askFilmTask1()
hm.winLose11()
'''     

        
        
        
        
        
        
        
        
        
        
        
        
        