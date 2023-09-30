from TextAnalysys import *

class Unit:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None


def build_shannon_fano_tree(data : list[tuple]) -> Unit:
    if len(data) == 0:
        return None
    if len(data) == 1:
        return Unit(symbol=data[0][0], frequency=data[0][1])

    total_frequency = sum(item[1] for item in data)
    half_frequency = total_frequency // 2
    current_sum = 0
    index = 0

    for i, (symbol, frequency) in enumerate(data):
        current_sum += frequency
        if current_sum >= half_frequency:
            index = i
            break

    left_data = data[:index + 1]
    right_data = data[index + 1:]

    root = Unit()
    root.left = build_shannon_fano_tree(left_data)
    root.right = build_shannon_fano_tree(right_data)

    return root


def getCodes(root, current_code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if root.symbol is not None:
        code_dict[root.symbol] = current_code
        return code_dict

    getCodes(root.left, current_code + "0", code_dict)
    getCodes(root.right, current_code + "1", code_dict)

    return code_dict


def shannon_fano_encode(data : str) -> (str, dict):
    symbol_frequency = countTwoLetterSyll(data)
    sorted_data = sorted(symbol_frequency.items(), key=lambda x: x[1], reverse=True)

    root = build_shannon_fano_tree(sorted_data)
    codes = getCodes(root)

    encoded_data = "".join([codes[symbol] for symbol in data])

    return encoded_data, codes


def shannon_fano_encode_2(data : str) -> (str, dict):
    symbol_frequency = countTwoLetterSyll(data)

    sorted_data = sorted(symbol_frequency.items(), key=lambda x: x[1], reverse=True)

    root = build_shannon_fano_tree(sorted_data)
    codes = getCodes(root)

    encoded_data = "".join([codes[data[i] + data[i + 1]] for i in range(0, len(data) - 1, 2])

    return encoded_data, codes


def shannon_fano_decode(encoded_data, codes : dict):
    decoded_data = ""
    current_code = ""
    swapcodes = {val : key for key, val in codes.items()}
    for bit in encoded_data:
        current_code += bit
        if current_code in swapcodes:
            decoded_data += swapcodes[current_code]
            current_code = ''

    return decoded_data
