import speech_recognition as sr


try:
    r = sr.Recognizer()

    audio_file = "audio.wav"
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        print('Done!')

        print('Recognition Initiated')
        # text = r.recognize_google(audio)
        text = r.recognize_google(audio)
        val = input("Enter text to find in Voice Clip: ")
        if(val in text):
            print(val + " is in ")
        else:
            print(val + " is not in ")
        print(text)

except Exception as ex:
    print(ex)
