
#ÖDEV6:
sayilar = "0123456789"
cift_sayilar = ""
tek_sayilar = ""
for sayi in sayilar:
    if int(sayi) % 2 == 0:
        cift_sayilar += sayi
    else:
        tek_sayilar += sayi
print("Çift Sayılar:", cift_sayilar)
print("Tek Sayılar:", tek_sayilar)
