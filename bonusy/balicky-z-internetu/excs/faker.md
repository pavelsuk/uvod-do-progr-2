---
title: Padělač
demand: 2
---

Vyzkoušej si práci s balíčkem `Faker` (česky "Padělač"). Balíček slouží ke generování náhodných údajů, například umí generovat jména, adresy, názvy firem a další. Balíček se dá využít například k vytváření dat pro ukázkovou nebo tréninkovou verzi aplikace, generování dat pro testování, anonymizaci dat, tvorbu simulací a počítačových her a další.

Otevři si stránku balíčku v na webu [pypi.org](https://pypi.org/project/Faker/). S pomocí této stránky si modul nainstaluj. Na stránce dále najdeš ukázky kódu. Zkus si první ukázku zkopírovat do svého programu a spustit. Pozor na to, že pro zobrazení výstupů je vždy nutné použít funkci `print()`, program je tedy potřeba upravit do podoby níže..

```py
from faker import Faker
fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())
```

Dále se podívej na druhou ukázku. Ta vygeneruje a vypíše 10 jmen.

```py
for _ in range(10):
  print(fake.name())
```

Pro nás program by se ale spíše hodila česká jména. Zkus si otevřít [část o lokalizaci na GitHubu](https://faker.readthedocs.io/en/stable/#localization). Všimni si, že při vytváření objektu `fake` z třídy `Faker` je použit parametr `"it_IT"`, který udává, pro jaký jazyk a "lokálního nastavení" mají být data generována. Namísto italských bychom preferovali česká. Podívej se na [stránku o českém lokálním nastavení](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html). Jaký je kód nastavení pro češtinu? Formát názvu je stejný jako pro italštinu, tj. řetezec složený ze dvou malých písmen, podtržítka a dvou velkých písmen. Určitě ho najdeš rychle, je přímo v nadpisu stránky.

Zkusme se nyní podívat na to, co přesně česká lokalizace "padělače" umí. Uvažujme například, že generujeme tréninkovou verzi aplikace pro správu kurzů Czechitas. Standardní metoda `.name()`, která náhodně generuje mužská i ženská jména, není úplně to pravé. Podívej se na metodu, která [generuje pouze ženská jména](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html#faker.providers.person.cs_CZ.Provider.name_female) a vyzkoušej ji ve svém programu. Nakonec zkus vygenerovat i nějaké [adresy](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html#faker.providers.address.cs_CZ.Provider.address).
