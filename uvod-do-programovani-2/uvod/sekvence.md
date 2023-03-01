## Sekvence

Sekvence jsou hodnoty, které v sobě obsahují jiné hodnoty. Zatím jsme poznali základní dva typy sekvencí - řetězec (`string`) a seznam (`list`).

### Řetězce jako sekvence

Řetězce jsou vlastně sekvence skládající se z jednotlivých písmen. K jednotlivým prvkům sekvence přistupujeme pomocí hranatých závorek, které píšeme za název řetězce. Písmena jsou číslovaná (indexovaná) od 0.

Ukážeme si například, jak z rodného čísla zjistit datum narození.

```py
id_number = input("Zadejte rodné číslo: ")
year_of_birth = id_number[0] + id_number[1]
year_of_birth = int(year_of_birth)
if year_of_birth > 20:
    year_of_birth = 1900 + year_of_birth
else:
    year_of_birth = 2000 + year_of_birth
print(f"Uživatel(ka) se narodil(a) v roce {year_of_birth}.")
```

### Seznamy

Seznamy zapisujeme do hranatých závorek. Do seznamu můžeme vložit libovolný datový typ, jaký už známe. Začněme například s řetězci.

```py
guest_list = ["Jirka", "Klára", "Natálie"]
```

Chceme-li přidat jednu položku do seznamu, použijeme funkci `append`.

```py
new_guest = input("Zadej jméno dalšího hosta: ")
guest_list.append(new_guest)
print(guest_list)
```

**Námět:** Vypiš uživateli informaci o počtu hostů v seznamu. Můžeš použít funkci `len`.

Chceme-li si ověřit, zda je nějaká hodnota v seznamu, můžeme použít operátor `in`.

```py
incoming_person = input("Zadej jméno příchozího hosta: ")
if incoming_person in guest_list:
    print("Buď vítán(a)!")
else:
    print("Bohužel nejsi na seznamu.")
```

Sekvence v sobě mohou obsahovat i jiné sekvence. Je to podobné, jako polička na knihy. Ta obsahuje několik knih, každá kniha má několik kapitol, každá kapitola se skládá ze spousty slov a písmen. Níže máš příklad seznamu uvnitř seznamu, který obsahuje jména a známky studentů v nějakém předmětu.

```py
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4],
    ["Klára", 3, 2, 4, 1, 3]
]

print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][-1]}.")
```
