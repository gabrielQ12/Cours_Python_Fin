#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jun 04, 2020 10:25:10 AM EDT  platform: Linux


import multiprocessing
import re
import sys
import tkinter as tk
from tkinter import messagebox
import webbrowser

import web

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def select_all(event):
    global w
    w.Listbox1.select_set(0, tk.END)


mqueu = multiprocessing.Queue()
wc = None
isscanning = False


def btn_scan_click():
    global w, root, wc, isscanning
    target = w, Entry1.get()
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...)'
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' #...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    if not re.match(regex, target):
        messagebox.showerror("Erreur d'URL", "L 'URL saisie n'est pas valide ! ")
        return
    if wc is None:
        wc = web.WebCrawler(target)
    elif wc.url not in target:
        wc.stopped = True
        wc = web.WebCrawler(target)
    if isscanning:
        rep = messagebox.askquestion("Scan en cours" , "Un scan est déjà en cours,  souhaitez-vous l'arreter ? ")
        if rep == 'yes':
            wc.stopped = True
            w.Label5['text'] = "Scan arrêté."
            isscanning = False
            sys.stdout.flush()
            return

    wc.stopped = False
    w.label5['text'] = "Scan en cours ..."
    wc.crawl(mqueue)
    isscanning = True
    root.after(1000, process_queue)
    sys.stdout.flush()


def process_queue():
    global root, isscanning, wc
    try:
        msg = mqueue.get(0)
        while msg != "" and msg != "END":
            w.Listbox1.see(tk.END)
            w.Listbox1.insert(tk.END, msg)
            msg = mqueue.get(0)
        if msg == "END":
            w.label5['text'] = "Scan terminé."
            isscanning = False
            wc.stopped = True
    except Exception as e:
        root.after(1000, process_queue)


def btn_stop_click():
    global wc, isscanning, w
    if wc is not None :
        wc.stopped = True
    isscanning = False
    w.Label5['text'] = "Scan arrêté."
    print('web_scan_support.btn_stop_click')
    sys.stdout.flush()


def btn_check_vuln():
    global w
    for el in w.Listbox1.curselection():
        print(w.Listbox1.get(el))
    print('web_scan_support.btn_check_click')
    sys.stdout.flush()


def btn_help_click():
    print('web_scan_support.btn_help_click')
    webbrowser.open("https://cyberini.com")


def btn_quit_click():
    print('web_scan_support.btn_quit_click')
    destroy_window()
    sys.stdout.flush()


def btn_save_click():
    print('web_scan_support.btn_save_click')
    sys.stdout.flush()


def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import web_scan
    web_scan.vp_start_gui()

















def btn_scan_click():
    print('web_scan_support.btn_scan_click')
    sys.stdout.flush()



def select_all():
    print('web_scan_support.select_all')
    sys.stdout.flush()







