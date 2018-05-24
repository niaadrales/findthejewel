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
plank = 0
stone = 0
emerald = 0
diamond = 0
pickaxe = 0
cobblestone = 0
point = 0
jewelart = """                               
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
print  "( ___|_  _| \( |  _ \   (_  _| )_( | ___)   (_  _| ___| \/\/ | ___|  )    "
print  " )__) _)(_ )  ( )(_) )    )(  ) _ ( )__)   .-_)(  )__) )    ( )__) )(__ "
print  "(__) (____|_)\_|____/    (__)(_) (_|____)  \____)(____|__/\__|____|____)  "
time.sleep(1)
print jewelart
answer = raw_input("Press Enter to start the game.")
clear()
print "Would you like easy?"
time.sleep(1)
print " ____    __    ___  _  _ "
print "( ___)  /__\  / __)( \/ )"
print " )__)  /(__)\ \__ \ \  / "
print "(____)(__)(__)(___/ (__) "
print "Or normal?"
time.sleep(1)
print " _  _  _____  ____  __  __    __    __   "
print "( \( )(  _  )(  _ \(  \/  )  /__\  (  )  "
print " )  (  )(_)(  )   / )    (  /(__)\  )(__ "
print "(_)\_)(_____)(_)\_)(_/\/\_)(__)(__)(____)"
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
clear()
print "The story: "
time.sleep(1)
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
while True:
	penny = raw_input("What has a tail and a head and has no body?")
	clear()
	if penny.lower() == "penny":
		break
	print "Your answer is wrong.Try again."
print "Your answer is correct!You got the jewel!"
score = score + 5
jewel = jewel + 1
print "Your current score is",score
raw_input("Level 2,while you were walking,you saw a village.(Press Enter)")
clear()
raw_input("Inside that village,you saw 5 villagers.(Press Enter)")
clear()
raw_input("Every villager trades different items.(Press Enter)")
clear()
raw_input("The librarian trades  pickaxe for 10 wooden planks.(Press Enter)")
clear()
raw_input("The blacksmith trades 10 cobblestones for for 1 stone pickaxe.(Press Enter)")
clear()
raw_input("The chef trades 2 emeralds for 10 cobblestones.(Press Enter)")
clear()
raw_input("The miner trades 1 diamond for 2 emeralds.(Press Enter)")
clear()
raw_input("The witch trades 1 jewel for 1 diamond.(Press Enter)")
clear()
print "You are given one axe that can last for 16 woods."
print "You'll have to make a crafting bench."
print "To do that you'll need 4 wood.And you'll need to craft a stone pickaxe and 10 wooden planks."
print "The wood looks like this.---> o.Or a letter o."
print "The stick looks like this.---> /"
print "The wooden planks looks like this.---> 0.Or number 0"
print "The cobblestones looks like this.---> @.Or an at."
print "To break wood type b."
while wood <= 15:
	wood_input = raw_input("")
	clear()
	if wood_input == "b":
		wood = wood + 1
		print "You now have",wood
		if wood == 1:
			print "You need to keep doing that until you have 16 woods."


print "Okay,now that you have enough wood craft a crafting bench."
print "To craft a crafting bench you'll need 4 woods."
print "To craft it place 4 wood with space on each of them.Just type four o's."
while True:
        bench = raw_input("")
        if bench == "o o o o":
               break
        print "There's no crafting recipe like that.Try again."
print "You crafted a crafting bench.But the crafting bench will only show up if needed."
print "But,you also need to learn how to craft things."
raw_input("Press Enter to show how to craft things in Level 2.")
clear()
time.sleep(1)
print "stick:o o"
time.sleep(1)
print "wooden planks:o"
time.sleep(1)
print "pickaxe:/ / / @ @ @"
time.sleep(1)
print "crafting bench:o o o o"
time.sleep(1)
raw_input("Press Enter when your done.")
clear()
print "Okay,your gonna craft a stick using the crafting bench.2 woods makes 5 sticks but you only need 3,but that's okay."
while True:
        craft = raw_input("")
        clear()
        if craft  == "o o":
			break
wood = wood - 2
stick = stick + 5
print "Okay,now to craft wooden planks.Use the crafting table to craft 10 wooden planks"
while plank <= 10:
	planks = raw_input("What would you like to craft?:")
	clear()
	if planks == "o":
		plank = plank + 1
		print "You now have",plank 
		if plank == 1:
			print "You need to keep doing that until you have 10 wooden planks."
print "Now that you have wooden planks,it's time to trade!Type t to trade."
while True:
	keyword = raw_input("")
	clear()
	if keyword.lower() == "t":
		break 
        print "You typed the wrong keyword.Try again."
answer = raw_input("Librarian:3 stones for 10 wooden planks.Press Enter to trade.")
clear()
stone = stone + 3
plank = plank - 10
print "Now,to craft a stone pickaxe.You know what to do.Use the crafting table to craft it."
while True:
	pick = raw_input("What would you like to craft?:")
	clear()
	if pick == "/ / / @ @ @":
		break
	print "There's no crafting recipe like that.Try again."
pickaxe = pickaxe + 1
stick = stick - 3
stone = stone - 3
print "Time to trade.Type t to trade."
while True:
	keyword = raw_input("")
	clear()
	if keyword == "t":
		break
	print "You type the wrong keyword.Try again."
answer = raw_input("Blacksmith:10 cobblestones for 1 pickaxe.Press Enter to trade.")
clear()
print "You traded 1 pickaxe for 10 cobblestones."
pickaxe = pickaxe - 1
cobblestone = cobblestone + 10
print "Now that you have cobblestones trade them for the next villager.Time to trade.Type t to trade."
while True:
	keyword2 = raw_input("")
	clear()
	if keyword2 == "t":
		break
	print "You typed the wrong keyword.Try again."
answer = raw_input("Chef:2 emeralds for 10 cobblestones.Press Enter to trade.")
clear()
print "You traded 10 cobblestones for 2 emeralds."
cobblestone = cobblestone - 10
emerald = emerald + 2
print "Time to trade!Again!Type t to trade."
while True:
	keyword3 = raw_input("")
	clear()
	if keyword3 == "t":
		break
	print "Wrong keyword.Try again."
answer = raw_input("Miner:1 diamond for 2 emeralds.Press Enter to trade.")
clear()
print "You traded 2 emeralds for 1 diamond."
emerald = emerald - 2
diamond = diamond + 1
print "Now,this is the final trade.Type t to trade."
while True:
	keyword4 = raw_input("")
	clear()
	if keyword4 == "t":
		break
	print "Wrong keyword.Try again."
answer = raw_input("Witch:1 jewel for 1 diamond.Press Enter to trade.")
clear()
diamond = diamond - 1
jewel = jewel + 1
score = score + 5
print "You got the jewel!"
print "You current score is",score
print "You now have",jewel 
answer = raw_input("Press Enter to start level 3.")
clear()
answer = raw_input("Later...you were celebrating because you got 2 jewels.Well,not this time.(Press Enter)")
clear()
answer = raw_input("It got snatched by the snather!The snather has 2 jewels.You need to get it before it's too late.(Press Enter)")
clear()
answer = raw_input("Too get it,you need to pass 3 puzzles.The snatcher dealed with you that if you pass his puzzle,you will get the two jewels.Every puzzle has points.You need to give it to the snather,and the 2 jewels will be yours.(Press Enter)")
clear()
answer = raw_input("First one is the wizard riddles.To pass that puzzle,you need to answer some riddles.(Press Enter)")
clear()
answer = raw_input("Second one is minecraft madness.To pass that puzzle,you will need to do the same thing on level 2.Well different i guess.I'ts just like the one you did on level 2.(Press Enter)")
clear()
answer = raw_input("Third one is Boss Math Battle.You will be battling Boss Math.To pass that puzzle,you need to answer some math questions.")
clear()
answer = raw_input("Press Enter to start the first puzzle.")
clear()
while True:
	riddle = raw_input("First riddle:What kind of table is good for you to eat?")
	clear()
	if riddle.lower() == "vegetable":
		break
	print "Your answer is wrong try again."
print "Your answer is correct!Now,for the second riddle."
while True:
	riddle2 = raw_input("Second riddle:What season does humpty-dumpty hate the most?")
	clear()
	if riddle2.lower() == "the fall":
		break
	print "Your answer is wrong,try again."
print "Your answer is correct!Now,for the final riddle."
while True:
	answer = raw_input("Final riddle:What is the sun's favourite day of the week?")
	clear()
	if answer.lower() == "sunday":
		break
	print "Your answer is wrong,try again."
print "Your answer is correct!You got 1 point."
point = point + 1






	
	


	















































































































































































































   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    








	

		



