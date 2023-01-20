## Parametry příkazové řádky

Velmi důležitý modul, jenž si v tuto chvíli představíme, je modul `sys`. Ten obsahuje funkce, které umožňují Pythonu komunikovat s operačním systémem, ve kterém je spuštěný. Nás z tohoto modulu bude zajímat především proměnná (ano, moduly mohou obsahovat kromě funkcí také proměnné) s názvem `argv` Ta nám umožní přistupovat k takzvaným _parametrům příkazové řádky_.

Všechny programy, které jsme zatím společně vytvořili, obsahovaly všechna nezbytná data jaksi natvrdo přímo uvnitř kódu programu. Možná vás napadne, že například program, který má naměřené teploty z minulého týdne zadrátované přímo uvnitř kódu, nám je jen pramálo k užitku. Nemůžeme mu předat nově naměřené teploty jinak, než upravit jeho zdrojový kód. Do skutečně užitečného programu musíme být schopni dostat data jaksi z venku. K tomu máme vícero možností ‒ například nahrát data ze souboru na disku, což se naučíme v příští lekci, můžeme je stáhnout z internetu (také se časem naučíme), ale také je můžeme programu předat přímo na příkazové řádce, když jej spouštíme.

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

# Cvičení: Parametry příkazové řádky
::exc[excs>cas-v-minutach]
::exc[excs>uprava-retezce]
::exc[excs>hada-na-velblouda]
::exc[excs>hazeni-kostkou]

