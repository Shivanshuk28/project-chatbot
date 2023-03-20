import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=aa.Recognizer()


machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()
global instruction


def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("LISTENING....")
            speech = listener.listen(origin)
            instruction=listener.recognize_goggle(speech)
            instruction=instruction.lower()
            if "sqube" in instruction:
                instruction=instruction.replace('sqube',' ')
                print(instruction)
            
        
        
        
        
    except:
        pass
    return instruction

def play_sqube():
    
    instruction = input_instruction()
    print(instruction)
    
    if 'play' in instruction:
        song=instruction.replace('play'," ")
        talk("playing"+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk("Current time"+time)
        
    elif 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's Date"+date)
        
    elif 'how are you' in instruction:
        talk('I am Fine,HOW about you')
        
    elif 'what is your name' in instruction:
        talk("I am SQUBE,What can I do for you?")
    
    elif 'who is' in instruction:
        human=instruction.replace('who is'," ")
        info = wikipedia.summary(human,1)
        print(info) 
        talk(info)       
    else:
        talk("PLEASE REPEAT")  
        
play_sqube()

