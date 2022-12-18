## Čtení na doma - finanční vyrovnání

Vraťme se nyní k našemu úplně prvnímu příkladu - finančnímu vyrovnání spolubydlících. Slovníky by nám zde mohly pomoci, protože nám pomůžou při tvorbě tabulky s celkovou útratou za jednotlivé spolubydlící.

Jeden nákup zapsaný do slovníku vypadá například takto:

```py
{"person": "Petr", "item": "Prací prášek", "value": 399}
```

Protože nákupů bylo více, jeden slovník by nám nestačil. Proto vytvoříme více slovníků a ty uložíme do seznamu.

```py
purchase_list = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]
```

Útraty jednotlivých spolubydlících si budeme ukládat do nového slovníku. Musíme si tedy nejprve vysvětlit, jak ověřit, jestli nějaká hodnota už ve slovníku je. Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.

```py
sum_per_person = {}
for item in purchase_list:
    person = item["person"]
    value = item["value"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value
```

Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. K tomu můžeme využít cyklus `for`. Zde je pouze jeden malý rozdíl.

```py
total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")
```

Jako poslední krok zbývá určení průměrné hodnoty na osobu. Zde opět využijeme funkci `len`, která umí pracovat i se slovníky.

```py
average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")
```
