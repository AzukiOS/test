def hungman(word):
    # player2 miss count
    wrong = 0

    stages = ["",
             "______   ",
             "|        ",
             "|    |   ",
             "|    o   ",
             "|   /|\  ",
             "|   / \  ",
             "         "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Let's play hungman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "one char..."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong+=1
        # score board
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose! answer => {}.".format(word))

hungman("tom")

