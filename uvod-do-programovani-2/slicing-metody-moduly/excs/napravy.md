---
title: Nápravy
demand: 4
---

Náprava je část vozidla, která spojuje kola s karosérií vozidla. V registru vozidel je u každého vozidla uložená informace o vzdálenostech jeho náprav. Počet náprav a jejich vzdálenosti jsou důležité napříkad kvůli maximální povolené hmotnosti vozidla. Ze vzdálenosti náprav můžeme určit jejich počet. Například osobní automobil má dvě nápravy, proto u něj evidujeme jednu vzdálenost náprav. Nákladní vozidlo se třemi nápravami (třemi dvojicemi kol) bude mít dvě vzdálenosti.

Dostala jsi následující seznam, kde jsou vzdálenosti mezi nápravami přípojných vozidel nákladních automobilů. Vzdálenosti jsou odděleny středníkem či čárkou.

```py
napravy = ["1323;1341", "3459;1023;1094", "1241;1231;1247", "3421,983,956,954", "3981"]
```

* Vytvoř seznam, kde bude použitý jednotný oddělovač (např. středník).
* Vytvoř dvourozměrný seznam, kde budou jednotlivé vzdálenosti jako samostatné prvky seznamu.
* Dále vytvoř jednorozměrný seznam, kde budou počty náprav jednotlivých vozidel. Protože počet náprav je vždy o 1 vyšší než počet vzdáleností, k délce každého seznamu přičti 1. Následně vypočti průměrný počet náprav v našem vzorku.
