## Slicing seznamů a řetězců

Představme si, že si chci zaznamenat počet vanilkových věnečků snědených za posledních 7 dní. V Pythonu si můžu pro tento účel vytvořit seznam, který si uložím do vhodně pojmenované proměnné.

```py
venecky = [1, 2, 4, 1, 6, 0, 1]
```

Chceme-li přistoupit k jednotlivým hodnotám uvnitř seznamu, použijeme k tomu hranaté závorky.

```py
print(venecky[0])
print(venecky[4])
```

**POZOR!** Programátoři jsou podivné bytosti, které vždy počítají od nuly, nikoliv od jedničky. Proto také první hodnota v našem seznamu má index 0.

Snadno také můžeme některou hodnotu v seznamu změnit. Například když si vzpomeneme, že jsme trošku zalhali ohledně konzumace věnečků v sobotu:

```py
venecky[5] = 12
```

Z jednoho seznamu můžeme také získat menší kusy podle zadaných mezí.

```py
print(venecky[2:5])
print(venecky[:3])
print(venecky[3:])
```


### Užitečné funkce nad seznamy

Pro práci se seznamy se nám může hodit několik funkcí:

`len()`
: Vrátí délku seznamu

`sum()`
: Vrátí součet všech prvků v seznamu

`min()`
: Vrátí nejmenší prvek seznamu

`max()`
: Vrátí největší prvek seznamu

`sorted()`
: Vrátí setříděný seznam


## Řetězce

Řetězce se chovají v něčem podobně jako čísla a v něčem podobně jako seznamy. Můžeme je například sčítat.

```py
jmeno = 'martin' + ' ' + 'podloucký'
```

Můžeme však také přistupovat k jednotlivým písmenům nebo pracovat s podřetězci.

```py
print(jmeno[3])
print(jmeno[:6])
print(jmeno[7:])
```

Podobně jako u seznamů můžeme na řetězcích volat také funkci `len()`.

```py
print(len(jmeno))
```

Můžeme též zkontrolovat, zda se nějaký podřetězec nachází v jiném řetězci. K tomu slouží operátor `in`, který můžeme využít v podmínce.

```py
inzerat = "Na této pracovní pozici budete využívat Python a SQL"
if "Python" in inzerat:
    print("Je to pro mě!")
```

Podobně můžeme využít i operátor `not in`, který vrací vždy opačný výsledek.

```py
email = "spatny-mail.cz"
if "@" not in email:
    print("V e-mailu chybí zavináč!")
```

Jelikož řetězec je opět hodnota jako každá jiná, není problém vyrobit seznam řetězců.

```py
jmena = ['martin', 'jana', 'petr', 'simona']
```

## Cvičení: Seznamy
::exc[excs>pohyby-na-uctu]
::exc[excs>prumer]
::exc[excs>rozpeti]

## Bonusy
::exc[excs>stred-seznamu]
::exc[excs>stred-seznamu-2]
