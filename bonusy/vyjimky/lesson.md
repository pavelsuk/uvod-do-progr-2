## Chyby v programu

Tato bonusová kapitola není nezbytně nutná pro základní programování v Pythonu. V mnoha případech se obejdeš bez znalosti práce s výjimkami. Pokud to ale s Pythonem myslíš vážně, tato část se ti bude rozhodně hodit.

Mnohokrát jsme se již setkali s tím, že náš program neudělal co jsme si mysleli a Python skončil s chybovou hláškou. V tuto chvíli je nejdůležitější nepanikařit a v klidu si přečíst co nám Python interpret říká. Drtivá většina základních chyb nejsou žádné záludnosti a Python interpret nám často přímo radí, jak chybu opravit. Důležité je nemít z těchto chyb špatný pocit. Programování je často neustálé zkoušení různých pokusů dokud to nebude dělat to, co chceme.

Chybové hlášky jsou taky ta lepší varianta chyby. Pokud nám ji Python vypíše a skončí, tak jistě víme, že je něco špatně. Mnohem hůř se hledají chyby v programu, který Python interpret vyhodnotí jako syntakticky a sémanticky správný, ale ve skutečnosti vůbec nedělá to co si myslíme, že má dělat.

### Chyby, které musíme opravit
Nyní si ukážeme pár typických chyb, které se ti jistě často dějí:
```pycon
>>> promenna = 10
>>> print(promenna)
10
>>> print(promena)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'promena' is not defined
```

_NameError_ nastává v momentě, kdy Python narazí na slovo, které nezná. Vzhledem k tomu, že klíčová slova, jako `if`, `else`, `def` nebo `import` všechna Python musí znát, zbývají jako další možnosti názvy našich proměnných, funkcí nebo tříd. Pokud v názvu uděláme překlep, nebo použijeme něco, co jsme si vůbec nedefinovali, Python zahlásí _NameError_ a my musíme tuto chybu v programu opravit.

```pycon
>>> if 1 > 0
  File "<stdin>", line 1
    if 1 > 0
           ^
SyntaxError: invalid syntax
```
Další častý problém je chyba v syntaxi. V předcházejícím případě chybí na konci řádku dvojtečka `:`.


```pycon
>>> if 1 > 0:
... print()
  File "<stdin>", line 2
    print()
    ^
IndentationError: expected an indented block
```
_Indentation_ je anglický výraz pro odsazení. Vše co je shodně odsazeno patří do jednoho bloku, který končí prvním řádkem, který je odsazen o jedno méně. V tomto případě je problém, že volání funkce `print()` není v bloku odsazeno vůbec. Dbej na správné nastavení editoru a nemíchej odsazování různým počtem mezer nebo tabulátorů. Pozor na kód, který kopíruješ z internetu!


### Chyby, které můžeme zkusit ošetřit
Dostáváme se k části chyb, které někdy mohou být naše neúmyslné chyby, ale někdy se může jednat o chybu vzniklou vstupem programu (např. od uživatele funkcí `input()` nebo v seznamu parametrů příkazové řádky `sys.argv`. Dokončený program nesmí na žádný vstup od uživatele zhavarovat s chybovou hláškou od Python interpretu (jako vidíme ve všech těchto případech).

```pycon
>>> l = [0, 1, 2]
>>> l[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
Častá chyba je hledání indexu, který už v seznamu není.

```pycon
>>> zvirata = {'dog': 'pes', 'cat': 'kocka'}
>>> zvirata['cat']
'kocka'
>>> zvirata['rat']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'rat'
```
Obdobně můžeme narazit na neexistující klíč slovníku.

Poslední příklad, který si ukážeme je chyba, která může nastat např. při pokusu o přetypování.
```pycon
>>> int(input("Zadej cislo: "))
Zadej cislo: 0
0
```
Funkce `input()` nám zastaví běh, programu a vyčkává na uživatele, než něco napíše a zmáčkne Enter. Můžeme se setkat s "hodným" uživatelem, který na výzvu k zadání čísla skutečně zadá číslo. My si ho přetypujeme pomocí funkce `int()` a můžeme s ním dále počítat.

Co když ale uživatel zadá řetězec, který není složen pouze z cifer desítkové číselné soustavy 0 až 9, a tím pádem ho není možné přetypovat na datový typ `int`?
```pycon
>>> int(input("Zadej cislo: "))
Zadej cislo: cislo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'cislo'
```

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
$ python program.py
Zadej parametr na příkazovou řádku!
```

```shell
$ python program.py PARAMETR
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
$ python program.py PARAMETR
Zadej číslo jako parametr na příkazovou řádku!
```

```shell
$ python program.py 100
Zadán parametr: 100
O jedničku vyšší je: 101
```

Už se nám to testování před provedením operace trochu komplikuje a to řešíme zatím jen dvě podmínky. V reálném světě je to ještě složitější.

### Proveď a řeš až problémy
Proto byl v mnoha programovacích jazycích vytvořen mechanismus výjimek a jejich obsluhy. Kromě Pythonu jsou to např. jazyky C++, Java nebo C#.

Slouží nám k tomu nová klíčová slova `try` a `except`. Kus kódu, ve kterém může dojít k výjimce obalíme blokem `try`. Za tím to blokem _odchytíme_ příslušnou výjimku v bloku `except`.

Předchozí příklad přepíšeme následujícím způsobem:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
```

Toto řešení nám odchytává _IndexError_ na seznamu `sys.argv`, tzn. nenapsali jsme na příkazovou řádku potřebný parametr.

Pro odchycení výjimky při chybném přetypování řetězce na číslo pomocí funkce `int()` zařadíme další blok `except`, kde odchytneme jinou výjimku:

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
