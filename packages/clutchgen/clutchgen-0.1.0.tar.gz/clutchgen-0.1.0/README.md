This README for develop
ing, read it if you are going to contribute.

Info about usage you can find on [WIKI pages](https://gitlab.com/AlexeyReket/clutchgen/-/wikis/home)

## Get started

If you wish you can config your poetry

```shell
poetry config --local virtualenvs.create true
poetry config --local virtualenvs.in-project true
```

Install required libraries

```shell
poetry install
```

Activate created environment

```shell
source .venv/bin/activate
```

and enable autoComplete

```shell
# for bash
eval "$(_CLUTCHGEN_COMPLETE=bash_source clutchGen)"

# for zsh
eval "$(_CLUTCHGEN_COMPLETE=zsh_source clutchGen)"
```

## Quality assurance

You can run tests

```shell
make test
```

And can apply formatting:

```shell
make format
```

Please in case if contributing make tests and save code-style 
