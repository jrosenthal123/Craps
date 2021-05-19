import random

bank = 100
again = 1

print("Bank Balance:", bank)

while again == 1:
    bet = int(input("Enter your bet: "))
    while bet > bank or bet <= 0:
        print("Your bet must be equal to or less than your bank")
        bet = int(input("Enter your bet: "))

    input("Press Enter to Roll...")
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    dsum = d1+d2
    i=0
    print(d1, d2)

    if dsum == 7 or dsum==11:
        print("Win!")
        bank = bank + bet
    elif dsum == 2 or dsum == 3 or dsum == 12:
        print("Lose!")
        bank = bank - bet
        #break
    else:
        while i == 0:
            print("Roll again.")
            input("Press Enter to Roll...")
            d1 = random.randrange(1,7)
            d2 = random.randrange(1,7)
            dsum_new = d1+d2
            print(d1, d2)
            if dsum_new == 7:
                print("Lose!")
                bank = bank - bet
                i=1
                break
            elif dsum_new == dsum:
                print("Win!")
                bank = bank + bet
                i=1
    print("Bank Balance:", bank)
    if bank > 0:
        play=input("Play again? (Y/N): ")
        again = 2
        while again == 2:
            if play == "Y" or play == "Yes" or play == "yes" or play == "y":
                again = 1
            elif play == "N" or play == "No" or play == "no" or play == "n":
                print("Thank you for playing!")
                print("Final winnings:", bank)
                again = 0
            else:
                print("Error: Please enter proper response.")
                play=input("Play again? (Y/N): ")
                again = 2
    elif bank <= 0:
        print("BANKRUPT - GAME OVER!")
        break
