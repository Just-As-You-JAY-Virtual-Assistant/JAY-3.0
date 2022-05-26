import datetime
import os
import time

# function to check how long its been since jay has been online
# this function takes the current time in years and 
# if the year is less than or equal to 2022 and month is less than the
# 8th month of the year 2022 it diplays a few month old as a message
# if the year is less than or equal to 2022 and month is between 
# the 8th and the 12th month it diplays almost a year as a message
# if the year is greater than 2022 it substracts 2021 from the
#current year and displays the defference as jay's age
if int(datetime.datetime.now().year <= 2022):
    age_now = "a few months"
    if int(datetime.datetime.now().year <= 2022) and int(datetime.datetime.now().month) >= 8 <=12:
        age_now = "almost 1 year"
else:
    age = int(datetime.datetime.now().year) - 2021
    if age <= 1:
        age_now = str(age) + " year "
    else:
        age_now = str(age) + " years "

# description about jay
about_jay = {
    "name":"jay",
    "age": f"{age_now} old",
    "use": "assist in simple daily task automation."
}

# variable holding the current time in hours
times = time.strftime('%H')


# JAY's task confirmation function
# this function checks if the user wants music or not
# it displays only a message if no and if yes
# it opens music and displays message too
def task_checker(message1, music_title):
    reply_mes = input("|NS| => ")
    if reply_mes.lower() in ["yes", "sure", "yup", "yeaa", "yeah"]:
        jay(message1)
        jayyt(music_title)
        time.sleep(5)
    else:
        jay(message1)

# JAY's time checking function
# this function checks for the time of the day
# and prepares a message according to the time
def timecheck(message1, message2, message3):
    if int(times) < 12 and int(times) >=6:
        jay(message1)
    elif int(times) >= 12 and int(times) < 18:
        jay(message2)
    elif int(times) >= 18 or int(times) < 6:
        jay(message3)


# JAY's study or work session checker
# this function checks if the user works on programming or networking
# if verify is programming it opens the last vs code session
# and checks if the user wants music and as usual checks with user
# if the user chooses networking it opens packettracer
# and checks if the user wants music and as usual checks with user
def env_check():
    verify  = input("|NS| => ")
    if "programming" in verify:
        jay("here is your las coding session")
        os.system("code")
        jay("Do you want any music while working?")
        task_checker("(o_o) => Setting up work station", "night time chill lofi")
        jay("Have a nice work session sir")
    elif "networking" in verify:
        os.system("packettracer &")
        time.sleep(2)
        jay("Do you want any music while working?")
        task_checker("(o_o) => Setting up work station", "night time chill lofi")
        jay("Have a nice work session sir")
    elif "cancel" in verify:
        pass
    else:
        error()
        env_check()

# JAY's texting and speaking ability
# this fubction allows jay to turn the string input into an audio file
# and he plays that audio file and also prints out the string input
# on the screen
def jay(msg):
    audio = 'speech.mp3'
    from gtts import gTTS
    from playsound import playsound
    sp = gTTS(text = msg, lang='en', tld='com.au')
    sp.save(audio)
    playsound(audio)
    print(f"(o_o) => {msg}")


# JAY's youtube system
# this function uses the pywhatkit module to open
# a youtube url with the string input as
# a search aparameter and opens the first search match
# and plays it on the default browser
def jayyt(title):
    import pywhatkit
    pywhatkit.playonyt(title)

# JAY's url opener
# this function takes the string input as a url and
# opens the url on the systems default browser using
# the webbrowser module
def openbrowser(search):
    import webbrowser
    webbrowser.open(search)

# JAY's google searcher
# this function uses the pywhatkit module to open
# a google url with the string input as
# a search parameter and displays the google search
# results on the default browser
def googlesearch(search):
    import pywhatkit
    jay("searching...")
    pywhatkit.search(search)

# error handler when the JAY isn't familiar with the request
# this function is used to alert the user that their input
# isn't known by jay's system
def error():
    jay("Sorry sir, I couldn't understand that, can you please repeat that")