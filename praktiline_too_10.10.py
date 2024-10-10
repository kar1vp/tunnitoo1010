"""Matemaatilised tehted"""


# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
import math

a = float(input("Sisesta kolmnurga kaatet A: "))
b = float(input("Sisesta kolmnurga kaatet B: "))

c = round(math.sqrt(a**2 + b**2), 2)

perimeter = round(a + b + c, 2)
area = round((a * b) / 2, 2)

print(f"Hüpoteenus C: {c}")
print(f"Kolmnurga ümbermõõt: {perimeter}")
print(f"Kolmnurga pindala: {area}")