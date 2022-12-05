
import json
import random
import time
import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class WOFPlayer():
    prizeMoney = 0
    prizes = []
    
    def __init__(self, name):
        self.name = name
        
    def addMoney(self, amt):
        self.prizeMoney += amt
         
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        state = f"{self.name} has (${str(self.prizeMoney)})"
        return state

player = WOFPlayer("Mateus Maris")
player.addMoneyF(200)
print(player)

    
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscured_phrase, guess):
        self.category = category
        self.obscured_phrase = obscured_phrase
        self.guess = guess
        guess = input(f"{WOFPlayer.state}\n\nCategory: {self.category}\n\nPhrase:  {self.obscured_phrase}\n\nGuessed: {self.guess}\n\nGuess a letter, phrase, or type 'exit' or 'pass': ")
        return guess
        
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"




####################################################################################

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }

# DONE
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")

# DONE
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())
        
        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"

# DONE
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

category, phrase = getRandomCategoryAndPhrase()

guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

print("\n{}\n".format("-"*5))

print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]), obscurePhrase(phrase, guessed)))

print("\n{}\n".format("-"*5))

obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}".format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]), showBoard(phrase, obscured_phrase, guessed)))

print("\n{}\n".format("-"*5))

num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())
    print("\n")


print("\n{}\n".format("-"*5))

print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")

time.sleep(2)

print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10: ', 1, 10))
