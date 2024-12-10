pkt = float(input("Podaj liczbę punktów: "))
forma_oceny = input("W jakiej formie chcesz otrzymać ocenę? (liczbowo/słownie/oba): ").strip().lower()

def ocena_liczbowo(pkt):
    if pkt < 50:
        return 2.0
    elif pkt < 60:
        return 3.0
    elif pkt < 70:
        return 3.5
    elif pkt < 80:
        return 4.0
    elif pkt < 90:
        return 4.5
    elif pkt < 100:
        return 5.0
    else:
        return 5.5

def ocena_slownie(pkt):
    if pkt < 50:
        return "niedostateczny"
    elif pkt < 60:
        return "dostateczny"
    elif pkt < 70:
        return "dostateczny plus"
    elif pkt < 80:
        return "dobry"
    elif pkt < 90:
        return "dobry plus"
    elif pkt < 100:
        return "bardzo dobry"
    else:
        return "bardzo dobry plus"

if forma_oceny == "liczbowo":
    print(f"Twoja ocena to {ocena_liczbowo(pkt)}")
elif forma_oceny == "słownie":
    print(f"Twoja ocena to {ocena_slownie(pkt)}")
elif forma_oceny == "oba":
    print(f"Twoja ocena to {ocena_liczbowo(pkt)} - {ocena_slownie(pkt)}")
else:
    print("Nieprawidłowa forma oceny. Wybiesz: liczbowo/słownie/oba.")