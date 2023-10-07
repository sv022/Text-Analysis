from string import punctuation, ascii_letters
from math import log2, ceil

def showStats(text : str, showall=True):
    chars = countChars(text)
    symcount = symCount(text)
    syll = countTwoLetterSyll(text)
    output = open('stats.txt', 'w')
    output.write(f'Sample size: {symcount} character\n')
    i = 1
    for x in chars:
        output.write(f'{x} : {chars[x]}\n')
        i += 1
        if not showall and i == 5: break
    output.write('\n')
    for x in sorted(syll, key=lambda x: syll[x]):
        output.write(f'{x} : {syll[x]}\n')
        if not showall: break
    output.close()


def format(filename : str, remove_whitespace=False) -> None:
    f = open(filename, 'r')
    text = f.read().lower()
    if remove_whitespace:
        text = text.replace(' ', '')
    for c in punctuation:
        text = text.replace(c, '')
    text = text.replace('\t', '')
    text = text.replace('\n', '')
    f.close()
    g = open(filename.removesuffix('.txt') + '_format.txt', 'w')
    g.write(text.lower())
    g.close()


def symCount(text : str) -> int:
    return len(text) - text.count(' ')


def countChars(text : str, count_whitespace=False) -> dict:
    chars = {}
    for c in text:
        if not(c in ascii_letters):
            if (c == ' ' and not count_whitespace):
                continue
        try:
            chars[c] += 1
        except Exception:
            chars[c] = 1
    return chars


def countTwoLetterSyll(text : str, count_whitespace=False) -> dict:
    text = text.replace(' ', '')
    syll = dict()
    for i in range(0, len(text) - 1, 2):
        if not(text[i] in ascii_letters and text[i + 1] in ascii_letters):
            continue
        try:
            syll[text[i] + text[i + 1]] += 1
        except Exception:
            syll[text[i] + text[i + 1]] = 1
    if len(text) % 2 != 0: syll[text[-1] + ' '] = 2
    return syll


def getEntropyPerChar(chars : dict, symcount : int) -> float:
    chardist = {}
    for c in chars:
        chardist[c] = chars[c] / symcount
    entropyPerLetter = 0
    for c in chardist:
        entropyPerLetter += (-chardist[c] * log2(chardist[c]))
    return entropyPerLetter


def entropyPerTwoLetterSyll(syll : dict, syllCount : int) -> float:
    entropyTwoLetter = 0
    for c in syll:
        p = syll[c] / syllCount
        entropyTwoLetter += (-log2(p) * p)
    return entropyTwoLetter


def minCodeLen(chars : dict) -> int:
    return ceil(log2(len(chars)))


def codeExcessiveness(entropy : float, symcount : int) -> float:
    return  1 - (log2(entropy) / log2(symcount))
