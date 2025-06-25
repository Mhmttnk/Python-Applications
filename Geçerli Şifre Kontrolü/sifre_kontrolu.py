import string

print("Gecerli Sifre Kontrolu Uygulamasina Hos Geldiniz\n")
print("1-15 Karakter Uzunlugunda Olusturmak Istediginiz Sifreyi Giriniz:")
min_length=8
max_length=15

def check_length(password): # Uzunluk Kontrolü
    print("\n🔎 Uzunluk Kontrolu Yapiliyor...")
    
    if len(password) < min_length:
        print("Sifre Cok Kısa. 8-15 Karakter Arasinda Olmali.\n")
        return False    
    elif len(password) > max_length:
        print("Sifre Cok Uzun. 8-15 karakter Arasinda Olmali.\n")
        return False
    else:
        print("Sifrenin Uzunlugu Uygun✅  Devam Etmek Icin Bir Tusa Bas: ")
        input()
        return True

def check_uppercase(password): # Büyük Harf Kontrolü
    print("🔎 Buyuk Harf Kontrolu Yapiliyor...")

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        print("⚠️  Sifrede En Az 1 Buyuk Harf Bulunmali. Lutfen Tekrar Dene: \n")
    else:
        print("Sifre, Buyuk Harf Kontrolunu Gecti✅  Devam Etmek Icin Bir Tusa Bas: ")
        input()

    return has_upper

def check_lowercase(password): # Küçük Harf Kontrolü
    print("🔎 Kucuk Harf Kontrolu Yapiliyor...")

    has_lower=any(char.islower() for char in password)
    if has_lower:
        print("Sifre, Kucuk Harf Kontrolunu Gecti✅  Devam Etmek Icin Bir Tusa Bas: ")
        input()
    else:
        print("⚠️  Sifre En Az 1 Kucuk Harf Icermeli")
    
    return has_lower

def check_digit(password): # Sayı Kontrolü
    print("🔎 Sayi Kontrolu Yapiliyor...")

    has_digit=any(digit.isdigit() for digit in password)
    if has_digit:
        print("Sifre, Sayi Kontrolunu Gecti✅  Devam Etmek Icin Bir Tusa Bas: ")
        input()
    else:
        print("⚠️  Sifrede En Az 1 Sayi Bulunmali. Lutfen Tekrar Dene: \n")

    return has_digit

def check_special_character(password): # Özel Karakter Kontrolü 
    print("🔎 Ozel Karakter Kontrolu Yapiliyor...")

    special_chars=string.punctuation # Standart özel karakterleri içerir.
    has_special_character=any(char in  special_chars for char in password)
    if has_special_character:
        print("Sifre, Ozel Karakter Kontrolunu Gecti✅")
    else:
        print("⚠️  Sifrede En Az 1 Ozel Karakter Olmali. Lutfen Tekrar Dene: \n")
    
    return has_special_character

def confirm_password(input_value): # Şifre kriterlerinden geçen şifrenin tekrar girilmesini isteyip eşleşme kontrolü yapar.
    print("\nSifreniz Kontrollerden Basariyla Gecti. Sifrenizi Olusturmak Icin Tekrar Giriniz: ")
    
    while True:
        value=input()
        if value == input_value:
            print("\nSifreniz Onaylandi ")
            return value
        else:
            print("\nSifreniz Onaylanmadi. Lutfen Tekrar Dene: ")        
    
if __name__ == "__main__":
    while True:
        input_value=input().strip()
        
        if not check_length(input_value): continue # Uzunluk Kontrolü geçersizse döngünün başına döner
        if not check_uppercase(input_value): continue # Büyük Harf Kontrolü geçersizse döngünün başına döner
        if not check_lowercase(input_value): continue # Küçük Harf Kontrolü geçersizse döngünün başına döner
        if not check_digit(input_value): continue # Sayi Kontrolü geçersizse döngünü başına döner
        if not check_special_character(input_value): continue # Özel Karakter Kontrolü geçersizse döngünün başına döner

        confirm_password(input_value)

        print("\nSifre Basarili Sekilde Olusturuldu ✅")
        break
            
