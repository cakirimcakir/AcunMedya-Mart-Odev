class Order:
     def __init__(self,customer,cart):
         self.customer = customer
         self.cart = cart
         self.total_amount = cart.get_amount()
     
     def place_order(self):
         if self.total_amount > 0:
             print(f"\n Siparişin başarılı bir şekilde oluşturuldu.")
             print(self.customer)
             print("\nSipariş detayları:")
             self.cart.display_cart()
             print(f"\n Toplam Tutar: {self.total_amount} TL")
         else:
             print("\nSepet boş, sipariş oluşturulamadı.")

class OnlineOrder(Order):
    def __init__(self, customer, cart, delivery_adress):
        super().__init__(customer,cart)
        self.delivery_adress=delivery_adress
    def place_order(self):
        print(f"Çevrimiçi sipariş:{self.delivery_adress}")
        super().place_order()

class InStoreOrder(Order):
    def __init__(self,customer,cart, store_location):
        super().__init__(customer,cart)
        self.store_location=store_location
    def place_order(self):
        print(f"Mağaza siparişi: {self.store_location}")
        print(f"Müşteri İsmi:{self.customer}")
        print("Sepet:")
        self.cart.display_cart()
        super().place_order()
