# -*- coding: utf-8 -*-
import os
import time
import datetime
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException


class Browser(webdriver.Firefox):
    def __init__(self, server_url, options=None, verbose=True, slowly=False, maximize=True):

        if not options:
            options = Options()
            if maximize:
                options.add_argument("--start-maximized")
            else:
                options.add_argument("--window-size=720x800")

        super(Browser, self).__init__(options=options)

        self.verbose = verbose
        self.slowly = slowly
        self.watched = False
        self.server_url = server_url

        if maximize:
            self.maximize_window()
        else:
            self.set_window_position(700, 0)
            self.set_window_size(720, 800)
        self.switch_to.window(self.current_window_handle)

    def wait(self, seconds=1):
        seconds = self.slowly and 3 or seconds
        time.sleep(seconds)

    def watch(self, e):
        if self.watched:
            raise e
        else:
            traceback.print_exc()
            self.watched = True
            self.save_screenshot('/tmp/test.png')
            if 'HEADLESS' not in os.environ:
                input('Type enter to continue...')

    def print(self, message):
        if self.verbose:
            print(message)

    def open(self, url):
        self.get("{}{}".format(self.server_url, url))

    def enter(self, name, value, submit=False, count=2):

        if callable(value):
            value = value()
        if type(value) == datetime.date:
            value = value.strftime('%d/%m/%Y')
        if value:
            self.print('{} "{}" for "{}"'.format('Entering', value, name))
        try:
            if submit:
                self.execute_script("enter('{}', '{}', 1)".format(name, value))
            else:
                self.execute_script("enter('{}', '{}')".format(name, value))
        except WebDriverException as e:
            if count:
                self.wait()
                self.enter(name, value, submit, count-1)
            else:
                self.watch(e)
                
    def choose(self, name, value, count=2):
        self.print('{} "{}" for "{}"'.format('Choosing', value, name))
        try:
            headless = 'HEADLESS' in os.environ and 'true' or 'false'
            self.execute_script("return choose('{}', '{}', {})".format(name, value, headless))
            self.wait(2)
        except WebDriverException as e:
            if count:
                self.wait()
                self.choose(name, value, count-1)
            else:
                self.watch(e)

    def dont_see_error_message(self, testcase=None):
        elements = self.find_elements_by_class_name('alert-danger')
        if elements:
            messages = [element.text for element in elements]
            if 'HEADLESS' not in os.environ:
                input('Type enter to continue...')
            elif testcase:
                exception_message = 'The following messages were found on the page: {}'.format(';'.join(messages))
                raise testcase.failureException(exception_message)

    def look_for(self, text, count=2):
        self.print('Looking for "{}"'.format(text))
        try:
            assert text in self.find_element_by_tag_name('body').text
        except WebDriverException as e:
            if count:
                self.wait()
                self.look_for(text, count-1)
            else:
                self.watch(e)

    def look_at_popup_window(self, count=2):
        self.print('Looking at popup window')
        try:
            self.execute_script("lookAtPopupWindow()")
        except WebDriverException as e:
            if count:
                self.wait()
                self.look_at_popup_window(count-1)
            else:
                self.watch(e)

    def look_at(self, text, count=2):
        self.print('Loking at "{}"'.format(text))
        try:
            self.execute_script("lookAt('{}')".format(text))
        except WebDriverException as e:
            if count:
                self.wait()
                self.look_at(text, count-1)
            else:
                self.watch(e)

    def look_at_panel(self, text, count=2):
        self.print('Looking at panel "{}"'.format(text))
        try:
            self.execute_script("lookAtPanel('{}')".format(text))
        except WebDriverException as e:
            if count:
                self.wait()
                self.look_at_panel(text, count-1)
            else:
                self.watch(e)

    def click_menu(self, *texts):
        self.print('Clicking menu "{}"'.format('->'.join(texts)))
        self.wait()
        for text in texts:
            self.wait()
            try:
                self.execute_script("clickMenu('{}')".format(text.strip()))
            except WebDriverException as e:
                self.watch(e)
        self.wait()

    def click_link(self, text):
        self.print('Clicking link "{}"'.format(text))
        try:
            self.execute_script("clickLink('{}')".format(text))
        except WebDriverException as e:
            self.watch(e)
        self.wait()

    def click_button(self, text):
        self.print('Clicking button "{}"'.format(text))
        try:
            self.execute_script("clickButton('{}')".format(text))
        except WebDriverException as e:
            self.watch(e)
        self.wait()
        self.dont_see_error_message()
        
    def click_tab(self, text):
        self.print('Clicking tab "{}"'.format(text))
        try:
            self.execute_script("clickTab('{}')".format(text))
        except WebDriverException as e:
            self.watch(e)
        self.wait()

    def click_icon(self, name):
        self.print('Clicking icon "{}"'.format(name))
        try:
            self.execute_script("clickIcon('{}')".format(name))
        except WebDriverException as e:
            self.watch(e)
        self.wait()

    def logout(self):
        self.print('Logging out')
        self.click_icon('Configurações')
        self.wait()
        self.click_link('Sair')
        self.wait()

    def close(self, seconds=0):
        self.wait(seconds)
        super(Browser, self).close()

