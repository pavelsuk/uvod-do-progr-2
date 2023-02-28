## Čtení ze souborů

V praxi často máme data uložena v nějakém souboru na disku v nějakém textovém formátu. Ukážeme si, jak takový soubor v Pythonu otevřít a data z něj přečíst.

Pro naše první experimenty si stáhněte soubor [mereni.txt](assets/mereni.txt). Ten obsahuje naměřené teploty během týdne, které jsme už několikrát v našich programech používali.

Pokud chceme otevřít tento soubor v nějakém našem programu, nejjednodušší je zkopírovat jej do téže složky, ve které máme program uložený. Potom v programu použijeme funkci `open()`, která slouží k otevírání souborů. Nejčastěji se soubor otevírá v kombinaci se klíčovým slovem `with`. Tím automaticky zajistíme uzavření souboru a nebudeme ho blokovat. Současně si otevřený soubor musíme pojmenovat. Jméno vložíme za další klíčové slovo `as`. Náš soubor `mereni.txt` tedy dostal "přezdívku" `file`.

Všimni si, že prostřední řádek je odsazený o jedno odsazení vpravo. To není náhoda, tento řádek se totiž nachází v **bloku**. Pomocí bloku říkáme, v jaké části programu chceme pracovat s naším souborem a kdy ho již Python může uzavřít. Mezi řádkem 2 a 3 tedy v tichosti dojde k uzavření souboru. Nám to ale vůbec nevadí, protože obsah souboru máme načtený a ten nám nikam nezmizí.

Na konci úvodního řádku bloku vkládáme dvojtečku. Dvojtečka na konci řádku pak pro nás bude sloužit jako připomenutí, abychom alespoň jeden následující řádek odsadili. Ve stresu z toho ale být nemusíme, protože editor kódu to většinou udělá za nás.


### Různé možnosti načítání souboru

Nejjednodušší je načíst si obsah souboru do jednoho řetězce. Slouží k tomu metoda `read()` u objektu _otevřený soubor_. Tento způsob se hodí, pokud máme v souboru uložený pouze jeden řádek nebo z nějakého důvodu chceme mít řetězec, který přesně odpovídá uloženému souboru.

```py
with open('mereni.txt', encoding='utf-8') as file:
    text = file.read()

print(text)
```

Častěji však budeme potřebovat rozdělit soubor na řádky. Celý obsah souboru uložíme do seznamu `lines` pomocí metody `readlines()`. Ta uloží každý řádek souboru jako jeden prvek seznamu.

Náš kód pak může vypadat například takto:
```py
with open('mereni.txt', encoding='utf-8') as file:
    lines = file.readlines()

print(lines)
```

Výstup z našeho programu pak bude vypadat takto:

```shell
['po\t17.3\n', 'út\t16.8\n', 'st\t15.1\n', 'čt\t13.2\n', 'pá\t14.0\n', 'so\t13.9\n', 'ne\t15.8\n']
```

Výstupem je skutečně seznam řetězců, které ale obsahují znaky zpětných lomítek. Tato zpětná lomítka slouží k vyjádření speciálních znaků, které by jinak nešly do řetězce vložit. Anglicko/česky se jim říká _escape sekvence_ a my si představíme základní dvě. Nový řádek se píše jako `'\n'`, tabulátor jako `'\t'`. Existuje jich ještě mnoho dalších, ale tyto nám zatím postačí.

Vidíme tedy, že každý náš řádek končí znakem nového řádku a hodnoty na něm jsou odděleny tabulátorem. Pokud bychom chtěli načtené řádky rozdělit na jednotlivé hodnoty, využijeme toho, že otevřený soubor můžeme také načítat v cyklu `for`. Do proměnné `radek` se nám uloží vždy jeden řádek souboru jako řetězec. Tento způsob má také tu výhodu, že po řádcích můžeme načíst i dost velký soubor, které by se nám jinak nevešel do operační paměti počítače, kdybychom ho načetli pomocí metod `read()` nebo `readlines()`.

```py
output = []

with open('mereni.txt', encoding='utf-8') as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])

print(output)
```

V předchozí ukázce vidíme elegantní uložení dvou hodnot na řádku rozdělené podle znaku tabulátor do samostatných proměnných `day` a `temp`. Jedná se o praktické využití datového typu :term{cs="n-tice" en="tuple"}. Toto si můžeme dovolit díky tomu, že přesně známe strukturu dat, se kterými pracujeme.

## Cvičení: Čtení ze souborů
::exc[excs>vyplata-presneji]
::exc[excs>pocet-slov]

## Bonus
::exc[excs>pujcovna]
