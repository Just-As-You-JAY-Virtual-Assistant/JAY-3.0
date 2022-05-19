from static_impulses import jay
import basic_functions
import main_intents as MI

def return_ctrl():
    jay("just try to do something fun, and any time you want to talk i am here")
    while not basic_functions.exit_system:
        if basic_functions.exit_system == True:
            exit()
        else:
            try:
                message_main = input("[\o_o/]: ")
                MI.main_requesting(message_main)
            except:
                jay("sorry sir something went wrong, try again")

def sad_engine():
    jay("Are you ok sir, do you want to talk")

def sad_talk1():
    jay("I know sometimes things can be hard but, its okay to be sad about it")