import random
import re
import sys

from typing import List

HIDDEN_CHAR = '▮'


def update_text(hidden_text: List[str], matches: List[int], guess: str) -> str:
    for m in matches:
        hidden_text[m] = guess

    return ''.join(hidden_text)


if __name__ == '__main__':
    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            texts = f.readlines()
    except (IndexError, FileNotFoundError):
        sys.exit(f'Usage: {sys.argv[0]} <input_file>')

    orig_text = random.choice(texts).strip().upper()
    hidden_text = re.sub(r'\w', HIDDEN_CHAR, orig_text)

    fails = 0
    error_msg = ''
    while hidden_text != orig_text:
        try:
            guess = input(f'{hidden_text} {error_msg}Hádej znak: ').upper()
        except KeyboardInterrupt:
            print('\nUkončuji hru')
            sys.exit(0)

        error_msg = ''

        matches = [i for i, ch in enumerate(orig_text) if ch == guess]
        if matches:
            hidden_text = update_text(list(hidden_text), matches, guess)
        else:
            error_msg = f"Znak '{guess}' tam není. "
            fails += 1

    line = len(hidden_text) * '='
    print(line)
    print(hidden_text)
    print(line)
    print(f'Chybných pokusů: {fails}')
