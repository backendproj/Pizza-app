shaharlar = {
    "Olmaliq": 30,
    "Ohangaron": 50,
    "Piskent": 65,
    "Angren": 90,
    "Toshkent": 110,
}

def deliver(city):
    summa = 5000
    try:
        if shaharlar[city] <= 30:
            print(f"Yetkazib berish narxi: {summa}so'm\nXarid uchun rahmat\n")
            return True
        elif shaharlar[city] <= 40:
            summa += 5000
            print(f"Yetkazib berish narxi: {summa}so'm\nXarid uchun rahmat\n")
            return True
        elif shaharlar[city] <= 60:
            summa += 8000
            print(f"Yetkazib berish narxi: {summa}so'm\nXarid uchun rahmat\n")
            return True
        elif shaharlar[city] <= 100:
            summa += 15000
            print(f"Yetkazib berish narxi: {summa}so'm\nXarid uchun rahmat\n")
            return True
        elif shaharlar[city] <= 150:
            summa += 25000
            print(f"Yetkazib berish narxi: {summa}so'm\nXarid uchun rahmat\n")
            return True
    except KeyError:
        print(f"Xurmatli mijoz biz bunday uzoq masofaga vaqtinchalik yetkazib bera olmaymiz...\nTez oraqada albatta {city} shahriga ham yetkazib berishni yo'lga qo'yamiz!")
        return False
