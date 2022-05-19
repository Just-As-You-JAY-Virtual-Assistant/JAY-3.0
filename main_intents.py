from neuralintents import GenericAssistant
from basic_functions import *
import logs.log_encryption as le
from angel_protocol import angel_protocol

def main():
    mappings = {"greet":greet, 
                "bye":bye, 
                "movies":movies, 
                "music":music, 
                "time":timefun, 
                "study":study, 
                "work":work,
                "search":search,
                "jokes":joke,
                "convo":convo,
                "network":net,
                "gartitude":gratitude,
                "about":about,
                "people":people_search,
                "calendar":calendar,
                "dictionary":dictionary,
                "error":error,
                "logger":le.encrypt_note,
                "delogger":le.decryption_check,
                "reboot":reboot,
                "angel_protocol":angel_protocol
                }


    # linking the intent file to the trainer
    global main_assistant
    main_assistant = GenericAssistant('neural1_main.json', intent_methods = mappings ,model_name = "models/main/main_model")

    # starting to read all data in the intent file and training according to that data
    main_assistant.train_model()
    main_assistant.save_model()
    os.system("clear")

def main_requesting(message):
    main_assistant.request(message)