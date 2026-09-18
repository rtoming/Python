# Ülesanne koosneb kahest osast. Kõik ülesande tegevused peavad olema esitatud ühes käivitatavas Pythoni skriptis:

# Esimene osa:
# Puhas vesi hakkab keema temperatuuril 100 oC. Samas ei tõuse vee temperatuur normaalrõhul ka üle 100 kraadi. 
# Kogu saadud energia kulub vee aurustumisele.

# Koostada programm, mis küsib vee temperatuuri täisarvudes ning väljastab vastuse:
# 1. Vee temperatuur on (sisestatud väärtus) kraadi, vesi veel ei kee.
# 2. Vee temperatuur on (sisestatud väärtus) kraadi, vesi keeb.
# 3. Vee temperatuur ei saa olla üle 100 oC.
# 4. Vesi on jääs.

# Teine osa:
# Teadupärast on kosmosejaamas ruum piiratud. Ent ometigi tehakse ka rahvusvahelisse kosmosejaama aeg-ajalt turismireise. Ütleme, et inimesed, keda lubatakse rahvusvahelisse kosmosejaama peavad olema kasvult maksimaalselt 190 cm (kaasa arvatud) pikad. Et eristada turiste töötajatest on töötajatel kaelakaart ja turistidel pilet.
# Koostada programm, mis küsib reisija pikkust sentimeetrites. Seejärel küsib kas reisijal on pilet (jah, ei) seejärel küsib kas reisijal on kaelakaart (jah, ei).
# Saanud reisijalt vastuse, et ta on alla 190 cm ja omab kas kaelakaarti või piletit, ilmub ekraanile kiri, et reisija pääseb kosmoselennule.
# Kui aga reisija on pikem kui 190 cm või ei oma kaelakaarti ega piletit, ilmub kiri, et reisija ei pääse kosmoselennule.
# Pange tähele, et vastus (jah või ei)võib olla kirjutatud ka suurte tähtedega.

veetemperatuur = int(input("Sisesta vee temperatuur: "))
if veetemperatuur < 0:
    print("Vesi on jääs!")
elif veetemperatuur < 100:
    print("Vesi veel ei kee")
elif veetemperatuur == 100:
    print("Vesi keeb")    
elif veetemperatuur > 100:
    print("Vesi muudab olekut, see aurustub!")