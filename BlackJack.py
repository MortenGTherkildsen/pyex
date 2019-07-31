"""
Python Eksamen, KEA

Navn: Morten Therkildsen








"""

import random

suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values ={'Two': 2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    # Initialise Card with suit and rank
    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank

    # toString()-method: Identifies card in a humanly readable fashion
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    # Constructs the Deck of cards (Cards), by iterating over the suits and ranks
    def __init__(self):
        self.deck = [] #Empty List
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # Append card object to the empty list

    # toString()-method for Deck: Identifies entire deck of cards in a humanly readable fashion
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # Make everything into a String Objet to print
        return 'The Deck has: '+ deck_comp
    
    # Shuffle Deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Deals a Card, and pop's it off the Deck 
    def deal (self):
        single_card = self.deck.pop()
        return single_card
"""
test_deck = Deck()
print(test_deck)
"""
class Hand:
    # Constructs an empty Hand
    def __init__(self):
        self.cards = [] # Empty list 
        self.value = 0 # Value of the cards starts at 0
        self.aces = 0 # to keep track of aces

    # Receives a Card 
    def receive_card(self,card):
        self.cards.append(card) # giving empty hand list, a card
        self.value += values[card.rank] # Adding a value witch is the rank of the card
        if card.rank == 'Ace': #Looking for Ace
            self.aces += 1

    # Dealing with Ace
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.receive_card(test_deck.deal())
test_player.receive_card(test_deck.deal())
test_player.value
for card in test_player.cards:
    print(card)

class Chips:

    def __init__(self):
        self.total = 100 # Default chip value
        self.bet = 0

    def win_bet(self):
        self.total += self.bet # Adding winning bet
    
    def lose_bet(self):
        self.total -= self.bet # Taking away losing bet

def take_bet(chips):

    while True: # Using while loop to keep it running to propmt the user to end up putting the right value
        try:
            chips.bet = int(input('Enter the amount of chips you like to bet:'))
        except ValueError: # Error handling if value is not a string 
            print('Oops! You need to enter a number')
        else: # If the amount is higher the amount of total chips
            if chips.bet > chips.total:
                print('Sorry but your amount of chips is lower then the bet you request.')
            else:
                break

def hit(deck, hand):
    hand.receive_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or stand? h = hit s = Stand ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player Stand. Dealer playing.')
            playing = False
        else:
            print('Sorry, please try again.')
            continue
        break

def show_some(player, dealer):
    print("\n Dealer's Hand:")
    print("<card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("player Wins")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("Dealer bust")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie, Push.")


while True:
    print("IT'S BLACKJACK TIME!")

    # Initializing deck of cards
    deck = Deck()
    deck.shuffle()

    # Initializing player hand
    player_hand = Hand()
    player_hand.receive_card(deck.deal())
    player_hand.receive_card(deck.deal())

    #Initializing dealer hand
    dealer_hand = Hand()
    dealer_hand.receive_card(deck.deal())
    dealer_hand.receive_card(deck.deal())

    #Player Chips
    player_chips = Chips()

    take_bet(player_chips)

    #Showing cards but keeps one secret the one from the dealer
    show_some(player_hand,dealer_hand)

    while playing:

        #Hit or stand
        hit_or_stand(deck,player_hand)

        #Show cards but keeps dealers card hidden so only one card showen
        show_some(player_hand,dealer_hand)

        #If a players hand exceed 21 run bust
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand,dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("Would you like to play another hand? enter 'y' or 'n' ")


    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        playing = False

