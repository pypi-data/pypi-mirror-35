from django.conf import settings

# https://justforex.com/education/currencies
ALL_CURRENCY_CODES = getattr(settings, 'ALL_CURRENCY_CODES', [
    'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'ARS',
    'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
    'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB',
    'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD',
    'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP',
    'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK',
    'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR',
    'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP',
    'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
    'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR',
    'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY',
    'KES', 'KGS', 'KHR', 'KPW', 'KRW', 'KWD',
    'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD',
    'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
    'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR',
    'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN',
    'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB',
    'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
    'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR',
    'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
    'SLL', 'SOS', 'SRD', 'STD', 'SYP', 'SZL',
    'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
    'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD',
    'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST',
    'XAF', 'XCD', 'XPF', 'YER', 'ZAR', 'ZMW',
])

PRIORITY_CURRENCY_CODES = getattr(settings, 'PRIORITY_CURRENCY_CODES', [
    'USD', 'CAD', 'EUR', 'AUD', 'GBP', 'HKD', 'JPY', 'CNY', 'CHF',
])

OPEN_EXCHANGE_RATES_URL = 'https://openexchangerates.org/api/latest.json'
OPEN_EXCHANGE_RATES_URL = getattr(settings, 'OPEN_EXCHANGE_RATES_URL', OPEN_EXCHANGE_RATES_URL)
OPEN_EXCHANGE_RATES_API_KEY = getattr(settings, 'OPEN_EXCHANGE_RATES_API_KEY', None)
