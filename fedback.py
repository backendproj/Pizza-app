def feedback(name, order, location):
    time = input("Buyurtma nechi daqiqada yetib keldi: ")
    status = input("Buyurtma holati qanday edi: ")
    grade = input("Bizga 1 dan 10 gacha baxo bering: ")
    file = open("feedback.txt", "a")
    file.writelines(f"{name} tomonidan berilgan feedback:\n{order} {location}ga yetib borish vaqti: {time} daqiqa\n{order} holati: {status}\nXizmat uchun berilgan baxo: {grade}\n\n")