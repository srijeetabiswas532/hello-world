#  File: Poker.py

#  Description: This program simulates a 5-Draw Poker game and returns a winner.

#  Student Name: Srijeeta Biswas

#  Student UT EID: sb48779

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/16/2019

#  Date Last Modified: 2/18/2019

import random
from collections import Counter


# creates class Card which inherits from object
class Card(object):
    # defining class variables
    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    SUITS = ('C','D','H','S')

    #initializer
    def __init__(self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'


    # string method
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

        # equality tests

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


# creates class Deck which inherits from object
class Deck (object):
    def __init__(self, num_decks =1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)


    # function to shuffle the cards
    def shuffle(self):
        random.shuffle(self.deck)

    # deals the first card to players
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

# creates class Poker which inherits from object
class Poker(object):
    def __init__(self, num_players = 2, num_cards = 5):
        assert num_players * num_cards < 52

        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards


        # deals cards to players, round robin style
        for player in range(num_players):
            self.all_hands.append([])
        # deal the cards to the players
        for card in range(self.numCards_in_Hand):
            for player_num in range(num_players):
                self.all_hands[player_num].append(self.deck.deal())


    # function that plays the game
    def play(self):
        # sort the hands of each player and print
        card_all = []
        players = []
        # sorts the hand of each player and prints it
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            card_person = []
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
                card_person.append(card.rank)
            print('Player ' + str(i + 1) + ' : ' + hand_str)
            # creates a list of cards of each player
            card_all.append(card_person)
            # creates a list of players
            players.append('Player ' + str(i + 1))
        print()


        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand


        for i in range(len(self.all_hands)):
            points = []
            hand = []

            # series of if/elif statements to check hand types
            if self.is_royal(self.all_hands[i]):
                returned_points, returned_hand = self.is_royal(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_straight_flush(self.all_hands[i]):
                returned_points, returned_hand = self.is_straight_flush(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_four_kind(self.all_hands[i]):
                returned_points, returned_hand = self.is_four_kind(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_full_house(self.all_hands[i]):
                returned_points, returned_hand = self.is_full_house(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_flush(self.all_hands[i]):
                returned_points, returned_hand = self.is_flush(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_straight(self.all_hands[i]):
                returned_points, returned_hand = self.is_straight(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_three_kind(self.all_hands[i]):
                returned_points, returned_hand = self.is_three_kind(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_two_pair(self.all_hands[i]):
                returned_points, returned_hand = self.is_two_pair(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_one_pair(self.all_hands[i]):
                returned_points, returned_hand = self.is_one_pair(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)
            elif self.is_high_card(self.all_hands[i]):
                returned_points, returned_hand = self.is_high_card(self.all_hands[i])
                points.append(returned_points)
                hand.append(returned_hand)

            # appends every player's points to hand_points
            hand_points.append(points)
            # appends every player's hand type
            hand_type.append(hand)

        # sorts the cards based on points
        # sorts hands, players, and cards based on how points is sorted
        card_all_sorted = [x for _, x in sorted(zip(hand_points, card_all), reverse=True)]
        hand_type_sorted = [x for _, x in sorted(zip(hand_points, hand_type), reverse=True)]
        players_sorted = [x for _, x in sorted(zip(hand_points, players), reverse=True)]
        hand_points_sorted= sorted(hand_points, key=lambda tup: (tup[0]))
        #print(hand_type_sorted,players_sorted,hand_points_sorted,card_all_sorted)


        tied = []
        # cases where there are more than 1 one pair
        for j in range(len(hand_type_sorted)-1):
            for i in range(len(hand_type_sorted)-1):

                # checks to see if there is more than one type of hand that is one pair
                if hand_type_sorted[i] == ['One Pair'] and hand_type_sorted[i+1] == ['One Pair']:
                    first = Counter(card_all_sorted[i]).most_common(1)
                    com_first = first[0][0]
                    second = Counter(card_all_sorted[i+1]).most_common(1)
                    com_sec = second[0][0]

                    # checks to see if the first one pair is higher in rank than the second
                    if (first[0][1]) != 1 and (second[0][1]) != 1:

                        # switches elements if the first one pair is smaller than the second
                        if com_first < com_sec:
                            hand_type_sorted[i], hand_type_sorted[i+1] = hand_type_sorted[i+1], hand_type_sorted[i]
                            players_sorted[i+1], players_sorted[i] = players_sorted[i], players_sorted[i+1]
                            card_all_sorted[i], card_all_sorted[i+1] = card_all_sorted[i+1], card_all_sorted[i]

                        # if the one pairs are of equal value,
                        # looks to highest points
                        if com_sec == com_first:
                            if hand_points_sorted[i] < hand_points_sorted[i+1]:
                                hand_type_sorted[i], hand_type_sorted[i + 1] = hand_type_sorted[i + 1], hand_type_sorted[i]
                                players_sorted[i + 1], players_sorted[i] = players_sorted[i], players_sorted[i + 1]
                                card_all_sorted[i], card_all_sorted[i + 1] = card_all_sorted[i + 1], card_all_sorted[i]



        # same as above, but with Two pair cases
        for j in range(len(hand_type_sorted)-1):
            for i in range(len(hand_type_sorted)-1):
                if hand_type_sorted[i] == ['Two Pair'] and hand_type_sorted[i + 1] == ['Two Pair']:
                    first = Counter(card_all_sorted[i]).most_common(1)
                    com_first = first[0][0]
                    second = Counter(card_all_sorted[i + 1]).most_common(1)
                    com_sec = second[0][0]
                    if (first[0][1]) != 1 and (second[0][1]) != 1:
                        if com_first < com_sec:
                            hand_type_sorted[i], hand_type_sorted[i + 1] = hand_type_sorted[i + 1], hand_type_sorted[i]
                            players_sorted[i + 1], players_sorted[i] = players_sorted[i], players_sorted[i + 1]
                            card_all_sorted[i], card_all_sorted[i + 1] = card_all_sorted[i + 1], card_all_sorted[i]
                        if com_sec == com_first:
                            if hand_points_sorted[i] < hand_points_sorted[i + 1]:
                                hand_type_sorted[i], hand_type_sorted[i + 1] = hand_type_sorted[i + 1], hand_type_sorted[i]
                                players_sorted[i + 1], players_sorted[i] = players_sorted[i], players_sorted[i + 1]
                                card_all_sorted[i], card_all_sorted[i + 1] = card_all_sorted[i + 1], card_all_sorted[i]



        # with three of a kind cases
        for j in range(len(hand_type_sorted)-1):
            for i in range(len(hand_type_sorted)-1):
                if hand_type_sorted[i] == ['Three of a Kind'] and hand_type_sorted[i + 1] == ['Three of a Kind']:
                    first = Counter(card_all_sorted[i]).most_common(1)
                    com_first = first[0][0]
                    second = Counter(card_all_sorted[i + 1]).most_common(1)
                    com_sec = second[0][0]
                    if (first[0][1]) != 1 and (second[0][1]) != 1:
                        if com_first < com_sec:
                            hand_type_sorted[i], hand_type_sorted[i + 1] = hand_type_sorted[i + 1], hand_type_sorted[i]
                            players_sorted[i + 1], players_sorted[i] = players_sorted[i], players_sorted[i + 1]
                            card_all_sorted[i], card_all_sorted[i + 1] = card_all_sorted[i + 1], card_all_sorted[i]
                        if com_sec == com_first:
                            if hand_points_sorted[i] < hand_points_sorted[i + 1]:
                                hand_type_sorted[i], hand_type_sorted[i + 1] = hand_type_sorted[i + 1], hand_type_sorted[i]
                                players_sorted[i + 1], players_sorted[i] = players_sorted[i], players_sorted[i + 1]
                                card_all_sorted[i], card_all_sorted[i + 1] = card_all_sorted[i + 1], card_all_sorted[i]



        # prints players and their handtypes
        for k in range(len(hand_type_sorted)):
            print(players[k],': ', hand_type[k][0])
        print()

        # if there is a tie
        if hand_type_sorted[0] == hand_type_sorted[1]:
            # appends to a list if any of the other hand types are the same as the first one
            # first hand type in the list also has the highest points
            for i in range(1):
                tied.append(players_sorted[i])
                for j in range(len(hand_type_sorted)-1):
                    if hand_type_sorted[i] == hand_type_sorted[j+1]:
                        tied.append(players_sorted[j+1])

            # prints out ties and the winner of the ties
            for i in range(len(tied)):
                print(tied[i],' ties.')
            print()
            print(tied[0],' wins.')

        # if there isn't a tie
        else:
            player_won = players_sorted[0]
            hand_type_won = hand_type_sorted[0]
            print(player_won,' wins.')

    #function that checks if a hand is a royal flush
    def is_royal(self,hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    #function that checks if a hand is a straight flush
    def is_straight_flush(self,hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)-1):
            rank_order = rank_order and (hand[i].rank -1 == hand[i+1].rank)

        if (not rank_order):
            return 0
        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points, 'Straight Flush'

    #function that checks if a hand is a four of a kind
    def is_four_kind(self,hand):
        num_same = 0
        for i in range(len(hand)-1):
            if hand[i].rank == hand[i+1].rank:
                num_same += 1
        if num_same != 3:
            return 0

        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Four of a Kind'

    #function that checks if a hand is a full house
    def is_full_house(self,hand):
        # also has to handle ties
        hand_rank = []
        for card in hand:
            hand_rank.append(card.rank)
        hand_sets = set(hand_rank)

        # Checks if the hand is a full house
        if len(hand_sets) != 2:
            return 0

        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points,'Full House'

    #function that checks if a hand is a flush
    def is_flush(self,hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
        if not same_suit:
            return 0
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'


    #function that checks if a hand is a straight
    def is_straight(self,hand):
        rank_order = True
        for i in range(len(hand)-1):
            rank_order = rank_order and (hand[i].rank - 1 == hand[i+1].rank)
        if not rank_order:
            return 0
        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points,'Straight'


    #function that checks if a hand is a three of a kind
    def is_three_kind(self,hand):
        num_cards = 0
        for i in range(len(hand)-1):
            if (hand[i].rank == hand[i+1].rank == hand[i-1].rank):
                num_cards+= 1
        if num_cards != 1:
            return 0
        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Three of a Kind'


    #function that checks if a hand is a two pair
    def is_two_pair(self,hand):
        num_card = 0
        for i in range(len(hand)-1):
            if (hand[i].rank == hand[i+1].rank):
                num_card += 1
        if num_card != 2:
            return 0
        points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points,'Two Pair'


    #function that checks if a hand is a one pair
    def is_one_pair(self,hand):
        one_pair = False
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                break
        if (not one_pair):
            return 0

        points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'One Pair'


    #function that checks if a hand is a high card
    def is_high_card(self,hand):
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'


# main function
def main():
    # prompt the user to enter the number of players
    num_players = int(input('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int(input('Enter number of players: '))

    print()

    # create the Poker object
    game = Poker(num_players)
    # play the game
    game.play()


# calls main function
main()