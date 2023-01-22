## List comprehension

Často se může stát, že potřebujeme nějakým způsobem zpracovat všechny hodnoty v nějakém seznamu a vyrobit tak seznam nový.

Představme si, že zpracováváme známky z písemek, které hodnotili programátoři. Ti místo známek 1 až 5 používali známky 0 až 4.

```py
pisemky = [0, 2, 0, 1, 1, 3]
```

Z takového zápisu nás bolí hlava, takže chceme známky převést do běžného formátu, tedy ke každé z nich přičíst jedničku. To provedeme pomocí takzvaného _list comprehension_.

```py
print([znamka+1 for znamka in pisemky])  # [1, 3, 1, 2, 2, 4]
```

**Poznámka:** Anglický termín _list comprehension_ nemá žádný oficiální český překlad. Čeští programátoři zcela běžně používají tento anglický termín.

Seznam můžeme zchroustat jakýmkoliv výrazem. Když si například půjdeme v záchvatu zodpovědnosti zaběhat, abychom vyvážili špatné svědomí z jedení věnečků, můžeme si například takto zaznamenat uběhnuté kilometry v prvních pěti dnech.

```py
kilometry = [2.4, 2.6, 0, 3.5, 1.8]
```

Pokud se pak rozhodneme, že bychom chtěli jen celé kilometry bez desetinných
čísel, napíšeme

```py
print([round(beh) for beh in kilometry])
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
