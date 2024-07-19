import spacy
import random

nlp = spacy.load('en_core_web_md')

with open("words.txt", "r") as f:
    line = next(f)
    for num, aline in enumerate(f, 2):
        if random.randrange(num):
            continue
        word = aline.strip()

guess = ""

while guess.lower() != word.lower():
    guess = input("Enter a guess: ")

    process = u"{} {}".format(word, guess)

    tokens = nlp(process)

    token1, token2 = tokens[0], tokens[1]

    print("Similarity:", token1.similarity(token2))

print("You got the word!")
