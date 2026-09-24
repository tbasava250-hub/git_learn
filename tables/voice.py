# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# def speak(text) :
    # engine.say(text)
    # engine.runAndWait()

# def promtcommand(c) :
    #  if "open google " in c.lower() :
        #  webbrowser.open("http://google.com")

# if __name__ == "__main__" :
    # speak("Hey,MANOJ HOW ARE YOU BRO....")
    # while True :
        # r = sr.Recognizer()



        # print("recognizing...")
        # try:   
            # with sr.Microphone() as source:
                # print("Listening...")
                # audio =r.listen(source, timeout=2, phrase_time_limit=1)
                # word = r.recognize_google(audio)
            # if(word.lower()== "jarvis") :
                # speak("Ya")
                # with sr.Microphone() as source:
                    # print("jarvis active...")
                    # audio =r.listen(source, timeout=2, phrase_time_limit=1)

                # promtcommand("c")
        # except Exception as e:
            # print("Error;(0)".format(e))





# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
    # print("Speak something...")
    # audio = recognizer.listen(source)

# try:
    # text = recognizer.recognize_google(audio)
    # print("You said:", text)
# except:
    # print("Sorry, could not understand")


import qrcode
img = qrcode.make("HEY,MANJUNATH T. HOW ARE YOU!")
img.show()