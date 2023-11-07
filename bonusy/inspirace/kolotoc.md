## Kolotoč

Naprogramuj simulaci televizní soutěže [Kolotoč](https://cs.wikipedia.org/wiki/Koloto%C4%8D_(sout%C4%9B%C5%BE)).

### Průběh hry

Vybraný řetězec je před uživatelem zamaskován (např. emoji symboly místo písmen) - vytisknuty jsou jen mezery a interpunkce. Uživatel hádá písmeno. Uhodnuté písmeno je odkryto ve všech jeho výskytech v textu. Nebude záležet na velikosti písmen (vše velkým, odpověď uživatele převést na velké).

#### Možná ukázka průběhu hry

```shell
python kolotoc.py prislovi.txt
▮▮▮▮▮ ▮▮▮▮▮, ▮▮▮ ▮▮▮▮▮▮ ▮▮▮▮. Hádej znak: a
▮▮▮▮A ▮▮▮▮▮, ▮▮▮ ▮▮▮▮▮▮ ▮▮▮▮. Hádej znak: e
▮▮▮▮A ▮▮▮▮▮, ▮▮E ▮▮▮▮▮▮ ▮E▮▮. Hádej znak: i
▮▮▮▮A ▮▮▮▮▮, ▮▮E ▮▮▮▮▮▮ ▮E▮▮. Znak 'I' tam není. Hádej znak: o
▮▮O▮A ▮▮▮▮▮, ▮▮E ▮O▮▮▮▮ ▮E▮▮. Hádej znak: k
▮KO▮A K▮▮▮▮, K▮E ▮O▮▮▮▮ ▮E▮▮. Hádej znak: d
▮KODA K▮▮▮▮, KDE ▮O▮▮▮▮ ▮E▮▮. Hádej znak: š
ŠKODA K▮▮▮▮, KDE ▮O▮▮▮▮ ▮E▮▮. Hádej znak: n
ŠKODA K▮▮▮▮, KDE ▮O▮▮▮▮ NEN▮. Hádej znak: í
ŠKODA K▮▮▮▮, KDE ▮O▮▮▮▮ NENÍ. Hádej znak: t
ŠKODA K▮▮▮▮, KDE ▮O▮▮▮▮ NENÍ. Znak 'T' tam není. Hádej znak: r
ŠKODA KR▮▮▮, KDE RO▮▮▮▮ NENÍ. Hádej znak: z
ŠKODA KR▮▮▮, KDE ROZ▮▮▮ NENÍ. Hádej znak: u
ŠKODA KR▮▮▮, KDE ROZU▮U NENÍ. Hádej znak: m
ŠKODA KR▮▮▮, KDE ROZUMU NENÍ. Hádej znak: á
ŠKODA KRÁ▮▮, KDE ROZUMU NENÍ. Hádej znak: č
ŠKODA KRÁ▮▮, KDE ROZUMU NENÍ. Znak 'Č' tam není. Hádej znak: s
ŠKODA KRÁS▮, KDE ROZUMU NENÍ. Hádej znak: y
=============================
ŠKODA KRÁSY, KDE ROZUMU NENÍ.
=============================
Chybných pokusů: 3
```

### Zdroj textu

[Česká přísloví](https://cs.wikiquote.org/wiki/Česká_přísloví) uložená v `txt` souboru [prislovi.txt](assets/prislovi.txt) - náhodně vybraný řádek.
