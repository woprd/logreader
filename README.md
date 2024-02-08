# clfreader

Reads [Combined Log Format](https://en.wikipedia.org/wiki/Common_Log_Format#:~:text=For%20computer%20log%20management%2C%20the,when%20generating%20server%20log%20files.) files and converts to something useful. 

![Under Construction](https://media.tenor.com/MRCIli40TYoAAAAi/under-construction90s-90s.gif)

## Installation 

```python 

pip install . 

```

## Usage 

```python
from clfreader import CLFReader
clfr = CLFReader(<path to logs file>)
# python data structures
clfr.logs
# pandas dataframe
clfr.df

```

Also see the file `clfreader/__main__.py`

And run that with 

```bash
python -m clfreader
```

## TODO

See issues.

