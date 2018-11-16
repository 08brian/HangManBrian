from turtle import *
from random import randint
import time

sw=600
sh=800

s=getscreen()
s.setup(sw, sh)
s.bgcolor('#16ffe0')
t=getturtle()
t.color('#fffbe8')
t.speed(0)
t.width(8)
t.hideturtle()


sWords = ['aberration','hockey','soccer','field','League','Legend','Chicago',\
          'Blackhawks','Lions','Apple']

tWriter = Turtle()
tWriter.hideturtle()

tBadLetters = Turtle()
tBadLetters.hideturtle()

alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
secretWord=""
displayWord=""
gameDone = False
lettersWrong = ""
lettersCorrect = ""
fails = 6
fontS = int(sh*0.045)

def displayText(newText):
    #print("displayText " + newText)
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sw*0.4),-int(sh*0.375))
    tWriter.write(newText, font=('Arial', fontS, 'bold'))

def displayBadLetters(newText):
    #print("displayText " + newText)
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sw*0.4),int(sh*0.36))
    tBadLetters.write(newText, font=('Arial', fontS, 'bold'))

def chooseWord():
    global secretWord
    secretWord = sWords[randint(0,len(sWords)-1)]
    #print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, secretWord, lettersWrong, lettersCorrect, alpha
    displayWord = ""
    for letter in secretWord:
        #print(letter)
        if letter in alpha:
            if letter in lettersCorrect:
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

    #print(displayWord)

def getGuess():
    boxTitle = "Letters Used" + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawRL()
    if fails == 2:
        drawLL()
    if fails == 1:
        drawRA()
    if fails == 0:
        drawLA()

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the Word!!"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess == secretWord:
        displayText("YES!!! " + secretWord + " is the word!!!")
        gameDone = True
    else:
        displayText("NO!!! " + guess + " is not the word!!!")
        time.sleep(1)
        displayText(displayWord)
        fails -=1
        updateHangmanPerson()
        

def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("NO!!! " + theGuess + " only one letter, please!")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("NO!!! " + theGuess + " not a letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        else:
            displayText("NO!!! " + theGuess + " is not in word!!!!")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Nott in word: {" + lettersWrong + "}")
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()

def drawGallows():
    t.penup()
    t.setheading(0)
    t.goto(-int(sw/4), -int(sh/4))
    t.pendown()
    t.forward(int(sw*0.6))
    t.backward(int(sw*0.1))
    t.left(90)
    t.forward(int(sh*0.6))
    t.left(90)
    t.forward(int(sw*0.3))
    t.left(90)
    t.forward(int(sh*0.1))

def drawHead():
    hr=int(sw*0.07)
    t.penup()
    t.goto(t.xcor()-hr, t.ycor()-hr)
    t.pendown()
    t.circle(hr)
    t.penup()
    t.left(90)
    t.goto(t.xcor()+hr, t.ycor()-
           hr)
    t.right(90)


def drawTorso():
    t.pendown()
    t.forward(int(sh*0.2))

def drawRL():
    t.left(25)
    t.forward(100)
    t.left(180)
    t.forward(100)
def drawLL():
    t.left(130)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(25)
    t.forward(130)
    t.right(160)
def drawRA():
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(140)
def drawLA():
    t.forward(100)



    
drawGallows()
drawHead()
drawTorso()
drawRL()
drawLL()
drawRA()
drawLA()
time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
playGame()
