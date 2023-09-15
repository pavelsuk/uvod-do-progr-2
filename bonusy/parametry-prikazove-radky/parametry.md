## Parametry příkazové řádky

Velmi důležitý modul, jenž si v tuto chvíli představíme, je modul `sys`. Ten obsahuje funkce, které umožňují Pythonu komunikovat s operačním systémem, ve kterém je spuštěný. Nás z tohoto modulu bude zajímat především proměnná (ano, moduly mohou obsahovat kromě funkcí také proměnné) s názvem `argv` Ta nám umožní přistupovat k takzvaným _parametrům příkazové řádky_.

Mít všechna nezbytná data pro běh programu natvrdo zadrátované přímo uvnitř kódu je nám jen pramálo k užitku. Nemůžeme mu předat např. nově naměřené teploty jinak, než upravit jeho zdrojový kód. Do skutečně užitečného programu musíme být schopni dostat data jaksi z venku. K tomu máme vícero možností ‒ například nahrát data ze souboru na disku, můžeme je stáhnout z internetu, ale také je můžeme programu předat přímo na příkazové řádce, když jej spouštíme.

Představme si například program, kterému bychom chtěli předat počet minut a on by nám vypsal v hezkém formátu kolik to dohromady dělá hodin a zbylých minut. Pojmenujme náš program například `cas.py`. Pokud chceme zjistit, jaký čas představuje 325 minut, zavoláme náš program takto:

```shell
python cas.py 325
```

Číslo 325 v tomto příkazu je právě to, čemu říkáme _parametr_. Teď už jen zbývá se k tomuto číslu nějak dostat zevnitř našeho programu.

```py
import sys

celkem = int(sys.argv[1])
hodin = celkem // 60
minut = celkem % 60

print('f{hodin}:{minut}')
```

To nejdůležitější se děje na druhém řádku, kde používáme hodnotu `sys.argv[1]`. Proměnná `sys.argv` totiž obsahuje seznam všech parametrů, které náš program dostal na příkazovém řádku. Zajímavé je, že tento seznam jako první položku obsahuje samotný název programu. Tedy, pokud bychom si nechali proměnnou `sys.argv` vytisknout na obrazovku, byl by její obsah po spuštění našeho programu

```
['cas.py', '325']
```

Tedy na prvním místě je název programu a na druhém je náš parametr, který jsme prve zadali na příkazové řádce. Všimněte si ovšem, že náš parametr je řetězec. Python totiž všechny parametry na příkazové řádce bere jako řetězce, nehledě na to, jestli jsou to čísla nebo cokoliv jiného. My chceme ale v našem programu čas jako číslo, neboť s ním chceme provádět různá matematická cvičení. Proto musíme náš parametr převést na číslo pomocí již známé funkce `int()`, což právě provádíme na druhém řádku našeho programu.


### Nač se držet při zemi

Zatím jsme na příkazové řádce předali pouze jeden parametr. Nebuďme ale troškaři. Na příkazové řádce si můžeme dovolit předávat zajímavější věci, například celý seznam hodnot. Můžeme kupříkladu napsat program, který spočítá součet všech zadaných hodnot. Pozor ovšem na to, že hodnoty na příkazové řádce jsou vždy řetězce, takže pokud je to potřeba, musíme si je sami převést na čísla a elegantně k tomu využít _list comprehension_.

```py
import sys

cisla = [int(c) for c in sys.argv[1:]]

print(f'Součet zadaných čísel: {sum(cisla)}')
```

Program poté můžeme volat třeba takto:

```shell
python soucet.py 57 41 37 22 12
Součet zadaných čísel: 169
```

Všimněte si, že na druhém řádku našeho programu používáme `sys.argv[1:]`. Je to proto, abychom se zbavili názvu programu, který vždy zabírá první prvek seznamu parametrů. Naše čísla se tedy nacházejí až od prvního indexu nahoru.


## Cvičení: Parametry příkazové řádky
::exc[excs/cas-v-minutach]
::exc[excs/uprava-retezce]
::exc[excs/hada-na-velblouda]
::exc[excs/hazeni-kostkou]


### Otevírání souboru zadaného jako argument na příkazové řádce

Následující ukázka je velmi časté použití parametrů příkazové řádky. Mějme soubor `cisla.txt` obsahující čísla (každé na novém řádku)

```
57
41
37
22
12
```

Následující program otevře soubor, který má název zadaný jako parametr `sys.argv[1]`

```py
import sys

with open(sys.argv[1]) as cisla:
    cisla = [int(c) for c in cisla]

print(f'Součet zadaných čísel: {sum(cisla)}')
```

Program je potřeba volat se zadaným parametrem příkazové řádky

```
python soucet.py cisla.txt
Součet zadaných čísel: 169
```
