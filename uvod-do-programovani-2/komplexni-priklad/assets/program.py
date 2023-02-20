with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

SL_VYSLEDEK = 13
SL_SILA_UTOCNICI = 17
SL_SILA_OBRANCI = 18
SL_VELITEL_UTOCNICI = 19
SL_VELITEL_OBRANCI = 20

velitele = []
for radek in radky[1:]:
    radek = radek.split("\t")
    if radek[SL_SILA_UTOCNICI] != "" and radek[SL_SILA_OBRANCI] != "":
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
            velitele = velitele + radek_velitele
        elif float(radek[SL_SILA_UTOCNICI]) < float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "won":
            radek_velitele = radek[SL_VELITEL_UTOCNICI].split(", ")
            velitele = velitele + radek_velitele
print(velitele)
