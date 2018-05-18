import os
import time

def clear():
	os.system("clear")
	print """
"""
score = 0
jewel = 0
wood = 0
stick = 0
jewelart = """                  MMMMMMMMMMMMMMM                              
                                MMMMMMMMMMMMMMM                                 
                                MMMMMMMMMMMMMMM                                 
                           88888.,,,,,,,,,,,,,.D8888                            
                           MMMMM               MMMMM                            
                           MMMMM               MMMMM                            
                           MMMMM               MMMMM                            
                      MMMMM                         MMMMM                       
                      MMMMM                         MMMMM                       
                      MMMMM                         MMMMM                       
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM          MMMMMMMMMMMMMMM         .MMMMM                  
                 MMMMM          MMMMMMMMMMMMMMM         .MMMMM                  
                 MMMMM          MMMMMMMMMMMMMMM         .MMMMM                  
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM          MMMMM               MMMMM          MMMMM             
            MMMMM               MMMMMMMMMMMMMMM               MMMMM             
            MMMMM               MMMMMMMMMMMMMMM               MMMMM             
            MMMMM               MMMMMMMMMMMMMMM               MMMMM             
                .MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                 MMMMM     MMMMM               MMMMM    .MMMMM                  
                .     MMMMMMMMMM               MMMMMMMMMM                       
                      MMMMMMMMMM               MMMMMMMMMM                       
                      MMMMMMMMMM               MMMMMMMMMM                       
                      88888MMMMM.,,,,,,,,,,,,,.MMMMM88888                       
                           MMMMMMMMMMMMMMMMMMMMMMMMM                            
                           MMMMMMMMMMMMMMMMMMMMMMMMM                            
                           MMMMMMMMMMMMMMMMMMMMMMMMM               """
finaljewel = """ ...............................................................................
................................................................................
................................................................................
............................................................................. ..
.................................................................. ..... .......
................................................................................
................................................................................
............ 7MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD..............
............MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.............
...........MMMMMMM:................MMMM8MMMM ............... .MMMMMM............
..........MMMM.,MMM............. $MMMM...MMMMD ..............MMM=MMMM. .........
........ MMMM...MMMI............MMMM:......MMMM ............OMMM..NMMM. ........
.......:MMMM.... MMM......... MMMMM.........MMMMM ..........MMM....IMMM+........
......8MMM=..... MMMO....... MMMM............ MMMM,........MMMN.....,MMMN.......
.....MMMM.......  MMM......MMMMD...............ZMMMM......+MMM .......MMMM .....
....MMMM..........MMMD...,MMMM...................MMMM=... MMM,.........MMMM ... 
...MMMM .......... MMM  MMMMZ.....................?MMMM  MMMM...........MMMM ...
  MMMM.............MMMMMMMM ........................MMMMNMMM.............8MMM:  
?MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:
.IMMMM  ............ MMMD.............................~MMM...............MMMM8 .
...MMMMM..............MMM? .........................  MMM............ .MMMMM....
.....MMMMZ.............MMM  .........................MMMD........... ?MMMM  ....
... ..~MMMM ...........8MMM.........................MMMM............MMMM$.......
........NMMMM...........MMMM.......................MMMM...........MMMMM.........
........ .MMMMD..........MMMD.....................,MMM..........7MMMM. .........
... ...... .MMMM:.........MMM, ...................MMM,........ MMMM= ...........
............ DMMMM .......:MMM ..................MMMZ....... MMMMM..............
.............. MMMMN.......DMMM.................MMMM.......ZMMMM  ..............
................ MMMM+......MMMM...............DMMM..... ,MMMM: .. .. ..........
................ .ZMMMM .... MMM8.............:MMM......MMMMD...................
....................MMMMM.... MMM.............MMM,....NMMMM.....................
.................... .MMMMI ..=MMM.......... MMMD...~MMMM,......................
...................... +MMMM...DMMM ........MMMM.. MMMMO ........ ..............
........................ MMMMM..MMMM.......DMMM  MMMMM....................... . 
.........................  MMMMZ.MMMI.....,MMM.+MMMM. ..........................
............................~MMMM,MMM.....MMM:MMMMI.............................
............................. MMMMMMMM . MMMMMMMM ..............................
............................... MMMMMMM.MMMMMMM.................................
.................................,MMMMMMMMMMM=..................................
...................................DMMMMMMMM................................... 
....... .............................MMMMM.... .................................
...................................... M,.......................................
.............................................. .................................
................................................................................
............ .......................... ...... .................................
................................................................................
...... .........................................................................
.............................................................. .................
................................................................................
........................ ............... ............. ....... ................."""


answer = raw_input("Please type your name here.---> ")
clear()
if answer.lower() == "nia":
	print "Hi maker of the program."
else:
	print "Hi",answer 
answer = raw_input("What is your age? ")
clear()
age = int(answer)
if age < 4:
	print "You are too young to play this game."
	exit()
else:
	print "Good."
answer = raw_input("Are you ready to play the game?Y for yes and N for no.")
clear()
if answer.lower() == "y":
	print "Okay."
else:
	print "Okay."
	exit()
print "Welcome,to FIND THE JEWEL!"
time.sleep(1)
print  " ____ ____ _  _ ____     ____ _   _ ____     ____ ____ _    _ ____ __     "
time.sleep(1)
print  "( ___|_  _| \( |  _ \   (_  _| )_( | ___)   (_  _| ___| \/\/ | ___|  )    "
time.sleep(1)
print  " )__) _)(_ )  ( )(_) )    )(  ) _ ( )__)   .-_)(  )__) )    ( )__) )(__   "
time.sleep(1)
print  "(__) (____|_)\_|____/    (__)(_) (_|____)  \____)(____|__/\__|____|____)  "
time.sleep(1)
print jewelart
answer = raw_input("Press Enter to start the game.")
clear()
print "Would you like easy?"
time.sleep(1)
print " ____    __    ___  _  _ "
time.sleep(1)
print "( ___)  /__\  / __)( \/ )"
time.sleep(1)
print " )__)  /(__)\ \__ \ \  / "
time.sleep(1)
print "(____)(__)(__)(___/ (__) "
time.sleep(1)
print "Or normal?"
time.sleep(1)
print " _  _  _____  ____  __  __    __    __   "
time.sleep(1)
print "( \( )(  _  )(  _ \(  \/  )  /__\  (  )  "
time.sleep(1)
print " )  (  )(_)(  )   / )    (  /(__)\  )(__ "
time.sleep(1)
print "(_)\_)(_____)(_)\_)(_/\/\_)(__)(__)(____)"
time.sleep(1)
answer = raw_input("Easy or Normal?")
clear()
if answer.lower() == "easy":
	print "Okay,loading easy mode....."
else:
	print "Okay,loading normal mode....."
time.sleep(2)
print "Printing texts....."
time.sleep(2)
print "Analizing answers....."
time.sleep(2)
print "Done!"
time.sleep(2)
raw_input("Press Enter to start the story.")
print "The story:"
clear()
raw_input("You are a survivor. One day,you were walking by the mountain. Then you saw a geany.(Press Enter)")
clear()
raw_input("You asked for one wish. To go home.But there was one condition. you have to find 5 jewels and have 25 points.(Press Enter)")
clear()
raw_input("Every jewel you find is 5 points.(Press Enter)")
clear()
raw_input("Level 1,there's a jewel in that house!But it's guarded by the wizard.(Press Enter)")
clear()
raw_input("You can only get it if you answered his riddle.(Press Enter)")
clear()
raw_input("What has a tail,and a head,but no body.")
clear()
if answer.lower() == "penny":
	print "Your answer is correct!You got the jewel!"
	print jewelart 
	print "Your current score is",score 
	score = score + 5
	jewel = jewel + 1
else:
	print "Your answer is wrong."
	score = score - 1	
raw_input("Level 2,while you were walking,you saw a village.(Press Enter)")
clear()
raw_input("Inside that village,you saw 5 villagers.(Press Enter)")
clear()
raw_input("Every villager trades different items.(Press Enter)")
clear()
raw_input("The luberjack trades 1 pickaxe for 10 woods.")
 
   
    
    








	

		



