import unicodedata # Unicode metinlerde karakterlerin standart forma getirilmesi için kullanılan kütüphane
import os
name=str

print("\nKisisel Not Defteri Uygulamasina Hos Geldiniz:\n","="*40,sep="")  

def entry(): 
    with open("C:\\Users\\ASUS\\Desktop\\İsimler.txt","r",encoding="utf-8-sig") as dosya:
        valid_name=[name.strip().casefold() for name in dosya.readlines()]
    
    print("Lutfen Isminizi Giriniz: ")
    while True:
        global name # name değişkenini fonksiyon dışında tanımlamamıza rağmen derleyici, fonksiyon içerisinde  local değişkenmiş gibi görmesin diye tekrar global olarak tanımladık
        name = input().strip().lower()
        name_cf=name.casefold() # Dil üzerinde bazı karakter dönüşümleri yapar 
        
        if name_cf in valid_name: 
            name=name.capitalize() # Değerin ilk harfini büyük yapar
            break
        else:
            print("Gecersiz Veya Nadir Bir Isim Girdiniz. Lutfen Tekrar Deneyin:\n")

    print(f'\nMerhaba {name}. Devam Etmek Istiyorsan Herhangi Bir Tusa Basabilirsin Ya Da Q ile Cikis Yapabilirsin: ')
    while True:
        selection=input().strip()
        if(selection == 'q'):
            print("Not Uygulamasindan Cikis Yapiliyor")
            break
        else:
            note_operations()
            break

def note_operations():
    print(f'{name}, Hangi Islemi Yapmak Istersin:\n1-Not Dosyasi Olusturmak\n2-Not Guncellemek\n3-Notlari Goruntulemek')
    while True:
        start=input().strip()

        if(start=='1'):
            adding_notes() 
            break
        elif(start=='2'):
            updating_notes() 
            break 
        elif(start=='3'):
            view_notes() 
            break 
        else:
            print(f'Yanlis Secim {name}. Sana Yardimci Olmam Icin Lutfen Gecerli Bir Islem Secer Misin')

def adding_notes():
    print(f'{name}, Olusturmak Istedigin Not Dosyasinin İsmini Girer Misin: ')
    while True:
        file_name=input()
        file_path=f'C:\\Users\\ASUS\\Desktop\\{file_name}.txt'

        if os.path.exists(file_path):
            print(f'{file_name}.txt',"Bu Isimde Zaten Dosya Var. Baska Isim Dener Misin: " )
        
        else:
            file_content=input(f'{name}, Olusturdugun Dosyanin Icerisine Yazmak Istedigin Yaziyi Girer Misin: ')
            with open(f'C:\\Users\\ASUS\\Desktop\\{file_name}.txt',"x",encoding="utf-8-sig") as dosya:
                dosya.write(file_content)
            with open(f'C:\\Users\\ASUS\\Desktop\\{file_name}.txt',"r",encoding="utf-8-sig") as dosya:
                print("\nOlusturdugun Dosyanin Icerigi:",*dosya.readlines(),sep="")
                break      

def updating_notes():
    print(f"{name}, Hangi Notu Guncellemek Istersin:\n1-İsimler.txt\n2-Zeynep'in Notu\n3-Yaz Stajı")
    while True:
        choose_notes=input().strip()
        
        if(choose_notes == '1'):
            updating_message=input(f'{name}, Guncellenmis Notunu Yazar Misin: ')
            with open("C:\\Users\\ASUS\Desktop\\İsimler.txt","w",encoding="utf-8-sig") as dosya:
                dosya.write(updating_message)   
            with open("C:\\Users\\ASUS\Desktop\\İsimler.txt","r",encoding="utf-8-sig") as dosya:
                print("Guncellenmis Notun:",dosya.readlines())
                break
        
        elif(choose_notes == '2'):
            updating_message=input(f'{name}, Guncellenmis Notunu Yazar Misin: ')
            with open("C:\\Users\\ASUS\\Desktop\\Zeynep'in Notu.txt","w") as dosya:
                dosya.write(updating_message)
            with open("C:\\Users\\ASUS\\Desktop\\Zeynep'in Notu.txt","r") as dosya:
                print("Guncellenmis Notun:",dosya.readlines())
                break
 
        elif(choose_notes == '3'):
            updating_message=input(f'{name}, Guncellenmis Notunu Yazar Misin: ')
            with open("C:\\Users\\ASUS\Desktop\\Yaz Stajı.txt","w",encoding="utf-8-sig") as dosya:
                dosya.write(updating_message)
            with open("C:\\Users\\ASUS\Desktop\\Yaz Stajı.txt","r",encoding="utf-8-sig") as dosya:
                print("Guncellenmis Notun:",dosya.readlines())
                break
        
        else:
            print(f'{name}, Sana Yardimci Olabilmem Icin Lutfen Gecerli Bir Secim Yapar Misin: ')         

def view_notes():
    print(f"\n{name}, Hangi Notu Goruntulemek Istersin:\n1-İsimler.txt\n2-Zeynep'in Notu\n3-Yaz Stajı")
    while True:
        choose_notes=input().strip()
        
        if(choose_notes == '1'):
            with open("C:\\Users\\ASUS\Desktop\\İsimler.txt","r",encoding="utf-8-sig") as dosya:
                print(dosya.readlines())
                break
        elif(choose_notes == '2'):
            with open("C:\\Users\\ASUS\\Desktop\\Zeynep'in Notu.txt","r") as dosya:
                print(dosya.readlines())
                break
        elif(choose_notes == '3'):
            with open("C:\\Users\\ASUS\Desktop\\Yaz Stajı.txt","r",encoding="utf-8-sig") as dosya:
                print(dosya.readlines())
                break
        else:
            print(f'{name}, Sana Yardimci Olabilmem Icin Lutfen Gecerli Bir Secim Yapar Misin: ')                  
             
if __name__ == "__main__":
    entry()
