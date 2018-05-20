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
answer = raw_input("What has a tail,and a head,but no body.")
clear()
if answer.lower() == "penny":
	print "Your answer is correct!You got the jewel!"
	score = score + 5
	jewel = jewel + 1 
	print "Your current score is",score 
	print "And you now have",jewel,"jewel"
else:
	print "Your answer is wrong."
	score = score - 1	
raw_input("Level 2,while you were walking,you saw a village.(Press Enter)")
clear()
raw_input("Inside that village,you saw 5 villagers.(Press Enter)")
clear()
raw_input("Every villager trades different items.(Press Enter)")
clear()
raw_input("The librarian 3 stones trades  pickaxe for 10 wooden planks.(Press Enter)")
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
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
print "You need to keep doing that until you have 16 woods."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
else:
	print "No wood breaked."
answer = raw_input("")
clear()
if answer.lower() == "b":
	print "You breaked one wood."
	wood = wood + 1
	print "You now have",wood
	print "Axe breaked."
else:
	print "No wood breaked."
print "Okay,now i think you have enough.Except if you breaked no wood.=)"
print "To craft a crafting bench you'll need 4 woods."
print "To craft it place 4 wood with space on each of them.Just type four o's."
answer = raw_input("")
clear()
if answer.lower() == "o o o o":
	print "You crafted a crafting bench."
	wood = wood - 4
else:
	print "No crafting bench crafted."
print "The crafted bench isn't just going to show up because you wanted it.It'll just show up when in need."
print "But you also need to type something to use it."
print "To use a crafting bench type c."
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
print "Okay,use the crafing table to make 3 sticks. 2 wood makes 5 sticks.But your only gonna need 3 but that's okay."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o o":
	print "You crafted five sticks."
	wood = wood - 2
	stick = stick + 5
else:
	print "No stick crafted."
print "Okay,now to craft wooden planks.Use the crafting table to craft 10 wooden planks.Every time you crafted 1,type c again."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "o":
	print "You crafted 1 wooden plank."
	plank = plank + 1
	wood = wood - 1
	print "You now have",plank
else:
	print "No wooden plank crafted."
print "Now that you have wooden planks,it's time to trade!Type t to trade."
keyword = raw_input("")
clear()
if keyword.lower() == "t":
	print ""
else:
	print "Wrong keyword.Error."
	exit()
answer = raw_input("Librarian:3 stones for 10 wooden planks.Press Enter to trade.")
clear()
wood = int(answer)

if wood <= 0:
	print "You dont have enough wooden planks.Try restarting the game."
	exit()
else:
	print "You traded 10 wooden planks for 3 stones."
	planks = planks - 10
	stone = stone + 3
print "Now,to craft a stone pickaxe.You know what to do.Use the crafting table to craft it."
keyword = raw_input("")
clear()
if keyword.lower() == "c":
	print ""
else:
	print "Error opening the crafting bench.Wrong keyword.Try restarting the game."
	exit()
answer = raw_input("What would you like to craft?:")
clear()
if answer.lower() == "/ / / @ @ @":
	print "You crafted one stone pickaxe."
	stone = stone - 3
	stick = stick - 3
	pickaxe = pickaxe + 1
else:
	print "No pickaxe crafted.Try restarting the game."
	exit()


	















































































































































































































   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    








	

		



