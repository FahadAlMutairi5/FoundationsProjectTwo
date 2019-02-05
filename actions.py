# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "TawaiqSite"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for item in stores:
        print ("Ths store name is %s" % item.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for item in stores:
        if item.name == store_name:
            return item
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    pickstore = input("Pick a store by typing its name Or type 'checkout' to pay your bills:")
    if pickstore == "checkout":
        return "checkout"
    else:
        stor = get_store(pickstore)
        if stor != False:
            return stor
        else:
            print ("No store with that name. Please try again:")
            pick_store()


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

    picked_store.print_products()
    user_input_product = input ("Pick the items you'd like to add in your cart by typing the product name Or type 'Back' to go back to the main menu:")
    while user_input_product != "back":
        for item in picked_store.products:
            if item.name == user_input_product:
                cart.add_to_cart(item)
        user_input_product = input("Type another products Or 'back' to main menu:")
    
    
def shop():
    """
    The main shopping functionality
    """
    
    cart = Cart()
    pickstore = True
    while pickstore:
        store = pick_store()
        if store == "checkout":
            pickstore = False
        else:
            pick_products(cart,store)
    cart.checkout()
    
        
    
    
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
