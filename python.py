#Python slot machine
import random
def spin_row():
    symbols = [' 🍒 ', ' 🍉 ',' 🥭 ', ' 🔔 ', ' ⭐ ']
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1]==row[2]:
        if row[0] ==' 🍒 ':
            return bet * 3
        elif row[0] ==' 🍉 ':
            return bet * 4
        elif row[0] == ' 🥭 ':
            return bet * 5
        elif row[0] == ' 🔔 ':
            return bet * 10
        elif row[0 ]== ' ⭐️ ':
            return bet * 50
    return 0
def main():
    balance = 1000
    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols:🍒 🍉 🥭 🔔 ⭐️")
    print("***********************")

    while balance > 0:
        print(f"The current balance is: ${balance:.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a number")
            continue

        bet = int(bet)

        if bet>balance:
            print("insufficient funds")
            continue

        if bet <=0:
            print("bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost  this round")

        balance += payout
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if not play_again == 'Y':
            break
    print("***********************************")
    print(f"The  Final balance is: ${balance:.2f}")
if __name__ ==  '__main__':
    main()




















