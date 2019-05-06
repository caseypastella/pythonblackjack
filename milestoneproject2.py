import random    

suits = ('Hearts','Spades','Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven':7, 'Eight': 8, 'Nine' :9,'Ten': 10, 'Jack': 10,'Queen': 10,'King': 10,'Ace': 11}

game_on = True

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck():
    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  
        
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)  
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
         
    
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)  
        self.value += values[card.rank] 
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
    
class Chips():
    def __init__(self):
        self.total = int(input("Please input a starting chip stack"))
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet            
         
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please Enter a bet: '))
        except:
            print('That was not a valid bet')
        else:
            if chips.bet > chips.total:
                print('You dont have enough chips! Your total is: {}'.format(chips.total))
            else: 
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace() 
    
def hit_or_stand(deck,hand): 
    global game_on  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            game_on = False

        else:
            print("Sorry, please try again.")
            continue
        break
            
def show_some(player, dealer):
    print('\nDealer Hand: ')
    print(dealer.cards[1])
    print('\n')
    print('\nPlayers Hand: ')
    for cards in player.cards:
        print(cards)

def show_all(player,dealer):
    print('\nDealers hand: ')
    for cards in dealer.cards:
        print(cards)      
    print('\n')
    print('Players hand: ')
    for cards in player.cards:
        print(cards)
    
            
def player_busts(player,dealer,chips):
    print('player busts')
    chips.lose_bet() 

def player_wins(player,dealer,chips):
    print('player wins')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('dealer busts')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('dealer wins')
    chips.lose_bet()
def push(): 
    print('Dealer and Player Tiie!')
           
print('Welcome to BlackJack')

while True:
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    player_chips = Chips()
    player_bet = take_bet(player_chips)
    
    show_some(player,dealer)
    
    while game_on:
        hit_or_stand(deck,player)
        show_some(player,dealer)
        if player.value > 21: 
            player_busts(player,dealer,player_chips)
            break

    if player.value <= 21:
        while dealer.value < 17: 
            hit(deck, dealer)
            show_all(player,dealer)
                
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips) 
        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)
        elif player.value > dealer.value:  
            player_wins(player,dealer,player_chips)
        else: 
            push(player,dealer) 
    print('\n Player total chips are at: {}'.format(player_chips.total)) 
    newgame = input('would you like to play again yes or no').lower()
    if newgame[0] == 'y':
        game_on == True
    else: 
        print('thanks for playing')
        break
            
   
                

        
        