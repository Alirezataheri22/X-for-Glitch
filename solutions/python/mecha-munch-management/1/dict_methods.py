"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    fulfillment = {}
    for item in sorted(cart.keys(), reverse=True):
        fulfillment[item] = [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]]
    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        if item in store_inventory:
            store_inventory[item][0] -= fulfillment_cart[item][0]
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
