## Podmínky

Naše programy se často musejí *rozhodovat* a některé bloky kódu se spouštějí pouze za předpokladu splnění nějaké podmínky. Podmínku začínáme klíčovým slovem `if`. Blok, který se spouští při splnění podmínky, je vždy odsazený (standardně čtyřmi mezerami).

Uvažujme například kino, které dává slevu 10 % při nákupu lístků za celkovou cenu více než 500 Kč. Pokud tedy zákazník zakoupí větší množství lístků, dostaneme informaci o získané slevě. Každý zákazník pak získá informaci o celkové ceně, protože tento blok již není odsazený.

```py
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100} %")

print(f"Celková cena nákupu je {total_price} Kč.")
```

**Námět:** Zkus přidat zaokrouhlení ceny na celé koruny.

#### Na co si dát pozor

Na konci řádku s podmínkou musíme zapsat dvojtečku (`:`). Poté Visual Studio Code provádí odsazení automaticky. Každá podmínka musí obsahovat alespoň jeden řádek, tj. minimálně jeden řádek po podmínce musí být odsazený.

#### Komplexnější podmínky

Pokud si přejeme spustit nějaký blok kódu v případě, že podmínka není splněná, použijeme klíčové slovo `else`.

```py
items_in_stock = 5
number_of_items = int(input("Kolik si přejete koupit kusů zboží? "))

if number_of_items <= items_in_stock:
    print("Položky byly vloženy do košíku.")
else:
    print(f"Bohužel máme na skladě posledních {items_in_stock} kusů.")
```

Větví podmínek můžeme mít i několik za sebou:

```py
points = int(input("Kolik bodů získal student v testu? "))
if points <= 60:
    mark = 5
elif points <= 70:
    mark = 4
elif points <= 80:
    mark = 3
elif points <= 90:
    mark = 2
else:
    mark = 1
print(f"Známka z testu je {mark}.")
```

 Všimni si, že Python "skočí" do prvního bloku, kde je podmínka splněná. Pokud tedy student například získá 55 bodů, byla by splněná i podmínka `points <= 75`, `points <= 90`. Díky první podmínce se ale do proměnné `mark` uloží známka 5 a program dále skočí na konec bloku s výpisem podmínek.

 **Námět**: Bylo by možné namísto operátoru `<=` použít operátor `>=`? Stačí pouze nahradit znaménka? Nebo je potřeba jinak seřadit podmínky?

Poslední možností jsou vnořené podmínky, tj. podmínky uvnitř podmínek. Uvažujme například dětem nepřístupný film. Není-li zájemce o film starší třinácti let, je mu vypsán text o nepřístupnosti. Pouze starší zákazník je tázán na počet lístků a při nákupu většího množství lístků může opět získat slevu. Tentokrát máme dvě možné slevy - 10 % při nákupu nad 500 Kč a 25 % při nákupu nad 1000 Kč.

```py
price_per_ticket = 190
age = int(input("Jaký je váš věk? "))
if age >= 13:
    number_of_tickets = int(input("Kolik si přejete lístků? "))
    total_price = number_of_tickets * price_per_ticket
    if total_price >= 1000:
        discount = 0.25
        print(f"Získáváte slevu {discount * 100} %")
    elif total_price >= 500:
        discount = 0.1
        print(f"Získáváte slevu {discount * 100} %")
    else:
        discount = 0
    total_price = total_price * (1 - discount)
    print(f"Celková cena nákupu je {round(total_price)} Kč.")
else:
    print("Tento film bohužel není dětem přístupný.")
```

Všimněte si, že klíčová slova `else` a `elif` jsou vždy zarovnaná stejně jako začátek podmínky, ke které se vztahují.

