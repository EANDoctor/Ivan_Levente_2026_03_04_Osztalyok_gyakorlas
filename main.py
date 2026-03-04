from car import Auto
import random as r

auto1 = Auto("Toyota", "Corolla", (2015))
auto2 = Auto("Ford", "Focus", (2018))
auto3 = Auto("Audi", "E-Tron 61", (2020))
auto4 = Auto("Ford", "Mustang", (2008))

# print(auto1)
# print(auto2)

# auto1.gyorsit(150)
# print(auto1)
# auto1.gyorsit(150)
# print(auto1)
# auto1.fekez(150)
# print(auto1)
# auto1.fekez(150)
# print(auto1)

autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)

print("\nGyorsít\n")

for auto in autok:
    auto.gyorsit(r.randint(30, 150))
    print(auto)

# Össz autók átlag életkor számíítása
gyartasi_evek = [auto.gyartasi_ev for auto in autok]
atlag_eletkor = (2026 * len(autok) - sum(gyartasi_evek)) / len(gyartasi_evek)
print(f"\nAz autók átlag életkora: {atlag_eletkor}")