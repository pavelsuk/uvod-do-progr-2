## Úvod

Seznamy jsou velmi užitečná datová struktura, protože umožňují ukládat spoustu dat do jedné proměnné. Pokud do nich ale ukládáme informace různého typu, může brzy vzniknout chaos. Podívejme se třeba seznam, který obsahuje informace o položce v e-shopu.

```py
["Čajová konvička s hrnky", 899, True]
```

Dokázali bychom asi odhadnout, že první prvek je název a druhý cena. Co však znamená `True`? To za seznamu na první pohled patrné není. Samozřejmě by bylo možné tu informaci někam poznamenat, ale možná by stálo za to mít tu informaci přímo v sekvenci.

A přesně toto řeší datový typ slovník (`dict`).
