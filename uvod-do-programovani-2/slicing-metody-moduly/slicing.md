## Slicing seznamů a řetězců

Představme si, že si chci zaznamenat počet vanilkových věnečků snědených za posledních 7 dní. V Pythonu si můžu pro tento účel vytvořit seznam, který si uložím do vhodně pojmenované proměnné.

```pycon
>>> venecky = [1, 2, 4, 1, 6, 0, 1]
```

Chceme-li přistoupit k jednotlivým hodnotám uvnitř seznamu, použijeme k tomu hranaté závorky.

```pycon
>>> venecky[0]
1
>>> venecky[4]
6
```

**POZOR!** Programátoři jsou podivné bytosti, které vždy počítají od nuly, nikoliv od jedničky. Proto také první hodnota v našem seznamu má index 0.

Snadno také můžeme některou hodnotu v seznamu změnit. Například když si vzpomeneme, že jsme trošku zalhali ohledně konzumace věnečků v sobotu:

```pycon
>>> venecky[5] = 12
```

Z jednoho seznamu můžeme také získat menší kusy podle zadaných mezí

```pycon
>>> venecky[2:5]
[4, 1, 6]
>>> venecky[:3]
[1, 2, 4]
>>> venecky[3:]
[1, 6, 12, 1]
```

### Vnořené seznamy

Seznam může obsahovat jakékoliv hodnoty, tedy nejen celá čísla. Nezapomeňte, že seznamy jsou také hodnoty, takže jeden seznam může obsahovat jiný seznam jako svůj prvek. Například takto:

```pycon
>>> seznam = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Rozmyslete si, co vypíšou následující výrazy:

```pycon
>>> seznam[0][1]
>>> seznam[2][0]
>>> seznam[1:][1]
>>> seznam[:1][2]
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

Řetězce se chovají v něčem podobně jako čísla a v něčem podobně jako seznamy. Můžeme je například sčítat

```pycon
>>> jmeno = 'martin' + ' ' + 'podloucký'
```

Můžeme však také přistupovat k jednotlivým písmenům nebo pracovat s podřetězci.

```pycon
>>> jmeno[3]
't'
>>> jmeno[:6]
'martin'
>>> jmeno[7:]
'podloucký'
```

Podobně jako u seznamů můžeme na řetězcích volat také funkci `len()`

```pycon
>>> len(jmeno)
16
```

Jelikož řetězec je opět hodnota jako každá jiná, není problém vyrobit seznam
řetězců

```pycon
>>> jmena = ['martin', 'jana', 'petr', 'simona']
```

## Cvičení
::exc[excs>domena-a-url]
