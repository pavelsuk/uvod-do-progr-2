## Dvourozměrné tabulky v Pythonu

O knihách můžeme evidovat mnohem více informací. Uvažujme nyní, že chceme mít uložen nejen počet prodaných kusů, ale i cenu knihy. Použijeme opět slovník, pro jednu knihu by zápis vypadal takto:

```py
book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347}
```

My ale máme další dvě knihy. Jak vložíme všechny knihy do jedné proměnné? Použijeme k tomu **seznamy**, které již známe! Seznam se všemi slovníky může vypadat takto:

```py
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
```
Je to v podstatě běžná **dvourozměrná tabulka**, jakou můžeme vytvořit například v Excelu.

Upravme nyní náš výpočet celkového počtu prodaných knih. Nyní pomocí cyklu `for` procházíme seznam, vrátíme se tedy zpět k jedné proměnné, kterou si pojmenujeme `item`. Do té cyklus nyní nebude ukládat číslo, ale slovník. Protože my chceme vědět počet prodaných kusů, z každého slovníku si načteme hodnotu uloženou pod klíčem `sold`.

```py
sales = 0
for item in books:
    sales += item["sold"]
print(f"Celkem bylo prodáno {sales} knih.")
```

Zkusme si ještě spočítat tržby nejen v prodaných kusech, ale i v penězích. Vždy tedy počet prodaných knih (hodnota s klíčem `sold`) vynásobíme cenou jedné knihy (hodnota s klíčem `price`).

```py
sales = 0
for item in books:
    sales += item["sold"] * item["price"]
print(f"Celkové tržby jsou {sales} Kč.")
```

Zkusme ještě jednu úpravu. Nakladatele zajímá, jaké jsou peněžní tržby za knihy vydané v roce 2019. U každé knihy tedy musíme zkontrolovat, zda vyšla v roce 2019, a pouze pokud je tato podmínka splněná, přičteme tržbu za knihu k proměnné `sales`.

```py
sales = 0
for item in books:
    if item["year"] == 2019:
        sales += item["sold"] * item["price"]
print(f"Celkové tržby za knihy prodané v roce 2019 jsou {sales} Kč.")
```
