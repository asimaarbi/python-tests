
import random
'''print('Hello World')


print('Halt !')
a=input('Who are you ?')
print(a,'You are allowed to pass')


b = [1,2,3,4,5,6,7,8,9,10]
secur_random = random.SystemRandom()

#First_name = input('First name :')
#Last_name = input('Last name :')

First_name = ( 'Shahid' )
Last_name = ( 'Ghafoor' )

print(First_name+Last_name)
print('Your Lucky num is :', secur_random.choice(b))



B = [1,2,3,4,5,6,7,8,9,10]
secur_random = random.SystemRandom()

a = input('enter your name : ')
a = a.capitalize()
print(a,",Your lucky num is :",secur_random.choice(B))

def ask():
    a=input('What is your name ?')
    
    if a == "shahid" :
        print('Welcome to bytehstaft')
    
    elif a == 'omer':
        print ('Welcomr to python')
    
    else :
        print('wrong input')
        ask()

ask()
'''

def ask():
    a = input("What is Your Name ?")
    a = a.lower()

    if a == "omer":
        print("Welcome to Python")

    elif a == "asim":
        print("Welcome to Byteshaft")
    else:
        print("Wrong input")
        ask()

ask()

