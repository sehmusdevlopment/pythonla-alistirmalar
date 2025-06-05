

# kullanıcıdan ilk sayıyı al
try:
    sayi1=float(input("ilk sayıyı girini: "))
except ValueError:
    print("geçersiz bir giriş yaptınız")
    exit() # hatalı bir giriş yapıldığı zaman program son bulur

# kulllanıcıdan işlem alma 
islem=input("yapmak istediğiniz işlemi secin(+,-,*,/):")

# kulllanucıdan ikinci sayıyı almak 
try:
    sayi2=float(input("ikinci sayıyı girin: "))
except ValueError:
    print("geçersiz tıklama veya sayı girdiniz :")
    exit()

sonuc=0


# işlemi kontrol et
if islem=='+':
    sonuc=sayi1+sayi2
elif islem=='-':
    sonuc=sayi1-sayi2
elif islem=='*':
    sonuc=sayi1*sayi2
elif islem=='/':
    if sayi2 !=0: # sıfıra bölme hatasını engelle
        sonuc=sayi1/sayi2
    else:
        print("sıfıra bölme hatası!")
        exit()
else:
    print("geçersiz işlem lütfen +,-,*,/ işlemlerinden birini seçin")
    exit()
print("sonuc", sonuc)        


