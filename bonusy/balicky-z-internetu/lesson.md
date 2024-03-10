## Balíčky z internetu

Internet nabízí obrovské množství frameworků, balíčků a knihoven, které si můžeme přidat do našeho programu, a které výrazně rozšíří možnosti našeho programu a ušetří nám spoustu práce. Řadu z nich můžeme jednoduše nainstalovat pomocí aplikace `pip`. Přehled nejoblíbenějších balíčků pro Python najdete v různých článcích, stačí například do vyhledávače zadat dotaz "the most popular python packages".

Použití nějakého balíčku v projektu je dobré si rozmyslet. Zde jsou nějaké kritéria, které je dobré vzít v úvahu:

- Popularita a velikost komunity: Obecně platí, že čím je balíček populárnější, tím více různých materiálů (např. blogové články, videa) k němu bude. Pokud narazíte na nějaký problém, s velikostí komunity roste pravděpodobnost, že stejný problém už řešil někdo před vámi a řešení je k dispozici na internetu.
- Dokumentace: Oficiální dokumentace může být cenným zdrojem informací, protože v ní autoři balíčku vysvětlují, jak ho správně používat.
- Aktivní vývoj balíčků: U balíčků, které nejsou aktivně vyvíjeny, hrozí, že přestanou být (nebo možná už nejsou) kompatibilní s novými verzemi Pythonu nebo jinými balíčky. Proto je dobré zkontrolovat datum vydání poslední verze.
- Licence: Některé balíčky mohou být omezeny pro nekomerční užití, placené atd.

Existují i další kritéria (např. pokrytí automatickými testy, potenciální zranitelnost kód, výkon atd.).

### Příklad balíčku

V úvodním kurzu jsme vytvářeli program pro směnárnu. Nevýhodou ale bylo, že jsme museli zadávat kurz ručně. Vyzkoušíme, jestli by bylo možné získat kurz přímo z internetu automaticky. Program by si pak vždy stáhl nový kurz z internetu a odpadly by nám starosti s aktualizací.

Podívejme se, jestli existuje něco, co by nám mohlo pomoci. Zadejme do vyhledávače výraz `python exchange rate`. Mezi prvními výrazy bude pravděpodobně balíček `forex-python`, která čerpá kurzy z kurzu s měnami Forex. Stránka balíčku přímo pro `pip` jde [zde](https://pypi.org/project/forex-python/). Na tomto webu najdeme obvykle základní informace o balíčku (co umí, nějaké příklad jeho použití atd.). Dále zde můžeme najít nějaké základní statistiky. Pokud je zdrojový kód uložený na GitHubu, vidíme počet hvěd (počet lidí, kteří dali balíčku hvězdu, jde o měřítko velikosti komunity), počet forků (počet lidí, kteří si vytvořili kopii repozitáře, například za účelem návrhu úprav, opět vypovídá o velikosti komunity) datum vydání poslední verze, licenci atd. Zdrojový kód balíčku `forex-python` můžete najít na [GitHubu](https://github.com/MicroPyramid/forex-python). Ten už obsahuje nějaké příklady, jak balíček použít. Dále si můžeme otevřít i dokumentaci programu, která je [zde](https://forex-python.readthedocs.io/en/latest/usage.html). Je trochu podrobnější než text na GitHubu.

### Instalace balíčku

Nyní můžeme nainstalovat knihovnu `forex-python`.

V návodu vidíme příkaz k instalaci:

```
pip install forex-python
```

Na MacOS nebo Linuxu využijeme příkaz

```
pip3 install forex-python
```

Zkusme si nyní otevřít terminál a vyzkoušet základní příkazy, které balíček umí. Nejprve vytvoříme objekt třídy `CurrencyRates`.

```py
from forex_python.converter import CurrencyRates

c = CurrencyRates()
```

Zkusme si vypsat kurzy české koruny.

```py
print(c.get_rates('CZK'))  
```

Výstup bude následovný:

```
{'EUR': 0.03927729772191673, 'USD': 0.042293794186959936, 'JPY': 6.35820895522388, 'BGN': 0.07681853888452474, 'DKK': 0.29279654359780044, 'GBP': 0.033623330714846814, 'HUF': 15.283974862529456, 'PLN': 0.1704634721131186, 'RON': 0.19548703849175175, 'SEK': 0.4424783974862529, 'CHF': 0.03727808326787117, 'ISK': 5.856245090337785, 'NOK': 0.4460133542812254, 'TRY': 1.3038138256087979, 'AUD': 0.06487431264728986, 'BRL': 0.21033385703063628, 'CAD': 0.057022780832678706, 'CNY': 0.3042458758837392, 'HKD': 0.3308562450903378, 'IDR': 661.3267871170464, 'INR': 3.5106637863315004, 'KRW': 56.366457187745475, 'MXN': 0.720879811468971, 'MYR': 0.20218381775333855, 'NZD': 0.06931657501963864, 'PHP': 2.3667714061272584, 'SGD': 0.05695208169677926, 'THB': 1.5250981932443048, 'ZAR': 0.7988020424194815}
```

Formát výstupu nám napovídá, že kurzy jsou uložené ve slovníku, klíčem je zkratka měny a hodnotou je kurz. Hodnoty se vám asi zdají divné. Zkusme se zeptat [ChatGPT](https://chat.openai.com/share/d174d38e-b250-4672-ab51-423468fea95f) nebo [Bing Copilota](https://copilot.microsoft.com/sl/kCPCMRAaC9k).

Pokud bychom chtěli vyjádřit kurz koruny v zápisu, na kterém jsme zvyklí, musíme provést úpravu. Využijeme toho, že data jsou uložena ve slovníku, a použijeme cyklus a metodu `.items()`.

```py
from forex_python.converter import CurrencyRates

c = CurrencyRates()
rates = c.get_rates('CZK')
for key, value in rates.items():
    rate = 1 / value
    print(f"1 {key} = {round(rate, 2)}")
```

Se seznamem si můžeme dále hrát. Můžeme si například vypsat jen měny, se kterými naše malá směnárna obchoduje.

```py
currency_list = ["GBP", "EUR", "USD"]
for key, value in rates.items():
    if key in currency_list:
        rate = 1 / value
        print(f"1 {key} = {round(rate, 2)}")
```

## Cvičení

::exc[excs/faker]
