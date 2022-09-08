# Welcome to my simple Hang Game code :D
import random
# Later, I'll try import a word list from a txt file to learn how to do it.
# I saw in stackoverflow
# def pick_word():
#     with open("words.txt", "r") as file:
#         alltext = file.read()
#         words_list = list(map(str, alltext.split()))
# print(random.choice(words_list))
# Also evaluate install random-word package to generate random english words.
def pick_word():
    # Just a example for testing
    word = random.choice(["absence","abuse","account","accident","beneath","bend","benefit","biology","bitter","candidate","campaign","camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient","supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle","global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat","yellowish","zone"])
    return word


def display(word):
    for i in range(0, len(word)):
        if i != len(word):
            print("_ ")
        else:
            print("_")


def check_char():
    c = ''
    while len(c) != 1:
        c = input('Write a character: ')
        c = c.lower()
        while ord(c) <= 97:
            c = input('Write a character, not a number: ')
            c = c.lower()
    return c


def check_str(word, cvalid):
    for char in str:
        if (ord(char) == ord(cvalid)):


if __name__ == "__main__":
    lives = 6
    win = False
    res = ""

    word = pick_word()
    print ("Estoy en main: {}".format(word))
    cvalid = check_char()
    print("Caracter valido: {}".format(cvalid))
    display(word)
