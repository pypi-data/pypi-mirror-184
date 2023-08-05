Hostsharing Utilities
=====================

A python package with some useful functions for working in a webspace or managed server of [Hostsharing eG](https://hostsharing.net).

Why
---

We have multiple uses for such functions, and it is useful to have them in one place.

Getting started
---------------

Installing:

    pip install hsutilities

A simple example:

```python
from hsutilities import domains as hsdomains
from hsutilities import users as hsusers
from hsutilities import admin as hsadmin

pac = hsusers.get_current_pac()
domains = hsdomains.get_domains_of_user(pac)

api = hsadmin.get_api(pac)
api.domain.add(set = {'name': 'example.org', 'user': 'xyz00-example'})
```
