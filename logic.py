from random import randrange

class Card:
    card_values = {
        11: "JACK",
        12: "QUEEN",
        13: "KING"
    }
    
    def __init__(self):
        self.value = randrange(1,14)

    def __str__(self):
        return self.card_values.get(self.value, str(self.value))
        

class Hand:
    cards = []

    def draw_card(self):
        self.cards.append(Card())


    def calculate_value(self):
        total = 0
        for card in self.cards:
            total += min(card.value, 10) # parse face cards down to numeric value

        return total

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])


class Game:
    def __init__(self):
        self.hand = Hand()

    def game_over(self):
        return self.hand.calculate_value() > 21

    def play_game(self):
        while True:
            answer = input("It is your turn. Press '1' to draw a card or press 'x' to end the game: ")

            if answer == 'x':
                print(f"You got {self.hand.calculate_value()}.")
                break
            elif answer == "1":
                self.hand.draw_card()
                if self.game_over():
                    print(f"{self.hand.calculate_value()}! You lose!")
                    break
                else:
                    print(f"Your current hand: {self.hand}.")
            else:
                continue
