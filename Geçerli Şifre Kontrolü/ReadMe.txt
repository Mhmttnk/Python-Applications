# 🔐 Geçerli Şifre Kontrolü Uygulaması
Bu proje, kullanıcıdan alınan bir şifrenin çeşitli güvenlik kriterlerine uygun olup olmadığını kontrol eden bir Python uygulamasıdır. Toplamda **5 farklı kontrol** uygulanmaktadır.

## Geliştirici Notu
Bu uygulama; Python öğrenim sürecinde fonksiyon kullanımı, kullanıcı girdisi alma, string işlemleri ve kontrol yapıları gibi temel konuları pekiştirmek amacıyla geliştirilmiştir.

## ✅ Şifre Kriterleri

1. **Uzunluk Kontrolü:**  
   Şifre 8 ile 15 karakter arasında olmalıdır.

2. **Büyük Harf Kontrolü:**  
   En az 1 adet büyük harf (`A-Z`) içermelidir.

3. **Küçük Harf Kontrolü:**  
   En az 1 adet küçük harf (`a-z`) içermelidir.

4. **Sayı Kontrolü:**  
   En az 1 adet rakam (`0-9`) içermelidir.

5. **Özel Karakter Kontrolü:**  
   En az 1 adet özel karakter içermelidir.  
   (Örneğin: `!@#$%^&*()_+{}[]:;<>,.?/~` vb.)

## ⚙️ Nasıl Çalışır?

- Uygulama çalıştırıldığında kullanıcıdan bir şifre girmesi istenir.
- Yukarıdaki beş kritere göre şifre kontrol edilir.
- Tüm kontrollerden geçen şifre, tekrar girilerek onaylanır.
- Onay başarılıysa şifre başarılı şekilde oluşturulmuş olur.

## 📂 Dosya İçeriği

- `sifre_kontrolu.py`: Tüm kontrollerin yer aldığı ana Python dosyası.

## 🚀 Çalıştırmak İçin

Python 3 yüklü bir sistemde terminal veya komut istemcisine aşağıdaki komutu yazmanız yeterlidir:

```bash
python sifre_kontrolu.py