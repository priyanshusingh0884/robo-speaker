import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to Robospeaker Tell me what you want me to speak (press 'q' to quit)")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.strip().lower() == "q":
            engine.say("say 'bye bye friend'")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()


