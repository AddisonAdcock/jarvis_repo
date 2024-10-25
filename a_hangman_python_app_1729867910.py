Sure, here's a simple Hangman game using Python:

```python
import random

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "csharp", "swift"]
    random_number = random.randint(0, 5)
    chosen_word = word_list[random_number]
    guess_word = []
    for letter in chosen_word:
        guess_word.append("_")
    running = True
    while running:
        guess = input("Please guess a letter: ")
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                guess_word[index] = guess
        print(guess_word)

        if not '_' in guess_word:
            running = False
            print("You won!")

hangman()
```

This game works by choosing a random word from the word list. It then creates a list of underscores, one for each letter in the word. The user is then asked to guess a letter. If the letter is in the word, the underscore is replaced with the letter. This continues until all the letters in the word have been guessed. If the user guesses a letter that is not in the word, nothing happens and they are asked to guess again.