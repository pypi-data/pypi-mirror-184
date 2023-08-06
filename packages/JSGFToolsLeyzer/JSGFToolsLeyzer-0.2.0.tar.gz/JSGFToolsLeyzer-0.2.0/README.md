JSGF Grammar Tools for Leyzer corpus
====================================

Introduction
============

This library generate strings from a JSGF grammar. Although it can be used to generate
strings from any JSGF grammar it was created as auxilary tool for Leyzer
(<https://github.com/cartesinus/leyzer>) grammars generation. It is slightly modified
version of <https://github.com/syntactic/JSGFTools>.

Notes:
- Larger grammars take a longer time to parse, so if nothing seems to be generating,
wait a few seconds and the grammar should be parsed.
- Most of JSGF as described in http://www.w3.org/TR/2000/NOTE-jsgf-20000605/ is
supported, but there are a few things that have not been implemented by these
tools yet:
    - Kleene operators
    - Imports and Grammar Names
    - Tags

Dependencies:
- Python 3.7
- PyParsing 3.0.9

JSGFTools were originaly created by Pastèque Ho (and others).

Library Usage
=============

To generate strings from grammar use it as in below example. Below example use
grammar that is included in this repository. Other, more complex grammars, can
be found in <https://github.com/cartesinus/leyzer> repository.

```python
from from JSGFToolsLeyzer import parser

fs = open("Ideas.gram")
grammar = parser.getGrammarObject(fs)

for rule in grammar.publicRules:
    expansions = processRHS(rule.rhs, grammar)
    for expansion in expansions:
        print(expansion)
```

License
=======

MIT License.
