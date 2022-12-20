## Moduly

Doposud jsme v našich programech měli k dispozici pouze několik základních funkcí. Zatím jsme viděli tyto

`abs`, `round`, `len`, `sum`, `min`, `max`, `sorted`, `int`,
`float`, `str`, `print`.

Později si ukážeme, že jich ještě několik přibude, ale o moc víc jich už k dispozici není. S takto omezeným množstvím funkcí bychom si dlouho nevystačili. Python naštěstí nabízí mnoho takzvaných _modulů_ , které obsahují spousty dalších užitečných funkcí.

Moduly jsou v podstatě balíčky funkcí zaměřených na nějaké konkrétní téma, například statistika, zpracování textu, práce se soubory na disku apod. Pokud chceme používat funkce z nějakého modulu, musíme jej nejdřív takzvaně _importovat_.

Prvním velmi užitečným balíčkem funkcí je modul `math`. Importujeme jej příkazem

```pycon
import math
```

který napíšeme na začátek našeho programu. Pokud pracujeme v Python konzoli, napíšeme tento příkaz prostě na konzoli a dokud ji nezavřeme, můžeme modul používat.

Kromě mnoha jiných obsahuje modul `math` funkce `ceil()` a `floor()`, které zaokrouhlují buď vždy jen dolů nebo jen nahoru. Abychom je mohli zavolat, musíme použít tečkovou notaci.

```pycon
>>> math.ceil(3.1)
4
>>> math.floor(3.7)
3
```

Mnozí z vás už si stěžovali, že Python neobsahuje funkci, která počítá průměr. Nyní takovou funkci můžeme získat, pokud importujeme modul `statistics`. Tento modul obsahuje mimo jiné funkci `mean()`, která počítá vytoužený průměr.

```pycon
>>> import statistics
>>> statistics.mean([1, 2, 3, 4, 5, 6])
3.5
```

### Pozor na názvy skriptů!

**Pozor!** Nikdy nepojmenovávejte svůj skript stejně jako modul, který používáte. Pokud byste pojmenovali svůj skript `math.py`, uvnitř napsali `import math` a používali nějakou funkci z tohoto modulu, Python ji bohužel nenajde. V tu chvíli totiž místo "pravého" modulu `math` naimportoval skript `math.py` ve vašem pracovním adresáři a v něm jistě volanou funkci nemáte definovanou.

Pokud se vám to náhodou stalo a Python vám vypsal něco jako:

```
AttributeError: partially initialized module 'math' has no attribute 'ceil' (most likely due to a circular import)
```

Víte už, čím to je. Přejmenujte váš skript na jiný název a pokud se vám v pracovním adresáři vytvořil adresář `__pycache__`, tak jej také smažte.

## Cvičení: Moduly
::exc[excs>zaokrouhlovani]

## Bonusy
::exc[excs>klasicke-zaokrouhlovani]
