## Cykly

Poslední kapitolou, kterou si zopakujeme, jsou cykly. Cykly jsou způsob, jak programu říct, aby opakoval nějakou činnost.

Ideální je využití cyklů spolu s sekvencemi. Pro každý prvek sekvence provedeme nějakou činnost. Uvažujme například vysvědčení studenta nebo studentky základní školy.

```py
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 2],
    ["Chemie", 4],
]
```

Nejprve si zkusme vypočítat průměrnou známku studenta na vysvědčení.

```py
sum_of_marks = 0
for mark in school_report:
    sum_of_marks += mark[1]
average = sum_of_marks / len(school_report)
print(f"Průměrná známka studenta/studentky je {average}.")
```

**Námět:** Uvažujme, že chceme vypočítat průměr předmětů, které jsou důležité pro přihlášku na střední školu technického charakteru, což jsou předměty: český jazyk, anglický jazyk, matematika a fyzika. Jak upravíme předchozí program? Určitě bude vhodné vložit si tyto důležité předměty do seznamu.

Dále můžeme například vypsat všechny předměty, které jsou problematické, tj. ty, ze kterých má známku horší než trojku.

```py
print("Pro studenta/studentku jsou problematické tyto předměty:")
for mark in school_report:
    if mark[1] > 3:
        print(mark[0])
```
