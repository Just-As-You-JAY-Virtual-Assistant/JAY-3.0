import datetime
import time
import os
import warnings
warnings.catch_warnings()
warnings.simplefilter("ignore")
from static_impulses import *
import speech_intents as SI

reboot_key = False

#nervous functions to execute specific tasks
def about():
    jay("My name is " + about_jay["name"] + " and I am " + about_jay["age"] + ", I was created to " + about_jay["use"])


#greeting function for intent response
def greet():
    greet_speech = "Always a pleasure to see you sir"
    timecheck(greet_speech + ", Good Morning", 
            greet_speech + ", Good Evening", 
            greet_speech + ", Good Evening")

#bye function for intent response   
def bye():
    global exit_system
    exit_system = True
    files = open("logs/decrypt.txt", "w")
    files.write("Decrypted message has been deleted! {o_o}")
    timecheck("Have a great day sir", "Have a good evening sir", "Have a good night sir")
    files = open("session.txt", "w")
    files.write("")


#conversation function for intent response
def convo():
    jay("I am fine, how are you today?")
    while not exit_system:
        try:
            speech_mes = input("[\o_o/]: ")
            SI.speech_requesting(speech_mes)
        except:
            jay("Sorry sir, i can't reply to that can you explain in another way!")

#gratitude function for intent response
def gratitude():
    jay("No problem sir happy to help")

#joke generartor function for intent response
def joke():
    import pyjokes
    jay(pyjokes.pyjokes.get_joke('en'))
    jay("ha ha ha")

#study session manager function for intent response
def study():
    jay("Do you want any music while studying?")
    task_checker("Opening your notebook", "chill lofi")
    openbrowser("https://docs.google.com/document/u/1/?tgif=d")
    jay("Have a nice study session sir.")

#work session manager function for intent response
def work():
    jay("Setting up workstation")
    jay("Will you be working on programming or networking")
    env_check("https://nigussolomon.atlassian.net/jira/your-work")

#movie manager function for intent response
def movies():
    type = input("||-JAY-|| => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        openbrowser(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        openbrowser(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    else:
        jay("Didn't understand that sir!")
        movies()

#yt music manager function for intent response
def music():
    jay("What shall i play for you sir")
    title = input("||NIGUS||: ")
    if title.lower() == "cancel":
        pass
    else:
        jayyt(title)

#google search function for intent response
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


#wiki or google search for people function for intent response
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

#dictionary function for intent response
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

#time teller function for intent response
def timefun():
    jay("The time is " + time.strftime('%l:%M'))

#network ping function for intent response
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
        
#google calendar checker function for intent response
def calendar():
    jay("Here is your google calendar....")
    openbrowser("https://calendar.google.com/calendar")

#vpn connection function for intent response
def secure():
    jay("Activating vpn please wait....")
    os.system("protonvpn-cli c -f")

def reboot():
    files = open("logs/decrypt.txt", "w")
    files.write("Decrypted message has been deleted! {o_o}")
    files = open("session.txt", "w")
    files.write("")
    jay("rebooting system")
    global reboot_key
    reboot_key = True