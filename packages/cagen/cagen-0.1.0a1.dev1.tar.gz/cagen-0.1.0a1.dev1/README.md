# cagen

## About

cagen is a static site generator intented for [cmpalgorithms project](https://sr.ht/~somenxavierb/cmpalgorithms/). So it's very rare you are interested in that.

## License
The software is distributed under [GPL2-only license](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).

## Acknowledgements

It assumes your documents are in markdown syntax. It is capable of convert those documents in any other format, using [pandoc](https://pandoc.org/) (specifically [pypandoc](https://github.com/JessicaTegner/pypandoc) wrapper). When html format is desired, it uses [Cheetah3 Templating System](https://cheetahtemplate.org/) for customizing the HTML (pandoc templates [lacks](https://pandoc.org/MANUAL.html#conditionals) to make an if with values; something like `if var == b...`).

## Installation

You can install via [pip](https://pypi.org/project/cagen/):

```
pip install cagen
```
