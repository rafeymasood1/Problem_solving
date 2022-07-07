import random

suits = ['hearts', 'diamonds', 'spades', 'club']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
value = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'jack': 10, 'queen': 11, 'king': 13, 'ace': 1}


class Card:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.rank = ranks
        # ranks are iterated into this to get values of all cards
        self.value = value[ranks]

    def __str__(self):
        return f"{self.rank} of {self.suits}"


class Deck:
    ''' contains 52 cards which are mutable'''

    def __init__(self):
        self.card_list = []
        for suit in suits:
            for rank in ranks:
                # cards are added to card list
                self.card_list.append(Card(suit, rank))

    def shuffle(self):
        ''' shuffle the self.card_list
        '''
        random.shuffle(self.card_list)

    def remove_card(self):
        self.card_list.pop()  # cards are removed from the end of the list

    def deal_card(self):
        return self.card_list.pop()  # cards are removed from the end of the list


class Table():
    def __init__(self):
        self.cards_on_table = []

    def deal_2_cards(self):
        self.cards_on_table.append(my_deck.deal_card())
        self.cards_on_table.append(my_deck.deal_card())

    def hit_card(self):
        self.cards_on_table.append(my_deck.deal_card())

    def total_value(self):
        total_value = 0
        for item in self.cards_on_table:
            total_value += item.value
        return total_value

    def reset(self):
        self.cards_on_table = []

    def deal_1_card(self):
        self.cards_on_table.append(my_deck.deal_card())


class Account:
    ''' money_account which allows deposit, witdraw and which can store account_money'''

    def __init__(self, account_money):

        self.account_money = account_money

    def deposit(self, amount):
        self.account_money += amount
        print(f"your current account balance is {self.account_money} ")

    def withdraw(self, amount):
        self.account_money -= amount
        print(f"your current account balance is {self.account_money} ")


# --- Game setup ---
my_deck = Deck()
player = Table()
dealer = Table()
player_account = Account(1000)


while True:
    choice = input("Ready To Play? ")

    if choice[0].lower() == 'y':
        game_on = True
        print("\n"*100)
        print(
            "\tWelcome To Our Game Of BlackJack, You now have $1000! \nYOU HAVE ONE GOAL:")
        print("\nTo Become a Millionaire")
        print("\nOnce you hit a MILLION, the game is OVER and you basically BEAT the GAME!! \n\n")

    else:
        break

    while game_on == True:
        print(f" You now have {player_account.account_money}")
        my_deck.shuffle()              # all the deck is now shuffled

        player.deal_2_cards()     # player is given 2 cards
        if player.total_value() > 21:
            player.reset()
            player.deal_2_cards()

        # ACE VALUE EITHER 13 OR 1 CHOSEN
        for item in player.cards_on_table:
            if item.value == 1:
                if player.total_value() + 13 < 21:
                    item.value = 13

        num = 0
        # the 2 cards are displayed
        for item in player.cards_on_table:
            num += 1
            print(f"YOUR card number {num}: {item}")

        # VALUE OF PLAYER CARDS DISPLAYED
        print(f"Your Total Value: {player.total_value()} \n")

        dealer.deal_2_cards()            # Dealer is given 2 cards

        # ACE VALUE EITHER 13 OR 1 CHOSEN
        for item in dealer.cards_on_table:
            if item.value == 1:
                if dealer.total_value() + 13 < 21:
                    item.value = 13

        # Only 1 Card of Dealer is Displayed
        print(f"dealer card: {dealer.cards_on_table[0]}")

        # ASKING THE GAMBLING MONEY in this loop
        while True:
            dealer = Table()
            try:
                money = int(
                    input("\nChoose amount from $1000 you wanna bet..."))
            except:
                print("\nYou didn't enter a valid number")
                continue

            if money <= player_account.account_money:
                player_account.withdraw(money)
                break
            else:
                print(
                    f"\nyou only have {player_account.account_money} in your account")
                continue

        print(
            f" dealer: I am now adding in ${money} for an easy win!!")

        # 'While loop' and WIN CHECK
        while True:
            turn = 'player'
            if player.total_value() >= 21:
                print("YOu BuStEd!")
                break

            if dealer.total_value() >= 21:
                print("DEALER BUSTED!! CONGRAT!")
                print(f"{2*money} deposited to your account")
                player_account.deposit(2*money)
                break

            else:
                if turn == 'player':

                    player_input = input("Hit or Stay?  ")
                    if player_input[0].lower() == 'h':
                        player.deal_1_card()
                        num = 0
                        # the 2 cards are displayed
                        for item in player.cards_on_table:
                            num += 1
                            print(f"YOUR card number {num}: {item}")
                        print(f"Your Total Value: {player.total_value()} \n")

                    else:
                        if 21 - dealer.total_value() < 5:
                            c = dealer.deal_1_card()
                            a = random.choice(c, 1)
                            a

                        else:
                            dealer.deal_1_card()
                        print(f"dealer: {dealer.total_value()}")

                        if dealer.total_value() >= 21:
                            print("DEALER BUSTED!! CONGRAT!")
                            print(f"You NOW get a sum of {2*money}")
                            player_account.deposit(2*money)
                            break

                        if dealer.total_value() >= player.total_value():
                            print("YOu lost!")
                            break

        if input("Do you want to play again y or n")[0].lower() == 'n':
            game_on = False

        else:
            game_on = True

    break
