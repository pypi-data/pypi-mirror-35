# -*- coding: utf-8 -*-
import os
import warnings
from djangoplus.utils.webdriver import Browser
import json
from django.conf import settings
from djangoplus.test import cache
from django.core.management import call_command
from selenium.webdriver.firefox.options import Options
from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.staticfiles.handlers import StaticFilesHandler


class TestStaticFilesHandler(StaticFilesHandler):
    def _middleware_chain(self, request):
        from django.http import HttpResponse
        return HttpResponse()


# StaticLiveServerTestCase
class TestCase(LiveServerTestCase):

    static_handler = TestStaticFilesHandler

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.login_count = 0
        self.current_username = None
        self.current_password = None
        self.restored = False
        warnings.filterwarnings('ignore')

    def setUp(self):
        super(TestCase, self).setUp()
        self.slowly = False
        self.username = None
        options = Options()
        options.add_argument("--window-size=1920x1080")
        if 'HEADLESS' in os.environ:
            options.add_argument("--headless")
        self.browser = Browser(self.live_server_url, options)

    def create_superuser(self, username, password):
        from djangoplus.admin.models import User
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, None, password)
        self.wait(1)

    def wait(self, seconds=1):
        self.browser.wait(seconds)

    def open(self, url):
        self.browser.open(url)

    def enter(self, name, value, submit=False, count=2):
        self.browser.enter(name, value, submit, count)

    def choose(self, name, value, count=2):
        self.browser.choose(name, value, count)

    def dont_see_error_message(self):
        self.browser.dont_see_error_message(self)

    def look_for(self, text, count=2):
        self.browser.look_for(text, count)

    def look_at_popup_window(self, count=2):
        self.browser.look_at_popup_window(count)

    def look_at(self, text, count=2):
        self.browser.look_at(text, count)

    def look_at_panel(self, text, count=2):
        self.browser.look_at_panel(text, count)

    def click_menu(self, *texts):
        self.browser.click_menu(*texts)

    def click_link(self, text):
        self.browser.click_link(text)

    def click_button(self, text):
        self.browser.click_button(text)

    def click_tab(self, text):
        self.browser.click_tab(text)

    def click_icon(self, name):
        self.browser.click_icon(name)

    def login(self, username, password):
        print('Logging as', username)
        self.login_count += 1
        self.current_username = username
        self.current_password = password
        if self.login_count >= cache.LOGIN_COUNT:
            self.dump()
            self.open('/admin/login/')
            self.enter(_('Username'), username)
            self.enter(_('Password'), password, True)
            self.wait()
            return True
        else:
            if not self.restored:
                self.restore()
            return False

    def logout(self):
        self.browser.logout()
        self.username = None

    def tearDown(self):
        super(TestCase, self).tearDown()
        self.browser.close()
        self.browser.service.stop()
        # len(self._resultForDoCleanups.errors)>0

    def dump(self, failed=False):
        file_path = '/tmp/{}.test'.format(settings.PROJECT_NAME)
        dump_file_path = '/tmp/{}.json'.format(settings.PROJECT_NAME)
        data = dict(login_count=self.login_count, username=self.current_username, password=self.current_password)
        open(file_path, 'w').write(json.dumps(data))
        output = open(dump_file_path,'w')
        app_labels = []
        for app in settings.INSTALLED_APPS:
            app_label = app.split('.')[-1]
            if app_label not in 'auth':
                app_labels.append(app_label)
        call_command('dumpdata', *app_labels, format='json', indent=3, stdout=output, skip_checks=True, verbosity=0)
        output.close()

    def restore(self):
        dump_file_path = '/tmp/{}.json'.format(settings.PROJECT_NAME)
        call_command('loaddata', dump_file_path)
        self.restored = True

