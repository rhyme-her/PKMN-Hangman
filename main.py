# Simple Algorithm
    # 1. Program is executed.
    # 2. Player can pick between the four categories or exit.
    # 3. Player clicks category. Program picks a random line in category list.
    # 4. GUI displays keyboard.
    # 5. Player can click ATTACK, RUN.
    # 5.1. Attack opens up the keyboard.
    # 5.2. Run prompts the user if they would like to return to the main menu.
    # 6.1. If player fails, the answer is revealed and is asked to exit or resume playing.
    # 6.2. If player is correct, the player is asked to exit or resume playing/
    # 7.1. If player exits, program closes.
    # 7.2. If player decides to continue, go to back to main menu and repeat step 2.
    # The player can also choose to catch the Pokemon. If Hp is less than half, then 1/6. If less than 1/4 , catch chance will be 1/2.
        # If successful, the word is shown (w/victory).

# Graphic Notes
    # Stoke Value = 5
    # Yellow: ffcb05
    # Blue: 2d70b7

# Menu
    # Click.
    # If the button is clicked, deactivate it and send information to engine

from graphics import *
from button import *
from random import *
from time import * 

def menu(win):
    try:
        win.setCoords(0,0,59,59)
        menu = Image(Point(30,30),"menu2.gif")
        menu.draw(win)

        box1= button(win,Point(30,45),50,8," ")
        box2= button(win,Point(30,35),50,8," ")
        box3= button(win,Point(30,25),50,8," ")
        box4= button(win,Point(30,15),50,8," ")
        box5= button(win,Point(10,5),10,4,"")
        box1.boxstylepokemon()
        box2.boxstylepokemon()
        box3.boxstylepokemon()
        box4.boxstylepokemon()
        box5.boxstylepokemon()
        text1 = Image(Point(30,45),"names.gif")
        text2 = Image(Point(30,35),"items.gif")
        text3 = Image(Point(30,25),"attacks.gif")
        text4 = Image(Point(30,15),"abilities.gif")
        text5 = Image(Point(10,5),"exit.gif")
        text1.draw(win)
        text2.draw(win)
        text3.draw(win)
        text4.draw(win)
        text5.draw(win)
        x = ""
        listsize = 0
        listname = ""
        while x == "":
            click = win.getMouse()
            if box1.clicked(click):
                listsize = 721
                listname = "pokemon.txt"
                x = "a"
            if box2.clicked(click):
                listsize = 424
                listname = "items.txt"
                x = "b"
            if box3.clicked(click):
                listsize = 620
                listname = "attacks.txt"
                x = "c"
            if box4.clicked(click):
                listsize = 192
                listname = "abilities.txt"
                x = "d"
            if box5.clicked(click):
                win.close()
                x = "."
                break

        if x != ".":
            engine(win,listname,listsize)
        text1.undraw()
        text2.undraw()
        text3.undraw()
        text4.undraw()
        text5.undraw()
        box1.undraw()
        box2.undraw()
        box3.undraw()
        box4.undraw()
        box5.undraw()
        menu.undraw()
    except:
        KeyboardInterrupt()


#-------------------------


def correctorwrong(word,lettercount,v,listofletters,answers,guess,button):
    x = ""
    cia = answers.count(v)
    if cia == 0:
        x = "not answered"
#------------------------- The section above checks if it is answeered.
    if x == "not answered":
        TorF = False
        for i in range(lettercount):
            if word[i] == v:                    # If the letter is correct:
                if i == 0:
                    v = v.upper()               # Capital for first letter.
                    listofletters[i] = v        # Indexing.
                    v = v.lower()               # Return back to lower case value.
                else:
                    listofletters[i] = v
                TorF = True                     # It will stay true for the rest of the if statement.
                answers = answers + v

        if TorF == False:                       # Wrong Answer
            guess = guess + 1                   # Adds 1 for being incorrect.
            answers = answers + v
            button = "red"

        if TorF == True:
            button = "green"

        return (listofletters,answers,guess,button,x)




#-------------------------


def colorcheck(guess):       #USER HP -> Integers only
    x = "green"
    if guess >= 3:
        x = "yellow"
    if guess >= 5:
        x = "red"
    return x




#-------------------------
def colorcheck2(guess):     #OPPONENT HP (Has to be done separately due to the way it's calculated)
    x = "green"
    if guess <= 0.5:
        x = "yellow"
    if guess <= 0.20:
        x = "red"
    return x



#-------------------------

def rngcatch(value):        #Random Number Generation for determining if capture is true.
    if value > 0.5:
        x = randrange(1,21) #1/20 chance
    elif value <= 0.25:
        x = randrange(1,3)  #1/2 chance
    elif value <= 0.5:
        x = randrange(1,7)  #1/6 chance

    if x == 1:
        rng = True
        pokeball = randrange(1,60) #Fun extra
        pokeballist =["poke.gif","great.gif","ultra.gif",]
        if pokeball <= 30:
            pokeball = pokeballist[0]
        elif pokeball <= 45:
            pokeball = pokeballist[1]
        elif pokeball <= 55:
            pokeball = pokeballist[2]
        else:
            pokeball = "master"

        return rng, pokeball
    else:
        pokeball = "failure"
        rng = False
        return rng,pokeball

    return x




# -------------------------------------------------------------------- GAME ENGINE
def engine(win,pokelist,maxnum):
    try:
        ffile = open(pokelist,"r") # File is opened.
        x = randrange(1,maxnum)
        z,guess,remainder = 0,0,0
        TorF= False
        answers = ""
        word = ""
        letteraz = "abcdefghijklmnopqrstuvwxyz"
        text = ""
        runaway = False
        opponentoruserhp = False
        catch = False       # For catching game mechanic.
        continueorexit = False
        pokeball = True
        rng = False
        winner = False # Reveals the true answer later.



#------------------------- Values are defined early.
        for i in ffile:
            z = z + 1
            if z == x:                          #This means the program has arrived at the random line.
                word = i
                ffile.close()
                break
        print (word)
        word = word.lower()                     # Easier comparison for future use.
        lettercount = len(word) -1              #This will be used for indexing later.
        listofletters = "_ " * lettercount         # This will be what is edited.
        listofletters = listofletters.split()       # It's a list so it can be manipulated.

        spacecount = word.count(" ")                # This will check for spaces.
        count2 = word.count("2")                    #There is one word with a number.
        if spacecount >= 1 or count2 == 1:
            for i in range (lettercount):
                if word[i] == " ":
                    listofletters[i]=" "
                if word[i] == "2":
                    listofletters[i]="2"




#------------------------- Draw Graphics
        win.setCoords(0,0,59,59)                    #-- Seems odd why I restate it here. If the player continues this is in place
        backdrop = Image(Point(30,30),"img.gif")    #   -- So the background can be properly centred.
        backdrop.draw(win)
        win.setCoords(0,0,512,512)
        letterscompiled = " ".join(listofletters)
        lineonscreen = Text(Point(256,200),letterscompiled)
        lineonscreen.draw(win)
        lineonscreen.setStyle("bold")
        lineonscreen.setSize(24)



#------------------------- Opponent and User Sprites + HP Bars(Extra)
        enemyno = randrange(1,721)
        if pokelist == "pokemon.txt":
            enemyno = x                  # Fun easter egg. The Pokemon name will correspond with the image when it is this category.
        if enemyno > 232 and x < 522:
            enemyno = enemyno + 1       # Fixs bug where program would start displaying the wrong Pokemon at these points in the list
        enemyno = "/monster" + str(enemyno) + ".gif"
        enemyno = Image(Point(430,450),enemyno)
        enemyno.draw(win)               # Opponent Image

        usersprite = Image(Point(50,200),"user.gif")
        usersprite.draw(win)

        ox1,ox2 = 176,236
        ux1,ux2 = 392, 452
        oppohp = Rectangle(Point(ox1,440),Point(ox2,445)) #Bar is divisible by 6. The amount of chances you have.
        userhp = Rectangle(Point(ux1,135),Point(ux2,140))

        oppohp.draw(win)
        userhp.draw(win)

        oppohp.setFill("green")
        userhp.setFill("green")



#------------------------- Buttons
        letterq = button(win,Point(30,65),20,20,"Q")
        letterw = button(win,Point(60,65),20,20,"W")
        lettere = button(win,Point(90,65),20,20,"E")
        letterr = button(win,Point(120,65),20,20,"R")
        lettert = button(win,Point(150,65),20,20,"T")
        lettery = button(win,Point(180,65),20,20,"Y")
        letteru = button(win,Point(210,65),20,20,"U")
        letteri = button(win,Point(240,65),20,20,"I")
        lettero = button(win,Point(270,65),20,20,"O")
        letterp = button(win,Point(300,65),20,20,"P")

        lettera = button(win,Point(45,40),20,20,"A")
        letters = button(win,Point(75,40),20,20,"S")
        letterd = button(win,Point(105,40),20,20,"D")
        letterf = button(win,Point(135,40),20,20,"F")
        letterg = button(win,Point(165,40),20,20,"G")
        letterh = button(win,Point(195,40),20,20,"H")
        letterj = button(win,Point(225,40),20,20,"J")
        letterk = button(win,Point(255,40),20,20,"K")
        letterl = button(win,Point(285,40),20,20,"L")

        letterz = button(win,Point(60,15),20,20,"Z")
        letterx = button(win,Point(90,15),20,20,"X")
        letterc = button(win,Point(120,15),20,20,"C")
        letterv = button(win,Point(150,15),20,20,"V")
        letterb = button(win,Point(180,15),20,20,"B")
        lettern = button(win,Point(210,15),20,20,"N")
        letterm = button(win,Point(240,15),20,20,"M")

        run = button(win,Point(450,25),80,30,"")
        runtext = Image(Point(450,25),"run.gif")
        runtext.draw(win)
        catch = button(win,Point(450,60),80,30,"")
        catchtext = Image(Point(450,60),"catch.gif")
        catchtext.draw(win)



#-------------------------
        lettera.boxstylepokemon2()
        letterb.boxstylepokemon2()
        letterc.boxstylepokemon2()
        letterd.boxstylepokemon2()
        lettere.boxstylepokemon2()
        letterf.boxstylepokemon2()
        letterg.boxstylepokemon2()
        letterh.boxstylepokemon2()
        letteri.boxstylepokemon2()
        letterj.boxstylepokemon2()
        letterk.boxstylepokemon2()
        letterl.boxstylepokemon2()
        letterm.boxstylepokemon2()
        lettern.boxstylepokemon2()
        lettero.boxstylepokemon2()
        letterp.boxstylepokemon2()
        letterq.boxstylepokemon2()
        letterr.boxstylepokemon2()
        letters.boxstylepokemon2()
        lettert.boxstylepokemon2()
        letteru.boxstylepokemon2()
        letterv.boxstylepokemon2()
        letterw.boxstylepokemon2()
        letterx.boxstylepokemon2()
        lettery.boxstylepokemon2()
        letterz.boxstylepokemon2()
        run.boxstylepokemon2()
        catch.boxstylepokemon2()



#------------------------- Guessing Process

        while guess != 6 and runaway != True:                           # Amount of guesses until wrong.
            while text == "":
                click = win.getMouse()              # WAITING FOR CLICKS
                if lettera.clicked(click):
                    lettera.deactivate()
                    v = "a"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettera.color(color)

                if letterb.clicked(click):
                    letterb.deactivate()
                    v = "b"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterb.color(color)

                if letterc.clicked(click):
                    letterc.deactivate()
                    v = "c"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterc.color(color)

                if letterd.clicked(click):
                    letterd.deactivate()
                    v = "d"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterd.color(color)

                if lettere.clicked(click):
                    lettere.deactivate()
                    v = "e"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettere.color(color)

                if letterf.clicked(click):
                    letterf.deactivate()
                    v = "f"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterf.color(color)

                if letterg.clicked(click):
                    letterg.deactivate()
                    v = "g"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterg.color(color)

                if letterh.clicked(click):
                    letterh.deactivate()
                    v = "h"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterh.color(color)

                if letteri.clicked(click):
                    letteri.deactivate()
                    v = "i"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letteri.color(color)

                if letterj.clicked(click):
                    letterj.deactivate()
                    v = "j"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterj.color(color)

                if letterk.clicked(click):
                    letterk.deactivate()
                    v = "k"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterk.color(color)

                if letterl.clicked(click):
                    letterl.deactivate()
                    v = "l"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterl.color(color)

                if letterm.clicked(click):
                    letterm.deactivate()
                    v = "m"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterm.color(color)

                if lettern.clicked(click):
                    lettern.deactivate()
                    v = "n"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettern.color(color)

                if lettero.clicked(click):
                    lettero.deactivate()
                    v = "o"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettero.color(color)

                if letterp.clicked(click):
                    letterp.deactivate()
                    v = "p"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterp.color(color)

                if letterq.clicked(click):
                    letterq.deactivate()
                    v = "q"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterq.color(color)

                if letterr.clicked(click):
                    letterr.deactivate()
                    v = "r"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterr.color(color)

                if letters.clicked(click):
                    letters.deactivate()
                    v = "s"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letters.color(color)

                if lettert.clicked(click):
                    lettert.deactivate()
                    v = "t"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettert.color(color)

                if letteru.clicked(click):
                    letteru.deactivate()
                    v = "u"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letteru.color(color)

                if letterv.clicked(click):
                    letterv.deactivate()
                    v = "v"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterv.color(color)

                if letterw.clicked(click):
                    letterw.deactivate()
                    v = "w"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterw.color(color)

                if letterx.clicked(click):
                    letterx.deactivate()
                    v = "x"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterx.color(color)

                if lettery.clicked(click):
                    lettery.deactivate()
                    v = "y"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    lettery.color(color)

                if letterz.clicked(click):
                    letterz.deactivate()
                    v = "z"
                    listofletters,answers,guess,color,text = correctorwrong(word,lettercount,v,listofletters,answers,guess,button)
                    letterz.color(color)

                if run.clicked(click):
                    runaway = True
                    text = "dummy"

                if catch.clicked(click) and pokeball == True: # Can't capture with a capture ball.
                    pokeball = False
                    rng,pokeballs = rngcatch(remainder/lettercount)
                    text = "dummy"
                    catch.deactivate()
                    if rng == False:
                        fail = Image(Point(256,325),"fail.gif")
                        fail.draw(win)
                        sleep(2)
                        guess = guess + 1
                        fail.undraw()



            remainder = listofletters.count("_")                    # Used to check how many letters were answered. Will be used later.




#------------------------- HP GUI INDICATOR
            userhp.undraw()                                     #UNDRAW TO UPDATE COLOR
            ux2 = 452 - (10*guess)                              #DETERMINE HOW MUCH HEALTH LEFT
            userhp = Rectangle(Point(ux1,135),Point(ux2,140))
            userhp.draw(win)                                    #HP BAR
            hpcolor = colorcheck(guess)                         #RETRIEVE COLOR FOR HP BAR
            opponentoruserhp = False                            #BACK TO FALSE FOR THE NEXT LOOP
            userhp.setFill(hpcolor)                             #FILL HP BAR

            oppohp.undraw()                                     #UNDRAW TO UPDATE COLOR
            ox2 = 176 + ((remainder/lettercount)*60)            #RECEIVE PERCENTAGE
            oppohp = Rectangle(Point(ox1,440),Point(ox2,445))
            oppohp.draw(win)                                    #OPPONENT HP BAR DRAWN AGAIN
            hpcolor2 = colorcheck2((remainder/lettercount))   #CALCULATING HP
            oppohp.setFill(hpcolor2)



#------------------------- PROGRESS INDICATOR
            lineonscreen.undraw()
            letterscompiled = " ".join(listofletters)
            lineonscreen = Text(Point(256,200),letterscompiled)
            lineonscreen.draw(win) # -> updates the lines
            lineonscreen.setStyle("bold")
            lineonscreen.setSize(24)



#-------------------------
            text = ""             # Resets to being nothing for the next loop.
            if runaway == True: #Player chose to quit.
                guess = 6

            elif rng == True: # Player successfully captured.
                pokeballimg = Image(Point(0,0),pokeballs) #Extra animation
                pokeballimg.draw(win)
                for i in range(5):
                    pokeballimg.move(85,86)
                    sleep(0.5)
                pokeballimg.undraw()
                enemyno.undraw()
                enemyno = Image(Point(425,430),pokeballs) #Undrawn and changed to a Pokeball. Victory!
                enemyno.draw(win)
                guess = 6
                status = Image(Point(256,300),"capture.gif")
                status.draw(win)
                winner = True

            elif remainder == 0:  # Player guessed correctly.
                status = Image(Point(256,300),"victory.gif")
                status.draw(win)
                guess = 6
                winner = True
            elif remainder !=0 and guess == 6: # Player failed to answer.
                status = Image(Point(256,300),"gameover.gif")
                status.draw(win)

            else:
                print ("Answered", answers)





# ------------------------ Revealing the true answer.
        lineonscreen.undraw()
        word = word.capitalize()
        lineonscreen = Text(Point(256,180),word)
        lineonscreen.draw(win)
        lineonscreen.setStyle("bold")
        lineonscreen.setSize(24)
        if winner == True:
            lineonscreen.setTextColor("green")
        else:
            lineonscreen.setTextColor("red")




#------------------------- Post Game Options

        if runaway != True: # ---------> The user didn't run and the game prompts the user to respond.
            keepgoing = button(win,Point(128,250),100,30,"") #No need to draw it if runnaway was used.
            turnback = button(win,Point(384,250),100,30,"")
            keepgoinggif = Image(Point(128,250),"keepgoing.gif")
            turnbackgif = Image(Point(384,250),"mainmenu.gif")

            keepgoing.boxstylepokemon()
            turnback.boxstylepokemon()
            keepgoinggif.draw(win)
            turnbackgif.draw(win)

#-------------------------
            run.undraw()
            runtext.undraw() #------------ These are undrawn here to prevent players from clicking them.
            catch.undraw()
            catchtext.undraw()
            lettera.undraw()
            letterb.undraw()
            letterc.undraw()
            letterd.undraw()
            lettere.undraw()
            letterf.undraw()
            letterg.undraw()
            letterh.undraw()
            letteri.undraw()
            letterj.undraw()
            letterk.undraw()
            letterl.undraw()
            letterm.undraw()
            lettern.undraw()
            lettero.undraw()
            letterp.undraw()
            letterq.undraw()
            letterr.undraw()
            letters.undraw()
            lettert.undraw()
            letteru.undraw()
            letterv.undraw()
            letterw.undraw()
            letterx.undraw()
            lettery.undraw()
            letterz.undraw()


#------------------------- Wait for mouse click.

            while text == "":
                temp = False
                click = win.getMouse()
                if keepgoing.clicked(click):
                    continueorexit = True
                    text = "t"
                    temp = True #-------------> This allows the objects that don't apply to the run function to undraw.
                if turnback.clicked(click):
                    text = "f"
                    temp = True
                if temp == True:
                    status.undraw() #
                    turnback.undraw() #
                    keepgoing.undraw() # ------------ > These five are only defined here and will be undrawn.
                    keepgoinggif.undraw()
                    turnbackgif.undraw()

# ------------------------- Undraw some more stuff.
            backdrop.undraw()
            oppohp.undraw()
            userhp.undraw()
            lineonscreen.undraw()
            enemyno.undraw()
            usersprite.undraw()
#-------------------------- After undrawing everything. True or False redirects the player.
        if runaway == True or continueorexit == False:
            menu(win)

        else:
            engine(win,pokelist,maxnum)

    except:
        KeyboardInterrupt() #Mouse close.



def main():
# -------------------------------------------------------------------- Title Screen
    try:
        win = GraphWin("Hangman Pokemon Edition",512,512)
        win.setCoords(0,0,59,59)

# --------------------------------------------------------------------
        title = Image(Point(30,30),"title.gif")
        title.draw(win)
        instruction = Image(Point(30,5),"instructions.gif")
        instruction.draw(win)
# -------------------------------------------------------------------- Button
        gobutton = button(win,Point(30,20),15,4,"Click to play!!")
        gobutton.boxstylepokemon()

        x = ""
        while x != "OK":
            click = win.getMouse()
            if gobutton.clicked(click):
                gobutton.deactivate()
                x = "OK"
        gobutton.undraw()
        title.undraw()
        instruction.undraw()
        menu(win)
    except:
        KeyboardInterrupt()
main()
