# Generated by Django 2.0.6 on 2018-07-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(help_text='CURRENCY.CODE.DESC', max_length=3, primary_key=True, serialize=False, verbose_name='CURRENCY.CODOE')),
                ('number', models.CharField(blank=True, help_text='CURRENCY.NUMBER.DESC', max_length=3, null=True, verbose_name='CURRENCY.NUMBER')),
                ('unit', models.IntegerField(blank=True, help_text='CURRENCY.UNITS.DESC', null=True, verbose_name='CURRENCY.UNITS')),
                ('country', models.CharField(blank=True, help_text='CURRENCY.COUNTRY.DESC', max_length=255, null=True, verbose_name='CURRENCY.COUNTRY')),
            ],
            options={
                'verbose_name': 'CURRENCY.LABEL.SINGULAR',
                'verbose_name_plural': 'CURRENCY.LABEL.PLURAL',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('AED', 'UAE Dirham'), ('AFN', 'Afghani'), ('ALL', 'Lek'), ('AMD', 'Armenian Dram'), ('AOA', 'Kwanza'), ('ARS', 'Argentine Peso'), ('AUD', 'Australian Dollar'), ('AWG', 'Aruban Florin'), ('AZN', 'Azerbaijanian Manat'), ('BAM', 'Convertible Mark'), ('BBD', 'Barbados Dollar'), ('BDT', 'Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundi Franc'), ('BMD', 'Bermudian Dollar'), ('BND', 'Brunei Dollar'), ('BOB', 'Boliviano'), ('BRL', 'Brazilian Real'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Ngultrum'), ('BWP', 'Pula'), ('BYR', 'Belarusian Ruble'), ('BZD', 'Belize Dollar'), ('CAD', 'Canadian Dollar'), ('CDF', 'Congolese Franc'), ('CHF', 'Swiss Franc'), ('CLP', 'Chilean Peso'), ('CNY', 'Yuan Renminbi'), ('COP', 'Colombian Peso'), ('CRC', 'Costa Rican Colon'), ('CUP', 'Cuban Peso'), ('CVE', 'Cabo Verde Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djibouti Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EGP', 'Egyptian Pound'), ('ERN', 'Nakfa'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('FJD', 'Fiji Dollar'), ('FKP', 'Falkland Islands Pound'), ('GBP', 'Pound Sterling'), ('GEL', 'Lari'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Dalasi'), ('GNF', 'Guinea Franc'), ('GTQ', 'Quetzal'), ('GYD', 'Guyana Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Lempira'), ('HRK', 'Kuna'), ('HTG', 'Gourde'), ('HUF', 'Forint'), ('IDR', 'Rupiah'), ('ILS', 'New Israeli Sheqel'), ('INR', 'Indian Rupee'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Iceland Krona'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('JPY', 'Yen'), ('KES', 'Kenyan Shilling'), ('KGS', 'Som'), ('KHR', 'Riel'), ('KPW', 'North Korean Won'), ('KRW', 'Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Tenge'), ('LAK', 'Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lanka Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Loti'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Denar'), ('MMK', 'Kyat'), ('MNT', 'Tugrik'), ('MOP', 'Pataca'), ('MRO', 'Ouguiya'), ('MUR', 'Mauritius Rupee'), ('MVR', 'Rufiyaa'), ('MWK', 'Malawi Kwacha'), ('MXN', 'Mexican Peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Mozambique Metical'), ('NAD', 'Namibia Dollar'), ('NGN', 'Naira'), ('NIO', 'Cordoba Oro'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('NZD', 'New Zealand Dollar'), ('OMR', 'Rial Omani'), ('PAB', 'Balboa'), ('PEN', 'Sol'), ('PGK', 'Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistan Rupee'), ('PLN', 'Zloty'), ('PYG', 'Guarani'), ('QAR', 'Qatari Rial'), ('RON', 'Romanian Leu'), ('RSD', 'Serbian Dinar'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychelles Rupee'), ('SDG', 'Sudanese Pound'), ('SEK', 'Swedish Krona'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinam Dollar'), ('STD', 'Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Lilangeni'), ('THB', 'Baht'), ('TJS', 'Somoni'), ('TMT', 'Turkmenistan New Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Pa’anga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Hryvnia'), ('UGX', 'Uganda Shilling'), ('USD', 'US Dollar'), ('UYU', 'Peso Uruguayo'), ('UZS', 'Uzbekistan Sum'), ('VEF', 'Bolívar'), ('VND', 'Dong'), ('VUV', 'Vatu'), ('WST', 'Tala'), ('XAF', 'CFA Franc BEAC'), ('XCD', 'East Caribbean Dollar'), ('XPF', 'CFP Franc'), ('YER', 'Yemeni Rial'), ('ZAR', 'Rand'), ('ZMW', 'Zambian Kwacha')], help_text='RATE.CURRENCY.CODE.DESC', max_length=3, verbose_name='RATE.CURRENCY.CODE')),
                ('rate', models.FloatField(default=0.0, help_text='RATE.CURRENCY.DESC', verbose_name='RATE.CURRENCY')),
                ('date', models.DateTimeField(help_text='RATE.DATE.DESC', verbose_name='RATE.DATE')),
            ],
            options={
                'verbose_name': 'RATE.LABEL.SINGULAR',
                'verbose_name_plural': 'RATE.LABEL.PLURAL',
            },
        ),
    ]
