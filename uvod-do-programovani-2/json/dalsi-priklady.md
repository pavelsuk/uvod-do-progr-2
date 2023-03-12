## Čtení na doma - další příklady JSON souborů

Podívejme se na ještě jeden příklad zápisu dat. Data reprezentují informace o konání kurzu Úvod do programování.

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

Všimni si, jak obsah JSON souboru představující jeden kurz, obsahuje pod klíčem `konani` seznam dalších slovníků. Každý z nich reprezentuje jedno konání kurzu a dále obsahuje například seznam koučů atd.

## Cvičení: JSON
::exc[excs>kurz]
