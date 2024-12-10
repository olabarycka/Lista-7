import math

a = float(input("Podaj pierwszą liczbę (a): "))
b = float(input("Podaj drugą liczbę (b): "))

if a > b:
    print("Pierwsza liczba (a) jest większa.")
elif a < b:
    print("Druga liczba (b) jest większa.")
else:
    print("Obie liczby są równe.")