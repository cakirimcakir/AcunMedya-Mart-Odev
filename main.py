from product import Product
from customer import Customer
from cart import Cart
from order import Order, OnlineOrder, InStoreOrder

def main():
#Müşteri Oluşturuyoruz.
    customer1=Customer("Ali Emir Çakır","ornek@ornek.com")
#Sepet oluşturuyoruz.
    cart=Cart()
#Ürünler Ekleniyor.
    product1=Product("Bilgisayar", 425000,100)
    product2=Product("Telefon", 75000, 80)
    product3=Product("Mouse", 800,300)
#Sepetimizi oluşturuyoruz
    cart.add_product(product1,63)
    cart.add_product(product2,70)
    cart.add_product(product3, 140)

    online_order=OnlineOrder(customer1,cart, "Rize, Türkiye")
    online_order.place_order()

    in_Store_order=InStoreOrder(customer1, cart, "Ana Mağaza")
    in_Store_order.place_order()

if __name__=="__main__":
    main()






