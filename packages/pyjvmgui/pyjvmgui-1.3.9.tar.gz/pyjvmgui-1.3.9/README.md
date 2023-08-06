# `pyjvmgui`

## Based on [PyJVM](https://github.com/andrewromanenco/pyjvm)
Java 7 virtual machine implemented in pure python

- GPL
- Requires python 2.7
- https://github.com/andrewromanenco/pyjvm
- check docs for implementation details

> Andrew Romanenco, 2014
> andrew@romanenco.com
> https://twitter.com/andrewromanenco

## Installation

**Requires Python 2 (hence `pip2`).**

You can install `pyjvmgui` from the [PyPI](https://pypi.org/project/pyjvmgui/).

```
pip2 install pyjvmgui
```

When upgrading, it's advised to add `--no-deps` flag. Otherwise, the [PySide2](###PySide2) dependency might be downloaded again.

```
pip2 install pyjvmgui --upgrade --no-deps
```

## Dependencies

### PySide2

[PySide2](https://wiki.qt.io/Qt_for_Python) is used for the GUI.

You can install it by running

```
pip2 install PySide2
```

**Note:** done by `pip` if following the [installation instructions](##Installation)
