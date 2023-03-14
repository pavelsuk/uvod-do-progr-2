## List comprehension

Často se může stát, že potřebujeme nějakým způsobem zpracovat všechny hodnoty v nějakém seznamu a vyrobit tak seznam nový.

Představme si, že zpracováváme známky z písemek, které hodnotili programátoři. Ti místo známek 1 až 5 používali známky 0 až 4. Z takového zápisu nás bolí hlava, takže chceme známky převést do běžného formátu, tedy ke každé z nich přičíst jedničku.

```py
pisemky = [0, 2, 0, 1, 1, 3]

pisemky_bezne = []
for znamka in pisemky:
    pisemky_bezne.append(znamka + 1)

print(pisemky_bezne)  # [1, 3, 1, 2, 2, 4]
```

Kratší a přehlednější způsob je pomocí takzvaného _list comprehension_.

```py
pisemky = [0, 2, 0, 1, 1, 3]

pisemky_bezne = [znamka + 1 for znamka in pisemky]

print(pisemky_bezne)  # [1, 3, 1, 2, 2, 4]
```

**Poznámka:** Anglický termín _list comprehension_ nemá žádný oficiální český překlad. Čeští programátoři zcela běžně používají tento anglický termín.

Seznam můžeme zchroustat jakýmkoliv výrazem. Když si například půjdeme v záchvatu zodpovědnosti zaběhat, abychom vyvážili špatné svědomí z jedení věnečků, můžeme si například takto zaznamenat uběhnuté kilometry v prvních pěti dnech.

```py
kilometry = [2.4, 2.6, 0, 3.5, 1.8]
```

Pokud se pak rozhodneme, že bychom chtěli jen celé kilometry bez desetinných
čísel, napíšeme

```py
zaokrouhleno = [round(beh) for beh in kilometry]
print(zaokrouhleno)
```

## Seznamy seznamů

Ještě zajímavější situace nastane, budeme-li chtít zchroustat seznam seznamů. Zkusme se podívat na seznam známek ze čtyř písemek od šesti účastníků kurzu. Mohl by vypadat například takto:

```py
pisemky = [
    [1, 3, 2, 1],
    [3, 1, 1, 2],
    [4, 2, 2, 2],
    [1, 1, 1, 1],
    [1, 2, 2, 1],
    [1, 4, 1, 3]
]
```

Pokud chceme získat dejme tomu všechny známky z první písemky, chceme vlastně všechny první hodnoty ze všech seznamů uvnitř seznamu písemky. To můžete udělat takto:

```py
prvni = [znamky[0] for znamky in pisemky]
print(prvni)  # [1, 3, 4, 1, 1, 1]
```

## Cvičení: list comprehension
::exc[excs>seznamy-cisel]
::exc[excs>seznamy-retezcu]
::exc[excs>seznam-teplot]
::exc[excs>cteni-kodu]

## Doporučené úložky na doma
::exc[excs>overovani-veku]
::exc[excs>promitani]
::exc[excs>pocty-obyvatel]
::exc[excs>volby]

## Volitelné úložky na doma
::exc[excs>elegantni-volby]


## Podmínky v list comprehension

Podmínky slouží k tomu, abychom nějaký kus kódu mohli vykonat jen v případě, že je splněna nějaká podmínka. Doplněním list comprehension o klíčové slovo `if` můžeme ovlivnit, aby se do výsledného seznamu dostaly prvky pouze na základě určité podmínky.

Mějme například seznam uběhnutých kilometrů a chceme z něj jen nenulové hodnoty. Z délky seznamu pak můžeme snadno zjistit počet dní, kdy jsme trénovali.

```py
ubehnuto = [12, 0, 4, 5, 0, 6]
nenulove = [beh for beh in ubehnuto if beh != 0]
print(nenulove)  # [12, 4, 5, 6]
```

Nebo bychom mohli z následujícího seznamu měst chtít pouze názvy těch měst, která mají nad 50 000 obyvatel.

```py
mesta = [['Zlín', 76010], ['Jičín', 16792], ['Aš', 13093]]
velka_mesta = [mesto[0] for mesto in mesta if mesto[1] > 50000]
print(velka_mesta)  # ['Zlín']
```
