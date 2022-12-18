## Slovníky a cykly

Na kurzu Úvod do programování v Pythonu jsme si ukázali, že pro práci se sekvencemi jsou ideální cykly. Vyzkoušíme si nyní, jak se slovníky pracovat pomocí cyklů.

Abychom si ukázali průchod slovníkem pomocí cyklu, použijeme slovník s údaji o prodejích knih z cvičení z minulé kapitoly. Ve slovníku tedy máme následující data:

```py
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
```

Zkusme si nejprve vypsat názvy všech knih ve slovníku (bez počtu prodaných kusů). K tomu použijeme cyklus `for`, který již známe. Pomocnou proměnnou si pojmenujeme `key`. Tato proměnná funguje podobně jako u seznamu - postupně se do ní vloží hodnoty jednotlivých klíčů slovníku.

```py
for key in sales:
    print(key)
```

Zkusme nyní informaci o každém prodeji vypsat pomocí věty, do které vložíme název knihy a počet prodaných kusů. Oproti předchozímu příkladu je tu změna. **Každá položka** slovníku se skládá z **klíče** a **hodnoty**. V cyklu můžeme použít oboje (a často i používáme). Využijeme tedy **dvě proměnné**, které oddělíme čárkou. Do první proměnné je uložený klíč a do druhé hodnota. 

Všimni si též, že za slovník vkládáme `.items()`. To je důležité, protože bez metody `.items()` bychom získali pouze klíče.


```py
for key, value in sales.items():
    print(f"Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
```

Zkusme si nyní spočítat celkový počet prodaných kusů. Vytvoříme si tedy proměnnou `total_sales` a pro každou knihu do ní přičteme počet prodaných kusů.

```py
total_sales = 0
for key, value in sales.items():
    print(f"Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
    total_sales += value
print(f"Celkem bylo prodáno {total_sales} výtisků.")
```
