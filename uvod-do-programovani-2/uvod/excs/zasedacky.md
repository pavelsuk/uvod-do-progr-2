---
title: Zasedačky
demand: 1
---

Níže máš dva seznamy se seznamem akcí, které se konaly v jedné firmě v zasedačkách Forman a Goya.

```py
zasedacka_forman = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
]

zasedacka_goya = [
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
```

Napiš program, který zjistí následující:

- Kolik se uskutečnilo v jednotlivých zasedačkách pohovorů? A kolik jich bylo celkem?
- V jakých jazycích se mohou zaměstnanci firmy vzdělávat?

**Tip:** Může se ti hodit spojení dvou seznamů do jednoho s využitím operátoru `+`:

```py
obe_zasedacky = zasedacka_forman + zasedacka_goya
```
