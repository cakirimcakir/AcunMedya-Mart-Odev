#sınıf oluşturuyoruz.
class Product:
#ilgili parametrelerel fonksiyon oluşturuyoruz.
     def __init__(self,name,price,stock):
         self.name = name
         self.price = price
         self.stock = stock
#Ürün fiyatını döndüren fonskiyonumuz.
     def get_price(self):
         return self.price
#Ürün fiyatının pozitif bir sayı olmasını gerektiren fonksiyonumuz.     
     def set_price(self, price):
         if price>0:
             self.price=price
         else:
             print("Fiyat geçerli olmalıdır.")
#Ürün stok miktarını döndüren fonksiyonumuz.
     def get_Stock(self):
         return self.stock
#Stok miktarının pozitif olması gerektiğini gösteren fonksiyonumuz.
     def set_Stock(self,stock):
         if stock>=0:
             self.stock=stock
         else:
             print("Stok sayısı negatif olamaz.")
#Gelen sipariş mevcut stoktan fazlaysa yanlış döndüren, eğer değilse de istenen miktarı mevcut stoktan düşürüp true döndüren fonksiyonumuz.
     def update_stock(self,quantity):
         if quantity > self.stock:
             print(f"Stok yetersiz! Mevcut Stok: {self.stock}")
             return False
         self.stock -= quantity
         return True
#Ürünü str olarak yazdıran fonksiyon
     def __str__(self):
         return f"{self.name} - {self.price} TL (Stok: {self.stock})"