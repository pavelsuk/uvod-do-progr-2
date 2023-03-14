## Zápis do souboru

Když už umíme data ze souboru číst, pojďme se také naučit jak data do souboru zapsat. Konec konců, naše programy budou potřebovat nejen data zpracovávat ale také data produkovat.

Nejprve musíme náš soubor otevřít takzvaně pro zápis. Změna je u druhého parametru `mode='w'` (_write_) při volání funkce `open()`. Pokud soubor na disku ještě neexistuje, funkce `open()` jej před otevřením vytvoří. Pokud soubor již existuje, funkce `open()` vymaže před otevřením jeho obsah. Tímto způsobem vždy zapisujeme do prázdného souboru. Pokud bychom chtěli přidat nový obsah na konec souboru, místo `'w'` použijeme `'a'` (_append_).

Funkce `print()` umí kromě výpisu na terminál zapisovat i do souboru, pokud jako volitelný parametr `file` nastavíte náš otevřený soubor:

```py
text = "Tento text bude zapsán do souboru."

with open('soubor.txt', mode='w', encoding='utf-8') as output_file:
    print(text, file=output_file)
```

Dejme tomu, že máme seznam uživatelů, které chceme zapsat do souboru `uzivatele.txt`.

```py
names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)
```


## Cvičení: Zápis do souborů
::exc[excs>dny-v-mesici]
::exc[excs>vytvoreni-souboru]
::exc[excs>rozepsana-vyplata]
