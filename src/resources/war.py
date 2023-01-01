from flask import jsonify
from flask_restful import Resource
import random

RANKS = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

SUITS = ["Spades", "Cloves", "Hearts", "Diamonds"]


class Card:
    """A class used to represent a single card of particular rank and suit."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def compare(self, other):
        return RANKS.index(self.rank) - RANKS.index(other.rank)


class Deck:
    """A class used to represent a deck of 52 cards."""

    def __init__(self):
        self.deck = []
        for rank in RANKS:
            for suit in SUITS:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def is_empty(self):
        return not self.deck


class Player:
    """A class used to represent a player in the game of war."""

    def __init__(self, hand):
        self.hand = hand
        self.pile = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def draw_from_hand(self):
        return self.hand.pop(0)

    def hand_size(self):
        return len(self.hand)

    def is_hand_empty(self):
        return not self.hand

    def add_to_pile(self, card):
        self.pile.append(card)

    def draw_from_pile(self):
        return self.pile.pop(0)

    def pile_size(self):
        return len(self.pile)

    def is_pile_empty(self):
        return not self.pile

    def give_pile_to(self, other):
        """Transfers self's entire pile to other's hand."""

        while not self.is_pile_empty():
            other.add_to_hand(self.draw_from_pile())


class War(Resource):
    """A class used to represent a War game route."""

    def __init__(self, users_collection):
        self.users_collection = users_collection

    def deal(self):
        """Initalizes the hands for player 1 and player 2."""

        deck = Deck()
        deck.shuffle()

        hand1 = []
        hand2 = []

        while not deck.is_empty():
            hand1.append(deck.draw_card())
            hand2.append(deck.draw_card())

        self.p1 = Player(hand1)
        self.p2 = Player(hand2)

    def run(self):
        """Plays a match of War."""

        self.deal()
        response = {}
        round = 1
        while not self.p1.is_hand_empty() and not self.p2.is_hand_empty():
            round_outcome = {"player1": {}, "player2": {}}

            p1_card = self.p1.draw_from_hand()

            round_outcome["player1"]["rank"] = p1_card.rank
            round_outcome["player1"]["suit"] = p1_card.suit
            round_outcome["player1"]["cards_left"] = self.p1.hand_size()
            round_outcome["player1"]["pile_size"] = self.p1.pile_size() + 1

            p2_card = self.p2.draw_from_hand()

            round_outcome["player2"]["rank"] = p2_card.rank
            round_outcome["player2"]["suit"] = p2_card.suit
            round_outcome["player2"]["cards_left"] = self.p2.hand_size()
            round_outcome["player2"]["pile_size"] = self.p2.pile_size() + 1

            if p1_card.compare(p2_card) > 0:
                round_outcome["round_winner"] = "player1"

                self.p1.add_to_hand(p1_card)
                self.p1.give_pile_to(self.p1)

                self.p1.add_to_hand(p2_card)
                self.p2.give_pile_to(self.p1)
            elif p1_card.compare(p2_card) < 0:
                round_outcome["round_winner"] = "player2"

                self.p2.add_to_hand(p2_card)
                self.p2.give_pile_to(self.p2)

                self.p2.add_to_hand(p1_card)
                self.p1.give_pile_to(self.p2)
            else:
                round_outcome["round_winner"] = "tie"

                self.p1.add_to_pile(p1_card)
                self.p2.add_to_pile(p2_card)

                # If a player does not have enough cards to complete War, he loses.
                if self.p1.is_hand_empty() or self.p2.is_hand_empty():
                    break

                self.p1.add_to_pile(self.p1.draw_from_hand())
                self.p2.add_to_pile(self.p2.draw_from_hand())

            response[f"round_{round}"] = round_outcome
            round += 1

        response["total_rounds"] = round - 1

        if self.p1.is_hand_empty():
            response["winner"] = "player2"
            return response
        elif self.p2.is_hand_empty():
            response["winner"] = "player1"
            return response

    def post(self):
        response = self.run()

        if response["winner"] == "player1":
            wins = self.users_collection.find_one({"id": 1})["wins"]
            self.users_collection.update_one(
                {"id": 1}, {"$set": {"wins": wins + 1}})
        else:
            wins = self.users_collection.find_one({"id": 2})["wins"]
            self.users_collection.update_one(
                {"id": 2}, {"$set": {"wins": wins + 1}})

        return jsonify(response)
