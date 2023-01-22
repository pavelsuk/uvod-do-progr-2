## Cyklus `while`
Aby byl tento text co nejkompletnější, je třeba zmínit i cyklus `while` a příkaz `continue`. Nejdříve si pro zopakování probereme, že cyklus `for` slouží k procházení složených datových typů. Při procházení seznamů získáváme přístup ke každému prvku seznamu. Při procházení řetězců se jedná o každý znak. Cyklus `for` využíváme i při procházení slovníků a pro velmi mnoho dalších případů (např. procházení otevřených souborů po řádcích).

Naproti tomu, cyklus `while` je obecný cyklus a svou konstrukcí má blíže k podmínce `if`. U podmínky `if` platí, že odsazený blok po podmínce `if` se provede, pokud se samotná podmínka, tj. výraz mezi `if` a dvojtečkou vyhodnotí jako `True`.

U cyklu `while` platí, že se jeho blok kódu provádí **opakovaně dokud** jeho podmínka platí. U následujícího příkladu je uživatel tázán na heslo stále dokola dokud heslo 123456 nezadá správně.

```py
spravne_heslo = "123456"
zadane_heslo = input("Zadej heslo: ")

while zadane_heslo != spravne_heslo:
    zadane_heslo = input("Zadej heslo: ")

print("Heslo zadano")
```

Pokud používáme cyklus `while` je třeba mít na paměti, že v těle cyklu musí existovat šance na to, že se podmínka cyklu změní a cyklus se tím ukončí. Při programování se však velmi často stane, že uděláme chybu, která neumožní ukončení cyklu a nám vznikne _nekonečný cyklus_. Naštěstí existuje klávesová zkratka Ctrl+C, která v terminálu program vykonávaný Python interpretem nemilosrdně ukončí i uprostřed nekonečného cyklu.

O pojmu _nekonečný cyklus_ si povíme něco více. Protože již z předchozí části známe příkaz `break`, který nám ukončí cyklus (to platí i pro cyklus `while`), můžeme si dovolit vytvořit nekonečný cyklus záměrně. Předchozí příklad je možné přepsat do následující podoby a například obohatit o výpis o nevyhovujícím heslu.

```py
spravne_heslo = "123456"

while True:
    if input("Zadej heslo: ") == spravne_heslo:
        break
    print("Špatné heslo")

print("Heslo zadano")
```

Podmínka cyklu `while` se bude vyhodnocovat vždy jako pravdivá (jedná se o hodnotu _True_) a pouze na nás je, abychom ve vhodném místě cyklus `while` ukončili pomocí příkazu `break`.

## Cvičení: Cyklus while
::exc[excs>hadani]

### Příkaz `continue`
Příkaz `continue` je podobný příkazu `break`, ale s tím rozdílem, že neukončí celý cyklus, ale pouze přeskočí zbytek těla cyklu a pokračuje další iterací. Pokud je použit v cyklu `for`, řídící proměnná cyklu `for` nabude nové hodnoty (tzn. zpracuje se další prvek seznamu nebo další číslo z rozsahu `range()`). U cyklu `while` dojde opět k vyhodnocování jeho podmínky.

Následující příkaz vytiskne pouze ta čísla z číselné řady, která jsou dělitelná 10. Zbytek přeskočí pomocí příkazu `continue`.

```py
stop = int(input("Zadej konec: "))

for i in range(stop):
    if i % 10 != 0:
        continue

    print(i)
```

Příkazy `break` a `continue` je možné v rámci jednoho cyklu zkombinovat, např.

```py
soucet = 0

while True:
    vstup = input("Zadej číslo: ")

    if not vstup:
        break

    if not vstup.isdigit():
        print("Nezadal jsi číslo")
        continue

    print(f"Zadáno číslo {vstup}")
    soucet += int(vstup)

print(f"Součet je {soucet}")
```

Nekonečný cyklus se ukončí příkazem `break` pokud `vstup` neobsahuje žádné znaky (jedná se o prázdný řetězec). Pokud by dále řetězec `vstup` nebyl složen pouze z cifer, zadaná hodnota se přeskočí.


### Část `else` u cyklů
Může se vám stát, že při čtení cizího kódu narazíte na `else`, před kterým se ale nenachází žádný blok `if`. Klíčové slovo `else` totiž může být použito ve více různých konstrukcích a jednou z nich je použití u cyklů. Jedná se o specifikum Pythonu, které obecně není moc běžné. Větev `else` patřící k cyklu `for` nebo k cyklu `while` se vykoná pokud cyklus **nebyl** ukončen příkazem `break`. Toto není příliš intuitivní je potřeba si to zapamatovat. Je to ovšem pokročilá věc, kterou vás nikdo nenutí používat je zde zmíněna pouze pro kompletnost.
