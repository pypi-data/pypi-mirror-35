pyoption
========

Add support to `Option`_ and `Result`_ types like in Rust.. but in
Python.

Usage
-----

.. code:: python

   from pyoption.result import *

   def division(a, b):
       if b == 0:
           return Err('Invalid division by 0: aborting')
       return Ok(a / b)

   a = float(input('Enter first number: '))
   b = float(input('Enter second number: '))

   print('%0.2f / %0.2f = %0.2f' % (a, b, division(a, b).unwrap()))

Installation
------------

.. code:: shell

   pip install pyoption

Manually
^^^^^^^^

Clone this repository:

.. code:: shell

   git clone https://github.com/domcorvasce/pyoption

Then install the module:

.. code:: shell

   python setup.py install

Getting Started
---------------

Result
~~~~~~

.. code:: python

   from pyoption.result import *

In order to emulate the Result type, **pyoption** offers two classes:
**Ok** and **Err**, both of them supporting the same identic methods
that the Rust types offers (minus the ones we don’t need in a language
like Python).

Methods
^^^^^^^

-  [x] ``expect``
-  [x] ``unwrap``
-  [x] ``unwrap_err``
-  [x] ``expect_err``
-  [x] ``is_ok``
-  [x] ``is_err``

They behaves exactly like in Rust, except for the fact you don’t have to
define ``Result`` as return type for functions and methods since Ok and
Err have the same methods and you can treat them like one single class.

By default, the ``Err`` class uses ``RuntimeError``.

In alternative, you could use the ``Result function`` as return type
like you would do in Golang.

.. code:: python

   def to_lower(name):
       return Result(name.lower(), None)

Option
~~~~~~

.. code:: python

   from pyoption.option import *

Since ``None`` is a built-in type in Python and we can’t extend the
methods we can call on it, just use ``Some(None)`` to be able to use all
the methods defined below.

.. _methods-1:

Methods
^^^^^^^

-  [x] ``expect``
-  [x] ``unwrap``
-  [x] ``unwrap_or``
-  [x] ``unwrap_or_else``
-  [x] ``is_some``
-  [x] ``is_none``

License
-------

This project is released under the terms of `GNU/GPL v3`_.

.. _Option: https://doc.rust-lang.org/std/option/enum.Option.html
.. _Result: https://doc.rust-lang.org/std/result/enum.Result.html
.. _GNU/GPL v3: LICENSE