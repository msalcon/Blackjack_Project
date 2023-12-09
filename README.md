# Python Blackjack Game

This Python project implements a simple text-based Blackjack game using the Tkinter library for the graphical user interface. The game follows standard Blackjack rules, allowing the player to hit or stand in an attempt to beat the dealer.

## Project Structure

- **Card Class:** Represents a playing card with a suit and value. Contains methods to retrieve the numeric value and image of the card.

- **Deck Class:** Manages a deck of cards, allowing shuffling and dealing.

- **EnglishDeck Class:** A specific type of deck with English suits (hearts, diamonds, clubs, spades) and values (2 to 10, J, Q, K, A).

- **Hand Class:** Represents a hand of cards for a player, with methods to add cards and calculate the total value of the hand.

- **Player Class:** Defines a player with a name and a hand of cards.

- **BlackjackGame Class:** Manages the overall game logic, including player actions, dealing cards, and determining the winner.

- **BlackjackGUI Class:** Implements the graphical user interface using Tkinter. Displays player and dealer cards, handles user interactions, and updates the interface during the game.

## Instructions

1. Ensure you have Python installed on your system.
2. Clone or download the repository.
3. Run the `blackjack.py` file to start the game.

## How to Play

- The game window displays the player's and dealer's cards.
- Click the "Hit" button to draw an additional card.
- Click the "Stand" button to keep the current hand.
- The game ends when the player busts (goes over 21) or decides to stand. The dealer then plays by drawing cards until reaching a total value of 17 or more.
- The result is displayed in a message box.

## Contributing

Contributions are welcome! If you find issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## Credits

This project was developed for educational purposes. Credits to the original author and contributors.

## License

This project is under the MIT License - see the `LICENSE.md` file for details.
