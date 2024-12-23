#ÖDEV3:

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
if sayi2 != 0:
    bolme = sayi1 / sayi2
else:
    bolme = "Bölme işlemi için sıfırdan farklı bir sayı giriniz"
print("Toplama:", toplama)
print("Çıkarma:", cikarma)
print("Çarpma:", carpma)
print("Bölme:", bolme)
print(toplama, cikarma, carpma, bolme)