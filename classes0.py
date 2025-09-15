import json
import os

class BaseJsonFile:
    def __init__(self,file_name):
        self.file_name = file_name

        os.makedirs("JSON_FILE", exist_ok=True)

        if not os.path.exists(self.file_name):
            with open(self.file_name,"w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii = False,indent=4)

    def read_store(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_store(self,product):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(product, f, ensure_ascii=False, indent=4)

class Store(BaseJsonFile):
    def __init__(self):
        super().__init__("JSON_FILE/Products.json")

    def list_product(self):
        products = self.read_store()
        if products == []:
            print("Mağzada Ürün Yoktur.")
        else:
            print("Ürün Listesi: \n")
            for product in products:
                print(f"Name: {product['name']}, Price: {product['price']}, Stok: {product['stok']}")

class User(BaseJsonFile):
    def __init__(self):
        super().__init__("JSON_FILE/Users.json")
class Cart(BaseJsonFile):
    def __init__(self):
        super().__init__("JSON_FILE/Cart.json")

    def add_product(self,email,name,quantity):
        products = Store().read_store()
        cart = self.read_store()

        try:
            product = next(item for item in products if item["name"].upper() == name.upper())
        except StopIteration:
            print("Girmiş Olduğunuz İsimde Ürün Mağzamızda Yoktur")
            return

        bulundu = False
        for item in cart:
            if item["email"] == email:
                bulundu = True
                break

        if not bulundu:
            cart.append({"email":email,"cart":[]})
            self.save_store(cart)

        bulundu = False
        for item in cart:
            if item["email"] == email:
                for product_in_cart in item["cart"]:
                    if name.upper() == product_in_cart["name"].upper():
                        bulundu =True
                        if product_in_cart["quantity"]+quantity <= product["stok"]:
                            product_in_cart["quantity"] += quantity
                            print("Ürün Sepetinize Başarıyla Eklenmiştir.")
                            self.save_store(cart)
                        else:
                            print("Ürün Stoğu Yetersiz.")
                            self.save_store(cart)
        if not bulundu:
            for item in cart:
                if item["email"] == email:
                    if quantity <= product["stok"]:
                        item["cart"].append({"name":name,"price":product["price"],"quantity":quantity})
                        print("Ürün Sepetinize Başarıyla Eklenmiştir.")
                        self.save_store(cart)
                    else:
                        print("Ürün Stoğu Yetersiz.")
                        self.save_store(cart)

    def remove_product(self,email,name,quantity):
        products = Store().read_store()
        cart = self.read_store()

        try:
            product = next(item["name"] for item in products if item["name"].upper() == name.upper())
        except StopIteration:
            print("Girmiş Olduğunuz İsimde Ürün Mağzamızda Yoktur")
            return

        bulundu = False
        for item in cart:
            if item["email"] == email:
                bulundu = True
                break

        if not bulundu:
            cart.append({"email": email, "cart": []})
            self.save_store(cart)

        bulundu = False
        for item in cart:
            if item["email"] == email:
                for product_in_cart in item["cart"]:
                    if name.upper() == product_in_cart["name"].upper():
                        bulundu = True
                        if product_in_cart["quantity"] > quantity:
                            product_in_cart["quantity"] -= quantity
                            self.save_store(cart)
                        elif product_in_cart["quantity"] == quantity:
                            item["cart"].remove(product_in_cart)
                            self.save_store(cart)
                        else:
                            print("Silmek İstediğiniz Miktarda Ürün Sepetinizde Bulunamadı.")
                            self.save_store(cart)
        if not bulundu:
            print("Yazdığınız İsimde Ürün Sepetinizde Bulunamadı.")

    def satin_al(self,email):
        products = Store().read_store()
        cart = self.read_store()

        bulundu = False
        for item in cart:
            if item["email"] == email:
                bulundu = True
                break

        if not bulundu:
            cart.append({"email":email,"cart":[]})
            self.save_store(cart)

        for item in cart:
            if item["email"] == email:
                for product_in_cart in item["cart"]:
                    for product in products:
                        if product["name"] == product_in_cart["name"]:
                            if product["stok"]< product_in_cart["quantity"]:
                                print("Stokta Yeterli Ürün Yok Satın Alma İşlemini Gerçekleştiremiyoruz.")
                                return

        toplam = 0
        for item in cart:
            if item["email"] == email:
                for product_in_cart in item["cart"]:
                    toplam += product_in_cart["price"]*product_in_cart["quantity"]
                    for product in products:
                        if product_in_cart["name"] == product["name"]:
                            product["stok"] -= product_in_cart["quantity"]
            item["cart"].clear()

        self.save_store(cart)
        Store().save_store(products)
        print(f"✅ Satın alma işlemi tamamlanmıştır. Toplam tutar: {toplam} TL")



