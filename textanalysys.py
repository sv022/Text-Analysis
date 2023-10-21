from string import punctuation, ascii_letters
from math import log2, ceil

def _getsymcount(text : str) -> int:
    return len(text) - text.count(' ')

def logstats(text : str, showall=True):
    chars = countchars(text)
    symcount = _getsymcount(text)
    syll = countsyll(text)
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


def formatfile(filename : str, remove_whitespace=False) -> None:
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
    

def format(text : str, remove_whitespace=False) -> str:
    text = text.lower()
    if remove_whitespace:
        text = text.replace(' ', '')
    for c in punctuation:
        text = text.replace(c, '')
    text = text.replace('\t', '')
    text = text.replace('\n', '')
    
    return text


def countchars(text : str, count_whitespace=False) -> dict:
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


def countsyll(text : str, syll_len=2, count_whitespace=False) -> dict:
    text = text.replace(' ', '')
    syll = dict()
        
    i = 0
    while i < len(text):
        if not(all(c in ascii_letters for c in text[i:i+syll_len])):
            continue
        try:
            syll[text[i:i+syll_len]] += 1
        except Exception:
            syll[text[i:i+syll_len]] = 1
        
        i += syll_len
    
    syll[text[i:len(text)]] = 1
    
    try:
        del syll['']
    except KeyError:
        pass

    return syll


def entropy(symbols: dict, symcount : int) -> float:
    entropypersymbol = 0
    for c in symbols:
        p = symbols[c] / symcount
        entropypersymbol += (-p * log2(p))
    return entropypersymbol


def mincodelength(chars : dict) -> int:
    return ceil(log2(len(chars)))


def excessiveness(entropy : float, symcount : int) -> float:
    return  1 - (log2(entropy) / log2(symcount))
