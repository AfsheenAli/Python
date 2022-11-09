import random

while True:
    words = ["rock", "paper", "scissor"]

    computer = random.choice(words)
    player = None

    player_points = []
    computer_points = []

    try:
        num = int(input("Select the number of points: "))
        print("---------------------------------------------------------------------------")
    except ValueError:
        print("You cannot enter an alphabet!")
        print('---------------------------------------------------------------------------')
        break
# ------------------------------------------------------------------------------------------
    def game():

        player = None

        while player not in words:
            player = input("Enter (rock, paper, or scissor): ").lower()

        if player == computer:
            print("COMPUTER: " + computer)
            print("PLAYER: " + player)
            print("DRAW")

        elif player == 'rock':
            if computer == 'paper':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("COMPUTER WINS!")
                computer_points.append(computer)
            elif computer == 'scissor':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("PLAYER WINS!")
                player_points.append(player)

        elif player == 'paper':
            if computer == 'scissor':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("COMPUTER WINS!")
                computer_points.append(computer)
            elif computer == 'rock':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("PLAYER WINS!")
                player_points.append(player)

        elif player == 'scissor':
            if computer == 'rock':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("COMPUTER WINS!")
                computer_points.append(computer)
            elif computer == 'paper':
                print("COMPUTER: " + computer)
                print("PLAYER: " + player)
                print("PLAYER WINS!")
                player_points.append(player)

# ---------------------------------------------------------------------------------------------
    def score():
        print("---------------------------------------------------------------------------")
        print("SCORE")
        print("PLAYER'S POINTS:", len(player_points))
        print("COMPUTER'S POINTS:", len(computer_points))

        print('---------------------------------------------------------------------------')
# ----------------------------------------------------------------------------------------------
    def winner():

        print("WINNER")
        if len(player_points) > len(computer_points):
            print("PLAYER WINS!")
        elif len(player_points) < len(computer_points):
            print("COMPUTER WINS!")
        else:
            print("DRAW!")
# -------------------------------------------------------------------------------------------
    try:
        for i in range(num):
            game()
        score()
        winner()
        print("---------------------------------------------------------------------------")

        choice = ["yes", "no"]

        replay = input("Do you want to play again(yes/no)?: ").lower()

        if replay == 'no':
            print("BYE! WE HOPE TO SEE YOU AGAIN!")
            break
        print('------------------------------------------------------')
    except NameError:
        print("Since you entered an alphabet, systems cannot perform the operations!")
        print("---------------------------------------------------------------------------")
        quit()
