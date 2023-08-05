import sys
import json
import codecs
import logging
import requests
from datetime import datetime

from django.conf import settings
from django.utils import timezone
from django.utils import translation
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from toolware.utils.generic import get_days_ago

from ...currency import get_display
from ...models import Rate, Currency
from ... import defaults as defs

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Translators: admin
    help = "Fetches live rates from open exchange rates api"

    OXR_URL = defs.OPEN_EXCHANGE_RATES_URL
    OXR_KEY = defs.OPEN_EXCHANGE_RATES_API_KEY
    LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--purge',
            action='store',
            dest='days',
            type=int,
            help='Remove rates older than x days'
        )

        parser.add_argument(
            '-f',
            '--fetch',
            action='store_true',
            dest='fetch',
            default=False,
            help='Fetch and load all rates to db'
        )

    def handle(self, *args, **options):
        translation.activate(self.LANGUAGE_CODE)
        self.verbosity = options['verbosity']
        days = options['days']
        fetch = options['fetch']

        if not (days or fetch):
            self.print_help("", subcommand='rate')
            return

        if days:
            if days < 2:
                # purge only after 2 days old (compensate for UTC)
                self.stdout.write('Purge can be done on data 2 days or older')
                return
            self.purge(days)

        if fetch:
            self.fetch()

    def fetch(self):

        if self.verbosity > 2:
            self.stdout.write('Preparing to fetch rates ...')

        resp = requests.get(self.OXR_URL, params={'app_id': self.OXR_KEY, 'base': defs.BASE_CURRENY_CODE})
        if resp.status_code != requests.codes.ok:
            self.stdout.write('Failed to fetch rates ...')
            self.stdout.write(resp.text)
            return

        data = resp.json()
        new_count, update_count = 0, 0
        updated = datetime.fromtimestamp(data['timestamp'], tz=timezone.utc)
        for code, rate in data['rates'].items():
            created = False
            defaults = {
                'code': code,
                'date': updated,
                'rate': rate,
                'name': get_display(code)
            }
            instance, created = Rate.objects.get_or_create_unique(defaults, ['code', 'date'])
            if created:
                new_count += 1
            else:
                update_count += 1
            
            if not instance and self.verbosity >=3:
                sys.stdout.write('Failed to create rate for ({code})\n'.format(code=code))

        self.stdout.write('Created {count} currenies'.format(count=new_count))
        self.stdout.write('Updated {count} currenies'.format(count=update_count))


    def purge(self, days):
        print('purged')
        return
        days_ago = get_days_ago(days)
        Rate.objects.filter(date__lte=days_ago).delete()
        self.stdout.write('Purged rates older than ({}) ago from db.'.format(days))
