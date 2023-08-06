# -*- coding: utf-8 -*-
import time
from django.core.management.base import BaseCommand
from djangoplus.tutorial.tools import VideoRecorder, Subtitle
from djangoplus.utils.webdriver import Browser


class Command(BaseCommand):

    def handle(self, *args, **options):
        subtitle = Subtitle()
        recorder = VideoRecorder()
        browser = Browser('http://google.com.br')
        browser.open('/')
        recorder.start()
        subtitle.display('This is only a test', 3)
        recorder.stop('Test')
        browser.close()
        browser.service.stop()
