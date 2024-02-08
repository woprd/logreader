# logreader

Reads files and converts various log files into something useful (e.g. pandas dataframes) for subsequent analyses. Ever expanding list of log formats is:

- [Combined Log Format](https://en.wikipedia.org/wiki/Common_Log_Format#:~:text=For%20computer%20log%20management%2C%20the,when%20generating%20server%20log%20files.) 

- [MongoDB logs](https://www.mongodb.com/docs/manual/reference/log-messages/)

![Under Construction](https://media.tenor.com/MRCIli40TYoAAAAi/under-construction90s-90s.gif)

## Installation 

```python 

pip install . 

```

## Usage 

Common Log Format files to a pandas dataframe:

```python

from logreader import CLFReader
clfr = CLFReader(<path to logs file>)
# python data structures
clfr.logs
# pandas dataframe
clfr.df

```

Also see the file `logreader/__main__.py`

And run that with 

```bash
python -m clfreader
```

## TODO

See issues.

