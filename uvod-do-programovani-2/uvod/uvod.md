## Úvod, proměnné a hodnoty

Během kurzu Úvod do programování 2 - Python se ponoříme o něco hlouběji do tajů programování a podíváme se, jaké další možnosti nabízí jazyk Python. Na začátku bychom si ale měli zopakovat věci, které jsme již probírali na kurzu Úvod do programování 1, případně je známe odjinud. Před kurzem si prosím nainstaluj Python a Visual Studio Code na svůj počítač. Návod najdeš [zde](https://kodim.cz/programovani/uvod-do-progr-1/priprava/jazyky-nastroje/instalace-python).

Na této stránce najdeš několik příkladů. Nejlepší způsob, jak si svoje znalosti procvičit, je zkopírovat si kódy příkladů do Visual Studia Code nebo jiného editoru a zkusit si, co dělají.

## Proměnné

Proměnné jsou způsob, jak v našem programu uložit nějaké hodnoty. Jak jejich název napovídá, hodnotu uloženou v proměnné můžeme kdykoli změnit. Proměnné můžeme použít například jako vstup pro nějaké výpočty, předat je funkci ke zpracování nebo vypsat uživateli.

Do proměnných jsme ukládali například vstupy od uživatelů nebo výsledky našich výpočtů. Hodnoty proměnných jsme též často vypisovali na obrazovku.

## Datové typy

Každá proměnná má nějaký datový typ. Datových typů jsme poznali celkem pět.

| Datový typ | Označení v Pythonu | Příklad hodnoty |
|------------|--------------------|-----------------|
| celé číslo |  `int` | `10`, `- 100` |
| desetinné číslo | `float`  | `5.0`, `-8.6`, `130.4582`
| řetězec | `str` | `"Kolik třešní, tolik višní"`
| pravdivostní hodnota | `bool` | `True`, `False`
| seznam | `list` | `[1, True, "Test", 3.3]`, `[1, 4, 8, 13]`

S různými datovými typy můžeme provádět různé operace. Například můžeme sečíst dvě celá čísla (výsledkem je běžný součet) nebo dva řetězce (výsledkem je spojení obou řetězců dohromady). 

Některé operace naopak dělat nemůžeme - například není možné sečíst číslo a řetězec. Naštěstí můžeme změnit datový typ proměnné pomocí funkcí `str()`, `int()` a `float()`. Ty jsou pojmenované vždy podle **cílového** datového typu.

#### Na co si dát pozor

Často zapomínáme, že funkce `input()` nám vrací vždy řetězec, bez ohledu na to, jestli uživatel zadal text nebo číslo. Vyzkoušejte si následující příklad:

```py
number_of_tickets = input("Kolik si přejete lístků? ")
price_per_ticket = 345
total_price = number_of_tickets * price_per_ticket
print(total_price)
```

Python bere náš vstup jako řetězec a pokud jej násobíme číslem, udělá standardní operaci při násobení čísla a řetězce - 345krát zopakuje daný text. Následující program už bude fungovat tak, jak čekáme:

```py
number_of_tickets = input("Kolik si přejete lístků? ")
price_per_ticket = 345
# Změníme typ proměnné number_of_tickets z řetězce na číslo
number_of_tickets = int(number_of_tickets)
total_price = number_of_tickets * price_per_ticket
print(total_price)
```

**Námět:** Zkus spojit funkce `input` a `int` do jedné, tj. napiš obě funkce do jednoho řádku. Tím program zkrátíš a zpřehledníš.

#### Tip

Pokud má náš program dát uživateli nějaký výstup, často v něm musíme kombinovat čísla a texty, spojovat je a převádět. Uvažujme například jednoduchou větu: "Cena 2 lístků na hru Každý má svou pravdu je celkem 690 Kč." V ní máme jako proměnné název hry, počet lístků a cenu. V Pythonu máme možnost využívání _formátovaných řetězců_ neboli f-stringů. Před uvozovky vložíme písmeno `f`. Poté můžeme vkládat do složených závorek přímo názvy proměnných, nemusíme tedy používat znaménka `+` a neprovádíme změny typů proměnných (to si Python zařídí sám).

```py
play = "Každý má svou pravdu"
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 345
total_price = price_per_ticket * number_of_tickets

print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")
```

## Cvičení
::exc[excs/zvetseni-promenne]
::exc[excs/zvetseni-promenne-2]

## Bonus
::exc[excs/fahrnheit-vs-celsius]
