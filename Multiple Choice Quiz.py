# Hanna Damarjian ~ Background Information

## CODE STARTS ON LINE 63!!!

# Who Wants to be a Millionaire (Questionnaire)



# Rules and Layout (Pseudocode) for program:

# I) Rules
# This exam contains 15 questions.
# For each question, there includes four choices (A., B., C., and D.). One choice is the correct answer.

# For the first 11 questions, the money amount is randomized in the program.
# For the last four questions, the money amount is set as $100,000 first, $250,000 second, $500,000 third, and $1,000,000 last.

# When transitioning from question to question, the user MUST answer each question correctly. That is, to go from
# Q1 to Q2, the user must first get Q1 correct.
# If the user gets a question incorrect, then the program ejects out of the game and the user will end the game with
# $1,000.



# II) Layout:

# A. First, I will create the 15 questions. However, each question has a prompt and four answer choices connected to it.
# Since it is difficult to create a variable that contains question types (as variable data types only include "float", "int", "str", "bool"),
# I will create a class called "Questionaire" that contains one object. This object will have two attributes.
    # 1) The first attribute (or object data value) is the question prompt.
    # 2) The second attribute is the answer choice.

# B. Second, I will create the questions and answer choices. Remember, the questions contain 15 question prompts which each contain 4 answer choices.

# C. Third, I will create a function that contains one parameter (as its input). This parameter is the set of 15 questions. Now, what will this function execute?
     # This function will execute the same list of commands (i.e. printing out questions, answer choices, and if you are right or wrong based upon user input) up to 15 times.
     # Since the list of commands are the same, and each command is executed one at a time, I will use a for loop to generate this command (sequence of questions).

# D. Finally, after the question and four answer choices are printed, if the user answers the question correctly, then the user wins a randomized amount of money.
     # Else, the user lost the game (the program stops), but leaves with $1,000. Remember, this is for the first 11 questions. The contestant also gets to add each prize money to his or her earnings from the previous question.
     # Also, note that the question amounts for the last four questions are fixed. That is, if the contestant answers Q12 worth $100,000 correctly, the contestant WINS
     # the $100,000 and it will not include the prior earnings because prior earnings < $100,000.

# E. Alright, let us go!



# This program includes:
    # 1) Arrays
    # 2) Classes and Objects
    # 3) For Loop
    # 4) If/Else statement
    # 5) Variable definition
    # 6) Importation of Files/Classes


# --------------------------------------------------------------------------------------------------------------------------------------
import sys
import random
from QuestionFile import Questionnaire
from QuestionElite import QuestionContinued

#B.
question_prompts = [
                "What state contains sights named San Francisco and Hollywood? \nA. California \nB. Utah \nC. Colorado \nD. Indiana\n",
                "What does Tesla produce? \nA. Soft drinks \nB. Electric Cars \nC. Cell phones \nD. Art supplies\n",
                "When playing Blackjack, how many points would be considered a bust? \nA. 11 \nB. 16 \nC. 21 \nD. 26\n",
                "Which of the following movies did Alec Baldwin not star in nor voice acted? \nA. Rise of the Guardians \nB. Beetlejuice \nC. The Shadow \nD. Scooby Doo: Mystery Incorporated\n",
                "If the Chinese dollar is currently worth $0.16, then 50 Chinese dollars is worth what? \nA. 400 pennies \nB. 200 nickels \nC. 80 dimes \nD. 40 quarters\n",
                "Representing the Democratic Party in the 19th century, which of the following former Presidents was elected for two non-consecutive terms? \nA. Theodore Roosevelt \nB. Franklin Roosevelt \nC. Grover Cleveland \nD. Andrew Jackson\n",
                "In astrology, the symbol for a Sagittarius is depicted as what? \nA. An archer \nB. A crab \nC. A goat \nD. A virgin\n",
                "Which of the following pop singers released a musical album titled '1989'? \nA. Michael Jackson \nB. Taylor Swift \nC. Katy Perry \nD. Luke Bryan\n",
                "A popular book and movie first established in the 1930's, the theme for which of the following movies features the poem 'Ten Little Indians'? \nA. The Wizard of Oz \nB. King Kong \nC. And Then There Were None \nD. One Flew Over the Cuckoo's Nest\n",
                "'It's a love that lasts forever. It's a love that had no past.' are lyrics for which of the Beatles song, established in 1970? \nA. Love Me Do \nB. Let It Be \nC. Don't Let Me Down \nD. And I Love Her\n",
]

#C.

questions = [ # question is a list of objects (from QuestionFile.py file)
            Questionnaire(question_prompts[0], "A"), # first question in list. It includes the object question (which has attributes question prompt and answer choice).
            Questionnaire(question_prompts[1], "B"),
            Questionnaire(question_prompts[2], "D"),
            Questionnaire(question_prompts[3], "D"),
            Questionnaire(question_prompts[4], "C"),
            Questionnaire(question_prompts[5], "C"),
            Questionnaire(question_prompts[6], "A"),
            Questionnaire(question_prompts[7], "B"),
            Questionnaire(question_prompts[8], "C"),
            Questionnaire(question_prompts[9], "C"),
]


prize_money = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000, 15000, 25000]
prize_elite = [100000, 250000, 500000, 1000000]

# For Round 2 in the game:

questions_prompts2 = [
    "The painting 'On a Sunday Afternoon on the Island of La Grande Jatte' was created by which of the following 19th century artists? \nA. Rene Magritte \nB. Georges Seurat \nC. Paul Cezanne \nD. Pablo Picasso\n",
    "In the Mario franchise, the original Mario Party on the Nintendo 64 featured all but which of the following as playable characters? \nA. Donkey Kong \nB. Yoshi \nC. Toad \nD. Luigi\n",
    "'You cannot swim for new horizons until you have courage to lose sight of the shore' was stated by which of the following well-known writers? \nA. Emily Dickinson \nB. Mark Twain \nC. William Faulkner \nD. Scott Fitzgerald\n",
    "An uncommon English word, which of the following words is defined as 'the day before yesterday'? \nA. Nudiustertian \nB. Yarborough \nC. Tittynope \nD. Xertz\n"
]

questions2 = [
    QuestionContinued(questions_prompts2[0], "B"),
    QuestionContinued(questions_prompts2[1], "C"),
    QuestionContinued(questions_prompts2[2], "C"),
    QuestionContinued(questions_prompts2[3], "A")
]

#D.
def run_game(a,b,c):
    bank = 0
    for question in questions:
        answer = input(question.prompt)
        answer = answer.upper() # uppercase the answer if not capitalized (because a = A here)
        if answer == question.answer:
            winnings = random.choice(prize_money)
            print("You answered correctly! You won $" + str(winnings) + " dollars.")
            bank = bank + winnings
            print("You now have $" + str(bank) + " dollars in your bank.")
            prize_money.remove(winnings)
        elif answer == "W":
            half_of_bank = bank/2
            print("You chose to leave the game. You are walking out of the game with $" + str(half_of_bank) + " dollars.")
            sys.exit()
        else:
            print("No, I am sorry but, that is incorrect. Your game is over, and you are leaving with $1,000. Thanks for playing!")
            sys.exit()

    print("Welcome to Round 2! This next question is worth $125,000.\n")

    new_winnings = 125000
    for question in questions2:
        answerS = input(question.prompting)
        answerS = answerS.upper()
        if answerS == question.answering: # selecting the correct answer.
            print("You answered correctly! You won $" + str(new_winnings) + " dollars.")
            print("You now have $" + str(new_winnings) + " dollars in your bank.")
            bank = new_winnings
            new_winnings = new_winnings*2
        elif answerS == "W": # walk away from the game (i.e. quit)
            print("You are walking out of the game with $" + str(bank) + " Congratulations!")
            sys.exit()
        else: # selecting the wrong answer or inputting the wrong character
            print("No, I am sorry, but that is incorrect. Your game is over, and you are leaving with $25,000. Thanks for playing!")
            sys.exit()
    if bank == 1000000:
        print("Congratulations! You won the game!")

run_game(questions,prize_money,questions2)
