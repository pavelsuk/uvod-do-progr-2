## Stahování dat z internetu

V předchozím příkladu jsem naše data načetli ze souboru na disku. Pokud však narazíte na vstřícného poskytovatele dat, je možné si data stáhnout z takzvaného API (Application Programming Interface) přímo z internetu. Zkratka API se používá jako označení nějakého přípojného bodu na internetu, odkud si můžete stáhnout data v nějakém strojově čitelném formátu. Nejčastěji je tímto formátem právě JSON.

Malá potíž je ovšem v tom, že Python sám o sobě neobsahuje modul pro stahování dat z internetu. Musíme proto do našeho Pythonu doinstalovat takzvaný externí balíček.

## Externí moduly a balíčky

Python sám o sobě obsahuje mnoho užitečných modulů pro řešení různých typů úloh. Už jsme viděli modul `random` pro práci s náhodnými čísly, modul `statistics` pro základní statistické funkce nebo modul `sys` pro práci s operačním systémem. Všem modulům, které jsou součástí základní instalace Pythonu, se dohromady říká :term{cs="standardní knihovna" en="standard library"}. Přehled všech modulů, které standardní knihovna obsahuje můžete najít [v Python dokumentaci](https://docs.python.org/3/library/).

Čas od času ale v Pythonu potřebujeme vykonat nějakou činnost, pro kterou není ve standardní knihovně dostupný žádný modul, například stáhnou data z internetu. V takovém případě budeme muset z internetu stáhnout a nainstalovat takzvaný :term{cs="balíček" en="package"}.

Balíčky obsahují moduly, které po instalaci balíčku můžeme importovat v našem programu.

Ke stahování dat z internetu potřebujete balíček jménem `requests`. Nainstalujeme jej příkazem

```shell
pip3 install requests
```

Pozor, že ve Windows tento příkaz vypadá takto.

```shell
pip install requests
```

Může se stát, že výše uvedený příkaz nebude fungovat protože nemáte nainstalovaný správce balíčků `pip`. V takovém případě vyzkoušejte následující příkaz:

```shell
python -m pip install requests
```

## Stahování dat z API

Jeden ze cvičných zdrojů dat najdeme na adrese `https://api.kodim.cz/python-data/people`. Knihovna `requests` ve svém objektu `response` obsahuje rovnou metodu pro převod získaných dat z JSON formátu.

```py
import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
print(data)
```

## Cvičení: API a JSON
::exc[excs>seznam-lidi]
::exc[excs>svatky]


### Čekání na odpověď

Naše get requesty se mohou po cestě internetem k serveru ztratit. Aby náš program nečekal na odpověď donekonečna, v produkčním kódu vždy uplatňujme parametr [timeout](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts), určující kolik sekund se má čekat na odpověď.
