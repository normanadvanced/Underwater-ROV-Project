#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jun 14, 2018 10:42:33 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1366x768+0+0")
        top.title("New Toplevel")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.59, rely=0.03, relheight=0.51, relwidth=0.39)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=530)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.01, rely=0.03, relheight=0.51, relwidth=0.39)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(width=535)

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.01, rely=0.65, relheight=0.27, relwidth=0.96)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(width=1305)

        self.TLabel1 = ttk.Label(self.Frame3)
        self.TLabel1.place(relx=0.01, rely=0.05, height=16, width=219)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Displacement (from Horn):''')

        self.TLabel2 = ttk.Label(self.Frame3)
        self.TLabel2.place(relx=0.01, rely=0.24, height=16, width=79)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Roll:''')

        self.TLabel4 = ttk.Label(self.Frame3)
        self.TLabel4.place(relx=0.01, rely=0.44, height=16, width=83)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Yaw:''')

        self.TLabel3 = ttk.Label(self.Frame3)
        self.TLabel3.place(relx=0.01, rely=0.34, height=16, width=171)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Pitch (NEEDS TO BE 0):''')






if __name__ == '__main__':
    vp_start_gui()



