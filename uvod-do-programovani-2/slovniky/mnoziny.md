## Množiny

Datový typ <term cs="množina" en="set"> umožňuje uložit více prvků do jedné struktury, kde je každý prvek uložen pouze jednou. Do seznamu přidáváme prvky metodou `append()`. U množin k tomu slouží metoda `add()`. Další hlavní rozdíl je ten, že pořadí prvků je u seznamů a n-tic zaručeno (stejně jako pořadí znaků v řetězci), ale u množin pevné pořadí není. Není možné množinu ani indexovat.

```py
names = set()

names.add('Martin')
names.add('Jana')
names.add('Petr')
names.add('Simona')
print(len(names), names)

names.add('Martin')
print(len(names), names)
```

### Vzájemné převádění datových typů

Už umíme převádět řetězce na celá čísla pomocí funkce `int()` nebo na desetinná čísla pomocí `float()`. Opačně můžeme číslo převézt na řetězec pomocí funkce `str()`. Podobně to funguje u datových typů `list`, `tuple` a `set`.

```py
t = 1, 2, 3, 2, 3, 2, 3, 1, 2
s = set(t)
print(s)
```

## Cvičení
::exc[excs>mnoziny]
