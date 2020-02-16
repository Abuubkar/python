import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something .... ')
    audio = r.listen(source)
    print('Done!')

try:
    print('Recognizing initiated')
    text = r.recognize_google(audio)
    print(text)

except Exception as ex:
    print(ex.__class__.__name__ + " : " + ex.__str__())
