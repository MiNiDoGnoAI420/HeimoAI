# Import requied modules.
import time, random

# The dictionary the program is gonna use.

dictionary = [    
    "vittu ",
    "saatana ",
    "perkele ",
    "päivää ",
    "helvetti ",
    "paska ",
    "jumalauta ",
    "joo ",
    "tyhmä ",
    "ah ",
    "kusipää ",
    "niin että ",
    "eieiei ",
    "hyvä ",
    "nyt "
]

# Function to convert string to ASCII value array 
# and return it's average multiplied with it's length as result.

def strToAscii(str):
    array = []
    num = 0
    for c in str:
        array.append(ord(c))
        num += ord(c)
    return int(num / len(str)) * len(str)

# Print function that prints characters with delay 
# to provide ChatGPT-like text generating.

def dprint(string, delay):
    for c in string:
        print(c, end='', flush=True)
        time.sleep(delay)

# Get input from the user and use it's characters ASCII
# values multiplied with it's length as the random seed.
        
question = input("User (Question) > ")
random.seed(strToAscii(question.lower()))
print("HeimoAI > ", end='', flush=True)

# How many words is there already in the current sentence?
wordsInSentence = 1

# Is there already a comma in the current sentence?
commaInCurrentSentence = False

# Was the sentence just created?
newSentenceJustCreated = False

# Last word printed out:
lastWord = random.choice(dictionary)

for num in range(random.randint(75, 125) + 1):
    newSentenceJustCreated = False
    lastWord = random.choice(dictionary)

    # If this is the first word in the sentence, capitalize it.
    if wordsInSentence == 1:
        dprint(lastWord.capitalize(), 0.025)

    # Else print it in lowercase.    
    else:
        dprint(lastWord, 0.025)

    # If there is 7 words in sentence, end it with
    # period or continue with a comma.
        
    if wordsInSentence > 7:

        # (If the sentence will end or go on is random.)

        if random.randint(1, 10) < 5:
            print("\b.")
            wordsInSentence = 0
            newSentenceJustCreated = True
            commaInCurrentSentence = False
        
        else:

            if not commaInCurrentSentence:
                print("\b, ", end="", flush=True)
                wordsInSentence = random.randint(3, 4)
                commaInCurrentSentence = True

            # However, if there is already a comma at the sentence,
            # it will end no matter what.
                
            else:
                print("\b.")
                wordsInSentence = 0
                newSentenceJustCreated = True
                commaInCurrentSentence = False
    
    # Increase amount of words in sentence.
    wordsInSentence += 1

# If the sentence ends with comma, remove it.
# (And end with period.)
    
if lastWord.endswith(", "):
    print("\b\b.")

# Or if the sentence isn't new, end with period.
    
elif not newSentenceJustCreated:
    print("\b.")