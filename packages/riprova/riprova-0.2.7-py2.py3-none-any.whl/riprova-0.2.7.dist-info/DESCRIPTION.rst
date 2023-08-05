riprova |Build Status| |PyPI| |Coverage Status| |Documentation Status| |Quality| |Versions|
===========================================================================================

``riprova`` (meaning ``retry`` in Italian) is a small, general-purpose and versatile `Python`_ library
that provides retry mechanisms with multiple backoff strategies for any sort of failed operations.

It's domain agnostic, highly customizable, extensible and provides a minimal API that's easy to instrument in any code base via decorators, context managers or raw API consumption.

For a brief introduction about backoff mechanisms for potential failed operations, `read this article`_.


Features
--------

-  Retry decorator for simple and idiomatic consumption.
-  Simple Pythonic programmatic interface.
-  Maximum retry timeout support.
-  Supports error `whitelisting`_ and `blacklisting`_.
-  Supports custom `error evaluation`_ retry logic (useful to retry only in specific cases).
-  Automatically retry operations on raised exceptions.
-  Supports `asynchronous coroutines`_ with both ``async/await`` and ``yield from`` syntax.
-  Configurable maximum number of retry attempts.
-  Highly configurable supporting max retries, timeouts or retry notifier callback.
-  Built-in backoff strategies: constant, `fibonacci`_ and `exponential`_ backoffs.
-  Supports sync/async context managers.
-  Pluggable custom backoff strategies.
-  Lightweight library with almost zero embedding cost.
-  Works with Python +2.6, 3.0+ and PyPy.


Backoff strategies
------------------

List of built-in backoff strategies.

- `Constant backoff`_
- `Fibonacci backoff`_
- `Exponential backoff`_

You can also implement your own one easily.
See `ConstantBackoff`_ for an implementation reference.


Installation
------------

Using ``pip`` package manager (requires pip 1.9+. Upgrade it running: ``pip install -U pip``):

.. code-block:: bash

    pip install -U riprova

Or install the latest sources from Github:

.. code-block:: bash

    pip install -e git+git://github.com/h2non/riprova.git#egg=riprova


API
---

- riprova.retry_
- riprova.Retrier_
- riprova.AsyncRetrier_
- riprova.Backoff_
- riprova.ConstantBackoff_
- riprova.FibonacciBackoff_
- riprova.ExponentialBackoff_
- riprova.ErrorWhitelist_
- riprova.ErrorBlacklist_
- riprova.add_whitelist_error_
- riprova.RetryError_
- riprova.RetryTimeoutError_
- riprova.MaxRetriesExceeded_
- riprova.NotRetriableError_


.. _riprova.retry: http://riprova.readthedocs.io/en/latest/api.html#riprova.retry
.. _riprova.Retrier: http://riprova.readthedocs.io/en/latest/api.html#riprova.Retrier
.. _riprova.AsyncRetrier: http://riprova.readthedocs.io/en/latest/api.html#riprova.AsyncRetrier
.. _riprova.Backoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.Backoff
.. _riprova.ConstantBackoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.ConstantBackoff
.. _riprova.FibonacciBackoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.FibonacciBackoff
.. _riprova.ExponentialBackoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.ExponentialBackoff
.. _riprova.ErrorWhitelist: http://riprova.readthedocs.io/en/latest/api.html#riprova.ErrorWhitelist
.. _riprova.ErrorBlacklist: http://riprova.readthedocs.io/en/latest/api.html#riprova.ErrorBlacklist
.. _riprova.add_whitelist_error: http://riprova.readthedocs.io/en/latest/api.html#riprova.add_whitelist_error
.. _riprova.RetryError: http://riprova.readthedocs.io/en/latest/api.html#riprova.RetryError
.. _riprova.RetryTimeoutError: http://riprova.readthedocs.io/en/latest/api.html#riprova.RetryTimeoutError
.. _riprova.MaxRetriesExceeded: http://riprova.readthedocs.io/en/latest/api.html#riprova.MaxRetriesExceeded
.. _riprova.NotRetriableError: http://riprova.readthedocs.io/en/latest/api.html#riprova.NotRetriableError


Examples
^^^^^^^^

You can see more featured examples from the `documentation` site.

**Basic usage examples**:

.. code-block:: python

    import riprova

    @riprova.retry
    def task():
        """Retry operation if it fails with constant backoff (default)"""

    @riprova.retry(backoff=riprova.ConstantBackoff(retries=5))
    def task():
        """Retry operation if it fails with custom max number of retry attempts"""

    @riprova.retry(backoff=riprova.ExponentialBackOff(factor=0.5))
    def task():
        """Retry operation if it fails using exponential backoff"""

    @riprova.retry(timeout=10)
    def task():
        """Raises a TimeoutError if the retry loop exceeds from 10 seconds"""

    def on_retry(err, next_try):
        print('Operation error: {}'.format(err))
        print('Next try in: {}ms'.format(next_try))

    @riprova.retry(on_retry=on_retry)
    def task():
        """Subscribe via function callback to every retry attempt"""

    def evaluator(response):
        # Force retry operation if not a valid response
        if response.status >= 400:
            raise RuntimeError('invalid response status')  # or simple return True
        # Otherwise return False, meaning no retry
        return False

    @riprova.retry(evaluator=evaluator)
    def task():
        """Use a custom evaluator function to determine if the operation failed or not"""

    @riprova.retry
    async def task():
        """Asynchronous coroutines are also supported :)"""


**Retry failed HTTP requests**:

.. code-block:: python

    import pook
    import requests
    from riprova import retry

    # Define HTTP mocks to simulate failed requests
    pook.get('server.com').times(3).reply(503)
    pook.get('server.com').times(1).reply(200).json({'hello': 'world'})


    # Retry evaluator function used to determine if the operated failed or not
    def evaluator(response):
        if response != 200:
            return Exception('failed request')  # you can also simply return True
        return False


    # On retry even subscriptor
    def on_retry(err, next_try):
        print('Operation error {}'.format(err))
        print('Next try in {}ms'.format(next_try))


    # Register retriable operation
    @retry(evaluator=evaluator, on_retry=on_retry)
    def fetch(url):
        return requests.get(url)


    # Run task that might fail
    fetch('http://server.com')



License
-------

MIT - Tomas Aparicio

.. _exponential: https://en.wikipedia.org/wiki/Exponential_backoff
.. _fibonacci: https://en.wikipedia.org/wiki/Fibonacci_number
.. _asyncio: https://docs.python.org/3.5/library/asyncio.html
.. _Python: http://python.org
.. _annotated API reference: https://h2non.github.io/paco
.. _async/await: https://www.python.org/dev/peps/pep-0492/
.. _yield from: https://www.python.org/dev/peps/pep-0380/
.. _documentation: http://riprova.readthedocs.io/en/latest/examples.html
.. _read this article: http://dthain.blogspot.ie/2009/02/exponential-backoff-in-distributed.html
.. _Constant backoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.ConstantBackoff
.. _Fibonacci backoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.FibonacciBackoff
.. _Exponential backoff: http://riprova.readthedocs.io/en/latest/api.html#riprova.ExponentialBackOff
.. _ConstantBackoff: https://github.com/h2non/riprova/blob/master/riprova/strategies/constant.py
.. _whitelisting: https://github.com/h2non/riprova/blob/master/examples/whitelisting_errors.py
.. _blacklisting: https://github.com/h2non/riprova/blob/master/examples/blacklisting_errors.py
.. _error evaluation: https://github.com/h2non/riprova/blob/master/examples/http_request.py
.. _asynchronous coroutines: https://github.com/h2non/riprova/blob/master/examples/http_asyncio.py

.. |Build Status| image:: https://travis-ci.org/h2non/riprova.svg?branch=master
   :target: https://travis-ci.org/h2non/riprova
.. |PyPI| image:: https://img.shields.io/pypi/v/riprova.svg?maxAge=2592000?style=flat-square
   :target: https://pypi.python.org/pypi/riprova
.. |Coverage Status| image:: https://coveralls.io/repos/github/h2non/riprova/badge.svg?branch=master
   :target: https://coveralls.io/github/h2non/riprova?branch=master
.. |Documentation Status| image:: https://img.shields.io/badge/docs-latest-green.svg?style=flat
   :target: http://riprova.readthedocs.io/en/latest/?badge=latest
.. |Quality| image:: https://codeclimate.com/github/h2non/riprova/badges/gpa.svg
   :target: https://codeclimate.com/github/h2non/riprova
.. |Stability| image:: https://img.shields.io/pypi/status/riprova.svg
   :target: https://pypi.python.org/pypi/riprova
.. |Versions| image:: https://img.shields.io/pypi/pyversions/riprova.svg
   :target: https://pypi.python.org/pypi/riprova



v0.2.7 / 2018-08-24
-------------------

  * Merge pull request #20 from ffix/forward-exception-instance
  * Correct linter warnings
  * Re-raise exception instance instead of new exception with no args
  * Merge pull request #19 from EdwardBetts/spelling
  * Correct spelling mistakes.
  * feat(setup): support Python 3.7
  * feat(History): add version changes

v0.2.6 / 2018-04-14
-------------------

* fix(#17): handle as legit retriable error Timeout exceptions.

v0.2.5 / 2018-03-21
-------------------

* Merge pull request #15 from jstasiak/allow-newer-six
* Allow newer six
* feat(History): update changes

v0.2.5 / 2018-03-21
------------------

* Merge pull request #15 from jstasiak/allow-newer-six
* Allow newer six
* feat(History): update changes

v0.2.4 / 2018-03-20
-------------------

* merge(#14): Allow subsecond maxtimes for ExponentialBackoff

v0.2.3 / 2017-01-13
-------------------

* refactor(retry): remove unnecessary partial function
* fix(retry): rename keyword param for partial application
* feat(docs): improve description
* refactor(Makefile): update publish task

v0.2.2 / 2017-01-06
-------------------

* feat(package): add wheel distribution

v0.2.1 / 2017-01-04
-------------------

* fix(retrier): remove debug print statement

v0.2.0 / 2017-01-02
-------------------

* feat(core): use seconds as default time unit (introduces API breaking changes)
* refactor(examples): update examples to use new time unit
* feat(contextmanager): adds context manager support
* feat(examples): add context manager example
* feat: add context managers support

v0.1.3 / 2016-12-30
-------------------

* refactor(async_retrier): simplify coroutine wrapper
* feat(whitelist): add whitelist and blacklist support
* feat(tests): add missing test cases for whitelist
* feat(retry): pass error_evaluator param
* fix(retrier): cast delay to float
* fix(tests): use valid exception for Python 2.7
* feat(#6): add custom error whilelist and custom error evaluator function
* Merge pull request #8 from tsarpaul/master
* refactor(decorator): do not expose retrier instance

v0.1.2 / 2016-12-27
-------------------

* fix(decorator): wrap retries instance per function call

v0.1.1 / 2016-12-27
-------------------

* fix(`#2`_): handle and forward ``asyncio.CancelledError`` as non-retriable error

v0.1.0 / 2016-12-25
-------------------

* First version


.. _#2: https://github.com/h2non/riprova/issues/2


