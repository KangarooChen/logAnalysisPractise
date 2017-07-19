#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox
import tkFileDialog
import ex2
top = Tkinter.Tk()
top.title('位置信息分析')
top.geometry('100x40')

# l = Tkinter.Label(top,text='选择文件',font='Arial -20 bold')

openwindow = tkFileDialog.askopenfilename()
print "open", openwindow.encode('utf-8')
if not openwindow.encode('utf-8'):
	tkMessageBox.showerror('No File selected!','One file must be optioned')
else:
	ex2.get_log(openwindow.encode('utf-8'))
	tkMessageBox.showinfo('Completed','Find analysis file under the same path of target file')

search = Tkinter.Button(top,text='Quit',font=('Arial',8),command=top.quit)
# def resize(ev=None):
# 	l.config(font='Arial -%d bold' % scale.get())

# scale = Tkinter.Scale(top,from_=20,to=100,orient='horizontal',command=resize)
# scale.set(20)

# l.pack()
# scale.pack(fill=Tkinter.X,expand=1)
search.pack(fill = Tkinter.X,expand = 1)

top.mainloop()