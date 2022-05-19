from static_impulses import jay
import basic_functions
import main_intents as MI

def return_ctrl():
    jay("So what shall we do today")
    while not basic_functions.exit_system:
        if basic_functions.exit_system == True:
            exit()
        else:
            try:
                message_main = input("[\o_o/]: ")
                MI.main_requesting(message_main)
            except:
                jay("sorry sir something went wrong, try again")
