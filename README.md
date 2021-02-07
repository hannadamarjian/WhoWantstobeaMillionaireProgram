# WHO WANTS TO BE A MILLIONAIRE

Author Hanna Damarjian 


## Rules and Layout (Pseudocode) for program:

- Rules:
  1. This exam contains 15 questions.
  2. For each question, there includes four choices (A., B., C., and D.). One choice is the correct answer.

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

Alex Helped



# This program includes:
    # 1) Arrays
    # 2) Classes and Objects
    # 3) For Loop
    # 4) If/Else statement
    # 5) Variable definition
    # 6) Importation of Files/Classes