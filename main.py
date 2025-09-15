from func import login_menu,customer_menu,message
from classes0 import User,Cart,Store
import re

user = User()
cart = Cart()
store = Store()

print("E-Ticaret Sistemimize Hoş Geldiniz :)\n")
while(True):
    choice = login_menu()

    if choice == 1:
        email = input("Lütfen E-Posta Adresinizi Giriniz: ")
        password = input("Lütfen Şifrenizi Giriniz: ")

        users = user.read_store()
        try:
            user0 = next(u for u in users if u["email"] == email and u["password"] == password)
            print("\nGiriş Başarılı. Customer Menüsüne Yönlendiriliyorsunuz...\n")
            break
        except StopIteration:
            print("\nYazdığınız Kullanıcı Bilgiler Sistemimizde Kayıtlı Değil. Login Menüsüne Yöneldiriliyorsunuz...\n")

    elif choice == 2:
        email = input("Lütfen E-Posta Adresinizi Giriniz: ")
        password = input("Lütfen Şifrenizi Giriniz: ")

        users = user.read_store()

        result = re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+$",email)
        result2 = re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!'^+%&/()=?_]).{8,}",password)

        if any(user["email"] == email for user in users):
            print("\nBu Eposta Sistemimize Kayıtlı Lütfen Başka Bir Eposta Deneyiniz.")
            print("Login Menüsüne Yönlendiriliyorsunuz...\n")
        else:
            if bool(result) and bool(result2):
                users.append({"email":email,"password":password})
                user.save_store(users)
                print("\nSisteme Kayıdınız Tamamlanmıştır. Login Menüsüne Yönlendiriliyorsunuz...\n")
            else:
                if not result:
                    print("\nLütfen e-posta standartlarına uygun bir mail giriniz.\n")
                if not result2:
                    if not re.search(r"(?=.*[a-z])", password):
                        print("Lütfen Şifrenizde Küçük Harf Kullanınız.")
                    if not re.search(r"(?=.*[A-Z])", password):
                        print("Lütfen Şifrenizde Büyük Harf Kullanınız.")
                    if not re.search(r"(?=.*[0-9])", password):
                        print("Lütfen Şifrenizde Rakam Kullanınız.")
                    if not re.search(r"(?=.*[!'^+%&/()=?_@∑€®₺¥])", password):
                        print("Lütfen Şifrenizde Sembol Kullanınız.")
                    if not re.search(r".{8,}", password):
                        print("Lütfen Şifrenizde Minimum 8 Karakter Kullanınız.")
                    print("\nLogin Menüsüne Yönlendiriliyorsunuz...\n")

while(True):
    choice = customer_menu()

    if choice == 1:
        store.list_product()
        message()
    elif choice == 2:
        try:
            name = input("Sepete Eklemek İstediğiniz Ürünün Adını Giriniz: ")
            quantity = int(input("Üründen Kaç Adet Eklemek İstediğinizi Giriniz: "))
            if quantity < 0:
                print("\nÜrün Sayısı Negatif Olamaz. Customer Menüsüne Yönlendiriliyorsunuz...\n")
            else:
                cart.add_product(user0["email"],name,quantity)
                message()

        except ValueError:
            print("Hata! Lütfen Bir Sayı Giriniz.")
    elif choice == 3:
        try:
            name = input("Sepetten Çıkarmak İstediğiniz Ürünün Adını Giriniz: ")
            quantity = int(input("Üründen Kaç Adet Çıkarmak İstediğinizi Giriniz: "))

            if quantity < 0:
                print("\nÜrün Sayısı Negatif Olamaz. Customer Menüsüne Yönlendiriliyorsunuz...\n")
            else:
                cart.remove_product(user0["email"], name, quantity)
                message()

        except ValueError:
            print("Hata! Lütfen Bir Sayı Giriniz.")

    elif choice == 4:
        cart.satin_al(user0["email"])

    elif choice == 5:
        print("Çıkış Yapılıyor. Tekrar Bekleriz :)")
        break






