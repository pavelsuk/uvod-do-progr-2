## Coding style

Programovací jazyk Python byl od začátku navržen s ohledem na snadné čtení a pochopení programu napsaného někým jiným. Například odsazování bloků kódu je vynucenou součástí jazyka. Jiné programovací jazyky v tomto striktní nejsou. V zápise kódu se však mezery na různých místech mohou nebo nemusí psát.

Pro začátek si ukážeme, kde se píší a nepíší mezery.

::fig[Kde psát mezery]{src=assets/psat_mezery.png}

::fig[Kde nepsat mezery]{src=assets/nepsat_mezery.png}

Dodržování stylu kódu v Pythonu, jak je definováno v [PEP 8](https://peps.python.org/pep-0008) (Python Enhancement Proposal 8), je klíčové pro zlepšení čitelnosti, udržovatelnosti a spolupráce ve vývojářských projektech. PEP 8 poskytuje doporučené standardy a konvence pro formátování kódu, čímž usnadňuje tvorbu kvalitního a efektivního kódu a přispívá k jednotnému vzhledu pythonových projektů.

Dokud se sami nepropracujeme ke zcela podvědomému psaní kódu podle PEP 8, je vhodné využít pomoc automatizovaných nástrojů.

Kromě různých vestavěných funkcionalit IDE jako např. PyCharm je asi nejjednodušší použít v příkazová řádce program `autopep8`, který přeformátovaný kód vypíše a nedělá v základním nastavení příliš agresivní změny (zalamování dlouhých řádku atd.). Alternativou může být nástroj `black`. [autopep8](https://pypi.org/project/autopep8) si nainstalujeme v příkazové řádce pomocí

```shell
pip install autopep8
```

Pro zobrazení změn, které v kódu nastaly, se dá použít vestavěný _diff_ ve VS Code. `autopep8 -i` pak udělá změny in-place (přepíše náš skript).
