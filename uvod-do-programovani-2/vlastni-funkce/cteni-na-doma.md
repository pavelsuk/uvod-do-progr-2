## Čtení na doma - typování funkcí

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
