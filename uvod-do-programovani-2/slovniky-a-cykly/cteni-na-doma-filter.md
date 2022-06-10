## Čtení na doma - funkce `filter`

K výběru určitých hodnot ze slovníku můžeme použít i funkci `filter()`. Tato funkce je zpravidla používána s tzv. anonymní funkcí, tj. funkcí, která nemá žádné jméno. Je to z důvodu, že funkce je použita pouze na tomto místě a nepotřebujete tedy jméno, aby byla volána. Anonymním funkcím se často říká i *lambda* funkce, protože se k jejich definici používá klíčové slovo `lambda`.

Níže je příklad, jak použít funkci `filter()` k výběru knih, které vyšly v roce 2019.

```py
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

books_2019 = list(filter(lambda item: item["year"] == 2019, books))
print(books_2019)
```
