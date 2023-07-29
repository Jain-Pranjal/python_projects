# text to speech 

import os 
import pyttsx3


# tts means text to speech 


# from here main program is starting 
#this means that now the program will start from here only from the main part
if __name__=="__main__" :  
    print("Welcome to RoboSpeaker , created by pranjal jain ")
    engine = pyttsx3.init()
    while True :
        enter = input("What would you like me to speak : ")
        if enter == "exit" :
            engine.say("Goodbye my dear Friend")
            engine.runAndWait()
            break

        # say() will repeat the things that is given as a input to program 
        else:
            engine.say(enter)
            engine.runAndWait()

# runandWat wait for the next command after the first is being completed
 





# logic

# while (True):
#     a=input()
#     if a=="q":
#         engine.say("bye niklo chalo ")
#         engine.runAndWait()
#         break
#     else:
#         engine.say(a)
#         engine.runAndWait()



    











