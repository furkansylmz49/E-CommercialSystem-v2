def customer_menu():
    actions = ["Ürünleri Listele","Sepete Ürün Ekle","Sepetten Ürün Çıkar","Sepettekileri Öde","Çıkış"]

    while(True):
        print("======CUSTOMER MENU======")
        for index,item in enumerate(actions,start=1):
            print(f"{index} -> {item}")

        try:
            choice = int(input("Lütfen Seçiminizi Giriniz: "))

            if 1 <= choice <= 5:
                print(f"{actions[choice-1]} Seçildi. Yönlendiriliyorsunuz...\n")
                return choice
            else:
                print("\nHata! Lütfen Geçerli Bir Sayı Giriniz.\n")
        except ValueError:
            print("\nHata! Lütfen Bir Sayı Değeri Girin.\n")

def login_menu():
    while (True):
        actions = ["Kullanıcı Girişi","Kullanıcı Kayıt"]
        print("======LOGIN MENU======")
        for index, item in enumerate(actions,start=1):
            print(f"{index} -> {item}")

        try:
            choice = int(input("Lütfen Seçiminizi Giriniz: "))

            if 1 <= choice <= 2:
                print(f"{actions[choice - 1]} Seçildi. Yönlendiriliyorsunuz...\n")
                return choice
            else:
                print("\nHata! Lütfen Geçerli Bir Sayı Giriniz.\n")
        except ValueError:
            print("\nHata! Lütfen Bir Sayı Değeri Girin.\n")

def message():
    print("\nİşleminiz Tamamlanmıştır Customer Menüsüne Yönlendiriliyorsunuz...\n")