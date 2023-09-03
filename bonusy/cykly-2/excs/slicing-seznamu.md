---
title: Slicing seznamu
---

Vlož si do programu následující kus kódu:

```python
seznam = [49, 38, 18, 82, 85, 60, 94, 21, 20, 14, 37,
          80, 13, 66, 41, 68, 82, 88, 41, 52, 28, 35, 55]

delka = 5
```

Napiš řešení, které bude ze seznamu krájet a vypisovat kusy o délce v proměnné `delka`. Nevadí, pokud poslední seznam se zbytkem čísel bude menší. Řešení musí fungovat tak, že pouze změníš proměnnou `delka` a zbytek programu zůstane stejný.

:::solution

Očekávaný výstup při `delka = 5`:

```shell
[49, 38, 18, 82, 85]
[60, 94, 21, 20, 14]
[37, 80, 13, 66, 41]
[68, 82, 88, 41, 52]
[28, 35, 55]
```

Očekávaný výstup při `delka = 6`:

```shell
[49, 38, 18, 82, 85, 60]
[94, 21, 20, 14, 37, 80]
[13, 66, 41, 68, 82, 88]
[41, 52, 28, 35, 55]
```

:::
