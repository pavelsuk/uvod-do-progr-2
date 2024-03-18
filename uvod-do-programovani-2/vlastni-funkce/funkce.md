## Funkce

Funkce nám umožňují program strukturovat do bloků a využívat stejný kód na více místech, aniž bychom ho museli kopírovat. Funkcí již jsme poznali několik (např. `round`, `int`, `len`, `print`, `input`), zatím jsme ale žádnou vlastní funkci nevytvořili. Vytváření funkcí se naučíme v této části.

K definici funkce používáme klíčové slovo `def`. Dále následuje **název funkce** a její **parametry** (`parameter`) v kulatých závorkách. Pojem parametr funkce už také známe, pomocí parametrů předáváme funkci hodnoty ke zpracování. Například funkci `print` předáváme řetězec, která má vypsat na obrazovku.

Po názvu funkce následuje **dvojtečka** `:`, která napovídá, že kód pod dvojtečkou bude **odsazený**. Kód funkce končí tam, kde již kód není odsazený.

**Poznámka:** Je zde též trochu zrádná terminologie. Při definici funkce definujeme její parametry, ale při volání funkce zapisujeme do závorek argumenty (`arguments`).

Začněme s jednoduchou funkcí, která pouze vypíše text na obrazovku.

```py
def greet_user():
    print("Ahoj!")
```

Pokud tento kód zkopírujeme do programu, zdánlivě se nic nestane. Funkce je sice vytvořena, ale nevoláme ji.

```py
def greet_user():
    print("Ahoj!")


greet_user()
```

Nyní již program náš pozdrav vypíše.

Všimni si ještě dvou dvou věcí:

- Volání funkce je až **pod její definicí**. Pokud bychom pořadí obrátili, Python vrátí chybu, protože by v čase volání funkci ještě neznal.
- Za **voláním** funkce musíme vždy uvést **kulaté závorky**. Pokud nepředáváme žádnou hodnotu, zůstanou závorky prázdné.

Upravme naši funkci tak, aby vypsala oslovení, které jí zadáme:

```py
def greet_user(name):
    print(f"Ahoj {name}!")


greet_user("Jirko")
```

Naše funkce zatím provedly nějakou akci, ale nevrátily nám žádný **výstup**. Často nám funkce vracejí nějakou hodnotu. Hodnotu, kterou má funkce vrátit, označíme klíčovým slovem `return`. Zkusme si tedy vytvořit funkci, která vrací součet dvou čísel.

```py
def sum_two_numbers(a, b):
    return a + b
```

Výstup funkce můžeme uložit do proměnné.

```py
returned_value = sum_two_numbers(5, 3)
print(returned_value)
```

V proměnné `returned_value` tedy budeme mít uložený výsledek našeho součtu a s ním můžeme dále pracovat.

**Poznámka:** Jakmile program narazí na slovo `return`, běh funkce se ukončí. Například funkce níže žádný výpis neprovede.

```py
def sum_two_numbers(a, b):
    return a + b
    print(a + b)
```

:::box{type=tip}
Doporučená struktura skriptu:

1. hlavička - komentář co skript dělá a kdo je autorem
2. importy
3. definice funkcí
4. hlavní kód, ze kterého se funkce volají
:::

### Čistá funkce

Níže definovaná funkce je bez tzv. :term{cs="vedlejších efektů" en="side effect"}, tj. používá pouze své parametry a nepoužívá žádné proměnné definované mimo ni (např. vstup od uživatele). Stejně tak mimo návratové hodnoty nijak neovlivňuje běh programu. Funkci bez vedlejších efektů se říká :term{cs="čistá funkce" en="pure function"}. Její výhodou je, že pro stejný vstup vždy vrací stejný výstup, což například usnadňuje testování nebo hledání chyby.

```py
def sum_two_numbers(a, b):
    return a + b
```

Níže uvedená funkce není čistá, protože čte tzv. globální proměnnou "zvenku". Může tedy v různých situacích vracet různé výsledky podle hodnoty uložené v té globální proměnné.

```py
exchange_rate = 26


def convert_to_euro(crown):
    return crown * exchange_rate
```

Takto uvedená funkce je již čistou funkcí.

```py
def convert_to_euro(crown, exchange_rate):
    return crown * exchange_rate
```

### Funkce bez kódu

Pokud si při návrhu programu uvědomíte, že je nějaká funkce potřeba, ale zatím nemáte čas naprogramovat ji, můžete funkci deklarovat a do jejího těla napsat klíčové slovo `pass`. Tento příkaz nic nevykoná, ale díky ní máte splněnou podmínku, že funkce musí mít alespoň jeden řádek.

```py
def code_me_later(par1, par2):
    pass
```
