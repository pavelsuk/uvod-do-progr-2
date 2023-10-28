---
title: Narozeniny ve školce
---

Toto pokročilé cvičení se úplně nedotýká formátu JSON, ale vyžaduje pokročilou práci se slovníky a hodně hledání na internetu.

Paní ředitelka školky si exportovala z informačního systému seznam dětí, jejich zařazení do třídy a datum narození: [kids.csv](assets/kids.csv). Potřebuje vytvořit pro učitelky každé třídy výpis měsíců se seznamy dětí, které mají v tom měsíci narozeny. Výstupem budou textové soubory podle názvů tříd. Napište program univerzálně. Názvy tříd nejsou pevné, takže je získejte až ze samotných dat.

:::solution

Obsah souboru `ježečci.txt`:
```shell
Třída ježečci
1: Marcela Burianová
2: Matylda Kocourková
3: Nataša Králová, Otakar Čížek, Amálie Sýkorová
4: Judita Pavlíková
5: Bohumír Němeček, Irena Trojanová
6: Miroslava Janková, Oliver Beneš
7: Xenie Mikešová
8: Albína Drábková, Albert Zdráhal
10: Radek Brotz, Bohdana Červinková
11: Beáta Šulcová, Nora Křížová, Aleš Dostál, Linda Kuchařová
12: Libuše Vítová, Jolana Vítová
```

Obsah souboru `koťátka.txt`:
```shell
Třída koťátka
1: Břetislav Jaroš, Slavomír Charvát, Dita Burianová, Dobroslav Souček, David Zukal
3: Valdemar Rýpal
5: Jiří Řehák, Jindřich Mach
6: Mikuláš Krejčí, David Kozák, Agáta Franková
7: Emanuel Šulc, Filip Šrámek
8: Hubert Suchánek, Servác Hošek, Zbyšek Toman, Adéla Urbánková
9: Oldřich Ptáček, Drahoslava Křížková
10: Zdeněk Petr
11: Bohumil Lukeš, Martina Vlachová
12: Xenie Boháčová
```

Obsah souboru `sovičky.txt`:
```shell
Třída sovičky
1: Vlasta Staňková
3: Libor Macháček, Michaela Pavelková, Tereza Tomanová
4: Valérie Vondráčková, Ctirad Podlezl, Nela Nosková
6: Iva Vítková
7: Kamil Přibyl, Lukáš Doležal, Svatava Beránková, Lucie Lukášová
8: Klement Řehák, Hedvika Beránková, Havel Vlach, Vavřinec Soukup
9: Hana Kozáková
10: Ljuba Svozilová, Vladimír Povýšil, Věroslav Nováček
11: Ida Tučková, Pravoslav Utěkal
12: Blažena Kohoutová, Natálie Coufalová, Adolf Ztratil, Herbert Krejčí
```

Obsah souboru `včeličky.txt`:
```shell
Třída včeličky
1: Pravoslav Válek
3: Květoslav Hanuš, Milena Stehlíková
5: Eva Procházková, Sáva Janečková, Irma Machová
8: Roland Macháček, Saskie Bartáková
9: Hana Blažková
10: Marta Mrázková
12: Rudolf Doskočil, Šimon Macek, Karel Lukeš
```

Obsah souboru `žabičky.txt`:
```shell
Třída žabičky
1: Benedikt Marek, Dominika Pavelková, Žaneta Řezáčová
2: Řehoř Zeman, Ilona Dvořáková
3: Lubomír Rýpal
4: Alice Kejsalová
5: Stanislav Šimek, Viktor Mašek, Ludvík Pavlíček
8: Berta Kolářová, Štěpán Holeček, Ivo Štěpán
9: Gizela Boháčová
10: Hugo Malík
11: Irma Navrátilová
12: Elena Tomanová
```

:::
