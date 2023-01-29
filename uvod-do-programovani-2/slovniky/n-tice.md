## N-tice

Kromě seznamů si povíme o dalších možnostech, jak uložit více hodnot naráz. Datový typ velmi podobný seznamu je <term cs="n-tice" en="tuple">. Představme si ji jako dvojici, trojici, čtveřici apod. nějakých hodnot. Hlavní rozdíly oproti seznamu jsou ty, že není možné měnit prvek na určitém indexu n-tice a není možné žádný prvek přidávat nebo mazat.

N-tici vytvoříme prostou posloupností prvků oddělených čárkou bez hranatých závorek.

```py
cookies_count = [1, 2, 4, 1, 6, 0, 1]
print(type(cookies_count))

cookies_count = 1, 2, 4, 1, 6, 0, 1
print(type(cookies_count))
```

```
<class 'list'>
<class 'tuple'>
```

Určitě se ptáte, k čemu jsou n-tice dobré, když neumí ani to, co seznamy a nic navíc? Hlavní důvod je určitý výkonností rozdíl oproti seznamům a jejich integrace do jazyka Python, která nabízí výbornou čitelnost kódu. V následující ukázce si rozbalíme seznam nebo n-tici do tří samostatných proměnných:

```py
item = "Čajová konvička s hrnky", 899, True

title, price, in_stock = item

print(title)
print(price)
print(in_stock)
```

```shell
Čajová konvička s hrnky
899
True
```

Nemusíte se existencí n-tic příliš trápit. Hlavní důvod, proč si je zmiňujeme, je vědět, že vůbec existují. Pokud ve vašem kódu někdy budete chtít vytvořit `list`, ale zapomenete hranaté závorky, Python vám vytvoří n-tici a na problém vás upozorní až při pokusu o zápis do této datové struktury.
