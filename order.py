from feedback import *
from nomlar import *
from delivery import *
from logo import *
from random import randrange


def order():
    # Ma'lumotlar olish bo'limi 
    name = input("Ismingiz: ")
    location = input("Manzil: ")
    if deliver(location) == True:
        pass
    else:
        return 
    phone = input("Telefon raqamingiz: ")
    print("Menu bilan tanishtiriaman:")
    print_pizza()
    pizza = input("Pitsa nomini kiriting: ")
    print_drinks()
    drink = input("Ichimlik nomini kiriting: ")
    deliver(location)
    feedback(name, pizza, location)

    # Ma'lumotlarni faylga joylashtirish bo'limi
    file = open("order.txt", "a")
    file.writelines(f"\nIsm: {name}\nManzil: {location}\nTelefon raqami: {phone}\nBuyurtma: {pizza}\nIchimlik: {drink}\n\n")
    file.close()


print(logo_list[randrange(0, 2)])
print("Xush kelibsiz Xurmatli mijoz 😊\n")