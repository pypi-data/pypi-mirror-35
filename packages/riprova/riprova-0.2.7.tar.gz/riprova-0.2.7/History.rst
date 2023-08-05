
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
