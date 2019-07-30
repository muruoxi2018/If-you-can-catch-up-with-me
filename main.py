#      ┏┛ ┻━━━━━┛ ┻┓
#      ┃　　　　　　 ┃
#      ┃　　　━　　　┃
#      ┃　┳┛　  ┗┳　┃
#      ┃　　　　　　 ┃
#      ┃　　　┻　　　┃
#      ┃　　　　　　 ┃
#      ┗━┓　　　┏━━━┛
#        ┃　　　┃   神兽保佑
#        ┃　　　┃   代码无BUG！
#        ┃　　　┗━━━━━━━━━┓
#        ┃　　　　　　　    ┣┓
#        ┃　　　　         ┏┛
#        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
#          ┃ ┫ ┫   ┃ ┫ ┫
#          ┗━┻━┛   ┗━┻━┛
import tkinter
import tkinter.messagebox
import random

win = tkinter.Tk()  # 生成一个Tk对象来初始化窗口信息
win.title("小游戏：  如果你能抓到我")
width, height = win.maxsize()
# 根据屏幕大小动态生成窗口尺寸，防止在过小屏幕下游戏体验较差
win.geometry("{}x{}+{}+{}".format(width-600, height-300, 300, 150))

label1 = tkinter.Label(win, text='愚蠢的凡人幺，你是抓不到我的',
                       font=("黑体", 28))  # 创建一个标签组件，初始化组件位置
label1.pack()
label1.update()  # 刷新组件信息
label1.place(x=(win.winfo_width()-label1.winfo_width())/2,
             y=(win.winfo_height()-label1.winfo_height())/2*0.65)  # 计算组件大小，让按钮能自适应窗口位置


def start():
    button1.destroy()  # 销毁按钮
    label1.destroy()  # 销毁标签
    button2.place(x=place_x(), y=place_y())  # 加载游戏按钮


button1 = tkinter.Button(
    win, text='点击开始', command=start, width=30, font=("黑体", 18))
button1.pack()
button1.update()    # 刷新组件信息
button1.place(x=(win.winfo_width()-button1.winfo_width()) /
              2, y=label1.winfo_y()/0.65)


def good():
    tkinter.messagebox.showinfo('游戏结束', '恭喜你抓到我嘞！')


button2 = tkinter.Button(win, text='如果你能点到我\n我就让你嘿嘿嘿',
                         command=good, font=("黑体", 18))
button2.pack()
button2.update()
button2.pack_forget()   # 将按钮加载到内存但不显示在窗口上


def func(event):
    # print(event.x, event.y)    打印鼠标坐标，用来调试
    button2.place(x=place_x(), y=place_y())


button2.bind('<Enter>', func)  # 接收鼠标进入按钮的事件


def place_x():  # 随机生成x坐标，防止超出窗口
    return random.randint(0, win.winfo_width()-button2.winfo_width())


def place_y():  # 随机生成y坐标，防止超出窗口
    return random.randint(0, win.winfo_height()-button2.winfo_height())


win.mainloop()  # 循环窗体消息
