import random
# First we must prompt the user with a random question or the quit option.
# quit_app

flashcards = [
    {"question" : "What python keyword is used to define a function? ", "answer" : "def"},
    {"question" : "What is the relative minor of G major? ", "answer" : "eminor"},
    {"question" : "What is the standard frequency for the note A4? ", "answer" : "440 Hertz"}
]
# Task: tell the user goodbye
# Input: none
# Side effect: Prints a goodbye message.
# Return: None
def quit_app():
    print("Thanks for studying. Come back later for more practice.")

# Task: Selects and retrieves a random element in the Flashcards list.
# Input: Flashcards list
# Side effects: None
# Return: the Flashcards(Dictionary)
def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card
# Task: Display the question
# Input: question card
# Side effects: print question text to the terminal
# Return: None

def display_question(card):
    question = card["question"]
    print("Question: ", question)

# Task: Display the answer
# Input: Question Card
# Side Effects: Answer displayed in terminal.
# Return: None
def display_answer(card):
    answer = card["answer"]
    print("Answer: ", answer)

def main():
    while True:
        chosen_card = get_random_question(flashcards)
        display_question(chosen_card)

        user_answer = input("What do you want to do? See answer, or quit? Enter q to quit, enter anything else to show the answer. ")
        if user_answer == "q":
            quit_app()
            break
        
        else:
            display_answer(chosen_card)



main()