"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number + 1, number + 2]



def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2



def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    true_avg = sum(hand) / len(hand)
    approx_avg1 = (hand[0] + hand[-1]) / 2
    middle_index = len(hand) // 2
    approx_avg2 = hand[middle_index]
    return approx_avg1 == true_avg or approx_avg2 == true_avg


def average_even_is_average_odd(hand):
    even_cards = hand[::2]  
    odd_cards = hand[1::2]  
    
    even_avg = sum(even_cards) / len(even_cards) if even_cards else 0
    odd_avg = sum(odd_cards) / len(odd_cards) if odd_cards else 0
    
    return even_avg == odd_avg


def maybe_double_last(hand):
    if hand and hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    
    return hand
