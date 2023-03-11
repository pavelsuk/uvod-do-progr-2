# Vytvoř program v Pythonu, který vyřeší následující problém: v souboru words.txt
# je vždy jedno slovo na řádku. Je potřeba jej zpracovat a vytvořit výstupní
# soubor ve formátu JSON obsahující slovník. Klíče budou písmena a hodnoty
# seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná
# slova nezačínají, tak ve výstupu toto písmeno nebude. Seznamy slov musí být
# seřezeny podle abecedy. I klíče ve výstupním JSON souboru musí být seřazeny a
# data odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

import json

# otevřít vstupní soubor a načíst slova do seznamu
with open('words.txt', 'r') as f:
    words = [line.strip() for line in f]

# vytvořit prázdný slovník
word_dict = {}

# projít slova a přidat je do slovníku podle prvního písmena
for word in words:
    first_letter = word[0]
    if first_letter not in word_dict:
        word_dict[first_letter] = []
    word_dict[first_letter].append(word)

# seřadit seznamy slov podle abecedy
for key in word_dict:
    word_dict[key].sort()

# vytvořit výstupní soubor ve formátu JSON
with open('output.json', 'w') as f:
    # seřadit klíče podle abecedy
    sorted_keys = sorted(word_dict.keys())
    # vytvořit slovník s seřazenými klíči a seznamy slov
    sorted_word_dict = {key: word_dict[key] for key in sorted_keys}
    # zapsat do souboru jako JSON s odsazením
    json.dump(sorted_word_dict, f, indent=4)


# Program nejprve načte slova ze vstupního souboru a uloží je do seznamu words.
# Poté vytvoří prázdný slovník word_dict. V cyklu prochází každé slovo v seznamu
# words a přidá ho do slovníku pod klíčem, který odpovídá prvnímu písmenu slova.
# Pokud klíč v slovníku ještě neexistuje, nejprve ho vytvoří s prázdným seznamem
# slov. Nakonec se seznamy slov seřadí podle abecedy.
#
# Poté program vytvoří výstupní soubor output.json a zapíše do něj slovník
# word_dict jako JSON s odsazením pomocí metody json.dump(). Nejdříve se vytvoří
# seznam seřazených klíčů a poté se vytvoří slovník s seřazenými klíči a seznamy
# slov.
#
# Doufám, že vám to pomůže!
