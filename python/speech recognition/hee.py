# import speech_recognition as sr

# sample_rate = 48000
# chunk_size = 64
# r = sr.Recognizer()

# while(1):
# 	print("source")
# 	with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
# 		print("noise")
# 		r.adjust_for_ambient_noise(source)
# 		print("Say Something, listening...")
# 		audio = r.listen(source)
# 		try:
# 			print("Recognizing...")
# 			text = r.recognize_google(audio)
# 			print("you said: " + text)
# 		except sr.UnknownValueError:
# 			print("Google Speech Recognition could not understand audio")
# 		except sr.RequestError as e:
# 			print("Could not request results from Google Speech Recognition service; {0}".format(e))


import speech_recognition as sr
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)