def main_menu(select_operation):
    print(f'{name}, Hangi Islemi Yapmak Istersin ?\n1-Gorev Ekleme\n2-Gorev Silme\n3-Gorevleri Listeleme\n4-Gorevleri ✅ Isaretleme\n5-Uygulamayi Kapatma \n')
    process_routing(select_operation)

def process_routing(select_operation): # İşlemlere Yönlendiren Fonksiyon 
    while True:
        select_operation=input()
        if select_operation == "1":
            add_task(select_operation)
            break
        elif select_operation == "2":
            delete_task(select_operation)
            break
        elif select_operation == "3":
            list_task(select_operation)
            break
        elif select_operation == "4":
            complette_task(select_operation)
            break
        elif select_operation == "5":
            print("Gorev Takip Uygulamasi Kapatiliyor...")
            break
        else:
            print(f'{name}, Lutfen Gecerli Bir Islem Secer Misin: \n')                

def add_task(task_name): # Görev Ekleme Fonksiyonu
    print(f'{name}, Eklemek Istedigin Gorevi Yazar Misin ✍️:\n')

    while True:
        task_name = input().strip().title()

        if not any(char.isalpha() for char in task_name): # Girilen görevin anlamlı olup olmadığını harf yoluyla kontrol eder
            print(f"⚠️  Harf Icermeyen Gorev! {name}, Lutfen Anlamli Bir Cumle Girer Misin ?")
            continue
        
        cleaned_task = task_name.replace(" ", "").lower() # Girilen görevin anlamlı olup olmadığını karakter yoluyla kontrol eder 
        if len(set(cleaned_task)) == 1:
            print(f"⚠️  Tum Karakterler Ayni Olamaz! {name}, Lutfen Anlamli Cumle Girer Misin ?")
            continue

        words = task_name.split()
        singel_letter_word = all(len(set(word)) == 1 for word in words) # Kelimenin sadece aynı harflerden mi oluştuğunu kontrol eder
        if singel_letter_word:
            print(f"⚠️  Tum Kelimeler Tekrarlanan Harflerden Olusamaz! {name}, Lutfen Anlamli Cumle Girer Misin ?")
            continue
        
        try:
            with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt", "r", encoding="utf-8") as file:
                existing_tasks = [line.strip().lower() for line in file]
        except FileNotFoundError:
            existing_tasks = []

        if task_name.lower() in existing_tasks:
            print(f"⚠️ Bu Gorev Zaten Mevcut. {name}, Lutfen Baska Gorev Girer Misin ?")
            continue

        with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt", "a", encoding="utf-8") as file:
            file.write(task_name + "\n")
        print(f"{name}, Yeni Gorevin Basariyla Eklendi ✅")
        break

def delete_task(tasks): # Gorev Silme Fonksiyonu
    print("🔍 Mevcut Gorevler Listeleniyor...\n")
    with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt", "r", encoding="utf-8") as file:
        tasks= [line.strip() for line in file.readlines()] # Mevcut gorevleri okur ve listeler

    if not tasks:
        print("❌ Listede Gorev Yok...")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print(f"\n{name}, Silmek Istedigin Gorevin Numarasini Girer Misin ✍️")

    while True:
        try:
            selected_index = int(input())
            if 1 <= selected_index <= len(tasks):
                deleted_task = tasks[selected_index - 1]  # Henüz silme!
                
                confirm = input(f"\n'{deleted_task}' Gorevini Silmek Istedigine Emin Misin ? (E/H): ").strip().lower() # Emin misin sorusu
                if confirm.lower() == "e":
                    tasks.pop(selected_index - 1)
                    break
                else:
                    print("❌ Silme Islemi Iptal Edildi.")
                    return
            else:
                print(f"⚠️  Gecersiz No! Lutfen 1 ile {len(tasks)} Arasinda Bir Sayi Girer Misin: ")
        except ValueError:
            print("⚠️  Gecersiz Giris! Lutfen Sadece Sayi Girer Misin.")

    with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")  # Güncellenmiş görevleri dosyaya yaz

    print(f"'{deleted_task}' Gorevi Basariyla Silindi 🗑️")

def list_task(task_name): # Görevleri Listeleme Fonksiyonu
    print("\nGorevler Listeleniyor...⏳ ")
    
    with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt","r",encoding="utf-8") as file:
        task_name=[line.strip() for line in file.readlines()]
        
        if not task_name:
            print("❌ Henuz Hic Gorev Eklenmemis...")

        for index, task in enumerate(task_name, start=1):
            print(f"{index}. {task}")    

def complette_task(completed_task): # Tamamlanan Görevleri ✅ ile İşaretleme Fonksiyonu
    print(f"\n{name}, Tamamladigin Hangi Gorevi ✅ Ile Isaretlemek Istersin ?")
    
    with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt","r",encoding="utf-8") as file:
        tasks=[line.strip() for line in file.readlines()]
        
        if not tasks:
            print("❌ Henuz Hic Gorev Eklenmemis...")
            return
        for index,task in enumerate(tasks,start=1):
            print(f'{index}.{task}')
        
        while True:
            try:
                selected_task=int(input("\n"))
                if 1 <= selected_task <= len(tasks):
                    if tasks[selected_task - 1].endswith("✅"):
                        print("❌ Bu Gorev Zaten Tamamlanmis...")
                        return
                    tasks[selected_task - 1] += " ✅"
                    break     
                else:
                    print(f"Gecersiz Secim! Lutfen 1 Ile {len(tasks)} Arasinda Bir Numara Girer Misin ? ")
            except ValueError:
                print("⚠️  Gecersiz Giris! Lutfen Sadece Sayi Girer Misin ? ")
    
    with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\Gorevler.txt","w",encoding="utf-8") as file:
        for task in tasks:
            file.write(task+ "\n")

    print(f"{tasks[selected_task-1]}  Gorevi Basariyla Isaretlendi.")       
    
if __name__ == "__main__":
    print("\nGorev Takip Listesi Uygulamasina Hos Geldiniz:","\n","-"*40,sep="")
    print("Ana Menuye Gecmeden Once Isminizi Girer Misiniz: \n")
    
    while True:
        name=input().strip().casefold()
        with open("D:\\STAJ 1\\Python Applications\\Görev Takip Uygulaması\\İsimler.txt","r",encoding="utf-8") as file:
           valid_name=[name.strip().casefold() for name in file.readlines()]
        
        if name in  valid_name:
            name=name.capitalize()
            print(f'📋 Merhaba {name}, Ana Menuye Yonlendiriyorum... \n')
            main_menu(name)
            break       
        else:
            print("❌ Gecersiz Ya Da Nadir Bir Isim Girdiniz: Lutfen Tekrar Deneyiniz: \n")