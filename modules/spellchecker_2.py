# write your solution here
from difflib import get_close_matches

text = input("Write text: ") + " "

wordlist = "wordlist.txt" 
words = []
suggestions = []

with open(wordlist) as new_file:
    for line in new_file:
        words.append(line.strip())

word = ""
whole_sentence= ""
for letter in text:
    if letter.isalpha():
        #print(letter)
        word += letter
        #print(word)
    else:
        if word.lower() not in words:
            #print("Miss")
            whole_sentence += f'*{word}* '
            suggestions.append(word)
            word = ""

        else:
            #print("ok")
            whole_sentence+= f'{word} '
            word = ""

print(whole_sentence)

for word in suggestions:
    words_match = str(get_close_matches(word, words)).strip("[]").replace("'", "")
    print(f'{word}: {words_match}')