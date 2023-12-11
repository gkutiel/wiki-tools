from typing import Generator, List

letters = set('אבגדהוזחטיכלמנסעפצקרשת')


def find_wordle_move(words: set[str], k: int) -> Generator[list[str], None, None]:
    if k == 0:
        yield []

    if len(words) == 0:
        raise ValueError("Dictionary is empty")

    for w in words:
        try:
            for ws in find_wordle_move(filter_words(words, w), k - 1):
                yield [w] + ws

        except ValueError:
            pass


def filter_words(words, w):
    # print(words, w)
    words = filter(lambda x: len(set(x) & set(w)) == 0, words)
    words = set(words)
    # print(words)
    return words


def norm(w: str):
    trans = str.maketrans('ךםןףץ', 'כמנפצ')
    return w.translate(trans)


def uncovered_letters(words: List[str]):
    return letters - set.union(*map(set, words))


if __name__ == "__main__":

    with open('/home/gilad/Work/vardale/wws/words.txt') as f:
        words = f.read().splitlines()
        words = [norm(w) for w in words]
        words = [w for w in words if len(set(w)) == 5]
        words = set(words)

    sols = list(find_wordle_move(words, 4))
    sols = [sorted(s) for s in sols]
    sols = set(tuple(s) for s in sols)
    for s in sols:
        print()
        print(*s, sep='\n')
        print(uncovered_letters(s))
        print()
