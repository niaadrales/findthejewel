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
log = 0
stone2 = 0
cobblestone2 = 0
diamond2 = 0
iron = 0
stick2 = 0
wpick = 0
ipick = 0
dpick = 0
spick = 0
siron = 0
obsidian = 0
woods = 0
stick3 = 0
wsword = 0
killed = 0
keys = 0
run = 0
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
instagram = """NMMMMMMMMMMMMMMMMMMMMMN         
      7MMMMMMMMMMMMMMMMMMMMMMMMM?       
     $MMMMMMMMMMMMMMMMMMMMMM   MM7      
     MMMMMMMMMMMMMMMMMMMMMMM   MMM      
    +MMMMMMMMMM7       .MMMMMMMMMM7     
    ?MMMMMMMM:           ~MMMMMMMM8     
    ?MMMMMMM.   .MMMMM.    MMMMMMM8     
    ?MMMMMM$   MMMMMMMMM   OMMMMMM8     
    ?MMMMMM   :MMMMMMMMM.   MMMMMM8     
    ?MMMMMM.  =MMMMMMMMM~   MMMMMM8     
    ?MMMMMM+   MMMMMMMMM   +MMMMMM8     
    ?MMMMMMM    NMMMMMD    MMMMMMM8     
    ?MMMMMMMM.            MMMMMMMM8     
    +MMMMMMMMMM         MMMMMMMMMMO     
    .MMMMMMMMMMMMMMMMMMMMMMMMMMMMM      
     MMMMMMMMMMMMMMMMMMMMMMMMMMMMM      
      MMMMMMMMMMMMMMMMMMMMMMMMMMM       
        MMMMMMMMMMMMMMMMMMMMMMM         """
facebook = """..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM...
.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM,.
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8
MMMMMMMMMMMMMMMMMMMMMMMM .......MMMMMMMM
MMMMMMMMMMMMMMMMMMMMMM..........MMMMMMMM
MMMMMMMMMMMMMMMMMMMMM...........MMMMMMMM
MMMMMMMMMMMMMMMMMMMM............MMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMM.................MMMMMMMM
MMMMMMMMMMMMMMM.................MMMMMMMM
MMMMMMMMMMMMMMM.................MMMMMMMM
MMMMMMMMMMMMMMM.................MMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM... ..MMMMMMMMMMMMMD
MMMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMMM.
.MMMMMMMMMMMMMMMMMMM......MMMMMMMMMMMM=.
. MMMMMMMMMMMMMMMMMM .....MMMMMMMMMMM ..
.... ?MMMMMMMMMMMMMM......MMMMMMM$  ...."""
snapchat = """...... ......+MMMMMMMMMMM+..............
 .....  ..MMMMMMMMMMMMMMMMMMM...........
 ..  ..DMMMMMMMMMMMMMMMMMMMMMMMM........
 ....=MMMMMMMMMMMMMMMMMMMMMMMMMMM?......
... MMMMMMMMMMMMMD. .ZMMMMMMMMMMMMM.....
 ..MMMMMMMMMMM:..........MMMMMMMMMMM....
 .MMMMMMMMMMM.............MMMMMMMMMMM ..
.MMMMMMMMMMM              .MMMMMMMMMMM .
:MMMMMMMMMMM               MMMMMMMMMMM:.
MMMMMMMMMMMM               MMMMMMMMMMMM.
MMMMMMMMMMMM               MMMMMMMMMMMM 
MMMMMMMMM..                   MMMMMMMMM7
MMMMMMMMMMZ                 $MMMMMMMMMMM
MMMMMMMMMMMM               MMMMMMMMMMMM7
MMMMMMMMMMM                 MMMMMMMMMMM 
MMMMMMMMM8.  ..   ...        ?MMMMMMMMM.
:MMMMM7 ...       .             ?MMMMM: 
.MMMMM+ ...............  .      +MMMMM  
  MMMMMMMM.  . .  ...        MMMMMMMM   
...MMMMMMMMMMMM         MMMMMMMMMMMM.   
  ..MMMMMMMMMMMMMN, .MMMMMMMMMMMMMM.    
  ...+MMMMMMMMMMMMMMMMMMMMMMMMMMM7      
.......NMMMMMMMMMMMMMMMMMMMMMMMM.. ..  .
  ........MMMMMMMMMMMMMMMMMMM.          
  .........  =MMMMMMMMMMM+     ..    . .
  .........                             """
youtube = """:78MMMMMMMMMMMMMMMMMMMD$=        
  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   
.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM. 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
MMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMMM:
MMMMMMMMMMMMMM      MMMMMMMMMMMMMMMMMMM7
MMMMMMMMMMMMMM        .MMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMM           .MMMMMMMMMMMMMM
MMMMMMMMMMMMMM           MMMMMMMMMMMMMMM
MMMMMMMMMMMMMM        MMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMM    .MMMMMMMMMMMMMMMMMMMM7
MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMMMMMM:
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 
=MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+ 
 +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM?  
     ~DMMMMMMMMMMMMMMMMMMMMMMMMMD~ .    """
vine = """ MMMMMMMMMM        
                    ,MMMMMMMMMMMM.      
                    MMMMMMMMMMMMMM      
    .MMMMM7        MMMMMM   ?MMMMM.     
     MMMMMM        MMMMM.    MMMMM=     
     MMMMMM        MMMMM     MMMMM.     
     .MMMMM.       MMMMMD   ,MMMMM.     
      MMMMMM       NMMMMM   :MMMMM      
      MMMMMM        MMMMMM    .  .      
       MMMMMO        MMMMMMM            
       MMMMMM         MMMMMMMMMMMM=     
        MMMMMM         .MMMMMMMMMM+     
        ZMMMMM~          MMMMMMMMO      
         MMMMMM         MMMMMM          
          MMMMMM       MMMMMM           
          .MMMMMM.   ,MMMMMM            
           .MMMMMMM MMMMMMZ             
             MMMMMMMMMMMM.              
              MMMMMMMMMM                
                MMMMMM                  
                                   """

time.sleep(1)
name1 = raw_input("Please type your name here.---> ")
clear()
if name1.lower() == "nia":
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
print "Loading game....."
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
print "What has a tail and a head but no body?"
waitfor("penny","Your answer is wrong,try again.")
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

raw_input("The cobblestones looks like this.---> @.Or an at.(Press Enter)")

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
waitfor("o o","There's no crafting recipe like that,try again.")
wood = wood - 2
stick = stick + 5
print "Okay,now to craft wooden planks.Use the crafting table to craft 10 wooden planks"
while plank <= 9:
	planks = raw_input("What would you like to craft?:")
	clear()
	if planks == "o":
		plank = plank + 1
		print "You now have",plank 
		if plank == 1:
			print "You need to keep doing that until you have 10 wooden planks."
print "Now that you have wooden planks,it's time to trade!Type t to trade."
waitfor("t","You typed the wrong keyword,try again.")
answer = raw_input("Librarian:3 stones for 10 wooden planks.Press Enter to trade.")
clear()
stone = stone + 3
plank = plank - 10
print "Now,to craft a stone pickaxe.You know what to do.Use the crafting table to craft it."
waitfor("/ / / @ @ @","There's no crafting recipe like that,try again.")
pickaxe = pickaxe + 1
stick = stick - 3
stone = stone - 3
print "Time to trade.Type t to trade."
waitfor("t","You typed the wrong keyword,try again.")
answer = raw_input("Blacksmith:10 cobblestones for 1 pickaxe.Press Enter to trade.")
clear()
print "You traded 1 pickaxe for 10 cobblestones."
pickaxe = pickaxe - 1
cobblestone = cobblestone + 10
print "Now that you have cobblestones trade them for the next villager.Time to trade.Type t to trade."
waitfor("t","You typed the wrong keyword,try again.")
answer = raw_input("Chef:2 emeralds for 10 cobblestones.Press Enter to trade.")
clear()
print "You traded 10 cobblestones for 2 emeralds."
cobblestone = cobblestone - 10
emerald = emerald + 2
print "Time to trade!Again!Type t to trade."
waitfor("t","You typed the wrong keyword,try again.")
answer = raw_input("Miner:1 diamond for 2 emeralds.Press Enter to trade.")
clear()
print "You traded 2 emeralds for 1 diamond."
emerald = emerald - 2
diamond = diamond + 1
print "Now,this is the final trade.Type t to trade."
waitfor("t","You typed the wrong keyword,try again.")
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
answer = raw_input("To get it,you need to pass 3 puzzles.The snatcher dealed with you that if you pass his puzzle,you will get the two jewels.Every puzzle has points.You need to give it to the snather,and the 2 jewels will be yours.(Press Enter)")
clear()
answer = raw_input("First one is the wizard riddles.To pass that puzzle,you need to answer some riddles.(Press Enter)")
clear()
answer = raw_input("Second one is minecraft madness.To pass that puzzle,you will need to do the same thing on level 2.Well different i guess.I'ts just like the one you did on level 2.(Press Enter)")
clear()
answer = raw_input("Third one is Boss Math Battle.You will be battling Boss Math.To pass that puzzle,you need to answer some math questions.(Press Enter)")
clear()
answer = raw_input("Press Enter to start the first puzzle.")
clear()
print "First riddle:What kind of table is good for you to eat?"
waitfor("vegetable","Your answer is wrong,try again.")
print "Your answer is correct!Now,for the second riddle."
print "Second Riddle:What season does humpty-dumpty hate the most?"
waitfor("the fall","Your answer is wrong,try again.")
print "Your answer is correct!Now,for the final riddle."
print "Final Riddle:What is the sun's favourite day of the week?"
waitfor("sunday","Your answer is wrong,try again.")
print "Your answer is correct!You got 1 point."
point = point + 1
answer = raw_input("Press enter to start the 2nd puzzle.")
clear()
answer = raw_input("You were locked up in a room that is tightly covered with obsidian.(Press Enter)")
clear()
answer = raw_input("You need to craft a diamond pickaxe for that though.(Press Enter)")
clear()
answer = raw_input("There is a furnace,a crafting table,3 iron ore,some trees,3 stones,and 3 diamond ores.(Press Enter)")
clear()
answer = raw_input("Now,to start the puzzle,break some wood.(Press Enter)")
clear()
log = int(log)

while log <= 12:
	logs = raw_input("Type b to break wood.")
	clear()
	if logs.lower() == "b":
		log = log + 1
		print "You now have",log
	if log <= 1:
		print "You need 12 more."
print "Okay,now craft 3 sticks.Type this to craft it.---> o o."
print "2 woods,makes 5 sticks."
while True:
	sti = raw_input("What would you like to craft?:")
	clear()
	if sti.lower() == "o o":
		break
	print "There's no crafting recipe like that,try again."
stick2 = stick2 + 5
log = log - 2
print "Okay,now that you have enough things,craft a wooden pickaxe."
print "To craft a wooden pickaxe,type this.---> / / / o o o(With space)"
waitfor("/ / / o o o","There's no crafting recipe like that,try again.")
wpick = wpick + 1
log = log - 3
stick2 = stick2 - 3
print "Okay,now that you have a wooden pickaxe,break some stone."
print "To break stone type m."
stone2 = int(stone2)

while stone2 <= 2:
	stones = raw_input("")
	clear()
	if stones.lower() == "m":
		stone2 = stone2 + 1
	if stone2 <= 1:
		print "You need 2 more."
print "Now,craft sticks again."
waitfor("o o","There's no crafting recipe like that,try again.")
stick2 = stick2 + 5
log = log - 2
print "Now that you have enough things,craft a stone pickaxe."
print "To craft it,type this.---> / / / @ @ @"
waitfor("/ / / @ @ @","There's no crafting recipe like that,try again.")
spick = spick + 1
stone2 = stone2 - 3
stick2 = stick2 - 3
wpick = wpick - 1
print "Wooden pickaxe breaked."
print "Okay,now that you have a stone pickaxe,break some iron ore."
print "To break iron ore,type mi."
iron = int(iron)

if iron <= 2:
	irons = raw_input("")
	clear()
	if irons == "mi":
		iron = iron + 1
	if iron <= 1:
		print "You need 2 more."
spick = spick - 1
print "Stone Pickaxe breaked."
print "Okay,to smelt it,use sticks as coal."
print "To smelt iron,type si"
siron = int(siron)

while siron <= 2:
	sirons = raw_input("")
	clear()
	if sirons.lower() == "si":
		siron = siron + 1
		iron = iron - 1
		print "You now have",siron
	if siron <= 1:
		print "You need 2 more."
print "Okay,now craft sticks.Type o o."
waitfor("o o","There's no crafting recipe like that,try again.")
stick2 = stick2 + 5
print "Now craft an iron pickaxe.To craft an iron pickaxe,type / / / * * *(With space)"
waitfor("/ / / * * *","There's no crafting recipe like that,try again.")
ipick = ipick + 1
stick2 = stick2 - 3
siron = siron - 3
print "To mine a diamond ore,type md."
diamond2 = int(answer)

while diamond2 <= 2:
	answer = raw_input("")
	clear()
	if answer.lower() == "md":
		diamond2 = diamond2 + 1
	if diamond2 <= 1:
		print "You need 2 more."
print "Iron Pickaxe breaked."
ipick = ipick - 1
print "Okay,now craft a stick."
waitfor("o o","There's no crafting recipe like that,try again.")
stick2 = stick2 + 5
print "Now craft a diamond pickaxe.To craft one,type / / / $ $ $(With space)"
waitfor("/ / / $ $ $","There's no crafting recipe like that,try again.")
stick2 = stick2 - 3
diamond2 = diamond2 - 3
dpick = dpick + 1
print "Okay,be ready,this is the final one.The diamond will not last with more than 3 obsidian."
print "Your only gonna be able to break 2 obsidians.To break obsidians type mo."
obsidian = int(answer)

while obsidian <= 1:
	answer = raw_input("")
	clear()
	if answer.lower() == "mo":
		obsidian = obsidian + 1
	if obsidian <= 1:
		print "Keep doing it!"
dpick = dpick - 1
print "Diamond pickaxe breaked"
print "You finished the 2nd level!That was the hardest one though."
point = point + 1
print "You now got",point
print "The third puzzle,much like a test maybe.But,Boss Math is going to speak to you so...Baii!!!"
print "And also,i will give you all the answer choices after he speaks."
time.sleep(5)
print "Loading....."
time.sleep(2)
print "Boss Math:I AM BOSS MATH!THE BOSS OF THE MATH.HOW DO YOU SAY IT?"
time.sleep(2)
print "Assistant:The boss of the entire math."
time.sleep(2)
print "Boss Math:THE BOSS OF THE ENTIRE  MATH."
time.sleep(2)
print "Boss Math:YOU DIE OR LIVE I'M STILL LIVING."
time.sleep(2)
print "Assistant:That's so lame boss."
time.sleep(2)
print "Boss Math:IT'S OK!IT'S MY TURN TO SPEAK!"
time.sleep(2)
print "Assistant:Sorry boss."
time.sleep(2)
print "Oh,i thought it was real,but,it turns out to be a hologram."
time.sleep(2)
print "Well,let's start this shall we?"
time.sleep(2)
print "Boss Math:THE FIRST WORD PROBLEM IS:JOHNY AND HIS FRIEND WENT OUT FOR A WALK,JOHNY FOUND SOME BEAUTIFUL STONES,AND HIS FRIEND HASN'T.JOHNY HAVE 10 STONES.JOHNY GAVE 5 TO HIS FRIEND.HOW MANY WERE LEFT TO JOHNY?"
time.sleep(2)
print "That one's easy,i dont need to tell you the choices."
print "How many were left to johny?"
waitfor("5","Your answer is wrong,try again.")
time.sleep(1)
print "Boss Math:DON'T CELEBRATE YET.YOU STILL HAVE MORE WORD PROBLEMS."
time.sleep(2)
print "Boss Math:THE SECOND WORD PROBLEM IS:JOHNY BOUGHT A BOOK AND A PEN,IF IT COST 1,000,000 DOLLARS AND 1 DOLLAR,HOW MUCH DID HE PAY?"
time.sleep(2)
print "You can beat this boss in no time man!"
while True:
	answer = raw_input("How much did Johny pay?No need to put a dollar sign or whatever,just the number.: ")
	clear()
	if answer == "1,000,001":
		break
	print "What?Still can't do it?That one's sooo easy man!Try again."
time.sleep(1)
print "Boss Math:I SEE...YOUR REALLY GOOD AT MATH HUH?WELL,TRY THIS!:JOHNY EATS 2 ORANGES IN A DAY,HOW MANY WILL HE EAT IN THE MONTH OF MARCH,2018?"
time.sleep(3)
print "Easy too.."
while True:
	answer = raw_input("How many will he eat in the month of march 2018?")
	clear()
	if answer == "62":
		break
	print "OMG your killin' meh!!!That's so easy!Try again!"
time.sleep(1)
print "Boss Math:OH MY GOSH!I CAN'T TAKE IT ANYMORE!HERE'S YOUR POINT,GO AWAY NOW!"
time.sleep(2)
point = point + 1
print "Good job,now let's give all the points to the snatcher."
time.sleep(2)
print "Loading....."
time.sleep(2)
print "Snatcher:Here ya go,tnx!"
point = point - 3
jewel = jewel + 2
score = score + 5
print "Well done!You got the jewel!Now,level 4..."
time.sleep(2)
print "Level 4,hmmm......"
time.sleep(2)
print "Loading....."
time.sleep(2)
print "In Level 4,let me see.....Oh!This is fun!"
time.sleep(2)
print "You need to guess the right social media on the icon that shows up."
time.sleep(1)
print "First one:"
print instagram
waitfor("instagram","Your answer is wrong try again.")
time.sleep(1)
print "Second one:"
print facebook
time.sleep(1)
while True:
	answer = raw_input("Your Answer: ")
	clear()
	if answer.lower() == "facebook":
		break
	print "Your answer is wrong,try again."
	print facebook
time.sleep(1)
print "Too easy?Try this!"
print snapchat
while True:
	answer = raw_input("Your answer: ")
	clear()
	if answer.lower() == "snapchat":
		break
	print "Your answer is wrong,try again."
	print snapchat
time.sleep(1)
print "Well,the next one's easy though."
print youtube
while True:
	answer = raw_input("Your answer: ")
	clear()
	if answer.lower() == "youtube":
		break
	print "Your answer is wrong,try again."
	print youtube
time.sleep(1)
print "Well,i bet you can't answer this!"
print vine
waitfor("vine","Your answer is wrong,try again.")
print "Congratulations!You got the jewel!"
jewel = jewel + 1
score = score + 5
raw_input("Now,onto the next level.Level 5!!!Your almost there.(Press Enter)")
clear()
raw_input("So for level 5,you were walking.Then,you were knocked out by someone.(Press Enter)")
clear()
raw_input("You woked up on a room,that is tightly locked.Nobody gets in,and nobody gets out.(Press Enter)")
clear()
raw_input("You were being tested by the group called,'Ract'.Lame right?(Press Enter)")
clear()
raw_input("You will die soon,because they will get all your blood,just to make a medicine.(Press Enter)")
clear()
raw_input("So you need to find a way out before it's too late.They also have a jewel,you should go get it too.(Press Enter)")
clear()
raw_input("The key is being guarded by the security guard,you need to get it.(Press Enter)")
clear()
raw_input("To get it,you need to craft again.There's some plant's over there,they are kinda big.You need 9 wood.(Press Enter)")
clear()
print "To break it,type bw."
while woods <= 8:
        answer = raw_input("")
        clear()
        if answer.lower() == "bw":
                woods = woods + 1
        if woods <= 1:
                print "You need 8 more."
print "Okay,now craft a crafting table.Type 4 o's again with space on each."
waitfor("o o o o","There's no crafting recipe like that,try again.")
woods = woods - 4
print "Okay,now craft sticks.Type 2 o's again with space on each."
waitfor("o o","There's no crafting recipe like that,try again.")
stick3 = stick3 + 5
print "Now,craft a sword.Type this.---> o o /"
waitfor("o o /","There's no crafting recipe like that,try again.")
wsword = wsword + 1
stick3 = stick3 - 1
woods = woods - 2
print "Okay,to attack type a."
print "On,my signal."
time.sleep(1)
print "3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
print "Go!!!!Just keep typing a 20 times!"
while killed <= 19:
        answer = raw_input("")
        clear()
        if answer.lower() == "a":
                killed = killed + 1
                print "You killed",killed
        if killed <= 1:
                print "Type a 19 more!GO!!!!"
print "That was...So scary!Well,it was fun though,for me."
time.sleep(1)
answer = raw_input("Was it fun?Y/N: ")
if answer.lower() == "y":
        print "Good!Because,you and i enjoyed it."
else:
        print "Well,okay."
time.sleep(1)
print "Now,you need to take the key,and unlock the door."
time.sleep(2)
print "Type e to take it."
waitfor("e","You typed the wrong keyword,try again.")
keys = keys + 1
print "Okay,type o to unclock the door."
waitfor("o","You typed the wrong keyword try again.")
keys = keys - 1
print "Now,take the jewel,type ej to take it."
waitfor("ej","You typed the wrong keyword,try again.")
jewel = jewel + 1
score = score + 5
print "Now,escape!!!!Keep typing r 20 times to escape!"
while run <= 19:
        answer = raw_input("")
        clear()
        if answer.lower() == "r":
                run = run + 1
        if run <= 1:
             print "Go!!!!19 more!!!"
print "Now,take a deep breath.Type d to take a longgg niceee breathhhhh..."
waitfor("d","C'mon,that's the wrong one,try again.")
run = run - 20
print "Congratulations!!!!!!!You got 5 jewels and 25 points!!!!!!!"
print finaljewel
time.sleep(1)
print "Now,let's give this to the geany."
time.sleep(1)
print "Loading...."
time.sleep(1)
raw_input("Geany:Well done.You got the jewel.You may now go home.Stingaling ngaling...Boom boom zuming!(Press Enter)")
print "Geany:Well,he didn't say thank you."
time.sleep(1)
print "Well done!But i may now say,bye.Bye,my old friend.Sting!"
time.sleep(1)
answer = raw_input("THE END...Want a post credit?Y/N: ")
if answer.lower() == "y":
        print "Okay."
else:
        print "Mkay,bye!"
        exit()
print "(scary music playin)???:Hmm...",name1 + "huh?"
time.sleep(2)
print "Bring",name1 + "to me."
time.sleep(1)
print "Assistant:Yes sir."
time.sleep(1)
print "Rrr..."
time.sleep(2)
raw_input("To be continued...Press Enter to continue.")
clear()
print "Credits"
time.sleep(1)
print "Game by:niaadrales"
time.sleep(1)
print "Yo!What's up!I'm nia.The creator of the game!"
time.sleep(1)
print "I'm 10 years old,and,yeah."
time.sleep(1)
print "Wanna follow my social medias?Here:"
time.sleep(1)
print "Instagram:@miss_nia3810"
time.sleep(1)
print "Facebook:Nia Kristel Salas Adrales(I have many account there,so just follow all of them.It's so confusing."
time.sleep(1)
print "Pinterest:Nia Kristel"
time.sleep(1)
print "Wattpad:@miss_potpot"
time.sleep(1)
print "Youtube:Chibi 101"
time.sleep(1)
print "And,keep that preety smile on your face,and see ya!Peace out!"
time.sleep(1)
print "To be continued....."
