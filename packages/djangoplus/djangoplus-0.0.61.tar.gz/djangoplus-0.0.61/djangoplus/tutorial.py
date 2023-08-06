import os
import sys
import signal
import random
from time import sleep
from subprocess import Popen, PIPE, DEVNULL
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

TYPING_SPEED = 50


def simulate_command_type(commands):
    for command in commands.split('&& '):
        if not command.startswith('source'):
            simulate_type(command)


def simulate_type(command):
    for c in command:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(random.random()*10.0/TYPING_SPEED)
    print('')

SERVER_URL = 'http://localhost:8000'
VIRTUALENV_PATH = '/var/opt/.virtualenvs/djangoplus3'
PYTHON_PATH = '{}/bin/python'.format(VIRTUALENV_PATH)
VIRTUALENV_ACTIVATION_PATH = '{}/bin/activate'.format(VIRTUALENV_PATH)


class TutorialMaker:
    def __init__(self, project_name):

        self.runserver = None
        self.driver = None
        self.osascript = None

        self.project_name = project_name
        self.base_dir = '/tmp/{}'.format(project_name)

    def start(self):
        try:
            # Create Project
            self.create_project()
            # Start Django
            self.start_django()
            # Start Selenium
            self.start_selenium()
            # Start Quicktime
            # self.start_quicktime()
            # Start Tutorial
            self.start_tutorial()
        finally:
            # Stop Quicktime
            # self.stop_quicktime()
            # Stop Selenium
            self.stop_selenium()
            # Stop Django
            self.stop_django()
            # Delete Project
            self.delete_project()

    def create_project(self):
        os.system('clear')
        command = 'source {} && cd /tmp && startproject {}'.format(VIRTUALENV_ACTIVATION_PATH, self.project_name)
        self.execute(command)

    def delete_project(self):
        os.system('rm -r {}'.format(self.base_dir))

    def execute(self, command, clear=True):
        if clear:
            os.system('clear')
        simulate_command_type(command)
        if command.startswith('python'):
            command.replace('python', PYTHON_PATH)
        command = 'cd {} && {}'.format(self.base_dir, command)
        os.system(command)

    def access(self, url):
        url = '{}{}'.format(SERVER_URL, url)
        self.driver.get(url)
        sleep(5)

    def start_django(self):
        command = 'cd {} && {} manage.py runserver'.format(self.base_dir, PYTHON_PATH)
        self.runserver = Popen(command, stdout=DEVNULL, stderr=DEVNULL, shell=True, preexec_fn=os.setsid)
        sleep(5)

    def start_selenium(self):
        options = Options()
        options.add_argument("--window-size=720x800")
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_position(720, 0)
        self.driver.set_window_size(720, 800)
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.get("https://www.google.com.br/")

    def start_quicktime(self):
        start_record_script = '''
            tell application "QuickTime Player"
                set newScreenRecording to new screen recording
                tell newScreenRecording
                    start
                end tell
            end tell
        '''
        self.osascript = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = self.osascript.communicate(start_record_script.encode())
        (self.osascript.returncode, stdout.decode(), stderr.decode())
        sleep(5)

    def start_tutorial(self):
        self.execute('ls')
        self.access('/')
        self.restart_django(True)
        self.access('/admin/')

    def stop_quicktime(self):
        stop_record_script = '''
            tell application "QuickTime Player"
                stop document "screen recording"
            end tell
        '''
        self.osascript = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = self.osascript.communicate(stop_record_script.encode())
        (self.osascript.returncode, stdout.decode(), stderr.decode())

    def stop_selenium(self):
        self.driver.close()

    def stop_django(self):
        os.killpg(os.getpgid(self.runserver.pid), signal.SIGTERM)

    def restart_django(self, sync=False):
        self.stop_django()
        if sync:
            self.execute('python manage.py sync', True)
        self.start_django()

if __name__ == '__main__':
    tm = TutorialMaker('abcdef')
    tm.start()