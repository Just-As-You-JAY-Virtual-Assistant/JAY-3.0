from neuralintents import GenericAssistant
import os
from speech_functions import *

def speech():

    mappings = {"task": return_ctrl}


    # directing the nervous system to the brain
    global speech_assistant
    speech_assistant = GenericAssistant('neural2_speech.json', intent_methods = mappings ,model_name = "models/speech/speech_model")

    # starting to read all data in the intent file and training according to that data
    speech_assistant.train_model()
    speech_assistant.save_model()
    os.system("clear")

def speech_requesting(request_cmd):
    speech_assistant.request(request_cmd)