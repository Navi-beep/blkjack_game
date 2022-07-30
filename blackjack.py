import random


run = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        show = '<['+self.rank +' ' 'of' ' ' + self.suit + ']>'
        return show 

    def get_card_value(self):
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank in {'J', 'K', 'Q'}:
            return 10
        else:
            return 11

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = []
        for suit in suits:
           for rank in ranks:
                deck.append(Card(suit,rank))
        return deck 


    def truffle_shuffle(self):
        random.shuffle(self.deck)  

    def deal(self):
        one_card = self.deck.pop()
        return one_card 

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        

    def add_card(self, card):
        self.cards.append(card)
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.value += values[card.rank]


def hit(deck,hand):
    hand.add_card(deck.deal())
    

def hit_or_stand(deck, hand):
    global run

    while True:
        response = input("What do you want to do? hit or stand? Press 'h' or 's': ")

        if response == 'h':
            hit(deck, hand)

        elif response == 's': # not working, i need to fix this
            print("You are standing, it is the Dealer's turn to go!")
            run = False

        else:
            continue

        break


def show_first_cards(player, dealer):
    print("\nDealer hand: ")
    print("~first card hidden!~")
    print("", dealer.cards[1])
    print("\nPlayer hand: ",*player.cards)


def show_rest_of_cards(player, dealer):
    print("\nDealer hand: ", *dealer.cards)
    print("Dealer hand: ", dealer.value)
    print("\nPlayer hand: ", *player.cards)
    print("Player hand: ",player.value)


def player_bust(player, dealer):
    print("player busts! you lose!!! Nobody beats sub-zero!!")


def dealer_bust(player, dealer):
    print("dealer busts! you win!!! great success! ")


def player_wins(player, dealer):
    print("You win!!")


def dealer_wins(player, dealer):
    print("dealer wins!! Nobody beats sub-zero")

def tie(player, dealer):
    print("It's a push! Nobody wins :(")


while run:
    
    deck = Blackjack()
    deck.truffle_shuffle()

    player_cards = Hand()
    player_cards.add_card(deck.deal())
    player_cards.add_card(deck.deal())

    dealer_cards = Hand()
    dealer_cards.add_card(deck.deal())
    dealer_cards.add_card(deck.deal())


    show_first_cards(player_cards, dealer_cards)

    while run:

        hit_or_stand(deck, player_cards)
        show_rest_of_cards(player_cards, dealer_cards)

        if player_cards.value == 21:
            print('Blackjack!!!!')
            player_wins(player_cards, dealer_cards)
            

        elif player_cards.value > 21:
            player_bust(player_cards, dealer_cards)
            break
            

    if player_cards.value <= 21:
        while dealer_cards.value < 17:
            hit(deck, dealer_cards)

            show_rest_of_cards(player_cards, dealer_cards)

            if dealer_cards.value == 21:
                dealer_wins(player_cards, dealer_cards)

            elif dealer_cards.value > 21:
                dealer_bust(player_cards, dealer_cards)

            elif dealer_cards.value > player_cards.value: 
                dealer_wins(player_cards, dealer_cards)

            elif dealer_cards.value < player_cards.value: 
                player_wins(player_cards, dealer_cards) 

            elif player_cards.value > 21:
                player_bust(player_cards, dealer_cards)

    
    start_new_session = input("Do you wanna play this game again??? Hit 'y' or 'q' to quit game ")
    if start_new_session == 'y':
        run = True
        continue

    else: 
        print("Have a great day! No more gambling. Go home. Go hang out with your cat or something.\n")
        