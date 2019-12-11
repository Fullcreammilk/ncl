import os
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk


d_area={"北部zq":"BBZQ", "南部zq":"NBZQ", "中部zq":"ZBZQ", "西部zq":"XBZQ", "兰州区域":"LZRCC"
                ,"乌鲁木齐区域":"WLMQRCC", "沈阳区域":"SYRCC", "北京区域":"BJRCC", "上海区域":"SHRCC", "广州区域":"GZRCC"
                , "成都区域":"CDRCC", "武汉区域":"WHRCC" , "北半球":"EQ_NH", "一带一路":"Road_Belt","东亚":"EA"
                ,"南亚":"SA","东亚-南亚":"SA_EA","西北太平洋-北印度洋":"NWP_NIO"}

d_factor={"160站降水距平百分率":"rain160x", "160站气温异常":"temp160", "台风GPI":"gpi", "降水异常":"precip", "降水距平百分率":"precipx", "气温异常":"air"}

d_season={"春":"MAM", "夏":"JJA", "秋":"SON", "冬":"DJF"}


class RootWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x450")  # 窗口大小

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

        mainframe.label_year = Label(mainframe, text="年份:")
        mainframe.label_season = Label(mainframe, text="季节:")
        mainframe.label_area = Label(mainframe, text="地区:")
        mainframe.label_factor = Label(mainframe, text="要素:")
        mainframe.label_precision = Label(mainframe, text="检验:")

        mainframe.entry_year = ttk.Combobox(mainframe)
        mainframe.entry_year["value"] = ("2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019")
        mainframe.entry_year.current(0)
        mainframe.entry_season = ttk.Combobox(mainframe)
        mainframe.entry_season["value"] = ("春", "夏", "秋", "冬")
        mainframe.entry_season.current(0)
        mainframe.entry_area = ttk.Combobox(mainframe)
        mainframe.entry_area["value"] = ("北部zq", "南部zq", "中部zq", "西部zq", "兰州区域",
                                         "乌鲁木齐区域", "沈阳区域", "北京区域", "上海区域", "广州区域"
                                         , "成都区域", "武汉区域", "北半球", "一带一路","东亚","南亚","东亚-南亚","西北太平洋-北印度洋")
        mainframe.entry_area.current(0)
        mainframe.entry_factor = ttk.Combobox(mainframe)
        mainframe.entry_factor["value"] = ("160站降水距平百分率", "160站气温异常", "台风GPI", "降水异常", "降水距平百分率", "气温异常")
        mainframe.entry_factor.current(0)
        mainframe.entry_precision = ttk.Combobox(mainframe)
        mainframe.entry_precision["value"] = ("ACC", "PS")


        mainframe.button_ok = Button(mainframe, text="确认", width=22,
                                     command=lambda : { self.execute(mainframe.entry_year.get(),d_season[mainframe.entry_season.get()]
                                                        ,d_area[mainframe.entry_area.get()],d_factor[mainframe.entry_factor.get()],
                                                        mainframe.entry_precision.get()),
                                                        top.destroy()})
        mainframe.button_cancel = Button(mainframe, text="清除", width=22,
                                         command=lambda : { mainframe.entry_year.current(0),
                                                            mainframe.entry_season.current(0),
                                                            mainframe.entry_area.current(0),
                                                            mainframe.entry_factor.current(0),
                                                            mainframe.entry_precision.current(0)})

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
            mainframe.entry_precision.current(0)

        mainframe.button_ok.grid(row=5, column=0, sticky=(N, W))
        mainframe.button_cancel.grid(row=5, column=1, sticky=(N, W))

    def execute(self,year,season,area,factor,precision):
        path="resource"
        dirs = os.listdir(path)
        url1="resource"
        url2="resource"
        for dir in dirs:
            if year in dir and season in dir and area in dir and factor in dir:
                url1=url1+'/'+dir
                break
        if precision == '':
            url2="resource/error.png"
        else:
            for dir in dirs:
                if year in dir and season in dir and area in dir and factor in dir and 'forecast' not in dir:
                    url2=url2+'/'+dir
                    break

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

        if precision != '' and url2 != 'resource/error.png':
            Label(self.root,text='PS=74.00 ACC=0.13', compound=CENTER).grid(row=1,column=1)


rootWin=RootWin()
rootWin.root.mainloop()