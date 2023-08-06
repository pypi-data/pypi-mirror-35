# -*- coding: utf-8 -*-
import os
import random
import platform
from time import sleep
import sys

TYPING_SPEED = 50


def simulate_command_type(commands, shell=False):
    for command in commands.split('&& '):
        if not command.startswith('source'):
            simulate_type(command, shell=shell)


def simulate_type(command, shell=False):
    sys.stdout.write('breno@localhost: ~$ ')
    for c in command:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(random.random()*10.0/TYPING_SPEED)
    print('')


# brew install tcl-tk (MAC OS)
# apt-get install tcl python3-tk (UNIX)
def display_subtitle(message, duration=4):
    import tkinter as tk
    root = tk.Tk()
    # Hide the root window drag bar and close button
    root.overrideredirect(True)
    # Make the root window always on top
    root.wm_attributes("-topmost", True)
    # root.wm_attributes("-transparent", True)
    # root.config(bg='systemTransparent')
    root.attributes('-alpha', 0.8)
    root.configure(background='black')
    l = list()
    break_line = False
    for i, letter in enumerate(message):
        if break_line or i and i % 50 == 0:
            if letter == ' ':
                l.append('\n')
                break_line = False
            else:
                break_line = True
        l.append(letter)
    message = ''.join(l)
    line_breaks = message.count('\n')
    if 'darwin' in platform.system().lower():
        font_size, width, top, right = 30, 82, int(root.winfo_screenwidth()/2-20*35), int(root.winfo_screenheight() - [90, 120, 156][line_breaks])
    else:
        font_size, width, top, right = 20, 70, int(root.winfo_screenwidth()/2-70*7.5), int(root.winfo_screenheight() - [77, 110, 140][line_breaks])
    label = tk.Label(root, text=message, font=("Helvetica", font_size), width=width, height=2+line_breaks)
    label.configure(foreground="white", background='black')
    label.pack(expand=tk.YES, fill=tk.BOTH)
    root.geometry("+{}+{}".format(top, right))
    root.after(1000*duration, lambda: root.destroy())
    root.mainloop()