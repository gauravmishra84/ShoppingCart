from typing import Dict
from pricing.special_offers import MultiByOffers, MixnMatch

class Checkout:
    '''
    This class represents the mechanism to caculate the total price payable by
    a customer for their checkout cart
    
    params: pricing_rule: Dict ( A Dictionary of a product type with unit and special pricing if any)
    
    returns: A new SupermarketCheckout Object
    '''
    def __init__(self, inventory, offers):
        self.inventory = inventory
        self.offers = offers
        self.items = {}
        
    def scan(self, item: str):
        '''
        Method to add items in the cart
        
        params: item: string
        '''
        # check if the item is part of the inventory
        self.checkout = {prod.name:float(prod.unit_price) for prod in self.inventory.inventory}
        if item not in self.checkout:
                raise ValueError(f"Invalid item: {item}")        
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

        

        
    def total(self) -> int:
        '''
        Method to check the checkout basket and calculate the total payable price
        
        returns: int ( The total price payable with any special offers applicable on the cart)
        '''
        # Check if the shopping cart isn't empty
        if not self.items:
            raise KeyError(f" Empty Cart ")
        
        total = 0
        cart = list(self.items.keys())
        for item in cart:
            price = self.checkout[item]
            total += self.items[item] * price   
            if self.offers:
                for offer in self.offers:                
                    if isinstance(offer, MultiByOffers):
                        if item == offer.product_name and self.items[item] >= offer.required_quantity:
                            quotient, remainder = divmod(self.items[item], offer.required_quantity)
                            total -= offer.required_quantity*price
                            total += quotient* offer.offer_price
                            for _ in range(offer.required_quantity):
                                if self.items[item] > 1:
                                    self.items[item] -= 1  
                                else:
                                    del self.items[item]
                    if isinstance(offer, MixnMatch):
                        mix_match_items = all(i in self.items for i in offer.products)
                        if mix_match_items:
                            total += offer.offer_price
                        for x in offer.products:                                
                            if item == x:
                                total -= self.checkout[x]
                                if self.items[x] > 1:
                                    self.items[x] -= 1
                                else:
                                    del self.items[x]

        return total
    