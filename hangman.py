def hangme(word):
  wrong = 0
  stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
  words = list(word)
  win = False
  board = ['_'] * len(words)
  while wrong < len(stages)-1:
    char = input('Guess the word ')
    if char in words:
      cind = words.index(char)
      board[cind] = char
    else:
      wrong += 1
    print('\n'.join(board))
    e = wrong + 1
    print("\n".join(stages[0: e]))
    if '_' not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
  if not win:
      print("\n".join(stages[0:wrong]))
      print("You lose! It was {}.".format(word))
hangme('cat')

