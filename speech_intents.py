from neuralintents import GenericAssistant
import os
from speech_functions import *

def speech():

    # mappings is a dictionary that links the intent mappings
    # with their respective functions to initiate the right
    # function for the users need according to jay's training 

    mappings = {"task": return_ctrl}

    # linking the intent file to the trainer
    # so that the intent files can be changed
    # to model files so that jay can use it
    # to understand and respond

    global speech_assistant
    speech_assistant = GenericAssistant('neural2_speech.json', intent_methods = mappings ,model_name = "models/speech/speech_model")

    # starting to read all data in the intent file and 
    # training according to that data and saves it to
    # the specified directory

    speech_assistant.train_model()
    speech_assistant.save_model()

    # clears the terminal after the trainer finishes

    os.system("clear")

# this function initiates a user prompt so that
# the user can enter the request they want

def speech_requesting(request_cmd):
    speech_assistant.request(request_cmd)