# ve-utils

[![CircleCI](https://circleci.com/gh/mano8/ve_utils.svg?style=svg)](https://app.circleci.com/pipelines/github/mano8/ve_utils)
[![PyPI package](https://img.shields.io/pypi/v/ve_utils.svg)](https://pypi.org/project/ve_utils/)
[![codecov](https://codecov.io/gh/mano8/ve_utils/branch/master/graph/badge.svg?token=ADZ070QHDR)](https://codecov.io/gh/mano8/ve_utils)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d5241461e15b492e9008ba87b3d24a3a)](https://www.codacy.com/gh/mano8/ve_utils/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mano8/ve_utils&amp;utm_campaign=Badge_Grade)  

This is a Python utilities helper. 

## Installation

#### Install from PyPi :

You can install the ve_utils helper from PyPI:

```plaintext
$ pip install ve_utils
```

#### Install from GitHub repository :

To install directly from GitHub:

```plaintext
$ python3 -m pip install "git+https://github.com/mano8/ve_utils"
```

# How to use

### UType :
import package :

```plaintext
from ve_utils.utype import UType as Ut
```

#### Test format :
Example for is_list method:

    >>> my_var = [ 0, 1 ,2 ,3 ]
    >>> Ut.is_list(my_var, not_null=True)
    >>> True
    >>> Ut.is_list(my_var, min_items=5)
    >>> False
    >>> Ut.is_list(my_var, max_items=2)
    >>> False
    >>> Ut.is_list(my_var, eq=4)
    >>> True 
    >>> Ut.is_list([], not_null=True)
    >>> False 
    >>> Ut.is_list([])
    >>> True 
    >>> Ut.is_list(dict())
    >>> False 

The methods ```is_list, is_dict and is_tuple ``` takes the sames arguments.

Example for is_int method:

    >>> my_var = 10
    >>> Ut.is_int(my_var, not_null=True)
    >>> True
    >>> Ut.is_int(my_var, mini=15)
    >>> False
    >>> Ut.is_int(my_var, maxi=2)
    >>> False
    # value is_int an is equal to 2
    >>> Ut.is_int(2, eq=2)
    >>> True
    >>> Ut.is_int(0, not_null=True)
    >>> False 
    >>> Ut.is_int(-10, positive=True)
    >>> False
    >>> Ut.is_int(-10, negative=True)
    >>> True 
    >>> Ut.is_int("hello")
    >>> False 

The methods ```is_int, is_float and is_numeric ``` takes the sames arguments.
``is_numeric`` method allow to work with float and int instances.
