from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# import make_pic_2   在这里导入自己的py包文件
num = 1
url = "resource/2019-春-北半球-降水.png"


def calculate(*args):
    print(addr.get(), ":", port.get())
    # make_pic_2.main(int(fft.get()),int(start.get()),int(stop.get()),int(cent.get()))


# 调用自己的内核函数

def change():  # 更新图片操作
    global num
    num = num + 1
    if num % 3 == 0:
        url1 = "resource/2019-春-北半球-降水.png"
        pil_image = Image.open(url1)
        pil_image = pil_image.resize((500, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        label_img.configure(image=img)
    if num % 3 == 1:
        url1 = "resource/2019-春-北半球-降水.png"
        pil_image = Image.open(url1)
        pil_image = pil_image.resize((500, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        label_img.configure(image=img)
    if num % 3 == 2:
        url1 = "resource/2019-春-北半球-降水.png"
        pil_image = Image.open(url1)
        pil_image = pil_image.resize((500, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        label_img.configure(image=img)
    root.update_idletasks()  # 更新图片，必须update


root = Tk()
root.title("Draw GUI")

mainframe = ttk.Frame(root, padding="5 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

addr = StringVar()
port = StringVar()
fft = StringVar()
cent = StringVar()
start = StringVar()
stop = StringVar()

ttk.Label(mainframe, text="Address:").grid(column=1, row=1, sticky=W)
addr_entry = ttk.Entry(mainframe, width=7, textvariable=addr)
addr_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Port:").grid(column=3, row=1, sticky=W)
port_entry = ttk.Entry(mainframe, width=7, textvariable=port)
port_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="FFt:").grid(column=1, row=2, sticky=W)
fft_entry = ttk.Combobox(mainframe, width=7, textvariable=fft)
fft_entry['values'] = (2048, 4096, 8192)
fft_entry.current(1)
fft_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="CenterFR:").grid(column=3, row=2, sticky=W)
cent_entry = ttk.Entry(mainframe, width=7, textvariable=cent)
cent_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="StartFR:").grid(column=1, row=3, sticky=W)
start_entry = ttk.Entry(mainframe, width=7, textvariable=start)
start_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="StopFR:").grid(column=3, row=3, sticky=W)
stop_entry = ttk.Entry(mainframe, width=7, textvariable=stop)
stop_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Draw!", command=calculate).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Update!", command=change).grid(column=4, row=4, sticky=W)

pil_image = Image.open(url)
pil_image = pil_image.resize((500, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(pil_image)
label_img = ttk.Label(root, image=img, compound=CENTER)
label_img.grid(column=0, row=5, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
addr_entry.focus()

root.bind('<Return>', calculate)  # 主循环，除了这一行可以一直循环，其他行只执行一次

if __name__ == '__main__':
    root.mainloop()
