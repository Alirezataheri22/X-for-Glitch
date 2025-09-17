EXPECTED_BAKE_TIME = 40
"""int: The expected bake time (in minutes) for the lasagna."""

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    Args:
        elapsed_bake_time (int): The number of minutes the lasagna has already been baking.

    Returns:
        int: The number of minutes remaining until the lasagna is done baking.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time.

    Args:
        number_of_layers (int): The number of layers of lasagna.

    Returns:
        int: Total preparation time in minutes (2 minutes per layer).
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time (prep + bake so far).

    Args:
        number_of_layers (int): The number of layers of lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has already been baking.

    Returns:
        int: Total time spent (preparation + baking so far).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


    
    

