word = "EVAPORATE"
guessWord = "_" * len(word)

word = list(word)
guessWord = list(guessWord)

guessedList = []

print('Guess a letter : ')
print("_ "*(len(word)))

while True:
    guessLetter = input()
    guessLetter = guessLetter.upper()

if guessLetter in guessedList:
    print('Already guessed!')
else:
    guessedList.append(guessLetter)
    for i in range(len(word)):
        if guessLetter in word[i]:
            guessWord[i] = guessLetter

if "_" not in guessWord:
    print('You Win!')
    print(' '.join(guessWord))
    break
print(' '.join(guessWord))
print('Guess a letter : ')