from ast import While
import datetime
import time
import os
import warnings
warnings.catch_warnings()
warnings.simplefilter("ignore")
from static_impulses import *
import speech_intents as SI

# this varibale is called in the neural_network and
# is false if the reboot function is not called
# and true if the reboot function called

reboot_key = False

# this function feeds data from the about_jay dictonary
# and concatinates it into a message that describes a simple
# message about jay

def about():
    jay("My name is " + about_jay["name"] + " and I am " + about_jay["age"] + ", I was created to " + about_jay["use"])


# triggers a greeting response for jay according to the time of the day
# calls the timecheck function to check for the time and passes the 
# appropriate parameters for the timecheck fuction

def greet():
    greet_speech = "Always a pleasure to see you sir"
    timecheck(greet_speech + ", Good Morning", 
            greet_speech + ", Good Evening", 
            greet_speech + ", Good Evening")

# this function makes sure the system breaks the loop and
# the try catch block doesn't catch the error it main job
# to make sure the exit system variable called in the 
# neural_network is true and its additional tasks are
# cleaning out temporary files like the session and
# decrypt file

def bye():
    global exit_system
    exit_system = True
    files = open("logs/decrypt.txt", "w")
    files.write("Decrypted message has been deleted! {o_o}")
    timecheck("Have a great day sir", "Have a good evening sir", "Have a good night sir")
    files = open("session.txt", "w")
    files.write("")


# this function gives a simple reply to a conversation starter
# and initiates the speech_intents to accept input and reply
# acording to the model from neural2_speech

def convo():
    jay("I am fine, how are you today?")
    while not exit_system:
        try:
            speech_mes = input("[\o_o/]: ")
            SI.speech_requesting(speech_mes)
        except:
            jay("Sorry sir, i can't reply to that can you explain in another way!")

# simple response for gratitude inputs to the program

def gratitude():
    jay("No problem sir happy to help")


# calls the task_checker function and checks if the user
# wants music or not if the reply is yes opens music 
# and gives a message if not just gives a message 
def study():
    jay("Do you want any music while studying?")
    task_checker("Setting up your study session", "chill lofi")
    openbrowser("https://docs.google.com/")
    jay("Have a nice study session sir.")

# this function calls the env_check functions and checks
# the work type "programming" or "networking" and if programming
# opens the las vs code session and if networking opens
# packet tracer and also checks if the user wants music or not

def work():
    jay("Setting up workstation")
    jay("Will you be working on programming or networking")
    env_check()

# this function checks if the user wants simple movies or series movies
# and uses hdtoday.tv to display the most recent movies and series movies
# according to hdtoday.tv

def movies():
    type = input("||-JAY-|| => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        openbrowser(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        openbrowser(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    else:
        jay("Didn't understand that sir!")
        movies()

# this function use the jayyt function from the static_impulses
# module to open the video title the user inputs on youtube
def music():
    jay("What shall i play for you sir")
    title = input("||NIGUS||: ")
    if title.lower() == "cancel":
        pass
    else:
        jayyt(title)

# this function asks the user to input waht the user wants to search for
# and opens a new tab and searches for what the user inputs and checks
# if the user wants to search for something else or whether the user 
# wants to quit the search

def search():
    def search_check():
            confirm_search = input("||-CONFIRMATION-||: ")
            if "yes" in confirm_search:
                search()
            elif "no" in confirm_search:
                pass
            else:
                error()
                search_check()

    jay("What do you want to search for sir?")
    searchtitle = input("||-SEARCH-|| =>  ")
    if searchtitle.lower() == "cancel":
        pass
    else:
        jay("Searching...")
        jay("Here are the search results sir")
        googlesearch(searchtitle)
        jay("Do you want to search for something else")
        search_check()


# intiates a search for a person using the wiki module and
# also asks if the user wants detail or not if not prints
# out a summary of that person and if there is no summary asks
# if the user wants to do a google search and also does a 
# google search if the user wants details and in addition
# checks if the user wants another search or not

def people_search():
    def people_search_check():
        def check_loop():
            jay(f"Can't find {name} sir do you want to do a google search")
            error = input("||-CONFIRMATION-|| => ")
            if "yes" in error:
                googlesearch(name)
                people_search_recheck()
            elif "no" in error:
                people_search_recheck()
            else:
                check_loop()
        if "yes" in reply:
            googlesearch(name)
            print("")
            people_search()
        elif "no" in reply:
            try:
                import wikipedia
                jay("searching pls wait a moment sir...")
                print(wikipedia.summary(name))
                people_search_recheck()
            except:
                check_loop()
        else:
            error()
            people_search_check()
    def people_search_recheck():
        jay("Do you need to look for someone else?")
        recheck = input("||-CONFIRMATION-|| => : ")
        if "no" in recheck:
            pass
        elif "yes" in recheck:
            people_search()
        else:
            error()
            people_search_recheck()
    value = 0
    jay("Please enter the full name of the person your looking for")
    name = input("||-NAME-|| => ")
    for i in ["cancel", "stop", "leave it", "leave"]:
        if i in name:
            value+=1
    if value > 0:
        pass
    else:
        jay("Do you need details")
        reply = input("||-CONFIRMATION-|| => : ")
        people_search_check()

# takes a word as input from the user and retrieves the words from
# the json file and checks the key with the input if it finds
# a match it prints out the value of that key and if the users
# input isn't found but if there are close matches the functions
# prints close matching words and asks the user if its one of them
# then the user inputs the specified word and the functions outputs
# the value for that key and finally asks if the user wants to do
# another dictionary search

def dictionary():
    import json
    from difflib import get_close_matches
    def check():
        jay("Do you want to search for another word sir?")
        reply = input("||-CONFIRMATION-|| => ")
        if "yes" in reply:
            dictionary()
        else:
            pass
    words_data = json.load(open("words.json"))
    jay("Please enter a word sir")
    word = input("||-SEARCH KEY-|| => ")

    word = word.lower()
    if word in words_data or word.title() in words_data or word.upper() in words_data:
            res = words_data[word][0]
            jay(f"{str(res)}\n")
            check()
    elif len(get_close_matches(word, words_data.keys())) >0:
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        jay("Did you mean %s instead: " % similar_words_list)
        ans = input("||-CONFIRMATION-|| => ")
        if "no" in ans:
            jay("Sorry, I don't understand you!!!!")
            check()
        else:
            jay(words_data[ans][0] + "\n")
            check()
                
    else:
        jay("I can't find the word sir please double check it!!!")
        check()

# uses the time module to check for the time and formats
# it in hour and minute and prints it out

def timefun():
    jay("The time is " + time.strftime('%l:%M'))

# this function checks where the user is if the user is at home
# simply pings the home networks gateway and if the ping is
# succesful prints that the local connection is okay and
# goes on to ping the google dns server 8.8.8.8 and prints
# that the internet connection is safe

# if the user is not at home it follows the same step but
# the only difference is that the function takes in the 
# gateway of the network as an input from the user

def net():
    jay("Is it your home network, Sir?")
    net_mes = input("||-CONFIRMATION-|| =>  ")
    if "yes" in net_mes.lower():
        jay("Checking local network")
        net_local_res = (os.system("ping -c4 192.168.1.1"))
        if net_local_res == 0:
            jay("Local network is up and running")
            jay("Pinging Google servers")
            net_remote = (os.system("ping -c4 192.168.1.1"))
            if net_remote == 0:
                jay("Internet is up and running too sir")
            else:
                jay("There seems to be an Internet failure sir.")
        else:
            jay("There seems to be a network failure sir.")
    elif "no" in net_mes.lower():
        jay("Please input the gateway address of the network your on")
        ip = input("||-GATEWAY-|| => ")
        jay("Checking local network")
        net_res = (os.system(f"ping -c4 {ip}"))
        if net_res == 0:
            jay("Local network is up and running")
            jay("Pinging Google servers")
            net_remote = (os.system("ping -c4 8.8.8.8"))
            if net_remote == 0:
                jay("Internet is up and running too sir")
            else:
                jay("There seems to be an Internet failure sir.")
        else:
            jay("There seems to be a network failure sir.")
    else:
        error()
        net()
        
# opens a browser and opens the logged in users google
# calendar

def calendar():
    jay("Here is your google calendar....")
    openbrowser("https://calendar.google.com/calendar")

# use the protonvpn-cli vpn to connect to the fastest
# available connection

def secure():
    jay("Activating vpn please wait....")
    os.system("protonvpn-cli c -f")

# creates a session by writing to the session.txt file and
# changes the reboot_key value to true so that the neural network
# recieves the key and starts exiting the loop and running the
# file neural_network again

def reboot():
    files = open("logs/decrypt.txt", "w")
    files.write("Decrypted message has been deleted! {o_o}")
    files = open("session.txt", "w")
    files.write("")
    jay("rebooting system")
    global reboot_key
    reboot_key = True


# this function simply uses the linux built in
# ls function to list all files in the secure/log
# directory

def list_logs():
    while True:
        jay("do you need details on each file")
        option = input("| OPTION |: ")
        if option.lower() == "yes":
            jay("listing files with details")
            os.system("ls -ls logs/secure")
            break
        elif option == "no":
            jay("listing files")
            os.system("ls logs/secure")
            break
        elif option == "cancel":
            break
        else:
            jay("don't understand that command, please input yes or no or cancel")