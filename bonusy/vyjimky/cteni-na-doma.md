## Čtení na doma: Pokročilá práce s výjimkami v Pythonu

Pro úplnost doplním, že je možné odchytávat více chyb v jednom bloku `except`. Tyto chyby jsou oddělený čárkou **musí** a být v závorkách, aby tvořily <term cs="n-tici" en="tuple">. Rozšířením bloku `except` o klíčové slov `as` si můžeme název chyby uložit do proměnné. V Pythonu je možný i mechanismus odchytávání všech možných chyb v jednom bloku `except`, ale to patří k zavrženíhodným programátorským technikám, a proto si to ani nebudeme ukazovat.

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    print(f"O jedničku vyšší je: {int(sys.argv[1])+1}")
except (IndexError, ValueError) as e:
    print(f"Chyba: {e}")
    print("Zadej číslo jako parametr na příkazovou řádku!")
```

Pokud stále pokračuješ ve čtení této dobrovolné části, věz, že kromě bloku `try` a `except` je možné zařadit i blok `else` (toto `else` se nekamarádí s `if`, ale patří k obsluze výjimek. Je to pouze znovu využité klíčové slovo). Blok `else` se vykoná, pokud chyba v bloku `try` nenastala.

Poslední parťák mezi klíčovými slovy k obsluze výjimek je `finally`. Uvozuje blok kódu, který se vykoná za všech okolností (i kdyby chyba nastala či nenastala). Důležité je zachovat pořadí těchto bloků:

* `try`
* `except`
* (`except`) - více možných bloků `except` pod sebou
* `else`
* `finally`

Jedná už o pokročilé téma, proto zde nebudu uvádět žádné příklady a odkážu tě na oficiální dokumentaci [oficiální tutoriál](https://docs.python.org/3/tutorial/errors.html).

### Vyvolání výjimky
Až budeš tvořit složité programy v Pythonu a budeš dobře rozumět obsluze výjimek, může ti přijít na mysl otázka, jestli můžeme výjimku sami vyvolat.

Uvažujme předchozí příklad s přetypováním čísla na příkazové řádce a zvolme si další podmínku, např. musí se jednat o kladné číslo. Tuto podmínku musíme otestovat pomocí `if`:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    cislo = int(sys.argv[1])
    if cislo < 1:
        raise RuntimeError

    print(f"O jedničku vyšší je: {cislo+1}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
except ValueError:
    print("Zadej číslo jako parametr na příkazovou řádku!")
except RuntimeError:
    print("Zadej KLADNÉ číslo jako parametr na příkazovou řádku!")
```

Pomocí klíčového slova `raise` jsme zde vyvolali obecnou chybu v běhu programu, kterou poté v příslušném bloku `except` odchytíme výjimkou. _RuntimeError_ jsem vybral ze seznamu vestavěných chyb v Pythonu a nejlépe vystihuje náš problém. _ValueError_ by byl také dobrou volbou, ale už se používá pro jinou chybu. Pokud bychom potřebovali, můžeme si vytvořit úplně nový vlastní název chyby, ale to už si zájemci přečtou v [oficiální dokumentaci](https://docs.python.org/3/tutorial/errors.html).
