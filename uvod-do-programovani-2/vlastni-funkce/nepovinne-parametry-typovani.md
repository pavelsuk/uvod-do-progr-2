## Nepovinné parametry a typování

### Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Vraťme se k funkci `get_mark()`. Uvažujme nyní, že studenti mají možnost získat bonusové body (např. za odevzdání úkolů), které se pak připočítávají k bodům z testu.

```py
def get_mark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark
```

Nyní opět zavoláme funkci. Uvažujeme stále možnost jednoho opravného pokusu, počet bonusových bodů zůstává.

```py
points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = get_mark(points, bonus)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")
```

::exc[excs/hotel]

### Typování funkcí

Python patří mezi *dynamicky typové jazyky*, což znamená, že při vytvoření proměnné neříkáme, jaký typ hodnoty do ní budeme ukládat. Od verze 3.5 ale podporuje `typing`. Můžeme tedy říct, jaký typ hodnoty by *měla obsahovat* nějaká proměnná, Python to však nekontroluje a neukončí program s chybou, pokud do proměnné vložíme hodnotu jiného typu. Typování ale funguje jako nápověda pro programátory a především vývojová prostředí, která pak umějí vývojářům lépe napovídat při psaní programů a případně je upozornit, pokud plánují do proměnné vložit něco, co tam nepatří.

Níže je příklad funkce `get_mark()` s typováním. Typovat můžeme jednotlivé parametry i návratovou hodnotu, jejíž typ je za "šipkou" `->`.

```py
def get_mark(points: int, bonus: int = 0) -> int:
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

print(get_mark(50, 30))
```
