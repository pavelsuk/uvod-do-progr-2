## Zápis do souboru

Když už umíme data ze souboru číst, pojďme se také naučit jak data do souboru zapsat. Konec konců, naše programy budou potřebovat nejen data zpracovávat ale také data produkovat.

Zápis do souboru se provádí pomocí metody `write()`. Ta jako svůj parametr bere řetězec a zapíše jej do toho otevřeného souboru, na kterém ji zavoláme. Abychom ale mohli tuto metodu zavolat, musíme náš soubor otevřít takzvaně pro zápis. K tomu nám poslouží druhý parametr funkce `open()`. Druhý způsob je pomocí metody `writelines()`, která zapíše do souboru celý seznam řetězců. Pojďme si to vyzkoušet na příkladu.

Dejme tomu, že máme seznam uživatelů, které chceme zapsat do souboru `uzivatele.txt`.

```py
names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output:
    output.writelines(names)
```

Změna je u druhého parametru `mode='w'` při volání funkce `open()`. Díky němu se nám soubor otevře pro zápis. Pokud soubor na disku ještě neexistuje, funkce `open()` jej před otevřením vytvoří. Pokud soubor již existuje, funkce `open()` vymaže před otevřením jeho obsah. Vždy tedy pomocí metody `write()` zapisujeme do prázdného souboru. Pokud bychom chtěli přidat nový obsah na konec souboru, místo `'w'` použijeme `'a'`.

Pokud však otevřete soubor, který vytvořil náš předchozí program, uvidíte následující výsledek

```shell
RomanJanaRadekPetraVlasta
```

Je to proto, že metoda `writelines()` na rozdíl od funkce `print()` nedělá
automatické odřádkování. Dopíšeme tedy konce řádků k jednotlivým jménům v seznamu.
Upravíme tedy zápis do souboru v našem předchozím programu takto:

```py
names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output:
    for name in names:
        output.write(name + '\n')
```

### Bonusová znalost

Zapisovat do souboru lze i funkcí `print()`, pokud jako volitelný parametr `file` nastavíte náš otevřený soubor:

```py
names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output:
    for name in names:
        print(name, file=output)
```

Funkce `print()` v základním nastavení udělá odřádkování, takže oba způsoby dělají stejnou věc. Můžete používat, co se vám víc líbí.

## Cvičení: Zápis do souborů
::exc[excs>rozepsana-vyplata]
::exc[excs>hody-kostkou]

## Bonus
::exc[excs>dny-v-mesici]
