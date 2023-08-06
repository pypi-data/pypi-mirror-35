# -*- coding: utf-8 -*-
import re
import platform
import os
import signal
from time import sleep
from subprocess import Popen, PIPE, DEVNULL


class Subtitle(object):

    @staticmethod
    def display(message, duration=4):
        import tkinter as tk
        root = tk.Tk()
        root.overrideredirect(True)
        root.wm_attributes("-topmost", True)
        root.attributes('-alpha', 0.8)
        root.configure(background='black')
        lines = list()
        break_line = False
        for i, letter in enumerate(message):
            if break_line or i and i % 50 == 0:
                if letter == ' ':
                    lines.append('\n')
                    break_line = False
                else:
                    break_line = True
            lines.append(letter)
        message = ''.join(lines)
        line_breaks = message.count('\n')
        if 'darwin' in platform.system().lower():
            font_size, width, top, right = 30, 82, int(root.winfo_screenwidth() / 2 - 20 * 35), int(
                root.winfo_screenheight() - [90, 120, 156][line_breaks])
        else:
            font_size, width, top, right = 20, 70, int(root.winfo_screenwidth() / 2 - 70 * 7.5), int(
                root.winfo_screenheight() - [77, 110, 140][line_breaks])
        label = tk.Label(root, text=message, font=("Helvetica", font_size), width=width, height=2 + line_breaks)
        label.configure(foreground="white", background='black')
        label.pack(expand=tk.YES, fill=tk.BOTH)
        root.geometry("+{}+{}".format(top, right))
        root.after(1000 * duration, lambda: root.destroy())
        root.mainloop()


class VideoRecorder(object):
    def __init__(self):
        self.proccess = None

    def start(self):
        if 'darwin' in platform.system().lower():
            list_divices_procces = Popen('ffmpeg -f avfoundation -list_devices true -i ""'.split(), stdout=PIPE, stderr=PIPE)
            output, err = list_divices_procces.communicate()
            i = 0
            for line in err.decode('utf-8').split('\n'):
                if 'capture screen' in line.lower():
                    for i in range(0, 3):
                        if '[{}]'.format(i) in line:
                            break
            self.proccess = Popen(['ffmpeg', '-y', '-f', 'avfoundation', '-i', str(i), '/tmp/video.mkv'], stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        else:
            xrandr = Popen("xrandr".split(), stdout=PIPE)
            sizes = xrandr.stdout.readlines()
            size = re.findall(r'\d+x\d+', [line.decode('utf-8').strip().split()[0] for line in sizes if '*' in line.decode('utf-8')][0])[0]
            cmd = 'ffmpeg -video_size {} -framerate 25 -f x11grab -i :0.0+0,0 -f pulse -ac 2 -i default /tmp/video.mkv'
            self.proccess = Popen(cmd.format(size).split(), stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        sleep(5)

    def stop(self, file_name=None, audio_file_path=None):
        os.kill(self.proccess.pid, signal.SIGTERM)
        sleep(2)
        tmp_file_path = '/tmp/video.mkv'
        desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        if not os.path.exists(desktop_path):
            desktop_path = os.path.join(os.path.expanduser('~'))
        output_file_path = '{}/{}.mkv'.format(desktop_path, file_name)
        if file_name:
            if os.path.exists(output_file_path):
                os.unlink(output_file_path)
            os.rename(tmp_file_path, output_file_path)
            print('Video Ouput: {}'.format(output_file_path))
            if audio_file_path and 'darwin' in platform.system().lower():
                output_audio_path = '{}/tmp{}.mkv'.format(desktop_path, file_name)
                combine_audio_cmd = 'ffmpeg -y -i {} -i {} -c copy -map 0:0 -map 1:0 -shortest {}  > /dev/null 2>&1'
                os.system(combine_audio_cmd.format(output_file_path, audio_file_path, output_audio_path))
                sleep(5)
                os.rename(output_audio_path, output_file_path)
