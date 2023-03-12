---
title: Závod
demand: 3
---

Pracuj dál se souborem `zavod.json` a zjisti čas závodníka, který získal stříbrnou medaili. Dále projdi data pomocí cyklu a vytvoř seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není DNF.

Můžeš postupovat následujícím způsobem:

1. Vytvoř si prázdný seznam `finishers`, kam budeš vkládat jména závodníků, kteří závod doběhli.
1. Pomocí cyklu projdi seznam závodníků. Struktura vyjmuté položky bude obdobná jako struktura dat o vítězi závodu. Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
1. Dovnitř podmínky vlož kód, který vloží jméno závodníka do seznamu `finishers`.
1. Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu `finishers`.
