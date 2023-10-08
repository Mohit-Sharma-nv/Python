# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32.client.Dispatch("SAPI.SpVoice")

while 1:
	print("Enter the word you want to speak it out by computer")
	s = input()
	speaker.Speak(s)

# To stop the program press
# CTRL + Z
