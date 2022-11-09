#!/bin/python3
import threading
import socket
from os import system, name
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
def fake_type(s,wpm=None,end='\n'):
    import random
    import time
    for i in s:
        print(i, end='',flush=True)
        if wpm==None:
            time.sleep(random.random()/10) 
        else:  
            time.sleep(1/wpm)
    print(end,end='') 

clear()

alias = input('USERNAME: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",int(input("Enter port: "))))
fake_type("NETWORK INTERCEPTED",40)


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                fake_type(message)
        except:
            print('CONNECTION LOST')
            client.close()
            break



def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
