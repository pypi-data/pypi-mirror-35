# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from djangoplus.tutorial.utils import display_subtitle


class Command(BaseCommand):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('words', nargs='*', default=None)

    def handle(self, *args, **options):
        words = options.pop('words')
        display_subtitle(' '.join(words).replace('\\n', '\n'))
