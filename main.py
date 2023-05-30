# чисто рофлоштука чтобы делать Вот такОй текСт потОмУ Что Мне самОму ленЬ


import random
import colorama


def maker(word):
    if len(word) == 1:
        return word

    start = 0

    if len(word) <= 3:
        symbol = random.randint(0, len(word) - 1)

        return word[:symbol] + word[symbol].capitalize() + word[symbol + 1 :]

    symbols = []

    while start < len(word):
        start_now = random.randint(2, 3)

        start += start_now

        symbols.append(start)

    symbols += [-1]

    pointer = 0
    result = ""

    for i in range(len(word)):
        if i == symbols[pointer]:
            result += word[i].capitalize()
            pointer += 1
        else:
            result += word[i]

    return result


print(
    colorama.Fore.RED
    + " ".join(list(map(maker, input().split())))
    + colorama.Style.RESET_ALL
)
