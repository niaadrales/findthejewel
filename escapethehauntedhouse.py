import os
import time

def clear():
	os.system("clear")
	print """
"""
def waitfor(word,output):
	
	while True:
		answer = raw_input("")
		clear()
		if answer.lower() == word:
			break
		print output
time.sleep(1)
name = raw_input("Please type your name here.--->")
if name.lower() == "nia":
      print "Hi maker of the program."
else:
      print "Hi",name + "."
time.sleep(1)
answer = raw_input("Dare to continue?Y/N: ")
if answer.lower() == "y":
        print "Okay."
        time.sleep(1)
        print "Loading....."
        time.sleep(1)
else:
        print "Mkay,bye!"
        time.sleep(1)
        exit()
print "But first!I need to know your age."
time.sleep(1)
age = raw_input("How old are ya?: ")
age = int(age)

if age <= 7:
	print "Sorry but,you are too young to play this game."
	time.sleep(2)
	exit()
else:
        print "Okay."
        time.sleep(1)
        print "Loading....."
        time.sleep(1)
gender = raw_input("What's your gender?Girl/Boy: ")
time.sleep(1)
print "WARNING!!!:This game is gonna be scary,for the past people,because all the future people don't like games that are just texts.They are more on high tech."
time.sleep(1)
































































































