## Různé přístupy k ošetřování vstupů

Ještě než se pustíme do samotného ošetřování výjimek povíme si něco o ošetřování vstupů programu. Pokud totiž program nemá žádné uživatelské vstupy, nejedná se o moc užitečný program. Takový program by se choval vždy stejně a vypsal by jen to, co jsme mu zadrátovali uvnitř (např. text "Hello world!").

Důležité je si pod pojmem vstup programu představit mnoho různých věcí, např.:
* Návratovou hodnotu funkce `input()` - vstup textu z klávesnice
* Parametry programu na příkazové řádce (`sys.argv`)
* Data z načítaného souboru
* Data stažená přes internet z API nebo webové stránky
* Formuláře na webové stránce (viz [xkcd komix](https://xkcd.com/327/))
* Posloupnost klikání na tlačítka a jiné prvky u GUI aplikací

Všechny tyto vstupy mohou způsobit v našem programu chyby, kterým se vždy musíme snažit předejít. K tomu se používají dva hlavní přístupy.

### Nejprve otestuj a pak proveď
Pokud bychom neznali nic jiného a chtěli např. ošetřit, že program je vždy spuštěn alespoň s jedním parametrem na příkazové řádce, uděláme to nějak takto:

```py
import sys

if len(sys.argv) > 1:
    print(f"Zadán parametr: {sys.argv[1]}")
else:
    print("Zadej parametr na příkazovou řádku!")
```

```shell
python program.py
Zadej parametr na příkazovou řádku!
```

```shell
python program.py PARAMETR
Zadán parametr: PARAMETR
```

Teď přichází druhý problém, a to, že chceme, aby parametr byl číslo, protože s ním chceme počítat (např. vypsat číslo o jedničku vyšší). Dá se to provést složenou podmínku, kde budeme zároveň kontrolovat, jestli se parametr skládá z cifer. Použijeme k tomu metodu řetězců [isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit)

```py
import sys

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    cislo = int(sys.argv[1])
    print(f"Zadán parametr: {cislo}")
    print(f"O jedničku vyšší je: {cislo+1}")
else:
    print("Zadej číslo jako parametr na příkazovou řádku!")
```

```shell
python program.py PARAMETR
Zadej číslo jako parametr na příkazovou řádku!
```

```shell
python program.py 100
Zadán parametr: 100
O jedničku vyšší je: 101
```

Už se nám to testování před provedením operace trochu komplikuje a to řešíme zatím jen dvě podmínky. V reálném světě je to ještě složitější.

### Proveď a řeš až problémy
Proto byl v mnoha programovacích jazycích vytvořen mechanismus obsluhy výjimek. Kromě Pythonu jsou to např. jazyky C++, Java nebo C#.

Slouží nám k tomu nová klíčová slova `try` a `except`. Kus kódu, ve kterém může dojít k chybě obalíme blokem `try`. Za tím to blokem _odchytíme_ příslušnou chybu v bloku `except`.

Předchozí příklad přepíšeme následujícím způsobem:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
```

Toto řešení nám odchytává _IndexError_ na seznamu `sys.argv`, tzn. nenapsali jsme na příkazovou řádku potřebný parametr.

Pro odchycení chyby při nevhodném přetypování řetězce na číslo pomocí funkce `int()` zařadíme další blok `except`, kde odchytneme jinou chybu:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    print(f"O jedničku vyšší je: {int(sys.argv[1])+1}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
except ValueError:
    print("Zadej číslo jako parametr na příkazovou řádku!")
```


## Cvičení: Výjimky
::exc[excs/deleni]
