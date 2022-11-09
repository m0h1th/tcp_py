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
    
clear()

alias = input('USERNAME: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def fake_type(s,end='\n'):
    import random
    import time
    timings = [0.1,0.04,0.06,0.05,0.07,0.03,0.09,0.02,0.08,0.01,0.12,0.2]
    for i in s:
        print(i, end='',flush=True)
        time.sleep(random.choice(timings))   
    print(end,end='') 

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
