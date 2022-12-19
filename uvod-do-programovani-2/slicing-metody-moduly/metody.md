## Metody

V minulé lekci jsme viděli takzvané funkce, které za nás vykonávají často
opakované činnosti jako například zaokrouhlování, zjišťování délky seznamu
apod. Některé funkce se však hodí na práci pouze s jedním typem hodnoty.
Například bychom mohli mít funkci `upper()`, která by převedla všechna písmena
v řetězci na velká písmena. Kdyby taková funkce existovala, mohli bychom ji
volat třeba takto

```pycon
>>> upper('martin')
'MARTIN'
```

Je pochopitelné, že taková funkce funguje pouze pro řetězce. Pro ostatní
hodnoty nedává smysl. Těžko si představit, co by taková funkce měla vrátit
například v takovémto případě:

```pycon
>>> upper(3.14)
```

Funkce, které pracují pouze na jednom typu hodnoty, se programátoři Pythonu
rozhodli svázat přímo s touto hodnotu. Můžeme tedy říct, že funkce `upper()`
patří řetězcům. Pokud tedy máme nějaký řetězec, funkci, která patří pouze k
typu řetězec, zavoláme pomocí takzvané _tečkové notace_.

```pycon
>>> 'martin'.upper()
'MARTIN'
```

Funkcím, které patří jen konkrétním typům hodnot, říkáme _metody_. Všimněte
si, že metoda `upper()` pro řetězce v Pythonu skutečně existuje, takže výše
uvedený kód bude opravdu fungovat. Podobně existuje například metoda
`lower()`. Vyzkoušejte si ji.

### Užitečné metody na řetězcích

`strip()`
: Odstraní všechny bílé znaky na začátku a konci řetězce

```pycon
>>> '  martin   '.strip()
'martin'
```

`split(sep)`
: Rozseká řetězec na kousky podle zadaného oddělovače sep. Např.

```pycon
>>> 'po ut st čt pá'.split(' ')
['po', 'ut', 'st', 'čt', 'pá']
```

nebo

```pycon
>>> '3.12,4.1,9.6,-127,0'.split(',')
['3.12', '4.1', '9.6', '-127', '0']
>>> '3.12,4.1,9.6,-127,0'.split('.')
['3', '12,4', '1,9', '6,-127,0']
```

`join(list)`
: Spojí řetězce v seznamu list do jednoho velkého řetězce podle zadaného separátoru.

```pycon
>>> '+'.join(['1', '2', '3', '4'])
'1+2+3+4'
>>> '/'.join(['dokumenty', 'dapraha', 'python', 'priklady'])
'dokumenty/dapraha/python/priklady'
```

## Cvičení: Řetězce, metody
::exc[excs>prevod-pismen]
::exc[excs>cisla-jako-text]
::exc[excs>cisla-v-textu]

## Bonusy
::exc[excs>chytrejsi-cisla-jako-text]
