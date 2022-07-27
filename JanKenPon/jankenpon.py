import random

choiceArr = ["rock", "paper", "scissor"]
replay = True

while(replay):
    computerChoice = random.randrange(0,2)
    playerChoice = int(input("Pick your option (number): 0 for rock, 1 for paper or 2 for scissor: "))
    if playerChoice > 2 or playerChoice < 0:
        print("Sorry, not a valid option! Pick one of the following: 0 for rock, 1 for paper or 2 for scissor.")
        replayAnswer = input("Do you want to play again? Type y (yes) or n (no)")
    elif choiceArr[playerChoice] == choiceArr[computerChoice]:
        print(f"Both players picked {choiceArr[playerChoice]}. It is a tie!")
        replayAnswer = input("Do you want to play again? Type y (yes) or n (no)")
    elif (choiceArr[computerChoice] == "rock" and choiceArr[playerChoice] == "scissor") or (choiceArr[computerChoice] == "scissor" and choiceArr[playerChoice] == "paper") or (choiceArr[computerChoice] == "paper" and choiceArr[playerChoice] == "rock"):
        print(f"The computer picked {choiceArr[computerChoice]}. You lost!")
        replayAnswer = input("Do you want to play again? Type y (yes) or n (no)")
    elif (choiceArr[playerChoice] == "rock" and choiceArr[computerChoice] == "scissor") or (choiceArr[playerChoice] == "scissor" and choiceArr[computerChoice] == "paper") or (choiceArr[playerChoice] == "paper" and choiceArr[computerChoice] == "rock"):
        print(f"The computer picked {choiceArr[computerChoice]}. You won!")
        replayAnswer = input("Do you want to play again? Type y (yes) or n (no)")
    if replayAnswer != "y" and replayAnswer != "n":
        print("Sorry, this is an invalid option. Please type y or n!")
        replayAnswer = input("Do you want to play again? Type y (yes) or n (no)")
    elif replayAnswer == "y":
        replay = True
    elif replayAnswer == "n":
        print("Thanks for playing!")
        replay = False