## Chyby v programu

Tato bonusová kapitola není nezbytně nutná pro základní programování v Pythonu. V mnoha případech se obejdeš bez znalosti práce s výjimkami. Pokud to ale s Pythonem myslíš vážně, tato část se ti bude rozhodně hodit.

Mnohokrát jsme se již setkali s tím, že náš program neudělal, co jsme si mysleli a Python skončil s chybovou hláškou. V tuto chvíli je nejdůležitější nepanikařit a v klidu si přečíst co nám Python interpret říká. Drtivá většina základních chyb nejsou žádné záludnosti a Python interpret nám často přímo radí, jak chybu opravit. Důležité je nemít z těchto chyb špatný pocit. Programování je často neustálé zkoušení různých pokusů dokud to nebude dělat to, co chceme.

Chybové hlášky jsou taky ta lepší varianta chyby. Pokud nám ji Python vypíše a skončí, tak jistě víme, že je něco špatně. Mnohem hůř se hledají chyby v programu, který Python interpret vyhodnotí jako syntakticky a sémanticky správný, ale ve skutečnosti vůbec nedělá to co si myslíme, že má dělat.

### Chyby, které musíme opravit
Nyní si ukážeme pár typických chyb, které se ti jistě často dějí:
```py
promenna = 10
print(promenna)  # vypíše 10
print(promena)   # chyba v programu
```

```shell
10
Traceback (most recent call last):
  File "/home/martin/test.py", line 3, in <module>
    print(promena)
NameError: name 'promena' is not defined. Did you mean: 'promenna'?
```

_NameError_ nastává v momentě, kdy Python narazí na slovo, které nezná. Vzhledem k tomu, že klíčová slova, jako `if`, `else`, `def` nebo `import` všechna Python musí znát, zbývají jako další možnosti názvy našich proměnných, funkcí nebo tříd. Pokud v názvu uděláme překlep, nebo použijeme něco, co jsme si vůbec nedefinovali, Python zahlásí _NameError_ a my musíme tuto chybu v programu opravit.

```py
if 1 > 0
```

```shell
  File "/home/martin/test.py", line 1
    if 1 > 0
            ^
SyntaxError: expected ':'
```
Další častý problém je chyba v syntaxi. V předcházejícím případě chybí na konci řádku dvojtečka `:`.


```py
if 1 > 0:
print()
```

```shell
  File "/home/martin/test.py", line 2
    print()
    ^
IndentationError: expected an indented block after 'if' statement on line 1
```

_Indentation_ je anglický výraz pro odsazení. Vše co je shodně odsazeno patří do jednoho bloku, který končí prvním řádkem, který je odsazen o jedno méně. V tomto případě je problém, že volání funkce `print()` není v bloku odsazeno vůbec. Dbej na správné nastavení editoru a nemíchej odsazování různým počtem mezer nebo tabulátorů. Pozor na kód, který kopíruješ z internetu!


### Chyby, které můžeme zkusit ošetřit
Dostáváme se k části chyb, které někdy mohou být naše neúmyslné chyby, ale někdy se může jednat o chybu vzniklou vstupem programu (např. od uživatele funkcí `input()` nebo v seznamu parametrů příkazové řádky `sys.argv`. Dokončený program nesmí na žádný vstup od uživatele zhavarovat s chybovou hláškou od Python interpretu (jako vidíme ve všech těchto případech).

```py
l = [0, 1, 2]
print(l[3])
```

```shell
Traceback (most recent call last):
  File "/home/martin/test.py", line 2, in <module>
    print(l[3])
IndexError: list index out of range
```

Častá chyba je hledání indexu, který už v seznamu není.

```py
zvirata = {'dog': 'pes', 'cat': 'kocka'}
print(zvirata['cat'])
print(zvirata['rat'])
```

```shell
kocka
Traceback (most recent call last):
  File "/home/martin/test.py", line 3, in <module>
    print(zvirata['rat'])
KeyError: 'rat'
```

Obdobně můžeme narazit na neexistující klíč slovníku.

Poslední příklad, který si ukážeme je chyba, která může nastat např. při pokusu o přetypování.
```py
cislo = int(input("Zadej cislo: "))
print(cislo)
```

```shell
Zadej cislo: 0
0
```
Funkce `input()` nám zastaví běh, programu a vyčkává na uživatele, než něco napíše a zmáčkne Enter. Můžeme se setkat s "hodným" uživatelem, který na výzvu k zadání čísla skutečně zadá číslo. My si ho přetypujeme pomocí funkce `int()` a můžeme s ním dále počítat.

Co když ale uživatel zadá řetězec, který není složen pouze z cifer desítkové číselné soustavy 0 až 9, a tím pádem ho není možné přetypovat na datový typ `int`?
```shell
Zadej cislo: cislo
Traceback (most recent call last):
  File "/home/martin/test.py", line 1, in <module>
    cislo = int(input("Zadej cislo: "))
ValueError: invalid literal for int() with base 10: 'cislo'
```
