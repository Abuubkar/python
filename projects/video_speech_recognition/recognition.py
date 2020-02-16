import speech_recognition as sr


try:
    r = sr.Recognizer()

    audio_file = "recording.wav"
    with sr.AudioFile(audio_file) as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        print('Recording: '+audio_file)
        audio = r.record(source)

        # audio = r.record(source, duration=52, offset=2)
        print('Done!')

        print('Recognition Initiated')
        # text = r.recognize_google(audio)
        text = r.recognize_google(audio)

        print(text)

except Exception as ex:
    print(ex.__class__.__name__ + " : " + ex.__str__())
