import speech_recognition as sr

class listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything\n")
        audio = r.listen(source, phrase_time_limit=1)
        try:
            text = r.recognize_google(audio)
            formated = format(text)
            print(formated)
        except:
            print("Ooops!")

