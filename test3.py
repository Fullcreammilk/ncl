import os
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk


class RootWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")  # 窗口大小

        self.first=StringVar()
        self.second=StringVar()

        menu0 = Menu(self.root)  # 参数是父级控件
        # 二级菜单
        cascade0 = Menu(menu0, tearoff=False)   # tearoff=False 表示这个菜单不可以被拖出来
        for x in ['SPS预测预测', 'SPS预测回报']:
            cascade0.add_radiobutton(label=x,variable = self.first,command = lambda : {self.begin()})

        menu0.add_cascade(label='SPS预测', menu=cascade0)

        for x in ['EPS预测', '历史资料查询', '系统设置', '系统帮助']:
            menu0.add_command(label=x)

        self.root.config(menu=menu0)  # 窗口root的menu是menu0

    def begin(self):
        self.cofigwin(self.first.get())

    def cofigwin(self,wintype):
        top = tk.Toplevel()
        top.option_add('*Font', 'Verdana 12 bold')
        top.master.title('ncl')
        top.master.iconname('ncl')

        mainframe = Frame(top)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        year = StringVar()
        season = StringVar()
        area = StringVar()
        factor = StringVar()
        precision = StringVar()

        mainframe.label_year = Label(mainframe, text="年份:")
        mainframe.label_season = Label(mainframe, text="季节:")
        mainframe.label_area = Label(mainframe, text="地区:")
        mainframe.label_factor = Label(mainframe, text="要素:")
        mainframe.label_precision = Label(mainframe, text="检验:")

        mainframe.entry_year = Entry(mainframe, relief=SUNKEN, textvariable=year)
        mainframe.entry_season = Entry(mainframe, relief=SUNKEN, textvariable=season)
        mainframe.entry_area = Entry(mainframe, relief=SUNKEN, textvariable=area)
        mainframe.entry_factor = Entry(mainframe, relief=SUNKEN, textvariable=factor)
        mainframe.entry_precision = Entry(mainframe, relief=SUNKEN, textvariable=precision)

        mainframe.button_ok = Button(mainframe, text="确认", width=20,
                                     command=lambda a=year, b=season, c=area, d=factor, e=precision: {self.execute(a,b,c,d,e),
                                                                                                      top.destroy()})
        mainframe.button_cancel = Button(mainframe, text="清除", width=20,
                                         command=lambda a=year, b=season, c=area, d=factor, e=precision: {a.set(''),
                                                                                                          b.set(''),
                                                                                                          c.set(''),
                                                                                                          d.set(''),
                                                                                                          e.set('')})

        mainframe.label_year.grid(row=0, column=0, sticky=(N, W))
        mainframe.label_season.grid(row=1, column=0, sticky=(N, W))
        mainframe.label_area.grid(row=2, column=0, sticky=(N, W))
        mainframe.label_factor.grid(row=3, column=0, sticky=(N, W))
        if wintype == 'SPS预测回报':
            mainframe.label_precision.grid(row=4, column=0, sticky=(N, W))

        mainframe.entry_year.grid(row=0, column=1, sticky=(N, W))
        mainframe.entry_season.grid(row=1, column=1, sticky=(N, W))
        mainframe.entry_area.grid(row=2, column=1, sticky=(N, W))
        mainframe.entry_factor.grid(row=3, column=1, sticky=(N, W))
        if wintype == 'SPS预测回报':
            mainframe.entry_precision.grid(row=4, column=1, sticky=(N, W))

        mainframe.button_ok.grid(row=5, column=0, sticky=(N, W))
        mainframe.button_cancel.grid(row=5, column=1, sticky=(N, W))

    def execute(self,year,season,area,factor,precision):
        path="resource"
        dirs = os.listdir(path)
        url1="resource"
        url2="resource"
        for dir in dirs:
            if year.get() =='' or season.get() =='' or area.get() =='' or factor.get() =='':
                url1="resource/error.png"
                url2 = "resource/error.png"
            elif year.get() in dir and season.get() in dir and area.get() in dir and factor.get() in dir:
                url1=url1+'/'+dir
                if precision.get() != '':
                    url2=url2+'/'+dir

        if len(url1)<=8:
            url1="resource/error.png"

        if len(url2)<=8:
            url2="resource/error.png"

        pil_image1 = Image.open(url1)
        pil_image1 = pil_image1.resize((390, 400), Image.ANTIALIAS)
        self.root.img1 = ImageTk.PhotoImage(pil_image1)
        label_img1 = Label(self.root, image=self.root.img1, compound=CENTER)
        pil_image2 = Image.open(url2)
        pil_image2 = pil_image2.resize((390, 400), Image.ANTIALIAS)
        self.root.img2 = ImageTk.PhotoImage(pil_image2)
        label_img2 = Label(self.root, image=self.root.img2, compound=CENTER)

        label_img1.grid(row=0, column=0, sticky=W)
        label_img2.grid(row=0, column=1, sticky=E)


rootWin=RootWin()
rootWin.root.mainloop()