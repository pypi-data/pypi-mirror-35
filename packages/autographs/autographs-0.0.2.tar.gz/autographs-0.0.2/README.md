# `autographs`
A collection of tools for making graph stuff easy. Used by the
[MGGG](https://sites.tufts.edu/gerrymandr/), this package provides a wide array
of facilities for interacting with graphs.

## Inlcuded Tools
(Check these off as they're completed)

- [x] Finding faces of planar graphs
- [ ] Making graphs
- [ ] Grid graph stuff (?)
- [ ] Tree-walk stuff

## Docs
Forthcoming Overleaf documents with more information about the math we
use here.

# Installation
If you run into trouble with installation, please take a look at the
[help](#Help) section.

## With Pip
The Python Package Index's package manager, Pip, comes installed with every
version of Python. For more info on how to use it, type `pip -h` in a terminal
or look at [their documentation](https://pip.pypa.io/en/stable/).

To intall `autographs` with Pip, simply run

```
$ pip install autographs
```

and you're set!
You can test out your installation by opening an interactive Python shell and
importing `autographs`.

## Manually
You can also install `autographs` manually. To do this, clone this repository,
navigate to the root directory, and run

```
$ python setup.py install
```

This will install all necessary dependencies and make `autographs` globally
available (after a shell restart).

# Contributing
To contribute to this project, make yourself a fork and submit pull requests.
You can also set up the development environment by running `make dev`.
Otherwise, follow [this contributor's guide](http://bit.ly/2AlTKy7). Make runs
the Python install script in development mode; this means that there is a
symlink in the global packages folder that points to this directory, making
all code (including live changes) available globally. Additionally, it unzips
the test data in the `test/data` directory.

# Usage
Import as you normally would: `import autographs`. As an example program, we can
find the faces of the dual graph induced by the counties of Iowa using a
half-edge structure:

```python
from autographs.faces import HalfEdge

# Create a new half-edge data structure.
he = HalfEdge("./test/data/2018_19_counties/county.shp")

# Simply iterate over the faces.
for face in he.faces:
    print(face)
```

# Help
Running into errors? There are quite a few you can encounter, and hopefully this
document covers a few.

## `ModuleNotFoundError: No module named 'autographs'`
There are a number of reasons that this error can pop up.

1. **When installing, the wrong `pip` was used.** For those that have multiple
interpreters (e.g. Homebrew users), using the right `pip` command is key. Run
`which python` and `which pip` in a shell and make sure that the resulting paths
are the same.
2. **Your shell isn't new enough (when using interactive Python)**. Just close
your prompt and open a new one.
3. **The Pip install location isn't in your `$PATH`**. Most OSes use environment
variables to help processes run. Depending on your interpreter, look up the
filepath for Pip's storage and make sure that filepath is in `$PATH`.
[Follow these instructions](http://bit.ly/2AvmHI7) for adding things to `$PATH`.

