## Klíčové slovo assert

Klíčové slovo `assert` v Pythonu se používá k ověření, zda je daný výraz pravdivý. Pokud je výraz nepravdivý, vyvolá výjimku `AssertionError`. Tento mechanismus je užitečný pro debugování a ověřování, že se kód chová tak, jak má, během vývoje. 

Vraťme se k funkci `sum_two_numbers`, která přijímá dva argumenty `a` a `b` a vrací jejich součet:

```python
def sum_two_numbers(a, b):
    return a + b
```

Pokud chceme ověřit, že tato funkce správně vrací součet dvou čísel, můžeme použít `assert` k testování této funkcionality. Například:

```python
value = sum_two_numbers(2, 3)
assert value == 5, "Sum of 2 a 3 should be 5"
```

Tento příkaz `assert` ověří, že hodnota uložená v proměnné `value`, kterou jsme získali voláním funkce `sum_two_numbers()` s hodnotami 2 a 3, je skutečně 5. Pokud ano, program pokračuje bez přerušení. Pokud ne, Python vyvolá `AssertionError` s uvedenou chybovou zprávou `"Sum of 2 a 3 should be 5"`.

Klíčové slovo `assert` je jedním ze způsobů, jak otestovat funkci. Pro funkci máme nějaký testovací vstup a očekávaný výstup. Pokud funkce vrátí jinou než očekávanou hodnotu, znamená to, že je ve funkci nějaká chyba. Pozor ale na to, že jeden správný výstup funkce nemusí nutně znamenat, že je vše naprosto v pořádku. Uvažujme například, že jsme ve funkci udělali chybu a použili špatný operátor.

```python
def sum_two_numbers(a, b):
    return a * b
```

U hodnot 2 a 2 tato funkce "projde", ale jde čistě o náhodu - pro čísla 2 a 2 je výsledek sčítání i násobení stejný. Je proto dobré při testování využít více různých testovacích vstupů a výstupů.

```python
value = sum_two_numbers(2, 2)
assert value == 5, "Sum of 2 a 2 should be 2"
```