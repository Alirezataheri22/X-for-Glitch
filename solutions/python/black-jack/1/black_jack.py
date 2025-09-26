"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    def value_of_card(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)  
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two) 
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)

def value_of_ace(card_one, card_two):
    def get_card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    total_with_ace_as_1 = get_card_value(card_one) + get_card_value(card_two) + 1
    total_with_ace_as_11 = get_card_value(card_one) + get_card_value(card_two) + 11
    if total_with_ace_as_11 > 21:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    def get_card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    has_ace = 'A' in (card_one, card_two)
    has_ten_value = any(card in ['10', 'J', 'Q', 'K'] for card in (card_one, card_two))
    total = get_card_value(card_one) + get_card_value(card_two)
    return total == 21


def can_split_pairs(card_one, card_two):
    def get_card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)
    
    value_one = get_card_value(card_one)
    value_two = get_card_value(card_two)
    
    return value_one == value_two


def can_double_down(card_one, card_two):
    def get_card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)
    
    total = get_card_value(card_one) + get_card_value(card_two)
    
    return total in [9, 10, 11]
