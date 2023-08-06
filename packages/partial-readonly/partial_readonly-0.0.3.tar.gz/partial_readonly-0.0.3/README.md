# partial readonly

`partial_readonly` provide a decorator for conveniently making some fields read-only in dataclass. No dependencies other than the Python Standard Library.




## Usage


### Quick Start

With `partail_readonly`, we can easily make some of the fields in `dataclass` read-only by creating property related to them. __(Notice: We still can't make the origin field read-only, cause it still need to be set while calling `__init__`)__

For example, the following code
```python
from dataclasses import dataclass

@dataclass
class Data:
    id: int = 0
    name: str = ''

    @property
    def full_name(self): return self.name
```
can be written like this by using `partial_readonly`
```python
from dataclasses import dataclass

@dataclass
class Data:
    id: int = 0
    _name: 'str alias=full_name' = ''
```

### Details

1. Mark a field read-only by adding an underline prefix
    - `_id: int` means `id` is read-only
2. By default, the relative property named like field without underline prefix
    - `_id: int` will generate a property named `id`
3. Use string annotation and add `alias=alias_you_want` at the end, and you'll have a property named `alias_you_want`
    - `_id: 'int alias=security_id` will generate a property named `security_id`


## Installation

To install `partial_readonly`, simply use `pip`:

```pip install partial_readonly```

Or use `easy_install`:

```easy_install partial_readonly```


## Deep down

1. Making property read-only by set a getter[ and ban a setter]
2. Using AST to build a getter for new property
3. The idea about abusing annotation comes from [zmitchell/annotation-abuse](zmitchell/annotation-abuse)


## Why partial_readonly

Lastest python offer us dataclass for creating some class in convenient way.

But it's not convenient when we want not all the fields be readonly.


## Requirements

- Python >= 3.7


## Postscript

I built this for practicing AST and publish.

I think it work fine.

There are some more easily implementation.

If you sharing some idea about this feature I'll be greatful!


## License

```
MIT License

Copyright (c) 2018 book987

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```