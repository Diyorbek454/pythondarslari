# 1. Oila a'zolari haqida lug'at
otam = {
    "ism": "Karimboy",
    "tugilgan_yil": 1982,
    "shahar": "Xorozm"
}

onam = {
    "ism": "Zulhmor",
    "tugilgan_yil": 1982,
    "shahar": "Xorazm"
}

akam = {
    "ism": "Doniyor",
    "tugilgan_yil": 2007,
    "shahar": "Toshkent"
}

# Konsolga chiqarish
print(f"Otamning ismi {otam['ism']}, {otam['tugilgan_yil']}-yilda, {otam['shahar']}da tug'ilgan")
print(f"Onamning ismi {onam['ism']}, {onam['tugilgan_yil']}-yilda, {onam['shahar']}da tug'ilgan")
print(f"Akamning ismi {akam['ism']}, {akam['tugilgan_yil']}-yilda, {akam['shahar']}da tug'ilgan\n")

# 2. Sevimli taomlar lug'ati
sevimli_taomlar = {
    "Ali": "osh",
    "Vali": "manti",
    "Zarina": "shashlik",
    "Olim": "lag'mon",
    "Nilufar": "somsa"
}

# Kamida uch kishining sevimli taomini chiqarish
print(f"Alining sevimli taomi {sevimli_taomlar['Ali']}")
print(f"Valining sevimli taomi {sevimli_taomlar['Vali']}")
print(f"Zarinaning sevimli taomi {sevimli_taomlar['Zarina']}\n")

# 3. Python izohli lug'at
python_lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn qatori",
    "if": "Shart operatori",
    "else": "Aks holda",
    "for": "Takrorlash sikli",
    "while": "Shartli sikl",
    "list": "Ro'yxat",
    "dict": "Lug'at",
    "function": "Funktsiya"
}

# Foydalanuvchidan so'z so'rash
soz = input("Tarjimasini bilmoqchi bo'lgan Python so'zingizni kiriting: ")

# If-else orqali lug'atni tekshirish va natijani chiqarish
if soz in python_lugat:
    print(f"{soz} so'zining tarjimasi: {python_lugat[soz]}")
else:
    print("Bunda so'z mavjud emas")
