#The default speed for Windows speaks
speakingRate = 175

#These variables control speaking and platform
mute = False
isWindows = True

try:
    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate', speakingRate)
except:
    isWindows = False
    #mute = True

import sys
from os import system
import threading
import time
import Queue
def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))

input_queue = Queue.Queue()

input_thread = threading.Thread(target=add_input, args=(input_queue,))
input_thread.daemon = True
input_thread.start()

class speaker:
    global engine
    def say(self, text):
        if not mute and isWindows:
            engine.say(text)
            engine.runAndWait()
        else:
            system('say ' + text)

class get:
    global input_queue
    global add_input
    def get(self, nonblocking = True):
        string = ''
        text = ''
        if nonblocking:
            while not input_queue.empty():
                string += input_queue.get()
            text = string[0:len(string)-1]
        else:
            text = raw_input()
        return text
    def new_input(self):
        if not input_queue.empty():
            return True
        else:
            return False
