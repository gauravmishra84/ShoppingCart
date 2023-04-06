from data.products import Product

class Inventory:
    
    inventory = []
    
    def add_to_inventory(self, product: Product) -> None:
        '''
        Method to add items to inventory
        
        params: 
                product: Product
        '''
        if product not in self.inventory:
            self.inventory.append(product)
    
    def remove_from_inventory(self, product: Product) -> None:
        '''
        Method to remove items from inventory
        
        params: 
                product: Product
        '''        
        if not self.inventory:
            raise ValueError("Empty Inventory")
        if product in self.inventory:
            self.inventory.remove(product)
            
            