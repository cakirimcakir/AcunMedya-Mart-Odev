class Product:
     def __init__(self,name,price,stock):
         self.name = name
         self.price = price
         self.stock = stock
     
     def get_price(self):
         return self.price
     
     def set_price(self, price):
         if price>0:
             self.price=price
         else:
             print("Fiyat geçerli olmalıdır.")
            
     def get_Stock(self):
         return self.stock
     
     def set_Stock(self,stock):
         if stock>=0:
             self.stock=stock
         else:
             print("Stok sayısı negatif olamaz.")
             
     def update_stock(self,quantity):
         if quantity > self.stock:
             print(f"Stok yetersiz! Mevcut Stok: {self.stock}")
             return False
         self.stock -= quantity
         return True
     
     def __str__(self):
         return f"{self.name} - {self.price} TL (Stok: {self.stock})"