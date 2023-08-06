# -*- coding: utf-8 -*-
import random
import curses
import time  #: 3
import os
import signal
from time import sleep
from subprocess import Popen, PIPE, DEVNULL
from djangoplus.tutorial.utils import display_subtitle, simulate_type, simulate_command_type


class Subtitle(object):

    def display(self, message, duration=4):
        display_subtitle(message, duration)


class Terminal(object):

    def __init__(self, verbose=True, python='python'):
        self.proccess = None
        self.verbose = verbose
        self.python = python

    def execute(self, command, clear=True, base_dir=None):
        if clear:
            os.system('clear')
            simulate_type('', shell=True)
        if self.verbose:
            simulate_command_type(command, shell=True)
        if command.startswith('python'):
            command.replace('python', self.python)
        if base_dir:
            command = 'cd {} && {}'.format(base_dir, command)
        if not self.verbose:
            command = '{}  > /dev/null'.format(command)
        os.system(command)

    def show(self, visible=True):
        minimize_terminal_script = '''
            tell application "Terminal"
              set miniaturized of window 1 to {}
            end tell
        '''.format(visible and 'false' or 'true')
        self.proccess = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.proccess.communicate(minimize_terminal_script.encode())

    def hide(self):
        self.show(False)


class HttpServer(object):
    def __init__(self, base_dir, verbose=True, python='python'):
        self.process = None
        self.base_dir = base_dir
        self.verbose = verbose
        self.python = python

    def start(self):
        command = 'cd {} && {} manage.py runserver'.format(self.base_dir, self.python)
        if self.verbose:
            os.system('clear')
            simulate_type('python manage.py runserver', shell=True)
            stdout = PIPE
        else:
            stdout = DEVNULL
        self.process = Popen(command, stdout=stdout, stderr=PIPE, shell=True, preexec_fn=os.setsid)
        sleep(5)

    def stop(self):
        if self.verbose:
            print('^C')
        if self.process:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)


class VideoRecorder(object):
    def __init__(self):
        self.proccess = None

    def start(self):
        self.proccess = Popen(['ffmpeg', '-y', '-f', 'avfoundation', '-i', '1', '/tmp/video.mkv'], stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        sleep(5)

    def stop(self, file_name=None, audio_file_path=None):
        os.kill(self.proccess.pid, signal.SIGTERM)
        sleep(2)
        tmp_file_path = '/tmp/video.mkv'
        desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        output_file_path = '{}/{}.mkv'.format(desktop_path, file_name)
        if file_name:
            if os.path.exists(output_file_path):
                os.unlink(output_file_path)
            os.rename(tmp_file_path, output_file_path)
            if audio_file_path:
                output_audio_path = '{}/tmp{}.mkv'.format(desktop_path, file_name)
                combine_audio_cmd = 'ffmpeg -y -i {} -i {} -c copy -map 0:0 -map 1:0 -shortest {}  > /dev/null 2>&1'
                os.system(combine_audio_cmd.format(output_file_path, audio_file_path, output_audio_path))
                sleep(5)
                os.rename(output_audio_path, output_file_path)


class EditorSimulator(object):

    COMMENT_MARKUP = '{}{} '.format('#', ':')

    def __init__(self, file_path=None, slow=True):  #: 0 Definindo o construtor
        self.screen = None  #: 0
        self.height = 0  #: 0
        self.width = 0  #: 0
        self.top = []  #: 0
        self.center = []  #: 0
        self.bottom = []  #: 0
        self.steps = {}  #: 0
        self.slow = slow  #: 0

        if file_path:  #: 0
            self.lines = open(file_path).readlines()  #: 0
        else:  #: 0
            self.lines = []  #: 0

        self.initialize_curses()

    def initialize_curses(self):
        self.screen = curses.initscr()
        self.height, self.width = self.screen.getmaxyx()

        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        curses.curs_set(0)

        self.top = []
        self.center = []
        self.bottom = []
        self.steps = {}

    def proccess_lines(self, start_step=None, end_step=None):
        i = 0
        for j, line in enumerate(self.lines):
            tokens = line.split(EditorSimulator.COMMENT_MARKUP)
            if len(tokens) > 1:
                step_number = float(tokens[1].strip().split()[0])
                if j and not self.lines[j - 1].strip():
                    self.lines[j - 1] = '{}{}{}'.format(self.lines[j - 1], EditorSimulator.COMMENT_MARKUP, step_number)
        for j, text in enumerate(self.lines):
            j += 1
            tokens = text.split(EditorSimulator.COMMENT_MARKUP)
            text = tokens[0].rstrip()
            if len(tokens) > 1:
                step = tokens[1].strip()
                step_number = float(step.split()[0])
                step_message = ' '.join(step.split()[1:]).strip()
                if start_step and step_number < start_step:
                    step_number = None
                    step_message = ''
            else:
                step_number = None
                step_message = ''
            if step_number is None:
                if i < self.height-1:
                    self.center.append(text)
                    self.screen.addstr(i, 0, text[0:self.width-1])
                    i += 1
                else:
                    self.bottom.append(text)
            else:
                if step_number not in self.steps:
                    self.steps[step_number] = []
                for line in self.lines[:j]:
                    tokens = line.replace('\n', '').split(EditorSimulator.COMMENT_MARKUP)
                    if len(tokens) > 1 and float(tokens[1].strip().split()[0]) > step_number:
                        j -= 1
                self.steps[step_number].append([text, j, step_message])

        self.screen.refresh()

    def simulate(self, start_step=None, end_step=None, pause=False):  #: 1 Definindo o método "simulate"
        if not self.screen:  #: 1
            self.initialize_curses()  #: 1
        self.proccess_lines(start_step, end_step)  #: 1
        for step in sorted(self.steps.keys()):  #: 1
            if end_step is not None and step > float(end_step):  #: 1
                break  #: 1
            for text, i, message in self.steps[step]:  #: 1
                if message:  #: 1
                    display_subtitle(message, self.slow and 3 or 1)  #: 1
                self.write(text, i)  #: 1
        self.close(validate=end_step is None, pause=pause)  #: 1

    def scroll(self, i):
        time.sleep(random.random() * 10.0 / (self.slow and 400 or 50))
        first_visible_line = len(self.top)
        # text goes up
        if i > first_visible_line:
            for j in range(first_visible_line, i):
                text = self.center.pop(0)
                self.top.append(text)
                self.screen.move(0, 0)
                self.screen.deleteln()
                if self.bottom:
                    text = self.bottom.pop(0)
                    self.center.append(text)
                    self.screen.addstr(len(self.center)-1, 0, text)
                self.screen.refresh()
                time.sleep(0.1)
        # text goes down
        elif i < first_visible_line:
            self.screen.move(0, 0)
            for j in range(i, first_visible_line):
                if self.top:
                    text = self.top.pop()
                    self.center.insert(0, text)
                    self.screen.insertln()
                    self.screen.addstr(0, 0, text)
                    if len(self.center) > self.height-1:
                        text = self.center.pop()
                        self.bottom.insert(0, text)
                    self.screen.refresh()
                    time.sleep(0.1)
        self.screen.refresh()

    def write(self, text, i, start=0):
        middle = int(self.height/2)
        if len(self.center) > middle and i > middle:
            shift = middle
            self.scroll(i-shift-1)
        else:
            shift = i - 1
            self.scroll(i - shift - 1)
        self.screen.move(0 + shift, 0)
        curses.setsyx(0 + shift, 0)
        if start:
            self.center[0] = '{}{}{}'.format(self.center[0][:start], text, self.center[0][start:])
        else:
            self.screen.insdelln(1)
            self.center.insert(0+shift, text)
            if len(self.center) == self.height:
                self.bottom.insert(0, self.center.pop())
        for j, c in enumerate(text):
            if j > 0:
                curses.curs_set(1)
            if start:
                self.screen.insstr(0+shift, start+j, c, curses.color_pair(1))
            else:
                self.screen.addstr(0+shift, j, c, curses.color_pair(1))
            time.sleep(random.random() * 10.0 / (self.slow and 50 or 400))
            self.screen.refresh()
            curses.curs_set(0)

    def save(self, file_path):  #: 4 Definindo o método "save"
        tmp = open(file_path, 'w')  #: 4
        tmp.write(self.get_content())  #: 4
        tmp.flush()  #: 4
        tmp.close()  #: 4

    def get_content(self):
        l = list()
        if self.top:
            l.append('\n'.join(self.top))
            l.append('\n')
        l.append('\n'.join(self.center))
        if self.bottom:
            l.append('\n')
            l.append('\n'.join(self.bottom))
        return ''.join(l)

    def validate(self):
        l = list()
        for line in self.lines:
            l.append(line.split(EditorSimulator.COMMENT_MARKUP)[0].rstrip())
        original_content = '\n'.join(l)
        content = self.get_content()
        if not original_content == content:
            open('/tmp/output0.txt', 'w').write(original_content)
            open('/tmp/output1.txt', 'w').write(content)
            raise Exception('Output content does not mach original content!!!')

    def close(self, pause=False, validate=False):  #: 2 Definindo a função "close"
        if pause:  #: 2
            self.screen.getch()  #: 2
        if validate:  #: 2
            self.validate()  #: 2
        if self.screen:
            self.screen.clear()  #: 2
            curses.endwin()  #: 2
            sleep(1)  #: 2
        self.screen = None  #: 2
