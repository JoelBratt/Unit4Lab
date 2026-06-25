"""
Coin Game
Joel Bratt
Runs the main program using the classes from coin and player.
6/24/2026
"""
from player import Player
def main():
    print("Coin Match Game")

    player1 = Player("Player1")
    player2 = Player("Player2")

    print(f'{player1.get_name()} has {player1.get_wallet()} coins.')
    print(f'{player2.get_name()} has {player2.get_wallet()} coins.')

    play_again = input("\nDo You want to toss the coins? (y/n): ")

    while play_again.lower() == "y":
        print("\n Throwing coins...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            print(f'... Match!! {player1.get_name()} wins a coin.')
            player1.win_coin()
            player2.lose_coin()

        else:
            print(f'No Match! {player2.get_name()} wins a coin.')
            player2.win_coin()
            player1.lose_coin()
        
        print(f'\n{player1.get_name()} has {player1.get_wallet()} coins.')
        print(f'\nand {player2.get_name()} has {player2.get_wallet()} coins.')

        play_again = input("\nDo You want to toss the coins? (y/n): ")

        print('\n Final Score')
        print(f'{player1.get_name()}: {player1.get_wallet()}')
        print(f'{player2.get_name()}: {player2.get_wallet()}')

        if player1.get_wallet() > player2.get_wallet():
            print(f'{player1.get_name()} wins the game!')
        elif player2.get_wallet() > player1.get_wallet():
            print(f'{player1.get_name()} wins the game!')
        else:
            print("Its a tie!")
main()