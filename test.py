#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import * # 导入 Tkinter 库

import tkinter.messagebox

from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk


class NCL(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Verdana 12 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('ncl')
        self.master.iconname('ncl')
        # self.master.geometry('500x300')

        mainframe = Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        type = StringVar()
        year = StringVar()
        season = StringVar()

        mainframe.label_type = Label(mainframe, text="类型:")
        mainframe.label_year = Label(mainframe, text="年份:")
        mainframe.label_season = Label(mainframe, text="季节:")

        mainframe.entry_type = Entry(mainframe, relief=SUNKEN, textvariable=type)
        mainframe.entry_year = Entry(mainframe, relief=SUNKEN, textvariable=year)
        mainframe.entry_season = Entry(mainframe, relief=SUNKEN, textvariable=season)

        mainframe.button_ok = Button(mainframe, text="确认", width=20,command = self.clickOK)
        mainframe.button_cancel = Button(mainframe, text="清除", width=20, command = lambda a=type,b=year,c=season:{a.set(''),b.set(''),c.set('')})

        mainframe.label_type.grid(row=0, column=0,sticky=(N,W))
        mainframe.label_year.grid(row=1, column=0,sticky=(N,W))
        mainframe.label_season.grid(row=2, column=0,sticky=(N,W))
        mainframe.entry_type.grid(row=0, column=1,sticky=(N,W))
        mainframe.entry_year.grid(row=1, column=1,sticky=(N,W))
        mainframe.entry_season.grid(row=2, column=1,sticky=(N,W))
        mainframe.button_ok.grid(row=3, column=0,sticky=(N,W))
        mainframe.button_cancel.grid(row=3, column=1,sticky=(N,W))

    def clickOK(self):
        url = "resource/test.png"
        pil_image = Image.open(url)
        pil_image = pil_image.resize((500, 500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(pil_image)
        label_img = Label(self, image=self.img, compound=CENTER)
        label_img.grid(row=4, column=0, sticky=W)


if __name__ == '__main__':
    NCL().mainloop()