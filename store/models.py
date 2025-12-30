from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def get_total_price(self, quantity):
        pass

    def display_info(self):
        print(f"Product: {self._name} | Base Price: ₦{self._price}")

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def get_total_price(self, quantity):
        return (self._price * quantity) + (self.weight * 200 * quantity)

class DigitalProduct(Product):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link 

    def get_total_price(self, quantity):
        return self._price * quantity