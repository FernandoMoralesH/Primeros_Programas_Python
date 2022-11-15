
import product

product.Product() 


class Product:
    def _init_ (self, name, price):
        self.name = name
        self.price

class ShoppingCar:
    def _init_(self):
        self.products = []
    
    def add_product (self, product)