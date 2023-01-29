---
title: Dny v měsíci
demand: 4
---

Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

```py
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

1. Nechte váš program vypsat tento seznam do souboru s názvem `kalendar.txt`, každé číslo na jeden řádek.
1. Pro další body už budete potřebovat znalosti, které jsme neprobírali:
    1. Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru. Názvy měsíců si můžete napsat taky přímo do programu, nebo můžete využít modul `calendar`, který obsahuje seznam `month_name` - [dokumentace](https://docs.python.org/3/library/calendar.html#calendar.month_name).
    1. Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy `měsíc` a `počet dní`.
