---
title: Závod
demand: 3
---

Pracuj dál se souborem [zavod.json](../assets/zavod.json). Cílem cvičení je zjistit čas závodníka, který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán jako první v našem souboru `zavod.json`. Budeš tedy muset projít data pomocí cyklu a vytvořit seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není `'DNF'`.

Můžeš postupovat následujícím způsobem:

1. Vytvoř si prázdný seznam `finishers`, kam budeš vkládat jména závodníků, kteří závod doběhli.
1. Pomocí cyklu projdi seznam závodníků.
1. Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
1. Dovnitř podmínky vlož kód, který vloží jméno a oficiální čas závodníka do seznamu `finishers`. (obě hodnoty můžes dát do nového seznamu, výsledný seznam `finishers` bude tedy obsahovat seznamy jako jeho položky). Pro přidání prvku do seznamu použij metodu `append()`, tedy `finishers.append(seznam_s_jmenem_a_casem_zavodnika)`
1. Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu `finishers`.
1. Zvol index výsledného seznamu `finishers` tak aby print vypisoval pouze stříbrného medailistu. 

U každého bodu si klidně ověř že tvůj aktuální kus kódu dělá to co má - například dočasným pomocným printem.
