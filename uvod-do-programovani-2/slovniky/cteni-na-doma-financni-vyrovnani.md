## Čtení na doma - finanční vyrovnání

Představte si šest spolubydlících: Libora, Zuzku, Patra, Pavlu, Ondru a Míšu. Žijí v jednom bytě a dělí se o náklady na společně používané věci jako je toaletní papír, mýdlo, prací prášek apod. Postupně svoje útraty zapisují do tabulky, která může vypadat například takto:

| Jméno | Položka | Částka |
| ------ | ---- | ----- |
| Petr   | Prací prášek | 399 |
| Ondra  | Savo | 80 |
| Petr   | Toaletní papír | 65 |
| Libor  | Pivo | 124 |
| Petr   | Pytel na odpadky | 75 |
| Míša   | Utěrky na nádobí | 130 |
| Ondra  | Toaletní papír | 120 |
| Míša   | Pečící papír | 30 |
| Zuzka  | Savo | 80 |
| Pavla  | Máslo | 50 |
| Ondra  | Káva | 300 |


Dejme tomu, že uplynulo například půl roku a spolubydlící se chtějí navzájem finančně vyrovnat. Vaším úkolem je vymyslet přesný postup, který mají následovat, aby došlo k celkovému vyrovnání všech lidí.

### Řešení s využitím slovníků

Slovníky by nám zde mohly pomoci, protože nám pomůžou při tvorbě tabulky s celkovou útratou za jednotlivé spolubydlící.

Jeden nákup zapsaný do slovníku vypadá například takto:

```py
{"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399}
```

Protože nákupů bylo více, jeden slovník by nám nestačil. Proto vytvoříme více slovníků a ty uložíme do seznamu.

```py
purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]
```

Útraty jednotlivých spolubydlících si budeme ukládat do nového slovníku. Musíme si tedy nejprve vysvětlit, jak ověřit, jestli nějaká hodnota už ve slovníku je. Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.

```py
sum_per_person = {}
for item in purchase_list:
    person = item["Jméno"]
    value = item["Položka"]
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
