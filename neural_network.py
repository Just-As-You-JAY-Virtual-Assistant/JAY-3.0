import main_intents as MI
import security
import speech_intents as SI
from static_impulses import jay, timecheck
import basic_functions
from getpass import getpass

MI.main()
SI.speech()
basic_functions.exit_system = False

def engine():
    while not basic_functions.exit_system:
        if basic_functions.exit_system == True:
            exit()
        else:
            try:
                message_main = input("[\o_o/]: ")
                MI.main_requesting(message_main)
            except:
                jay("sorry sir something went wrong, try again")

user = input("{USERNAME}: ")
passwd = getpass("{PASSWORD}: ")

security.hasher(passwd)

if user == "nigus" and security.hash == "c81871642fc40d074afe66e8f20ee1d135900e7ed4a0533a637f8236c3b460be":
    timecheck("Good Morning", "Good Afternoon", "Good Evening")
    engine()
else:
    jay("wrong credentials exiting system")
