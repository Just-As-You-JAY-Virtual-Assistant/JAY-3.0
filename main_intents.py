from neuralintents import GenericAssistant
from basic_functions import *
import logs.log_encryption as le
from angel_protocol import angel_protocol

def main():

    # mappings is a dictionary that links the intent mappings
    # with their respective functions to initiate the right
    # function for the users need according to jay's training 

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
                "angel_protocol":angel_protocol,
                "secure":secure
                }

    # linking the intent file to the trainer
    # so that the intent files can be changed
    # to model files so that jay can use it
    # to understand and respond

    global main_assistant
    main_assistant = GenericAssistant('neural1_main.json', intent_methods = mappings ,model_name = "models/main/main_model")

    # starting to read all data in the intent file and 
    # training according to that data and saves it to
    # the specified directory

    main_assistant.train_model()
    main_assistant.save_model()

    # clears the terminal after the trainer finishes

    os.system("clear")

# this function initiates a user prompt so that
# the user can enter the request they want

def main_requesting(message):
    main_assistant.request(message)