---
title: Transformace dat
demand: 4
---

Stáhněte si soubor [words.txt](assets/words.txt) a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude. Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

Vzorový výstup: [output.json](assets/output.json).

---solution

1. Vytvořím si prázdný slovník, do kterého budu vytvářet požadovaný výstup
1. Otevřu si vstupní soubor a budu ho načítat v cyklu po řádcích
1. Zbavím se znaku pro nový řádek v každém slově
1. Zjistím si první písmeno slova
1. Pokud písmeno není klíčem slovníku, tak tento záznam vytvořím a jako hodnotu vložím seznam s tímto slovem
1. Jinak slovo připojím na konec existujícího seznamu slov
1. Po zpracování celého vstupu seřadím seznamy slov na všech klíčích
1. Výstupní slovník zapíšu do souboru ve formátu JSON
1. V dokumentaci musím najít, jak zajistím, aby byl výstup hezky odsazovaný o 4 mezery a klíče slovníku byly seřazené
