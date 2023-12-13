'''
Description: Implement a product class that will manage product inventory

'''

class Product:

    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def add_inventory(self, amnt):
        self.count += amnt

    def sell_inventory(self, amnt):
        self.count -= amnt


if __name__ == "__main__":

    code = input()
    price = float(input())
    count = int(input())

    product = Product(code,price,count)

    product.add_inventory(count)
    product.sell_inventory(count)

    print(f'Name: {code}')
    print(f'Price: {price}')
    print(f'Count: {count}')
