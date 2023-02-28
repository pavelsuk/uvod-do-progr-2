## Formát JSON

JSON je formát pomocí kterého můžeme zapsat strukturovaná data jako čistý text. S jedním takovým datovým formátem jste se již potkali, jmenuje se CSV.

JSON formát původně pochází z jazyka, který se jmenuje JavaScript. Ten se hodně používá pro tvorbu webových stránek a jelikož výměna dat nejčastěji probíhá po internetu, ujal se formát JSON všeobecně jako standard pro výměnu dat mezi programy. Výhoda pro nás je, že JSON vypadá téměř stejně jako Python slovníky. Liší se pouze tím, že vždy používá dvojité uvozovky a hodnoty `True` a `False` se píší s malým písmenem, tedy `true` a `false`. Náš absolvent kurzu z úvody lekce by tedy ve formátu JSON vypadal takto:

```json
{
    "jmeno": "Petr",
    "prijmeni": "Roman",
    "rok": 2017,
    "dochazka": 0.95,
    "vyznamenani": true
}
```

### Čtení JSON dat

V Pythonu je velice jednoduché převést JSON na obyčejný Python slovník. Stačí nám k tomu modul jménem `json`. Vyzkoušíme si to na našem seznamu absolventů. Nejdřív si tato data stáhneme jako soubor [absolventi.json](assets/absolventi.json). Ten pak můžeme v Pythonu otevřít a převést na JSON následujícím programem.

```py
import json
with open('absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)
print(absolvents)
```

### Zápis JSON dat

Zápis JSON dat do souboru je podobně jednoduché jako čtení. Stačí si osvojit funkci `dump`. Dejme tomu, že máme jednoduchý JSON, který obsahuje například odpracované hodiny pro každý den v týdnu. Ten chceme zapsat do textového souboru.

```py
import json
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file)
```

#### Diakritika v JSON

Funkce `json.dump()` ve výchozím nastavení překóduje non-ASCI znaky do jejich číselného kódu:

```py
import json
data = {"řeřicha": "Česká Třebová"}

with open("rericha.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file)  # soubor obsahuje {"\u0159e\u0159icha": "\u010cesk\u00e1 T\u0159ebov\u00e1"}
```

Pokud chceš mít výstupní JSON v plném kódování UTF-8, lze toho dosáhnout volitelným parametrem `ensure_ascii=False`.


## Složitější JSON struktury

JSON podporuje vzájemné zanořování slovníků a seznamů, a tím podporuje široké možnosti pro reprezentaci hierarchických dat. Takto bychom mohli reprezentovat například kurz Czechitas jménem Úvod do programování.

```json
{
    "nazev": "Úvod do programování",
    "lektor": "Martin Podloucký",
    "konani": [
        {
            "misto": "T-Mobile",
            "koucove": [
                "Dan Vrátil",
                "Filip Kopecký",
                "Martina Nemčoková"
            ],
            "ucastnic": 30
        },
        {
            "misto": "MSD IT",
            "koucove": [
                "Dan Vrátil",
                "Zuzana Tučková",
                "Martina Nemčoková"
            ],
            "ucastnic": 25
        },
        {
            "misto": "Škoda DigiLab",
            "koucove": [
                "Dan Vrátil",
                "Filip Kopecký",
                "Kateřina Kalášková"
            ],
            "ucastnic": 41
        }
    ]
}
```

Všimněte si, jak obsah JSON souboru představující jeden kurz, obsahuje pod klíčem `konani` seznam dalších slovníků. Každý z nich reprezentuje jedno konání kurzu a dále obsahuje například seznam koučů atd.


## Cvičení: JSON
::exc[excs>kurz]
