# E-Commercial System v2

E-Commercial System v2, **Python ile geliştirilmiş etkileşimli bir e-ticaret uygulamasıdır**. Bu proje, JSON dosyaları üzerinden veri yönetimi, sınıf tabanlı programlama, temel algoritmalar, kullanıcı doğrulama ve regex kullanımı gibi temel konuları pekiştirmek amacıyla hazırlanmıştır. Proje, küçük ölçekli bir mağaza simülasyonu sağlar ve kullanıcıların ürünleri görüntülemesine, sepetlerine eklemesine ve satın almalarına olanak tanır.

---

## Özellikler

* **JSON Dosyası Yönetimi**: Tüm veriler (`Products.json`, `Users.json`, `Cart.json`) JSON formatında saklanır ve okunur.
* **Kullanıcı Kaydı ve Girişi**:

  * E-posta ve şifre doğrulama regex ile yapılır.
  * Şifre güvenliği için büyük/küçük harf, rakam ve sembol kullanımı zorunludur.
* **Ürün Yönetimi**:

  * Mağaza ürünlerini listeleyebilme
  * Ürün stoğunu kontrol ederek sepete ekleme/çıkarma
* **Sepet Yönetimi**:

  * Sepete ürün ekleme ve çıkarma
  * Sepetteki ürünleri satın alma ve toplam fiyat hesaplama
* **Stok Kontrolü**: Satın alma sırasında yeterli stok yoksa işlem engellenir.
* **CLI Tabanlı Menü Sistemi**: Kullanıcı dostu komut satırı arayüzü ile etkileşim.

---

## Kurulum

1. Bu repoyu klonlayın:

```bash
git clone https://github.com/furkansylmz49/E-CommercialSystem-v2.git
cd E-CommercialSystem-v2
```

2. Python 3 yüklü olmalıdır. Yüklü değilse [Python resmi web sitesi](https://www.python.org/downloads/) üzerinden yükleyebilirsiniz.

3. Projeyi çalıştırın:

```bash
python main.py
```

> Not: JSON dosyaları (`Products.json`, `Users.json`, `Cart.json`) otomatik olarak `JSON_FILE` klasöründe oluşturulur.

---

## Dosya Yapısı

```
E-CommercialSystem-v2/
│
├── JSON_FILE/
│   ├── Products.json      # Ürün bilgilerini saklar
│   ├── Users.json         # Kullanıcı bilgilerini saklar
│   └── Cart.json          # Sepet bilgilerini saklar
│
├── classes0.py            # Store, User, Cart sınıfları ve JSON işlemleri
├── func.py                # Menü ve mesaj fonksiyonları
└── main.py                # Ana çalışma dosyası, kullanıcı akışı
```

---

## Kullanım

### 1. Login Menüsü

* Programı başlattığınızda kullanıcıya **Login Menüsü** gelir.
* Seçenekler:

  * Kullanıcı Girişi
  * Kullanıcı Kayıt

### 2. Kayıt İşlemi

* E-posta formatı kontrol edilir: `^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+$`
* Şifre güvenliği için regex kullanılır: `(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!'^+%&/()=?_]).{8,}`
* Kayıt başarılı olursa kullanıcı login menüsüne yönlendirilir.

### 3. Customer Menüsü

* Ürünleri Listele
* Sepete Ürün Ekle
* Sepetten Ürün Çıkar
* Sepettekileri Öde
* Çıkış

#### Örnek Kullanım

```text
======CUSTOMER MENU======
1 -> Ürünleri Listele
2 -> Sepete Ürün Ekle
3 -> Sepetten Ürün Çıkar
4 -> Sepettekileri Öde
5 -> Çıkış
```

* Kullanıcı, ilgili numarayı girerek işlem yapar.
* Sepete ekleme ve çıkarma işlemleri sırasında stok kontrolü yapılır.
* Satın alma işlemi sırasında toplam tutar hesaplanır ve JSON dosyaları güncellenir.

---

## Regex ve Doğrulama

* **E-posta Doğrulama**:

```python
^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+$
```

* **Şifre Doğrulama** (en az 8 karakter, büyük/küçük harf, rakam ve sembol):

```python
(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!'^+%&/()=?_]).{8,}
```

---

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz:

1. Repoyu fork edin.
2. Yeni bir branch açın (`git checkout -b feature/özellik`).
3. Değişiklikleri commit edin (`git commit -m 'Yeni özellik ekledim'`).
4. Branch’i push edin (`git push origin feature/özellik`).
5. Pull request gönderin.

---

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.

---

## Notlar

* Proje, eğitim amaçlıdır ve küçük ölçekli mağaza simülasyonu için uygundur.
* GUI desteği yoktur; tüm işlemler **komut satırı üzerinden** yapılır.
* JSON dosyalarının elle düzenlenmesi önerilmez, tüm veri işlemleri program üzerinden yapılmalıdır.

```
# README.md dosyasını kaydetmek için:
nano README.md   # veya favori editörünüzü kullanın
```

---

## Örnek Görseller

```
Ürün Listeleme:
Name: Laptop, Price: 15000, Stok: 10
Name: Mouse, Price: 150, Stok: 50
```

```
Sepete Ürün Ekleme:
Sepetinize 2 adet Mouse eklendi.
```

```
Satın Alma:
✅ Satın alma işlemi tamamlandı. Toplam tutar: 300 TL
```
