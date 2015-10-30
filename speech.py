#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import time
from phue import Bridge

bridge = Bridge('192.168.11.8')
bridge.connect()
bridge.get_api()
bridge.set_light(2, 'on', True)
# obtain audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Say something!")
        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            result = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + result)
            if result == "lights off":
                bridge.set_light(2, 'on', False)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    time.sleep(0.5)
