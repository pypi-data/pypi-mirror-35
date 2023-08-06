# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--continue', action='store_true', dest='continue', default=False,
                            help='Will not create a new project. The existing one will be used.')

    def handle(self, *args, **options):
        fromlist = [settings.PROJECT_NAME, 'tutorial', 'AppTutorial']
        module = __import__('{}.tutorial'.format(settings.PROJECT_NAME), fromlist=fromlist)
        tutorial = module.AppTutorial(settings.BASE_DIR)
        create_project = not options.pop('continue', False)
        tutorial.start(create_project)
