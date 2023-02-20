## Skvělí velitelé

Nyní je naším úkolem vytvořit seznam velitelů, kteří zvítězili v boji proti přesile. Budeme k tomu potřebovat sloupečky s výsledkem bitvy, informacemi o síle útočníků a obránců a se jmény velitelů. Pro tyto sloupečky si opět vytvoříme konstanty.

```py
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

SL_VYSLEDEK = 13
SL_SILA_UTOCNICI = 17
SL_SILA_OBRANCI = 18
SL_VELITEL_UTOCNICI = 19
SL_VELITEL_OBRANCI = 20
```

Opět budeme procházet soubor řádek po řádku. Připravíme si nejprve podmínku, že je zadána síla útočníků i obránců, tj. že v daných sloupcích nejsou prázdné řetězce. Použijeme operátor `and`, který vyhodnotí celou podmínku jako pravda, pokud jsou pravda oba výrazy v podmínce.

```py
velitele = []
for radek in radky[1:]:
    radek = radek.split("\t")
    if radek[SL_SILA_UTOCNICI] != "" and radek[SL_SILA_OBRANCI] != "":
```

Dále si položme otázku: Kdy je vlastně bitva vyhraná? Pro naše data jde o následující dvě situace:

- síla útočníků je větší než síla obránců a útočníci prohráli,
- síla útočníků je menší než síla obránců a útočníci vyhráli.

První podmínku můžeme zapsat jako

```py
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
```

V řadě bitev dále platí, že armádu vedlo více velitelů. Velitelé jsou oddělení čárkami. Abychom z řetězce vytvořili seznam, kde bude každý velitel jako samostatná položka, použijeme metodu `.split()`.

```py
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
```

Jako poslední krok je potřeba nově nalezené šťastlivce přidat do seznamu `velitele`. Nyní máme dva jednorozměrné seznamy, které chceme propojit. Nepoužijeme tedy metodu `.append()`, protože ta by vytvořila dvourozměrný seznam. Můžeme použít operátor `+`, tj. stejný operátor, jaký používáme při sčítání, který jednoduše spojí oba seznamy dohromady.

```py
            velitele = velitele + radek_velitele
```

Zápis podmínek pro oba případy tedy můžete vypadat například takto:

```py
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
            velitele = velitele + radek_velitele
        elif float(radek[SL_SILA_UTOCNICI]) < float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "won":
            radek_velitele = radek[SL_VELITEL_UTOCNICI].split(", ")
            velitele = velitele + radek_velitele
```

Nakonec zkontrolujeme výsledek. Ti, kteří četli knihy či viděli seriál, mohou zavzpomínat, které ze jmen postav jsou jim povědomé.

```py
print(velitele)
```
