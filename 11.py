#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
#sozlik = {
#
#    "olma": ["anor", "qulupnay", "gilos"],
#    "ananos": ["olcha", "ajdarho", "mango"]
#}
#print(sozlik)
#
#
##2 - masala Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
#davlatlar_poytaxtlar = {
#    "O‘zbekiston": "Toshkent",
#    "AQSh": "Vashington",
#    "Rossiya": "Moskva",
#    "Fransiya": "Parij",
#    "Xitoy": "Pekin",
#    "Yaponiya": "Tokio",
#    "Germaniya": "Berlin"
#}
#
#for kalit , qiymat in davlatlar_poytaxtlar.items() :
#    print(f"{kalit , qiymat}")


# 4 - masala
menu = {
  "palov" : 25000 , 
  "ijjan" : 30000 , 
  "barak" : 15000
}
print("3 ta taom kiriting")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taomni kiritng"))

for buyurtma in buyurtmalar :
    if buyurtma in menu :
        print(f"{buyurtma} {menu{buyurtma}} som")
    else :
        print()