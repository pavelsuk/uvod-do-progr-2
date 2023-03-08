## Čtení na doma - vícerozměrné struktury

Na rozdíl od tabulek můžeme jít v seznamech do více rozměrů než do dvou. Uvažujme například seznam `vysledky`, který obsahuje jména a výsledky prvních čtyř běžců maratonu. Seznam je vícerozměrný. Na nulté pozici každého z vnořených seznamů je jméno běžce a na první pozici je seznam s časem běžce, který obsahuje počet hodin, minut a sekund, které běžec potřeboval na překonání trati.

```py
vysledky = [
    ["Brunner Radek", [3, 0, 9]], 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]
```

Pojďme si nyní rozkreslit jednotlivé úrovně seznamu. Obrázek v plné velikosti je [zde](assets/Indexování-Page-1.drawio.svg).

::fig[Indexování 1]{src=assets/Indexování-Page-1.drawio.svg size=50}

Můžeme se podívat i na [indexování pomocí záporných indexů](assets/Indexování-Page-2.drawio.svg).

::fig[Indexování 2]{src=assets/Indexování-Page-2.drawio.svg size=50}

Vyberme ze seznamu běžce na nulté pozici a uložme ho do proměnné `vitez`.

```py
vitez = vysledky[0]
```

Tím nám "zmizelo" jedno patro.

::fig[Indexování 3]{src=assets/Indexování-Page-3.drawio.svg size=100}

Nyní do proměnné `cas_viteze` uložíme čas vítěze.

```py
cas_viteze = vysledky[0][1]
```

Tím nám "zmizelo" další patro a dopracovali jsme se k jednorozměrnému seznamu.

::fig[Indexování 4]{src=assets/Indexování-Page-4.drawio.svg size=100}

Nyní použijeme **slicing** a vytáhneme si závodníky, kteří byli "na bedně", tj. tři nejrychlejší běžce. To uděláme následujícím příkazem:

```py
vitezove = vysledky[:3]
```

Tentokrát nám z obrázku "nezmizelo" celé patro. Výběr pomocí rozsahu totiž **zachová dimenzi původního seznamu.** 

::fig[Indexování 5]{src=assets/Indexování-Page-5.drawio.svg size=70}

Obrázek v plné velikosti je [zde](assets/Indexování-Page-5.drawio.svg).

## Cvičení: Vícerozměrné struktury
::exc[excs>zavody]
::exc[excs>zavody-2]
