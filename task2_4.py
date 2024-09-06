class ShoppingCart :
    def __init__(self):
        self.cart=[]
        # self.sum = 0
    def add_item(self,item_name,price,quantity):
        item = {
          "name":item_name,
          "price":price,
          "quantity":quantity
        }
        
        self.cart.append(item)
    def remove_item(self,item_name):
        for item in self.cart:
            if(item_name==item["name"]):
              self.cart.remove(item)
              break

        # print("Item not found")
    def calculate_total(self):
        sum=0
        for item in self.cart:
            sum+=item["price"] * item["quantity"]
        return sum
    def display_cart(self):
        for item in self.cart:
            print(item)
            
          
          

def main():
    cart = ShoppingCart()
    cart.add_item("Apple", 200, 3)
    cart.add_item("Banana", 150, 2)
    cart.add_item("Orange", 250, 4)
    
    cart.display_cart()
    cart.remove_item("Banana")
    cart.display_cart()
    print("Total cost of items:" + str(cart.calculate_total()))

if __name__ == "__main__":
    main()
