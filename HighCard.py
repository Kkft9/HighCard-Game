from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card() :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) :
        return self.rank + ' of ' + self.suit

    def isBlackOrRed(self) :
        if self.suit == 'Hearts' or self.suit == 'Diamonds' :
            return 'Red'
        else:
            return 'Black'
    

class Deck() :

    def __init__(self):
        self.deck = []
        for suit in suits :
            for rank in ranks :
                self.deck.append(Card(suit, rank))

    def shuffleDeck(self) :
        shuffle(self.deck)

    def dealCard(self) :
        topCard = self.deck.pop()
        return topCard


class Player :
    def __init__(self, name) :
        self.name = name
        self.cards = []

    def __str__(self) :
        return f'{self.name} has {len(self.cards)} cards'
    
    def removeCard(self) :
        topCard = self.cards.pop()
        return topCard

    def addCard(self, wonCards) :
        if type(wonCards) == type([]) :
            self.cards.extend(wonCards)
        else :
            self.cards.append(wonCards)


def distributeCards(deck, playerOne, playerTwo) :
    for i in range(26) :
        playerOne.addCard(deck.dealCard)
        playerTwo.addCard(deck.dealCard)


def checkCards(playerOne, playerTwo) :
    if len(playerOne.cards) > 0 and len(playerTwo.cards) > 0:
        return True
    return False 

def playRound(playerOne, playerTwo, drawDeck) :
    playerOneDeck = []
    playerTwoDeck = []

    playerOneDeck.append(playerOne.removeCard())
    
    playerOneDeck.append(playerOne.removeCard())
    
    if playerOneDeck[-1].value > playerTwoDeck[-1].value :
        playerOne.addCard(drawDeck)
        drawDeck = []
    elif playerTwoDeck[-1].value > playerOneDeck[-1].value:
       playerTwo.addCard(drawDeck)
       drawDeck = [] 



def main() :
    print("\nWelcome to HighCard Game!")

    player1 = input("\nEnter first player's name?\n")
    player2 = input("\nEnter second player's name?\n")

    print(f'\nHello {player1} and {player2}!')

    playerOne = Player(player1)
    playerTwo = Player(player2)

    deck = Deck()
    deck.shuffleDeck()

    distributeCards(deck, playerOne, playerTwo)

    drawDeck = []

    while(checkCards(playerOne, playerTwo) == True) :
        print(playerOne)
        print(playerTwo)
        playRound(playerOne, playerTwo, drawDeck)

    if(len(playerOne.cards) == 0) :
        print(f'\n{playerTwo.name} Won!!!')
    else :
        print(f'\n{playerTwo.name} Won!!!')


if __name__ == '__main__':
    main()






