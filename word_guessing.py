import random
word_bank = [
    "Skibidi Toilet",
    "Fanum Tax",
    "Gyatt",
    "Rizz",
    "Sigma",
    "NPC Energy",
    "Delulu",
    "Ohio Core",
    "Goofy Ahh",
    "Shawty Bae",
    "Slay Queen",
    "Skrrt Skrrt",
    "Bussin",
    "No Cap",
    "Mid",
    "Bruh Moment",
    "Bet",
    "Ate That",
    "Cooked",
    "Skibidi Dop Dop Yes Yes"
]

word= random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()

  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
      print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)