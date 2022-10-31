pizza_menu = {
    "🇮🇹Italy": [("Peperoni", 14), ("Mango", 12)],
    "🇺🇸America": [("Margarita", 10), ("Sausage", 8)],
    "🇺🇿Uzbek": [("Qazi", 9), ("4-sezon", 7)]
}

drink_menu = {
    "Cola"  : [("0,5L",5000), ("1.0L",8000),("1,5L",12000)],
    "Fanta" : [("0,5L",5000), ("1.0L",8000),("1,5L",12000)],
    "Pepsi" :[("0,5L",5000), ("1.0L",8000),("1,5L",12000)],
    "Choy"  :[("Limo'n Choy", 5000),("Qora Choy",3000),("Ko'k Choy",3000)],
    "Coffee" : [("3 в 1", 5000),("Cappuccino",6000)],
    "Sok"   : [("Mevali Sharbat",11000)]
}

def print_pizza():
    for davlat, tur in pizza_menu.items():
        print(f"{davlat}:")
        for ind, pizza in enumerate(tur):
            print(f"     {pizza[0]}: ${pizza[1]}")


def print_drinks():
    for drinks, sizes in drink_menu.items():
        print(f"{drinks}:")
        for ind, size in enumerate(sizes):
            print(f"     {size[0]}: ${size[1]}")