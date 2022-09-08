# Welcome to my simple Hang Game code :D
import random
# from words import world_list -> Import list instead create a list here?

def pick_word():
    # Just a example for testing
    word = random.choice(["absence","abuse","account","accident","beneath","bend","benefit","biology","bitter","candidate","campaign","camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient","supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle","global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat","yellowish","zone"])
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("Let's play Hangman Game!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")

def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]

if __name__ == '__main__':
    word = pick_word()
    play(word)
