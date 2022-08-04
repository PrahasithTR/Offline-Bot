import pyttsx3   
import datetime
import webbrowser
import os
import smtplib
from vosk import Model, KaldiRecognizer
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Jarvis Sir. Please tell me how may I help you")
    speak("I am Jarvis Sir. Please tell me how may I help you")

    print('')
    print('Listening...')

def time():
    time= datetime.datetime.now().strftime("%H:%M:%S")
    print(time)
    speak(time)
    #speak(f"Sir, the time is {strTime}")

def date():
    today= datetime.datetime.now().strftime("%d : %m :%y")
    print(today)
    speak(today)
  


    


model = Model(r"C:\Users\trpra\Desktop\nf task\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
os.system('cls')
wishme()

recognizer = KaldiRecognizer(model, 16000)
mic= pyaudio. PyAudio()
stream= mic.open(format= pyaudio.paInt16, channels =1, rate= 16000, input=True, frames_per_buffer =8192)
stream.start_stream()

while True:
        data = stream.read(4096)
        #if len(data) == 0:
            #break
        if recognizer.AcceptWaveform(data):
            result = recognizer. Result()
            #result= json.loads(result)
            print('Sir:' + result[14:-3])

            
            
            if "hello" in result[14:-3]:
                os.system('cls')
                stream.stop_stream()
                print(" Hello Sir, How may I help you")
                speak(" Hello Sir, How may I help you")
                stream.start_stream()
                print('')
                print('Listening...')
                print('')

            elif "time" in result[14:-3]:
                os.system("cls")
                stream.stop_stream()
                print("Sir:" + result[14:-3])
                time()
                speak("What else would you like me to do, Sir?")
                stream.start_stream()
                print('')
                print("Listening...")
                print('')

            elif "day" in result[14:-3]:
                os.system("cls")
                stream.stop_stream()
                print("Sir:" + result[14:-3])
                date()
                speak("What else would you like me to do, Sir?")
                stream.start_stream()
                print('')
                print("Listening...")
                print('')

            elif "stop" in result[14:-3]:
                print(" Bye Sir")
                speak(" Jarvis is Off, See you later sir")
                stream.stop_stream()

            else:
                os.system("cls")
                stream.stop_stream()
                print("Sir:" + result[14:-3])
                print("I am sorry. That is beyond my ability now.")
                speak("I am sorry. That is beyond my ability now.")
                print("Is there anything else I can help you with?")                
                speak("Is there anything else I can help you with?")
                stream.start_stream()
                print('')
                print("Listening...")
                print('')

if __name__ == '__main__':
    wishme()


   
                

            
                              
                      
            
                
                
    
    



