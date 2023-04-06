     
class Offers:
    
    current_offers = []
    
    def apply_offer(self):
        raise NotImplementedError()

class MultiByOffers(Offers):

    def __init__(self, offer_name: str, product_name: str, required_quantity: int, offer_price: float) -> None:      
        '''
        Init Method to create a new MultiByOffers Object.
        
        params:
                offer_name: str
                product_name: str
                required_quantity: int
                offer_price: float
        '''        
        self.offer_name = offer_name
        self.product_name = product_name
        self.required_quantity = required_quantity
        self.offer_price = offer_price
        self.current_offers.append(self)

    def apply_offer(self, offer_name: str, product_name: str, required_quantity: int) -> float:
        '''
        Method to apply the offer if the product name and require quantity matches in the cart
        
        params:
                offer_name: str
                product_name: str
                required_quantity: int
                
        returns: 
                offer_price: float
        '''
        if offer_name in self.current_offers:
            offer = self.current_offers[offer_name]
            if offer['product_name'] == product_name and offer['required_quantity'] == required_quantity:
                return offer['offer_price']

class MixnMatch(Offers):
    
    def __init__(self, offer_name: str, products: list, required_quantity_of_each: int, offer_price: float) -> None:
        '''
        Init Method to create a new MixnMatch Object.
        
        params:
                offer_name: str
                products: list
                required_quantity_of_each: int
                offer_price: float
        '''           
        self.offer_name = offer_name
        self.products = products
        self.required_quantity_of_each = required_quantity_of_each
        self.offer_price = offer_price
        self.current_offers.append(self)

    def apply_offer(self, offer_name: str, products: list, required_quantity_of_each: int) -> float:
        '''
        Method to apply the offer if all the products required for mix_match
        are in the cart with the require quantity of each matches in the cart.
        
        params:
                offer_name: str
                products: list
                required_quantity_of_each: int
                
        returns: 
                offer_price: float
        '''
        if offer_name in self.current_offers:
            offer = self.current_offers[offer_name]
            if all(item in offer['products'] for item in products) and offer['required_quantity_of_each'] == required_quantity_of_each:
                return offer['offer_price']