## Pár příkladů využití funkcí

Vraťme se k našemu příkladu z opakovací lekce, kde jsme měli určit známku z testu na základě počtu bodů. Uvažujme nyní, že student, který získá z testu známku 5, má možnost test jedenkrát opakovat. Podmínku, kterou jsme měli v prvním cvičení, tedy budeme potřebovat dvakrát - pro první a případný druhý pokus. Proto je ideální tuto podmínku umístit do funkce.

```py
def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark
```

Funkci můžeme volat z různých míst programu:

```py
points = int(input("Zadej počet bodů v testu: "))
mark = get_mark(points)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points)
print(f"Výsledná známka je {mark}.")
```
