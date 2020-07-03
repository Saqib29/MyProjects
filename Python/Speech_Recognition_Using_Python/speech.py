import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as mic:
    print("Say...")
    audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        print("You: ", text)
    except:
        print("Sorry, couldn't here you")



