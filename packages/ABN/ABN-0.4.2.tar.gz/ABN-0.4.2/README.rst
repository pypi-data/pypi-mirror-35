===
ABN
===

This package validates Australian Business Numbers (ABNs) and converts Australian Company Numbers (ACNs) or Australian Registered Body Numbers (ARBNs) to ABNs.

The following example show checking of a valid and an invalid ABN:

.. code-block:: python

    >>> import abn
    >>> abn.validate('53004085616')
    '53 004 085 616'

    >>> abn.validate('99999999999')
    False


To calculate the ABN based on an existing ACN or ARBN:

.. code-block:: python

    >>> abn.acn_to_abn('004085616')
    '53 004 085 616'


To run the tests or your current Python:

.. code-block:: bash

    $ python setup.py test

To run the tests over all supported Python versions, install Tox and run:

.. code-block:: bash

    $ tox
