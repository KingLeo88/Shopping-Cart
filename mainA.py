
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        self.print_cost = (self.item_quantity * self.item_price)
        print(self.item_name + " " +str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price *self.item_quantity))

def main():
    print('Item 1')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    product1 = ItemToPurchase(name, price, quantity)

    print('\nItem 2')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    product2 = ItemToPurchase(name, price, quantity)

    print('\nTOTAL COST')
    product1.print_item_cost()
    product2.print_item_cost()
    print('\nTotal: $%s' % (product1.print_cost + product2.print_cost))

if __name__ == "__main__":
    
    main()
