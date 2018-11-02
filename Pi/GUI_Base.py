#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Jun 17, 2018 04:29:46 PM

import sys
import picamera
import threading
import time
import os
#import SharedFunctions
        
def create_controller():
    os.system("printf 'raspberry\n' | sudo -S python3 HornClient.py")

#cli_thread = threading.Thread(target=create_controller)
#cli_thread.daemon = True
#cli_thread.start()

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


def vp_start_gui():
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    root.withdraw()
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel():
    def __init__(self, top=None):
        self.leftSpeed = self.rightSpeed = self.frontSpeed = self.backSpeed = 0
        self.text_roll = self.text_yaw = self.text_pitch = self.text_temperature = self.text_depth = "0"
        self.text_horn = "0"
        self.heard_time = self.sent_time = 0
        self.triangle = 0
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1280x720+0+0")
        top.title("ROV Command Hub")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.CameraFrame = Frame(top)
        self.CameraFrame.place(relx=0.59, rely=0.03, relheight=0.51, relwidth=0.39)
        self.CameraFrame.configure(borderwidth="2")
        self.CameraFrame.configure(relief=GROOVE)
        self.CameraFrame.configure(background="#d9d9d9")
        self.CameraFrame.configure(highlightbackground="#d9d9d9")
        self.CameraFrame.configure(highlightcolor="black")
        self.CameraFrame.configure(width=530)
        self.camera = picamera.PiCamera()
        self.camera.start_preview(fullscreen=False, window = (620, 2, 650, 450))

        self.ModelFrame = Frame(top)
        self.ModelFrame.place(relx=0.01, rely=0.03, relheight=0.51, relwidth=0.39)
        self.ModelFrame.configure(borderwidth="2")
        self.ModelFrame.configure(relief=GROOVE)
        self.ModelFrame.configure(background="#FFFFFF")
        self.ModelFrame.configure(highlightbackground=None)
        self.ModelFrame.configure(highlightcolor=None)
        self.ModelFrame.configure(width=535)

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.01, rely=0.65, relheight=0.27, relwidth=0.96)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=1305)

        self.HornLabel = ttk.Label(self.Frame3)
        self.HornLabel.place(relx=0.01, rely=0.05, height=16, width=219)
        self.HornLabel.configure(background="#d9d9d9")
        self.HornLabel.configure(foreground="#000000")
        self.HornLabel.configure(font="TkDefaultFont")
        self.HornLabel.configure(relief=FLAT)
        self.HornLabel.configure(text=self.text_horn)

        self.RollLabel = ttk.Label(self.Frame3)
        self.RollLabel.place(relx=0.01, rely=0.24, height=16, width=200)
        self.RollLabel.configure(background="#d9d9d9")
        self.RollLabel.configure(foreground="#000000")
        self.RollLabel.configure(font="TkDefaultFont")
        self.RollLabel.configure(relief=FLAT)
        self.RollLabel.configure(text=self.text_roll)

        self.PitchLabel = ttk.Label(self.Frame3)
        self.PitchLabel.place(relx=0.01, rely=0.34, height=16, width=171)
        self.PitchLabel.configure(background="#d9d9d9")
        self.PitchLabel.configure(foreground="#000000")
        self.PitchLabel.configure(font="TkDefaultFont")
        self.PitchLabel.configure(relief=FLAT)
        self.PitchLabel.configure(text=self.text_pitch)

        self.YawLabel = ttk.Label(self.Frame3)
        self.YawLabel.place(relx=0.01, rely=0.44, height=16, width=83)
        self.YawLabel.configure(background="#d9d9d9")
        self.YawLabel.configure(foreground="#000000")
        self.YawLabel.configure(font="TkDefaultFont")
        self.YawLabel.configure(relief=FLAT)
        self.YawLabel.configure(text=self.text_yaw)

        self.TemperatureLabel = ttk.Label(self.Frame3)
        self.TemperatureLabel.place(relx=0.31, rely=0.24, height=16, width=200)
        self.TemperatureLabel.configure(background="#d9d9d9")
        self.TemperatureLabel.configure(foreground="#000000")
        self.TemperatureLabel.configure(font="TkDefaultFont")
        self.TemperatureLabel.configure(relief=FLAT)
        self.TemperatureLabel.configure(text=self.text_temperature)
        
        self.DepthLabel = ttk.Label(self.Frame3)
        self.DepthLabel.place(relx=0.31, rely=0.34, height=16, width=170)
        self.DepthLabel.configure(background="#d9d9d9")
        self.DepthLabel.configure(foreground="#000000")
        self.DepthLabel.configure(font="TkDefaultFont")
        self.DepthLabel.configure(relief=FLAT)
        self.DepthLabel.configure(text=self.text_depth)

        self.frontSpeed_name = ttk.Label(self.Frame3)
        self.frontSpeed_name.place(relx=0.625, rely=0.04, height=16, width=140)
        self.frontSpeed_name.configure(text="Front Motor Speed")
        self.fspeed_bar = ttk.Progressbar(self.Frame3, mode='determinate')
        self.fspeed_bar.place(relx=0.61, rely=0.12, height=16, width=171)
        self.fspeed_bar.configure(maximum=1998)
        self.fspeed_bar.configure(value=self.frontSpeed)

        self.leftSpeed_name = ttk.Label(self.Frame3)
        self.leftSpeed_name.place(relx=0.525, rely=0.34, height=16, width=140)
        self.leftSpeed_name.configure(text="Left Motor Speed")
        self.lspeed_bar = ttk.Progressbar(self.Frame3, mode='determinate')
        self.lspeed_bar.place(relx=0.51, rely=0.42, height=16, width=171)
        self.lspeed_bar.configure(maximum=1998)
        self.lspeed_bar.configure(value=self.leftSpeed)

        self.rightSpeed_name = ttk.Label(self.Frame3)
        self.rightSpeed_name.place(relx=0.695, rely=0.34, height=16, width=140)
        self.rightSpeed_name.configure(text="Right Motor Speed")
        self.rspeed_bar = ttk.Progressbar(self.Frame3, mode='determinate')
        self.rspeed_bar.place(relx=0.68, rely=0.42, height=16, width=171)
        self.rspeed_bar.configure(maximum=1998)
        self.rspeed_bar.configure(value=self.rightSpeed)

        self.backSpeed_name = ttk.Label(self.Frame3)
        self.backSpeed_name.place(relx=0.625, rely=0.64, height=16, width=140)
        self.backSpeed_name.configure(text="Back Motor Speed")
        self.bspeed_bar = ttk.Progressbar(self.Frame3, mode='determinate')
        self.bspeed_bar.place(relx=0.61, rely=0.72, height=16, width=171)
        self.bspeed_bar.configure(maximum=1998)
        self.bspeed_bar.configure(value=self.backSpeed)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.48, rely=0.54, height=66, width=655)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=self.screenshot)
        self.Button1.configure(text='''Take Photo''')
        self.Button1.configure(width=520)

        self.updateData()


    def updateData(self):
        # raw_data writes to data.txt for the gui and model to read
        
        try:
            sent = open('sent.txt', 'r')
            self.sent_time = float(sent.readlines()[-1])
            sent.close()
        except:
            pass

        try:
            received = open('received.txt', 'r')
            self.heard_time = float(received.readlines()[-1])
            received.close()
        except:
            pass

        try:
            f = open('data.txt', 'r')
            self.data = (f.readlines()[-1])[1:-2].split(',')
            # print(data[0])
            self.pitch = float(self.data[0])
            self.roll = float(self.data[1])
            self.yaw = float(self.data[2])
            self.temperature = float(self.data[3])
            self.depth = float(self.data[4])
            f.close()
        except:
            pass

        self.text_pitch = "Pitch: " + str(self.pitch)
        self.PitchLabel.configure(text=self.text_pitch)

        self.text_roll = ("Roll (Must be near 0): " + str(self.roll))
        self.RollLabel.configure(text=self.text_roll)

        self.text_yaw = ("Yaw: " + str(self.yaw))
        self.YawLabel.configure(text=self.text_yaw)
        
        self.text_temperature = ("Temperature: " + str(self.temperature))
        self.TemperatureLabel.configure(text=self.text_temperature)
        
        self.text_depth = ("Depth: " + str(self.depth))
        self.DepthLabel.configure(text=self.text_depth)
        
        # only updates when the sent and heard time correspond to the same ping 
        if self.heard_time - self.sent_time < 7 and self.heard_time - self.sent_time > 0:
            self.text_horn = ("Time (from Horn): " + str(self.heard_time - self.sent_time))
            self.HornLabel.configure(text=self.text_horn)

        try:
            cont_f = open('controller_data.txt', 'r')
            self.cont_data = (cont_f.readlines()[-1])[1:-2].split(',')
            self.frontSpeed = float(self.cont_data[0])
            self.backSpeed = float(self.cont_data[1])
            self.leftSpeed = float(self.cont_data[2])
            self.rightSpeed = float(self.cont_data[3])
            self.triangle = float(self.cont_data[4])
            cont_f.close()
        except:
            pass

        if self.triangle == 1:
            self.screenshot()
        self.lspeed_bar.configure(value=self.leftSpeed)
        self.rspeed_bar.configure(value=self.rightSpeed)
        self.fspeed_bar.configure(value=self.frontSpeed)
        self.bspeed_bar.configure(value=self.backSpeed)
        

        # updates the Labels every 100 ms
        self.Frame3.after(100, self.updateData)
        
    def screenshot(self):
        self.amount = 0
        AmountFile = open('Photos/amount', 'r')
        self.x = AmountFile.readline().strip()
        try:
            self.amount = int(self.x)
        except ValueError:
            print("WHY??")
        AmountFile.close()
        self.camera.capture('Photos/' + 'snapshot' + str(self.amount) + '.jpg')
        self.amount += 1
        WriteAmount = open('Photos/amount', 'w')
        WriteAmount.write("%d" % self.amount)


if __name__ == '__main__':
    vp_start_gui()

