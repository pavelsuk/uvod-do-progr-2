## Podmínky

Naše programy se často musejí *rozhodovat* a některé bloky kódu se spouštějí pouze za předpokladu splnění nějaké podmínky. Podmínku začínáme klíčovým slovem `if`. Blok, který se spouští při splnění podmínky, je vždy odsazený (standardně čtyřmi mezerami).

Uvažujme například divadlo, které dává slevu 10 % při nákupu lístků za celkovou cenu více než 500 Kč. Pokud tedy zákazník zakoupí větší množství lístků, dostaneme informaci o získané slevě. Každý zákazník pak získá informaci o celkové ceně, protože tento blok již není odsazený.

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

* Na konci řádku s podmínkou musíme zapsat dvojtečku (`:`). Poté Visual Studio Code provádí odsazení automaticky. 
* Každá podmínka musí obsahovat alespoň jeden řádek, tj. minimálně jeden řádek po podmínce musí být odsazený.

#### Komplexnější podmínky

Pokud si přejeme spustit nějaký blok kódu v případě, že podmínka není splněná, použijeme klíčové slovo `else`.

```py
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")
```

Větví podmínek můžeme mít i několik za sebou. Klíčové slovo `elif` je kombinací `else` a `if`. Uvažujme například, že od nákupu za 500 Kč dáváme slevu 10 % a od nákupu za 1500 Kč dáváme slevu 20 %.

```py
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 1500:
    discount = 0.2
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
elif total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")
```

Všimni si, že Python "skočí" do prvního bloku, kde je podmínka splněná. Pokud tedy někdo koupí 10 lístků, Python provede příkazy v prvním bloku a následující ignoruje. To znamená, že ze tří bloků v našem kódu bude vždy spuštěn přesně jeden.

#### Vnořené podmínky

Poslední možností jsou **vnořené podmínky**, tj. podmínky uvnitř podmínek. Uvažujme například dětem nepřístupné divadelní představení. Není-li zájemce nebo zájemkyně o lístek starší třinácti let, je mu vypsán text o nepřístupnosti. Pouze starší zákazníci a zákaznice jsou tázání na počet lístků a při nákupu většího množství lístků může opět získat slevu.

```py
age = int(input("Jaký je Váš věk? "))
if age >= 13:
    number_of_tickets = int(input("Kolik si přejete lístků? "))
    price_per_ticket = 190
    total_price = number_of_tickets * price_per_ticket
    if total_price >= 1500:
        discount = 0.2
        total_price = total_price * (1 - discount)
        print(f"Získáváte slevu {discount * 100}.")
    elif total_price >= 500:
        discount = 0.1
        total_price = total_price * (1 - discount)
        print(f"Získáváte slevu {discount * 100}.")
    else:
        to_discount = total_price - 500
        print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

    print(f"Celková cena nákupu je {total_price} Kč.")
else:
    print("Představení je bohužel přístupné až od 13 let.")
```

Všimněte si, že klíčová slova `else` a `elif` jsou vždy zarovnaná stejně jako začátek podmínky, ke které se vztahují.

**Tip:** Pokud potřebuješ změnit odsazení většího množství řádků ve VS Code, všechny je označ a použij klávesu `Tab` (zvýšení odsazení) nebo `Shift+Tab` (snížení odsazení).
