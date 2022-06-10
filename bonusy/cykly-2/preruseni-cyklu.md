## Přerušení cyklu

Často se ocitneme v situaci, že cyklus chceme ukončit v jeho průběhu. Je to podobné, jako když něco hledáme a procházíme při tom všechny místnosti v domě. Jakmile danou věc nalezneme, hledání ukončíme.

K ukončení běhu cyklu používáme klíčové slovo `break`. Jakmile program narazí na slovo `break`, cyklus ukončí a pokračuje dál v kódu, který je pod cyklem. Příkaz `break` používáme v drtivé většině případů v kombinaci s podmínkou `if`.

Uvažujme třeba prekérní situaci, kdy na poslední chvíli potřebujeme objednat dárek na oslavu narozenin. Máme seznam zboží v e-shopu a u každého zboží máme jeho název, cenu a počet kusů skladem. Vzhledem k situaci potřebujeme, aby bylo zboží skladem a současně chceme dárek s cenou od 500 do 1000 Kč. Protože nemáme čas, spokojíme se s prvním nalezeným dárkem.

```py
list_of_items = [
    {"title": "Modrá kravata", "price": 239, "in_stock": True},
    {"title": "Luxusní psací pero", "price": 1599, "in_stock": True},
    {"title": "Degustační balíček kávy", "price": 599, "in_stock": True},
    {"title": "Parfém", "price": 559, "in_stock": False},
    {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True},
    {"title": "Sklenice na víno", "price": 799, "in_stock": True},
    {"title": "Fitness náramek", "price": 2399, "in_stock": False},
]

for item in list_of_items:
    if 500 <= item["price"] <= 1000 and item["in_stock"]:
        print(f"Vybraný dárek je {item['title']}")
        break
```

Pokud bychom příkaz `break` odebrali, program by pokračoval v hledání a vypsal ještě 2 další dárky, která vyhovují podmínkám.

#### Tip

Všimni si, že podmínku, zda určité číslo leží mezi dvěma jinými čísly, můžeme zapsat ve stylu `dolni_hranice <= cislo <= horni_hranice`. To je zjednodušení zápisu `dolni_hranice <= cislo and cislo <= horni_hranice`.