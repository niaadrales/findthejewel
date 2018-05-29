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
clear()
if name.lower() == "nia":
      print "Hi maker of the program."
else:
      print "Hi",name + "."
      time.sleep(1)
answer = raw_input("Dare to continue?Y/N: ")
clear()
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
clear()
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
clear()
time.sleep(1)
print "WARNING!!!:This game is gonna be scary,for the past people,because all the future people don't like games that are just texts.They are more on high tech."
time.sleep(1)
print "Loading game....."
time.sleep(1)
print "Spawning monsters....."
time.sleep(1)
print "Printing texts....."
time.sleep(1)
print "Done!" 
time.sleep(1)
raw_input("Press Enter to start the story.")
clear()
print "The story:"
time.sleep(1)
raw_input("You and your friends were going to the mall to have fun.(Press Enter)")
clear()
raw_input("But your car broke down while you were just heading home.(Press Enter)")
clear()
raw_input("You stopped infront of a creepy house.You have no where to go so you entered the house.(Press Enter)")
clear()
raw_input("Just before you leave to take all the things from your car,the front door shut by itself.(Press Enter)")
clear()
raw_input("You kept trying to open it but it won't.(Press Enter)")
clear()
raw_input("But your phone was in your pocket,so you tried to call your friends.But there was no signal.(Press Enter)")
clear()
print "*tug!*"
time.sleep(1)
print "You were knocked out by a crazy old woman.People call her granny.Granny was so famous all over the world.People ignore her."
time.sleep(1)
print "You were locked up in a room.You have 5 days before ganny gets angry at you for trying to escape.Otherwise,she might just kill you."
time.sleep(1)
print "If your out of days,you will go back to the start."
time.sleep(1)
print "DAY 1"
time.sleep(1)
print "You:Uh...My head feels so bad."

        


























































































