## Počet útočníků v Pandas

Počet útočníků můžeme spočítat i pomocí modulu `pandas`. Zkusme nejprve využít pouze sloupec `attacker_1`. V takovém případě lze aplikovat pouze agregaci typu `count()` nebo `size()`.

```py
import pandas

data = pandas.read_csv("battles.tsv", sep="\t")
data = data.groupby("attacker_1").size()
print(data)
```

My ale potřebujeme započítat i útočníky z dalších sloupců. Jak na to? Můžeme například postupovat tak, že ze všech čtyř sloupců (sérií) uděláme jeden dlouhý sloupec (sérii), který poté agregujeme. Jedná se o operaci spojení (v `pandas` označovaná jako `concat`, v SQL `UNION`), tj. vložení jednotlivých sérií pod sebe. Můžeme využít funkci `concat()`, která umí spojit série úplně stejně jako tabulky.

```py
data = pandas.concat([data["attacker_1"], data["attacker_2"], data["attacker_3"], data["attacker_4"]])
```

Jak ale nyní provést agregaci? Metoda `groupby()` se nám nyní příliš nehodí. Sice je možné ji [použít i pro sérii](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html), ale používá se spíše ve spojení s indexem. Zkusme si tedy odpověď vyhledat.

Můžeme začít využitím vyhledávače, například Google. Na začátku musíme dobře strukturovat dotaz, abychom se nedostali k řešení jiných (byť podobných) problémů. V našem dotazu bychom měli mít zmíněné následující důležité věci:

- Výraz `pandas`. Počet hodnot ve sloupci (v sérii) je problém řešený ve spoustě prostředí, ale nás aktuálně zajímá právě `pandas`.
- Co chceme udělat. Potřebujeme zjistit počet (anglicky *count*) hodnot (anglicky *values*). Dále je důležité uvést, že to provádíme pro sloupec (anglicky *column*) nebo sérii (anglicky *series*), jinak bychom se pravděpodobně dostali k návodu pro tabuku.

Google běžně zobrazuje různé výsledky pro různé uživatele a též v závislosti na tom, zda použijeme slovo *column* nebo *series*. V rámci výsledků se ale pravděpodobně zobrazí následující odkazy:

- [Oficiální dokumentace](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html) k metodě `value_counts`.
- Návod na [webu w3resource](https://www.w3resource.com/pandas/series/series-value_counts.php#:~:text=The%20value_counts()%20function%20is,Excludes%20NA%20values%20by%20default.).
- Článek Pandas Count Occurrences in Column – i.e. Unique Values na webu [marsja.se](https://www.marsja.se/pandas-count-occurrences-in-column-unique-values/).

Tyto weby zmiňují právě využití metody `value_counts`. Všechny z nich (včetně dokumentace) ukazují na jednoduchých datech, jak metodu použít a jaké jsou výsledky.

Další možností je použití chatovacího bota ChatGPT. Jeho určitou výhodou je, že s námi umí komunikovat v češtině. Nevýhodou je, že výsledky jsou často velmi nespolehlivé, protože se jedná o aplikaci, která je stále v počátečních fázích vývoje. 

Zkusme položit dotaz: "Používám modul pandas a mám data uložená v sérii. Jak můžu spočítat, kolikrát se tam každá hodnota vyskytuje?" Výsledek je vidět na obrázcích níže. ChatGPT nám nejprve doporučí použití metody `value_counts()`, což je stejná metoda, kterou nám doporučují i výsledky ve vyhledávači. Zdá se tedy, že jdeme správným směrem. Dále pro nás ChatGPT vytvořil ukázkový kód.

::fig[Odpověď chatovacího bota 1]{src=assets/chat_gpt_1}

A nakonec zobrazí i výsledky, které ukázkový kód vypíše.

::fig[Odpověď chatovacího bota 1]{src=assets/chat_gpt_2}

Oba zdroje nás tedy navedkou k tomu, že použití metody `value_counts()` je velmi jednoduché, stačí pouze napsat

```py
data = data.value_counts()
print(data)
```

Vidíme tedy, že nejútočnějším rodem je rod Lannisterů (což nás jistě moc nepřekvapí).
