class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        self.print_cost = (self.item_quantity * self.item_price)
        print(self.item_name + " " +str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price *self.item_quantity))
        cost = self.item_quantity * self.item_price
        return cost
    def print_item_description(self):
        print(self.item + " " +str(self.item_description))


class ShoppingCart:
    def __init__(self,customer_name='none', current_date="Feburary 1,2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self,ItemToPurchase):
      

        self.cart_items.append(ItemToPurchase)

    def remove_item(self,item_name):
        
        flag = False        
        for i in self.cart_items:
            if(i.item_name == item_name):
                self.cart_items.remove(i)
                flag = True
            else:
                flag = False

        if(flag == False):
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        
        for product in self.cart_items:
            if(product.item_name == ItemToPurchase.item_name):
                product.item_quantity = ItemToPurchase.item_quantity
                flag = True
                break
            else:
                flag = False
        if(flag == False):
            print("Item not found in cart. Nothing modified.")
    

    def get_num_items_in_cart(self):
        numItems = 0
        for product in self.cart_items:
            numItems += product.item_quantity
        return numItems

    def get_cost_of_cart(self):
        total = 0
        cost = 0
        new_total = 0
        for product in self.cart_items:
            cost = (product.item_quantity * product.item_price)
            new_total += cost
        return new_total

    def print_total(self):
        new_total = self.get_cost_of_cart()
        if (new_total == 0):
            print("SHOPPING CART IS EMPTY\n")
        else:
            output_cart()

    def print_description(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
        print("Item Descriptions")
        for product in self.cart_items:
            print(product.item_name + ": " + product.item_description )

    def output_cart(self):
        new = ShoppingCart()
        print("OUTPUT SHOPPING CART")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items: ", self.get_num_items_in_cart(), "\n", sep='')
        sum_total = self.get_cost_of_cart()
        if(sum_total == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            pass

        x = 0
        for product in self.cart_items:
            print(product.item_name, " " , product.item_quantity , " @ $" , product.item_price , " = $" , (product.item_quantity * product.item_price), sep='')
            x += (product.item_quantity * product.item_price)
        print("\nTotal: $", x, sep = '')

def print_menu(onlineCart):

        customerCart = onlineCart
              
        chooseOption = None
        while (chooseOption !="q"):
            chooseOption = None
            print()
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            while (chooseOption != "a" and chooseOption != "r" and chooseOption !="c" and chooseOption != "i" and chooseOption != "o" and chooseOption != "q"):
                chooseOption = input("Choose an option:\n")
            if(chooseOption == "a"):
                print("ADD ITEM TO CART")
                item_name = str(input("Enter the item name:\n"));
                item_description = str(input('Enter the item description:\n'));
                item_price = int(input("Enter the item price:\n"));
                item_quantity = int(input('Enter the item quantity:\n'))
                new=ItemToPurchase(item_name, item_price, item_quantity, item_description)
                customerCart.add_item(new)
            elif(chooseOption == "r"):
                 print("REMOVE ITEM FROM CART")
                 remove= input("Enter name of item to remove:\n")
                 customerCart.remove_item(remove)
            elif(chooseOption == "c"):
                 print("\nCHANGE ITEM QUANTITY")
                 modify = input("Enter the item name:\n")
                 change = int(input("Enter the new quantity:\n"))
                 new = ItemToPurchase(modify, 0, change, 'none')
                 customerCart.modify_item(new)
            elif(chooseOption == "i"):
                 customerCart.print_description()
            elif(chooseOption == "o"):
                 customerCart.output_cart()
            elif(chooseOption == 'q'):
                 exit()
              
        return chooseOption



if __name__ == "__main__":
    while True:
        customer_name = str(input("Enter customer\'s name:"))
        current_date = str(input("\nEnter today\'s date:"))
        print("\n")
        print("Customer name:", customer_name)
        print("Today\'s date:", current_date)
        onlineCart = ShoppingCart(customer_name, current_date)
        v=print_menu(onlineCart)

        while(v =='a' or v== 'r' or v=='c' or v == 'i' or v=='o'):
              print_menu(onlineCart)
