import main_intents as MI
import security
import speech_intents as SI
from static_impulses import jay, timecheck
import basic_functions
import os
import nltk

if nltk:
    pass
else:
    nltk.download('omw-1.4')


# initiates the trainers for both intents
MI.main()
# SI.speech()

# stores the variable for the exit(bye) call as false
# and the variable is overwritten whenever the exit(bye)
#function is called

basic_functions.exit_system = False

# this function checks the value of exit_system and
# if exit(bye) function is called the loop will break
# or exit

# the function also checks if a rebbot call was made
# by checking the session.txt file if the file is empty
# it starts the normal boot else it starts as a reboot
# with a message for the user

# the function loops until the exit(bye) function is
# called while accepting a user command or input
# in every iteration and runs the intent request
# function as specified in the intents module

def engine():
    while not basic_functions.exit_system:
        if basic_functions.exit_system == True:
            exit()
        else:
            if basic_functions.reboot_key:
                files = open("session.txt", "w")
                files.write("session saved!")
                break
            message_main = input("[\o_o/]: ")
            MI.main_requesting(message_main)

def GUIEngine(msg):
    print(msg)
    MI.main_requesting(msg)

# this function compares the user inputs hash equivalent to the stored
# hash password and if the passwords match and the username matches
# the function executes the engine function and if not it exits
# with an error message

def starter(user, passwd):
    security.hasher(passwd)

    if user == "nigus" and security.hash == "c81871642fc40d074afe66e8f20ee1d135900e7ed4a0533a637f8236c3b460be":
        filess = open("session.txt", "a")
        files = open("session.txt", "r")
        if files.read() == "session saved!":
            jay("System reboot was successful and my intents are up to date")
            return True
        else:
            timecheck("Good Morning " + user, "Good Afternoon", "Good Evening")
            return True 
    else:
        jay("wrong credentials please try again")
        return False

# starter('nigus', 'tony stark') function call used for testing
# engine() # function call used for testing
# GUIEngine("hello") # function call used for testing
# checks if the reboot_key variable is flase or and
# if it's true it just passes it to another block

# if this block gets executed then the system first 
# changes the value of the reboot_key variable back
# to false and continues to run the movie

if basic_functions.reboot_key:
    basic_functions.reboot_key = False
    os.system("clear")
    os.system("python neural_network.py")