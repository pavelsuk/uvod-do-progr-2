## Cyklus pomocí číselné řady

V první kapitole jsme si vyzkoušeli (nebo spíše zopakovali) cyklus spuštěný nad námi vytvořeným seznamem. Použití cyklů je ale širší. Například si můžeme číselně zvolit, kolikrát by se nějaký cyklus měl opakovat. K tomu využijeme funkci `range`. Tato funkce vytvoří posloupnost (`sequence`) čísel a cyklus je spuštěn pro každý prvek této posloupnosti. 

Funkci `range` můžeme zadat parametry `start` (začátek posloupnosti) a `stop` (konec posloupnosti, tato hodnota již v posloupnosti není !). Můžeme však zadat pouze parametr `stop` a pak jako `start` použita 0.

Samotný zápis cyklu se téměř neliší, používáme klíčová slova `for`, `in` a dvojtečku. Mezi `for` a `in` vkládáme název proměnné, která se stane dočasným nositelem čísla, se kterým cyklus právě pracuje. Pro tuto dočasnou číselnou proměnnou se v programování velice často používá jednoduchý název `i`.

Zkusíme si nejprve vypsat všechna čísla od 0 do nějaké hodnoty.

```py
stop = int(input("Zadej konec: "))
for i in range(stop):
  print(i)
```

Takto například vypadá průběh programu:

```
Zadej nejvyšší číslo: 5
0
1
2
3
4
```

Všimni si, že zadáme-li jako vstup `5`, výpis končí číslem `4`, hodnota zadaná jako `end` tam již skutečně není.

Zkusme nyní využít i parametr `start`. Zkusíme si třeba vypsat čísla nikoli od 0, ale od nějaké konkrétní hodnoty.

```py
start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))
for i in range(start, stop):
  print(i)
```

Opět platí, že dovnitř cyklu můžeme vložit podmínku. Zkusme si například vypsat pouze ta čísla z daného rozsahu, která jsou dělitelná třemi.

```py
start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))
for i in range(start, stop):
  if i % 3 == 0:
    print(i)
```

Pevný počet opakování ale zdaleka nevyužíváme jen v kombinaci s čísly. Vraťme se třeba k našemu příkladu na seznam hostů z opakovací lekce. Seznam hostů nemusíme zapisovat přímo do programu, ale můžeme požádat uživatele, aby nám jména hostů postupně zadával. Jména pak připojujeme k seznamu stávajícímu hostů pomocí funkce `append`.

```py
numberOfGuests = int(input("Zadej počet hostů: "))
guestList = []
for i in range(numberOfGuests):
  newGuest = input("Zadej jméno hosta: ")
  guestList.append(newGuest)
print(guestList)
```

#### Tip

Všimněte si, že prázdný seznam jsme vytvořili jednoduše pomocí prázdných hranatých závorek `[]`.
