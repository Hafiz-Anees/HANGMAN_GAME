
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# step 1 ===> declare and initialize the list
import random
word_list = ['anees','umer','musa','inam','ikram','muneeb','talha']
word = random.choice(word_list)

# step 2 ==> hide the word that is selected randomly

hidden = []

for i in range(0,len(word)):
  hidden += "_"
print(hidden)

# step 3 ===> logical implementation

end_game = False
lives = len(word)
print(f"\nRemaining guess:{lives}")
while not end_game:

  guess = input("Enter a character to guess the word:").lower()

  for position in range(len(word)):
    if word[position] == guess:
      hidden[position] = guess

  if guess not in word:
    lives = lives - 1
    print(f"\nRemaining guess:{lives}")
    if lives == 0:
      end_game = True
      print("you lost")

  print(hidden)

  if "_" not in hidden:
    end_game = True
    print("\nyou win")

print("\n=========================\n")
print(stages[lives])




