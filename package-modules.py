'''
Created on 5 de dic. de 2016

@author: andre_000
'''
import dictionary

# Your code goes here
Jill_members = []
for member in dir(dictionary):
    if "Jill" in member:
       Jill_members.append(member)

print sorted(Jill_members)
def print_tic_tac():
    size = int(raw_input('Enter size of the board:\n'))
    for n in range(0, size):
        print ' ---' * size
        print '{}{}'.format(' |', ' |' *(2+size))
        
        print ' ---' * size
       
print_tic_tac()