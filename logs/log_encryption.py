from getpass import getpass
from cryptography.fernet import Fernet
import datetime
import security
from static_impulses import jay

# stores a variable with the current week day, month and day of the month

filename = datetime.datetime.now().strftime("%A,%b,%d")

# key that the encryption and decryption algorithm uses to encrypt and
# decrypt the input of the user

fernet = Fernet(b'P6dHuHOnzvRk3c7330Cb-ZdQ1wgFlOcD5uFVogSy_cw=')

# an encryption function that takes in input from user
# encodes the string into bytes and finally encrypts
# the byte message into the final encrypted message

# after encryption is completed the functions decodes
# the bytes back to strings and writes it to the 
# file with the filename specified in the above
# variable at the begining

def encrypt_note():
    message = input("LOG: ")
    jay("encrypting log")
    encMessage = fernet.encrypt(message.encode('utf_8'))
    f = open(f"logs/secure/{filename}.txt", "a")
    f.write(encMessage.decode('utf_8') + "\n")
    jay(f"log encrypted and saved in log/secure/{filename}")

# a decryption algorithm that takes the filename to be decrypted
# as an input from the user and continues to read the data from
# the file and starts decrypting the file line by line and
# it writes it to the decrypt.txt file so the user can view
# it for a limitted time or until the program exits

def decrypt_note():
    files = input("Filename: ")
    f = open(f"logs/secure/{files}", "r")
    decfile = open("logs/decrypt.txt", "w")
    for x in f:
        decMessage = fernet.decrypt(x.encode()).decode()
        decfile.write(decMessage + "\n\n")
    jay("log has been decrypted and saved to file decrypt.txt")
    jay("this file will be erased when my system exits or reboots")
    
# before the decryption function is executed this file is called by
# the program and this file compares a stored hash password with
# input of the user after converting the input into a hash and
# if the hashes match it executes the decrypt_note function
# if the hashes don't match the program exits the current intent call

def decryption_check():
    passwd = getpass("DECRYPTION PHRASE: ")
    security.hasher(passwd)
    if security.hash == "c81871642fc40d074afe66e8f20ee1d135900e7ed4a0533a637f8236c3b460be":
        decrypt_note()
    else:
        jay("Wrong password can't decrypt")

