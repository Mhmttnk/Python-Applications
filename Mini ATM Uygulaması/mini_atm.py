print("Mini ATM Uygulamasına Hos Geldiniz: Yapmak Istediginiz Islemi Seciniz Ya Da Q Ile Cikis Yapabilirsiniz\n")

def entry():
    while True:
        start=(input("1-Bakiye Goruntuleme\n2-Para Yatirma\n3-Para Cekme "))
        
        if start.lower()=="q":
            print("\nProgramdan Cikis Yapiliyor")
            break
        elif start in ["1","2","3"]:
            get_operation(start)
        else:
            print("Yanlis Giris! Lutfen 1 veya 2 veya 3 Giriniz\n")
        
def get_operation(value):
    if value=="1": 
        view_balance()
    elif value == "2":
        investment()
    elif value== "3":
        withdrawal()

totalbalance=10000.0
amount=0.0
def view_balance(ıs_uptade=False): # Bakiye Goruntuleme
    if ıs_uptade:
        print("Guncel Hesap Bakiyeniz:",totalbalance,"TL\n\nYeni Islem Yapabilirsiniz Ya Da Q Ile Cıkıs Yapabilirsiniz")
    else:
        print("Hesap Bakiyeniz:",totalbalance,"TL\n\nYeni Islem Yapabilirsiniz Ya Da Q Ile Cıkıs Yapabilirsiniz")
def investment(): # Para Yatirma
    global totalbalance
    global amount
    
    print("\nLutfen Yatirmak Istediginiz Miktari Giriniz:")
    while True:
        try:
            amount=float(input())
            if (amount >= 0):
                totalbalance += amount
                view_balance(True)
                break    
            else:
                print("Yatirilmak Istenen Miktar Negatif Olamaz! Lutfen Tekrar Deneyiniz") 
        except ValueError:
            print("Yanlis Giris! Lutfen Tekrar Deneyiniz")

def  withdrawal(): # Para Cekme               
    global totalbalance
    global amount

    print("\nLutfen Cekmek Istediginiz Miktari Giriniz: ")
    while True:
        try:
            amount=float(input())
            if(amount>=0 and amount<=totalbalance):
                totalbalance -= amount   
                view_balance(True)
                break
            elif (amount > totalbalance):
                print("Yetersiz Bakiye! Lutfen Tekrar Deneyiniz")
            else:
                print("Cekilmek Istenen Miktar Negatif Olamaz! Lutfen Tekrar Deneyin")
        except ValueError:
            print("Yanlis Giris! Lutfen Tekrar Deneyiniz")   

if __name__ == "__main__":
    entry()

