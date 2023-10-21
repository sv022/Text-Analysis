# TextAnalysis
Module for getting text sample statistics, including entropy and sets of symbols.
Also includes module with Shannon-Fano encoding.

## Functionality description

### textanalysis.py

```
def logstats(text : str, showall=True) -> None:
```

Logs information about the given sample `text` into a file `stats.txt`.
To toggle shortened output set `showall=False`.

```
def formatfile(filename : str, remove_whitespace=False) -> None:
```

Formats `filename` file by removing special characters and punctuation. 
To leave whitespaces set `remove_whitespace=False`.
The formatted content of the file is put into `{filename}_format.txt`.

```
def format(text : str, remove_whitespace=False) -> str:
```

Formats the input string `text` by removing special characters and punctuation. 
To leave whitespaces set `remove_whitespace=False`.
Returns the formatted string.

```
def countchars(text : str, count_whitespace=False) -> dict:
```

Returns a dictionary in format `symbol : text.count(symbol)`.
To count whitespaces set `remove_whitespace=False`.

```
def countsyll(text : str, syll_len=2) -> dict:
```

Returns a dictionary in format `symbol : text.count(symbol)`. 
Used with syllables of any length `syll_len`.

```
def entropy(symbols: dict, symcount : int) -> float:
```

Returns the value of entropy per one symbol in the `symbols` dictionary in format `symbol : text.count(symbol)`.





