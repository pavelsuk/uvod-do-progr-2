## Využití modulu CSV

Modul `pandas` ale není jedinou možností, jak v Pythonu zpracovat soubory ve formátu CSV (nebo TSV). Přímo součástí Pythonu je i modul `csv`, který nám práci se soubory může trochu zjednodušit. Modul má svoji vlastní [oficiální dokumentaci](https://docs.python.org/3/library/csv.html).

Modul `csv` umožňuje výběr způsobu čtení. Lze využít `reader`, který data načte do sekvence, nebo `DictReader`, který každý řádek načte do slovníku. Použitím `DictReader` odpadne nutnost zjišťovat čísla sloupců, kde se nacházejí požadovaná data, nyní nám stačí znát jen jejich názvy. Ty si uložíme do konstanty `SLOUPCE`. Začneme otevřením souboru a načtení dat pomocí `DictReader`.

```py
import csv

SLOUPCE = ("attacker_1", "attacker_2", "attacker_3", "attacker_4")
utocnici = {}

with open('battles.tsv') as soubor:
    data = csv.DictReader(soubor, delimiter="\t")
```

Dále využijeme cyklus a budeme číst data řádek po řádku. V proměnné `radek` nyní máme slovník, nikoli seznam. Dále opět můžeme využít vnořený cyklus a projít všechny položky ve slovníku. Protože budeme potřebovat klíče i hodnoty, využijeme metodu `.items()`. Uvnitř cyklu zkontrolujeme, že klíč je v n-tici sloupců, která nás zajímá. Dále zkontrolujeme, že hodnota není prázdný řetězec. Protože pro uložení hodnoty musí být splněné obě podmínky, můžeme využít operátor `and`. Celá podmínka je vyhodnocena jako pravda, pokud jsou obě podmínky ve výrazu vyhodnoceny jako pravda. Alternativně bychom mohli využít i vnořenou podmínku. Dále už stačí využít metodu `.get()`

```py
    for radek in data:
        for klic, hodnota in radek.items():
            if klic in SLOUPCE and hodnota != "":
                utocnici[hodnota] = utocnici.get(hodnota, 0) + 1
print(utocnici)
```
