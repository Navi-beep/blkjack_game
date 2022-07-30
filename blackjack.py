import random


run = True

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [Card(suit,rank) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck


    def shuffle(self):
        random.shuffle(self.deck)  

    def deal(self):
        one_card = self.deck.pop()
        return one_card

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self): 
        return self.rank + ' of ' + self.suit

    
    def get_card_value(self):
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank in {'J', 'K', 'q'}:
            return 10
        else:
            return 11


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.value += values[card.rank]


def hit(deck,hand):
    hand.add_card(deck.deal())
    

def hit_or_stand(deck, hand):
    while True:
        response = input("What do you want to do? hit or stand? Press 'h' or 's': ")

        if response == 'h':
            hit(deck, hand)

        elif response == 's':
            print("You are standing, it is the Dealer's turn to go!")
            run = False

        else:
            continue

        break


def show_first_cards(player, dealer):
    print("\nDealer hand: ")
    print("--first card hidden!--")
    print(" ", dealer.cards[1])
    print("\nPlayer hand: ",*player.cards)


def show_rest_of_cards(player, dealer):
    print("\nDealer hand: ", *dealer.cards)
    print("Dealer hand: ", *dealer.value)
    print("\nPlayer's Hand: ", *player.cards)
    print("\nPlayer hand: ",*player.value)


def player_bust(player, dealer):
    print("player busts! you lose!!!")


def dealer_bust(player, dealer):
    print("dealer busts! you win!!! great success! ")


def player_wins(player, dealer):
    print("You win!!")


def dealer_wins(player, dealer):
    print("dealer wins!! Nobody beats sub-zero")

def tie(player, dealer):
    print("It's a push! Nobody wins :(")













