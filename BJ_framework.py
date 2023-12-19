import tkinter as tk
from tkinter import PhotoImage, messagebox
import random

class Card: # Here the class Card is created
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value        
        pass

    def get_numeric_value(self) -> int: # Here we link the values of the cards and if you see there is int because is a numeric value
        if self.value in ['K', 'Q', 'J']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)
    pass

    def get_image(self): # Here we call the image 
        return f"C:\\Users\\marco\\OneDrive\\Escritorio\\UNIVERSIDAD\\PROGRAMACIÓN II\\bj_project-main\\img/{self.value}_of_{self.suit}.png"
    pass

class Deck: # Here we create the class deck, that it will contain the attributes suits and values
    def __init__(self, suits = [], values = []):
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(suit,value))
        pass

    def shuffle(self): # Here si to suffle the deck after each game so the probability of the cards reset after this 
        random.shuffle(self.cards)
        pass

    def deal(self)-> Card: 
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop()
    pass

class EnglishDeck(Deck): # Here we define with 2 lists which are the differents suits and the differents values
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        super().__init__(suits, values)
        pass

class Hand: # This is the class that contains your cards to play
    def __init__(self):
        self.cards = []
        pass

    def add_card(self, card: Card): # Here we are calling the cards of your hand
        self.cards.append(card)
        pass

    def value(self)->int: # Here we are summing the values of the different cards
        total_value = sum(card.get_numeric_value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.value == 'A')

        while total_value > 21 and num_aces: # Here we are telling the program that if you get over 21 stop 
            total_value -= 10
            num_aces -= 1

        return total_value
    pass

class Player: # Here is the class player, that contains the object Hand by abstracction and the object name
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        pass

class BlackjackGame: # This is the class for the game, in the first function we are calling with the constructor the different objects
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.deck = EnglishDeck()
        self.deck.shuffle()
        pass

    def start_game(self): # Here we are calling the hand for the dealer and the player, and adding the cards
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        for i in range (2):
            self.player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())
        pass

    def hit(self)-> bool:
        self.player.hand.add_card(self.deck.deal())
        return self.player.hand.value() > 21
    pass

    def dealer_hit(self) -> bool: # Here we are giving the instructions that the dealer will fllow, if the value of the cards of the dealer is over 17, it won't ask for more cards
        while self.dealer.hand.value() < 17:
            self.dealer.hand.add_card(self.deck.deal())
        return self.dealer.hand.value() <= 21
    pass

    def determine_winner(self): # Here we are defining how to choose who win
        player_value = self.player.hand.value()
        dealer_value = self.dealer.hand.value()

        if player_value > 21:
            return "You've busted! The house wins."

        if dealer_value > 21:
            return "Dealer busts! You win."

        if player_value > dealer_value:
            return "You win!"
        elif dealer_value > player_value:
            return "Dealer wins." 
        else:
            return "It's a tie!"
    pass

# The GUI code is provided, so students don't need to modify it
class BlackjackGUI:
    def __init__(self, game):
        self.game = game

        self.root = tk.Tk()
        self.root.title("Blackjack")

        # Frames for the player and the dealer
        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(side=tk.LEFT, padx=10)

        self.deck_frame = tk.Frame(self.root)
        self.deck_frame.pack(side=tk.LEFT, padx=10)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(side=tk.RIGHT, padx=10)

        # "Stand" button
        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

        self.start_game()

    def start_game(self):
        self.game.start_game()
        self.update_interface()

    def handle_hit(self, event):
        if self.game.hit():
            self.update_interface()
            self.end_game("You've busted! The house wins.")
            return
        self.update_interface()

    def handle_stand(self):
        self.btn_stand.config(state=tk.DISABLED)
        while self.game.dealer_hit():
            self.update_interface()
        self.end_game(self.game.determine_winner())

    def update_interface(self):
        # Remove all widgets from player, deck, and dealer frames
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        
        for widget in self.deck_frame.winfo_children():
            widget.destroy()

        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        # Player's cards
        player_previous_frame = tk.Frame(self.player_frame)
        player_previous_frame.pack(side=tk.LEFT, pady=10)

        for card in self.game.player.hand.cards[:-1]:  # All cards except the last one
            img = PhotoImage(file=card.get_image())
            img = img.subsample(3, 3)  # Resize the image (adjust according to your preference)
            lbl = tk.Label(player_previous_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.TOP, pady=5)  # Add vertical space between cards

        # The last card of the player in the center
        last_card = self.game.player.hand.cards[-1]
        img = PhotoImage(file=last_card.get_image())
        lbl = tk.Label(self.player_frame, image=img)
        lbl.image = img
        lbl.pack(side=tk.LEFT, padx=10)  # Center the last card horizontally a bit more
        
        # Deck in the middle
        img = PhotoImage(file="C:\\Users\\marco\\OneDrive\\Escritorio\\UNIVERSIDAD\\PROGRAMACIÓN II\\bj_project-main\\img\\card_back_01.png")

        lbl = tk.Label(self.deck_frame, image=img, cursor="hand2")
        lbl.image = img
        lbl.pack(side=tk.TOP, padx=10)
        lbl.bind("<Button-1>", self.handle_hit)
        
        # "Stand" button below the deck
        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

        # Dealer's cards
        dealer_previous_frame = tk.Frame(self.dealer_frame)
        dealer_previous_frame.pack(side=tk.RIGHT, pady=10)

        for card in self.game.dealer.hand.cards[:-1]:  # All cards except the last one
            img = PhotoImage(file=card.get_image())
            img = img.subsample(3, 3)  # Resize the image (adjust according to your preference)
            lbl = tk.Label(dealer_previous_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.TOP, pady=5)  # Add vertical space between cards

        # The last card of the dealer in the center
        last_card = self.game.dealer.hand.cards[-1]
        img = PhotoImage(file=last_card.get_image())
        lbl = tk.Label(self.dealer_frame, image=img)
        lbl.image = img
        lbl.pack(side=tk.RIGHT, padx=10)  # Center the last card horizontally a bit more

    def end_game(self, message):
        messagebox.showinfo("Result", message)
        self.root.quit()

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    game_logic = BlackjackGame()
    app = BlackjackGUI(game_logic)
    app.run()