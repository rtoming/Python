# Ülesanne koosneb kahest osast. Kõik ülesande tegevused peavad olema esitatud ühes käivitatavas Pythoni skriptis:

# Esimene osa:
# Koostada programm, mis küsib kasutajalt: "Sisesta mitu viset täringuga sooritatakse: ",
# Ning sooritab kuuetahulise täringuga vastava arvu viskeid, kuvades iga viske järel ekraanile vastava tulemuse. 
# Näiteks:
# 2
# 3
# 4
# 2

# Teine osa:
# Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu. Leiutaja oli “tagasihoidlik” ja palus tasuks
# esimese ruudu eest 1 nisutera, teise ruudu eest 2 korda rohkem ehk 2, kolmanda ruudu eest veel 2 korda rohkem ehk 4,
# neljanda ruudu eest siis 8, viienda ruudu eest 16 jne. Malelaual on 64 ruutu.
# Koostada programm, mis küsib kasutajalt ühe täisarvu;
# arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu eest leiutaja küsis;
# tulemus väljastatakse ekraanile pärast tsüklit.

# Näide 1:
# Sisesta mitmenda ruudu eest tasu saadakse: 5
# Nisuteri 5. ruudu eest: 16

# Näide 2:
# Sisesta mitmenda ruudu eest tasu saadakse: 25
# Nisuteri 25. ruudu eest: 16777216


# Esimene osa:
import random

visked = int(input("Mitu viset soovid teha? "))

for i in range(visked):
    tulemus = random.randint(1, 6)
    print(tulemus)
print()




# Teine osa:
ruut = int(input("Sisesta ruudu number: "))

i = 1
nisuterad = 1

while i < ruut:
    nisuterad = nisuterad * 2
    i = i + 1

print(nisuterad)
print()

input("Vajuta Enter, et lõpetada...")