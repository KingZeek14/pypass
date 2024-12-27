import os
import time
from passlib.hash import pbkdf2_sha256
import sys

# TODO add a remove function

def parser():
    try:
        if sys.argv[1] == '-s' or sys.argv[1] == '--start':
            login()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help' :
            help = open('help', 'r')
            print(help.read())
        elif sys.argv[1] == '-a' or sys.argv[1] == '--add':
            addUser()
    except IndexError:
        print('Error: I need a argument like: -s.')
    except KeyboardInterrupt:
        print('')
    
def login():
    attemps = 3
    while attemps > 0:
            try:

                with open('userfile', 'r') as file:
                    userFileVar = file.read()
                with open('passfile', 'r') as file:
                    userPassVar = file.read()
        
                usrLogin = input('Login>> ') # the varables for user and login
                usrPass = input('Password>> ') 
                salt = pbkdf2_sha256.hash(usrPass)
                verifysalt = pbkdf2_sha256.verify(usrPass, salt)

                if usrLogin in userFileVar and verifysalt == True:
                    time.sleep(1)
                    os.system('clear && echo Logged in on tty && tty && echo -------------&& echo And at && date')
                    break 

                elif usrLogin not in userFileVar and usrPass not in userPassVar:
                    print('Incorrect Username and/or Password')
                    attemps = attemps - 1
        
            except FileNotFoundError:
                print("Creating userfile and passfile...")
                open('userfile', 'x')
                open('passfile', 'x')  # if files dont exist make them
            except FileExistsError:
                print('')
                pass # if they exist skip 
            except KeyboardInterrupt:
                print('')
                break

def addUser():
    add = input('Enter a username>> ')
    addPass = input('Now enter a password>> ')
    print(f'Made user with name {add}!')
    saltAdd = pbkdf2_sha256.hash(addPass)

    with open('userfile', 'a') as file:
        file.write(add + '\n')
    with open('passfile', 'a') as file:
        file.write(saltAdd + '\n')
parser()



    









