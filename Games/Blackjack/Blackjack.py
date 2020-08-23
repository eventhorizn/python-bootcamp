import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        val = ''
        for card in self.deck:
            val += card.__str__() + '\n'
        return val

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        val = ''
        for card in self.cards:
            val += card.__str__() + '\n'
        return val

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1

    def get_score(self):
        score = 0

        for c in self.cards:
            score += c.value

        # if we bust with aces, we try to avoid that by switching
        while self.aces > 0 and score > 21:
            score -= 10
            self.aces -= 1

        return score

    def clear_hand(self):
        self.cards = []


class Player:

    def __init__(self, name):
        self.name = name
        self.total = 100
        self.bet = 0
        self.hand = Hand()
        self.playing = True
        self.bust = False

    def __str__(self):
        return self.name + '\n' + self.hand.__str__() + '\n' + 'Chips: ' + str(self.total) + '\n' + 'Score: ' + str(self.hand.get_score()) + '\n'

    def give_card(self, deck):
        self.hand.add_card(deck.deal())

    def place_bet(self):
        while True:
            try:
                self.bet = int(input(self.name + ", place your bet: "))
            except:
                print("Your bet must be an integer")
                continue
            else:
                if self.bet > self.total:
                    print("You can't bet more than you own")
                    continue
                else:
                    print(self.name + "'s bet: " +
                          str(self.bet) + " chips" + '\n')
                    self.total -= self.bet
                    break

    def hit_or_stand(self, deck):
        hit = False
        while True:
            try:
                hit = bool(int(input("Hit (1) or Stand (0): ")))
            except:
                print("You must Hit (1) or Stand(0)")
                continue
            else:
                break

        if hit:
            self.hand.add_card(deck.deal())
        else:
            print("You stand at: ")
            self.playing = False

        if self.hand.get_score() > 21:
            self.bust = True
            print("You have gone over 21, and have busted\n")
            self.playing = False

    def blackjack(self):
        return len(self.hand.cards) == 2 and self.hand.get_score() == 21

    def get_score(self):
        return self.hand.get_score()

    def clear_hand(self):
        self.hand.clear_hand()

    # wining a bet generates different amounts
    # if you hit a blackjack, you get 2.5 the bet
    # if you beat the dealer, its 2
    def win_bet(self, bet_quantifier):
        self.total += self.bet * bet_quantifier

    def lose_bet(self):
        self.total -= self.bet


class Dealer(Player):

    # There's a danger in this method...need to fix on hand side
    def __str__(self):
        if len(self.hand.cards) > 0:
            i_card = self.hand.cards[0]
            return self.name + '\n' + i_card.__str__() + '\n' + 'Score: ' + str(i_card.value) + '\n'
        else:
            return self.name + '\n' + 'No Cards'

    def finishHand(self, deck):
        while self.hand.get_score() < 17:
            self.hit(deck)

    def hit(self, deck):
        self.hand.add_card(deck.deal())

        if self.hand.get_score() > 21:
            self.bust = True

    def showFullHand(self):
        print(self.name + '\n' + self.hand.__str__() + '\n' +
              'Score: ' + str(self.hand.get_score()) + '\n')


def handle_payout(player, dealer):
    # Player busts, so they lose
    if player.bust:
        print("You busted, and lost your bet\n")
        player.lose_bet()
        return
    # So, dealer didn't bust and they match the dealer, they 'win' their bet back (push)
    if not dealer.bust and player.get_score() == dealer.get_score():
        print("You match the dealer, push\n")
        player.win_bet(1)
    # Player hit blackjack and dealer either busted or has lower score
    if player.blackjack():
        print("You got a blackjack, 2.5 your bet\n")
        player.win_bet(2.5)
        return
    # Player wins regular. They haven't busted and they haven't hit blackjack
    if dealer.bust:
        print("Dealer busted, 2 your bet\n")
        player.win_bet(2)
        return
    if player.get_score() > dealer.get_score():
        print("You beat the dealer, 2 your bet\n")
        player.win_bet(2)
        return
    if dealer.get_score() > player.get_score():
        print("Dealer beat you, you lost your bet \n")
        player.lose_bet()
        return


def play_next_round():
    while True:
        try:
            playing = int(input("New Round (1) Yes, (0) No: "))
        except:
            print("Bad Input")
            continue
        else:
            if playing > 1 or playing < 0:
                print("(1) Yes, (0) No")
                continue
            else:
                break

    return bool(playing)


# Print an opening statement
# I could have a 'choose how many players and their names
print('We are playing blackjack with 4 players\n')

players = []
players.append(Player("Gary"))
players.append(Player("Katie"))
#players.append(Player("Rowan"))
#players.append(Player("Hazel"))

dealer = Dealer("Dealer")

while True:
    deck = Deck()
    deck.shuffle()

    # Players first place a bet
    for player in players:
        player.place_bet()

    # Go around the table and give a player a card, twice
    for i in range(2):
        for player in players:
            player.give_card(deck)

    # Give dealer 2 cards
    dealer.give_card(deck)
    dealer.give_card(deck)

    for player in players:
        print(dealer)  # Show the players the dealer hand
        print(player)  # Show the player their hand

        while player.playing:
            player.hit_or_stand(deck)
            print(player)

    dealer.finishHand(deck)

    for player in players:
        dealer.showFullHand()
        print(player)
        handle_payout(player, dealer)
        print(player)

    if not play_next_round():
        break