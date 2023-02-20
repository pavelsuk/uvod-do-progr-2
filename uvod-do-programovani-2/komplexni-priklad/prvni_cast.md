## Útočící rody

Nejprve je potřeba načíst soubor. K tomu můžeme využít metodu `readlines()`.

```py
# Otevřeme soubor
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()
```

Útočící rody je potřeba si poznamenávat do vhodné struktury. Abychom si mohli snadno evidovat i to, kolikrát daný rod útočil, můžeme využít slovník. Klíčem ve slovníku bude jméno útočícího rodu a hodnotou počet bitev, ve kterém rod útočil. Na začátku bude slovník prázdný a vytvoříme ho pomocí prázdných složených závorek.

```py
utocnici = {}
```

Soubor projdeme řádek po řádku pomocí cyklu. Každý řádek je jedním prvkem v seznamu `radky`. Zatím je celý řádek uložený v jednom řetězci. Abychom řetězec rozdělili na jednotlivé sloupce, využijeme metodu `split()`. Protože se jedná o soubor ve formátu `.tsv`, jako oddělovač zde slouží tabulátor. Tím nám vznikne seznam `radek`.

```py
for radek in radky[1:]:
    radek = radek.split("\t")
```

V bitvě může útočit více rodů, uvažujeme maximálně čtyři. První sloupec s útočícím rodem je `UTOCNIK_1`. My ale máme data uložená v seznamu, proto potřebujeme vědět pozici, na které se informace nachází. V souboru zjistíme, že sloupec `UTOCNIK_1` se nachází na pozici 5 (při číslování od 0). Číslo můžeme do souboru napsat rovnou nebo vytvořit konstantu, což je vlastně proměnná, jejíž hodnotu nastavíme pouze jednou a už ji neupravujeme. Konstanty obvykle zapisujeme velkými písmeny, abychom je odlišili od běžných proměnných. Konstanty pro přehlednost vkládáme pod importy.

```py
SL_UTOCNIK_1 = 5
```

Podobně můžeme přidat i konstanty pro další sloupce.

```py
SL_UTOCNIK_2 = 6
SL_UTOCNIK_3 = 7
SL_UTOCNIK_4 = 8
```

Po přípravě konstant se můžeme pustit do vnitřní části cyklu. Načteme jméno prvního útočícího rodu. Poté provedeme kontrolu, zda již rod máme ve slovníku `utocnici`. Pokud ano, přidáme mu k dobru další útok. Pokud ne, nastavíme mu počet útoků na 1.

```py
    utocnik = radek[SL_UTOCNIK_1]
    if utocnik in utocnici:
        utocnici[utocnik] = utocnici[utocnik] + 1
    else:
        utocnici[utocnik] = 1
```

Podobně budeme pokračovat u všech dalších sloupců. Pouze bychom měli zkontrolovat, zda hodnota v daném sloupci není prázdný řetězec. V řadě bitev totiž útočilo méně rodů než čtyři a některé sloupečky jsou pak prázdné, tj. jsou v nich prázdné řetězce.

Pro sloupec `UTOCNIK_2` bude zpracování vypadat takto.

```py
    utocnik = radek[SL_UTOCNIK_2]
    if utocnik != "":
        utocnik = radek[7]
        if utocnik in utocnici:
            utocnici[utocnik] = utocnici[utocnik] + 1
        else:
            utocnici[utocnik] = 1
```

Abychom zpracovali třetí a čtvrtý sloupec, můžeme kód zkopírovat a poté upravit první řádek, ostatní mohou zůstat stejné. Protože i v rámci jednoho řádku opakujeme činnost, můžeme opět využít cyklus, konkrétně tedy vnořený cyklus, protože půjde o cyklus uvnitř cyklu. Vysvětlíme tedy našemu programu, co udělat s jedním sloupečkem, a poté jej necháme danou činnost opakovat.

Budou nám nyní stačit dvě konstanty. První označí první sloupec ke zpracování a druhá konstanta poslední sloupec.

```py
SL_UTOCNIK_PRVNI = 5
SL_UTOCNIK_POSLEDNI = 8
```

Pro získání všech útočníků v jedné bitvě pak použijeme slicing. Pozor na to, že číslo za dvoutečkou musíme zvýšit o 1, protože číslo za dvoutečkou je první, které se nachází mimo vybranou část seznamu.

```py
radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]
```

Výsledný cyklus tedy můžeme vypadat takto.

```py
for radek in radky[1:]:
    radek = radek.split("\t")
    for utocnik in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        if utocnik != "":
            if utocnik in utocnici:
                utocnici[utocnik] = utocnici[utocnik] + 1
            else:
                utocnici[utocnik] = 1
```

### Využití metody get

Zkusme náš kód ještě trochu zjednodušit. V programu používáme podmínku ke kontrole, zda je nějaký klíč v cyklu. Pokud bychom totiž chtěli pomocí hranatých závorek přečíst neznámý klíč, program skončí chybou. Existuje ale i "bezpečný" způsob, jak přečíst hodnotu ze slovníku, a to je metoda `get()`. Metodě totiž můžeme nastavit hodnotu, kterou vrátí, pokud nějaký klíč ve slovníku není. Pro nás by byla ideální 0.

```py
for radek in radky[1:]:
    radek = radek.split("\t")
    for utocnik in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        if utocnik != "":
            utocnici[utocnik] = utocnici.get(utocnik, 0) + 1
```

Tím se náš program opět o něco zkrátil.

```py
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

SL_UTOCNIK_PRVNI = 5
SL_UTOCNIK_POSLEDNI = 8

utocnici = {}
for radek in radky[1:]:
    radek = radek.split("\t")
    for utocnik in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        if utocnik != "":
            utocnici[utocnik] = utocnici.get(utocnik, 0) + 1
print(utocnici)
```
