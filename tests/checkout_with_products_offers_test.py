import sys  
sys.path.append("./src")

import unittest
from checkout import checkout_with_products_offers as calc
from data import products as prod
from inventory.inventory import Inventory
from pricing.special_offers  import  Offers, MultiByOffers, MixnMatch


class CheckoutGenericTestCases(unittest.TestCase):
    
    def setUp(self) -> None:
        #products
        self.inventory = Inventory()
        self.inventory.add_to_inventory(prod.Product(name='A',unit_price='50'))
        self.inventory.add_to_inventory(prod.Product(name='B',unit_price='30'))
        self.inventory.add_to_inventory(prod.Product(name='C',unit_price='20'))
        self.inventory.add_to_inventory(prod.Product(name='D',unit_price='15'))    
        self.inventory.add_to_inventory(prod.Product(name='E',unit_price='10'))
        
        #special_buys
        self.offers = Offers()
        MultiByOffers(offer_name='multibyA',product_name='A',required_quantity=3, offer_price=130)
        MultiByOffers(offer_name='multibyB',product_name='B',required_quantity=2, offer_price=45)
        MixnMatch(offer_name='mix_match_DE',products=['D','E'],required_quantity_of_each=1, offer_price=20)
        self.current_offers = self.offers.current_offers

        return super().setUp()

    def tearDown(self):
        for i in self.inventory.inventory:
            del i
        del self.inventory
        del self.current_offers
        del self.offers

    def test_valid_item(self):
        checkout = calc.Checkout(self.inventory, self.current_offers)
        checkout.scan("A")
        self.assertEqual(checkout.items, {'A':1})
        
    def test_invalid_item(self):
        checkout = calc.Checkout(self.inventory, self.current_offers)
        with self.assertRaises(ValueError):
            checkout.scan("K")

    def test_empty_cart(self):
        checkout = calc.Checkout(self.inventory, self.current_offers)
        with self.assertRaises(KeyError):
            checkout.total_price()
            
    def test_calculate_total_without_special_price(self):
        offers = []
        checkout = calc.Checkout(self.inventory, offers)
        checkout.scan("A")
        checkout.scan("B")
        checkout.scan("C")
        checkout.scan("D")
        self.assertEqual(checkout.total_price(), 115)
        
    def test_calculate_total_with_special_price(self):
        checkout = calc.Checkout(self.inventory, self.current_offers)
        checkout.scan("B")
        checkout.scan("A")
        checkout.scan("B")
        checkout.scan("A")
        checkout.scan("B")
        self.assertEqual(checkout.total_price(), 175)
        
    def test_calculate_total_with_mix_match(self):
        offers = [MixnMatch(offer_name='mix_match_DE',products=['D','E'],required_quantity_of_each=1, offer_price=20)]
        checkout = calc.Checkout(self.inventory, offers)
        checkout.scan("E")
        checkout.scan("D")
        checkout.scan("D")
        self.assertEqual(checkout.total_price(), 35)        
        

if __name__ == "__main__":
    unittest.main()
