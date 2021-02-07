import sys
import random
from QuestionFile import Questionnaire
from QuestionElite import QuestionCont

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
