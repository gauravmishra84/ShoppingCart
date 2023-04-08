## Problem Statement

This is the implementation for the given problem statement of creating a checkout function for a Supermarket and calculate total price for a cart considering any special offers.

### Assumptions

The solution assumes that the user will provide an inventory consisting a `Product` objects to traverse and calculates total price of a cart. In the total price calculation, I've implemented two type of offers, `MultiByOffers` and `MixnMatch`. These are classes to allow us adding more of similar sort of offers. 

### Environment and Structure

The code is written using the version `python 3.10.4`

The implementation is structured as a module under `src` and called `checkout_with_product_offers`. All the test cases are in the `tests` directory.

### Running in Terminal

To run the code directly in Terminal, we would need do below steps.

`import sys`
`sys.path.append('./src')`
`from checkout import checkout_with_products_offers as calc`
`from data import products as prod`
`from inventory.inventory import Inventory`
`from pricing.special_offers  import  Offers, MultiByOffers, MixnMatch`

And now once the module is imported, we could potentially create the object and a dummy pricing for some items:
```
#products
inventory = Inventory()
inventory.add_to_inventory(prod.Product(name='A',unit_price='50'))
inventory.add_to_inventory(prod.Product(name='B',unit_price='30'))
inventory.add_to_inventory(prod.Product(name='C',unit_price='20'))
inventory.add_to_inventory(prod.Product(name='D',unit_price='15'))    
inventory.add_to_inventory(prod.Product(name='E',unit_price='10'))

#special_buys
offers = Offers()
MultiByOffers(offer_name='multibyA',product_name='A',required_quantity=3, offer_price=130)
MultiByOffers(offer_name='multibyB',product_name='B',required_quantity=2, offer_price=45)
MixnMatch(offer_name='mix_match_DE',products=['D','E'],required_quantity_of_each=1, offer_price=20)
current_offers = offers.current_offers
```

`checkout = calc.Checkout(inventory, offers)`

`checkout.scan("A")`

`checkout.scan("B")`

`checkout.scan("C")`

`checkout.scan("D")`

`print(checkout.total())`

 This should result in 115.


### Running the Unit Test Cases
 
 To run the Unit Tests from terminal, simply navigate to the root folder and run a test discovery using this command:

 ` python -m unittest discover`

 This will search for unit tests and add the appropriate directory in `sys.path`

 Then simply call the tests with:

 `python -m unittest tests.checkout_with_products_offers_test`

### Packaging Configuration

Added the setuptools based packaging configuration defining how the the solutions could be packaged and converted into a wheel distribution.

Additionaly a pyproject.toml file is also provided to showcase how the packaging could be done using pyproject.toml. It could be used with poetry to manage all configuration in just one file, which makes it easy to build and deliver.

## Further improvement and scaling of the solution

 To scale this solution further, in a distributed computing environment, we can run multiple instances of the SupermarketCheckout class and distribute the load among them, possibly using a load balancer. The pricing rules can be passed to each instance as an argument, so they can be customized for each location or store. We can also have a more defined storage and management for inventory and pricing rules targeting specific regions and stores. The solution could be organized in a microservices architecture running in a container orchestrated tool like kubernetes and serving a no of simultaneous requests.

