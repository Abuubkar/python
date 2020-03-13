import os

audio_file = input("Enter name of Audio File: ")


def get_length(fname):
    import wave
    import contextlib

    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def get_text(audio_file, off=None, dur=None):
    import speech_recognition as sr

    try:
        r = sr.Recognizer()

        text = ""
        with sr.AudioFile(audio_file) as source:
            r.adjust_for_ambient_noise(source, duration=0.1)

            audio = r.record(source, duration=dur, offset=off)
            text = r.recognize_google(audio)
            return text

    except Exception as ex:
        pass


result = ""
length = get_length(audio_file)
print(length)
context = get_text(audio_file)

find_text = input("Enter word you want to search in audio: ")
print("Searching....")
# SEARCHING ...............
if (find_text in context):
    offset = 0
    duration = 0.05

    while duration + offset < length:
        processed_text = get_text(
            audio_file, round(offset, 2), round(duration, 2))
        if(processed_text != None):
            if (find_text in processed_text):
                print(find_text + ' is present in ' + context +
                      ' in duration of ' + str(offset) + "-" + str(offset+duration))
                break
        duration = round(duration + 0.05, 2)
    print("Validating offset= " + str(offset) +
          " duration = " + str(offset+duration)+' ...')

    print('context was:- ' + context)
    print(str(find_text) + " was found at:  " +
          str(offset+duration) + "s")
else:
    print("Not Found(2)")
