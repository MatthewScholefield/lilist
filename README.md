# LiList

*A linear interpolation list class for Python*

This class implements a simple linear interpolation interface for python lists
of numbers.

## Usage

```python
from lilist import LiList

l = LiList([0, 2, 2.1, 3.1])
assert l[0] == 0
assert l[1] == 2
assert l[0.5] == 1.0
assert l[2] == 2.1
assert l[1.5] == 2.05
assert l[2.1] == 2.2

```

## Installation

```bash
pip install lilist
```

