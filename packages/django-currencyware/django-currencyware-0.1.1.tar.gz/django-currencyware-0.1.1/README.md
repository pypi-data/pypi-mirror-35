Django Currencyware
====================

**A Django application to provides translated currency names**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

Overview
====================

**Best attempt** to translate currency names while keeping it **DRY**.


How to install
====================

    1. easy_install django-currencyware
    2. pip install django-currencyware
    3. git clone http://github.com/un33k/django-currencyware
        a. cd django-currencyware
        b. run python setup.py install
    4. wget https://github.com/un33k/django-currencyware/zipball/master
        a. unzip the downloaded file
        b. cd into django-currencyware-* directory
        c. run python setup.py install


How to use
====================

   ```python
    # In a models.py
    from currencyware.utils.currency import get_all_currencies_prioritized
    from currencyware.fields import CurrencyField

    currency = CurrencyField(
        _("Currency"),
        choices=get_all_currencies_prioritized(),
    )
   ```

Advanced users:
====================

   ```python
    # In a settings.py
    # You can overwrite the default list of currency codes
    ALL_CURRENCY_CODES = ['USD', 'CAD', 'EUR'']

    # You can prepend priority countries to the lst
    PRIORITY_CURRENCY_CODES = ['CAD', 'USD']
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([MIT](LICENSE)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-currencyware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-currencyware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-currencyware.svg
[version-link]: https://pypi.python.org/pypi/django-currencyware

[coverage-image]: https://coveralls.io/repos/un33k/django-currencyware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-currencyware

[download-image]: https://img.shields.io/pypi/dm/django-currencyware.svg
[download-link]: https://pypi.python.org/pypi/django-currencyware
