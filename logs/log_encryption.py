from getpass import getpass
from cryptography.fernet import Fernet
import datetime
import security
from static_impulses import jay

filename = datetime.datetime.now().strftime("%A,%b,%d")
fernet = Fernet(b'P6dHuHOnzvRk3c7330Cb-ZdQ1wgFlOcD5uFVogSy_cw=')

def encrypt_note():
    message = input("LOG: ")
    jay("encrypting log")
    encMessage = fernet.encrypt(message.encode('utf_8'))
    f = open(f"logs/secure/{filename}.txt", "a")
    f.write(encMessage.decode('utf_8') + "\n")
    jay(f"log encrypted and saved in log/secure/{filename}")

def decrypt_note():
    files = input("Filename: ")
    f = open(f"logs/secure/{files}", "r")
    decfile = open("logs/decrypt.txt", "w")
    for x in f:
        decMessage = fernet.decrypt(x.encode()).decode()
        decfile.write(decMessage + "\n\n")
    jay("log has been decrypted and saved to file decrypt.txt")
    jay("this file will be erased when my system exits or reboots")
    


def decryption_check():
    passwd = getpass("DECRYPTION PHRASE: ")
    security.hasher(passwd)
    if security.hash == "c81871642fc40d074afe66e8f20ee1d135900e7ed4a0533a637f8236c3b460be":
        decrypt_note()
    else:
        jay("Wrong password can't decrypt")

