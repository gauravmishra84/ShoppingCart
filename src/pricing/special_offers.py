     
class Offers:
    
    current_offers = []
    
    def apply_offer(self):
        raise NotImplementedError()


class MultiByOffers(Offers):

    def __init__(self, offer_name, product_name, required_quantity, offer_price):      
        self.offer_name = offer_name
        self.product_name = product_name
        self.required_quantity = required_quantity
        self.offer_price = offer_price
        self.current_offers.append(self)

    def apply_offer(self, offer_name, product_name, required_quantity):
        if offer_name in self.current_offers:
            offer = self.current_offers[offer_name]
            if offer['product_name'] == product_name and offer['required_quantity'] == required_quantity:
                return offer['offer_price']


class MixnMatch(Offers):
    def __init__(self, offer_name, products, required_quantity_of_each, offer_price):
        self.offer_name = offer_name
        self.products = products
        self.required_quantity_of_each = required_quantity_of_each
        self.offer_price = offer_price
        self.current_offers.append(self)



    def apply_offer(self, offer_name, products, required_quantity_of_each):
        if not isinstance(products, list):
            raise ValueError("Invalid product list")
        elif offer_name in self.current_offers:
            offer = self.current_offers[offer_name]
            if all(item in offer['products'] for item in products) and offer['required_quantity_of_each'] == required_quantity_of_each:
                return offer['offer_price']