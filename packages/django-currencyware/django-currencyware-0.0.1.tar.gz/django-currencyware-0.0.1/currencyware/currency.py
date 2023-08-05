import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _

from . import defaults as defs
from .utils import memorize

_cache_currencies = {}
_cache_currencies_sorted = {}
_cache_currencies_sorted_prioritized = {}


def get_display(code):
    # Note: admin:skip
    display = _('ISO_4217.' + code)
    return display


def get_currencies(codes):
    """ Returns a list of (code, translation) tuples for codes  """
    currencies = [(code, get_display(code)) for code in codes]
    return currencies


@memorize(_cache_currencies)
def get_all_currencies(codes=defs.ALL_CURRENCY_CODES):
    """ Returns a list of (code, translation) tuples for all currency codes  """
    currencies = get_currencies(codes)
    return currencies


@memorize(_cache_currencies_sorted)
def get_all_currencies_sorted(codes=defs.ALL_CURRENCY_CODES):
    """ Returns a list of (code, translation) tuples for all currency codes  """
    currencies = sorted(
        get_currencies(codes),
        key=functools.cmp_to_key(lambda a, b: locale.strcoll(a[1], b[1]))
    )
    return currencies


@memorize(_cache_currencies_sorted_prioritized)
def get_all_currencies_prioritized(
        priority_codes=defs.PRIORITY_CURRENCY_CODES,
        codes=defs.ALL_CURRENCY_CODES
    ):
    """ Returns a sorted list of (code, translation) tuples for codes  """
    currencies = get_all_currencies_sorted(codes)
    prioritized = []
    if (priority_codes and len(priority_codes) > 0):
        prioritized = get_currencies(priority_codes)
        for priority in prioritized:
            if priority in currencies:
                del currencies[currencies.index(priority)]
    return prioritized + currencies