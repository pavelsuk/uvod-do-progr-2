seznam = [49, 38, 18, 82, 85, 60, 94, 21, 20, 14, 37,
          80, 13, 66, 41, 68, 82, 88, 41, 52, 28, 35, 55]

delka = 5


# minimalistická varianta:
start = 0
while vysek := seznam[start:start + delka]:
    print(vysek)
    start += delka


print()


# běžná varianta:
start = 0
konec = delka

while True:
    vysek = seznam[start:konec]
    if not vysek:
        break
    print(vysek)
    start += delka
    konec += delka


print()


# běžná varianta 2:
start = 0
konec = delka

vysek = seznam[start:konec]
while vysek:
    print(vysek)
    start += delka
    konec += delka
    vysek = seznam[start:konec]
