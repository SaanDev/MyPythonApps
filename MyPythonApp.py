"""
Name : Sahan Liyanage
Index Number : s14891
"""

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

################# FUNCTIONS START ##################

#functions to type the name
txt = ""
def btn_s_isclicked():
  global txt
  txt = txt + "s"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_a_isclicked():
  global txt
  txt = txt + "a"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_h_isclicked():
  global txt
  txt = txt + "h"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_n_isclicked():
  global txt
  txt = txt + "n"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_l_isclicked():
  global txt
  txt = txt + "l"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_i_isclicked():
  global txt
  txt = txt + "i"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_y_isclicked():
  global txt
  txt = txt + "y"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_g_isclicked():
  global txt
  txt = txt + "g"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_e_isclicked():
  global txt
  txt = txt + "e"
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

def btn_space_isclicked():
  global txt
  txt = txt + " "
  display_area.delete(0, 'end')
  display_area.insert(0, txt)

#function to clear display area
def clear(event):
  global txt
  txt = ""
  display_area.delete(0, 'end')
  display_area.insert(0, txt)
  display_area.configure(foreground = "black")
  return None


#function to reverese the name
def btn_reverseisclicked():
  mynametxt=display_area.get()
  mynametxt = mynametxt[::-1]
  display_area.delete(0, 'end')
  display_area.insert(0, mynametxt)

#function to change display area text color
def lbl_redisclicked(event):
  display_area.configure(foreground = "red") 

def lbl_blueisclicked(event):
  display_area.configure(foreground = "blue")

def lbl_yellowisclicked(event):
  display_area.configure(foreground = "yellow")

def lbl_greenisclicked(event):
  display_area.configure(foreground = "green") 

#function to display index number
#enter
def lblindex_enter(event):
  lblindex.configure(text = "s14891", foreground = "yellow", background = "red")
#leave  
def lblindex_leave(event):
  lblindex.configure(text = "", background = "cyan")

#function to display index number
#enter
def lblname_enter(event):
  lbl_name.configure(text = "Sahan Liyanage", foreground = "cyan", background = "black")
#leave
def lblname_leave(event):
  lbl_name.configure(text = "", background = "white")  

################# FUNCTIONS END ##################

################### UI START ####################

#main window
main = Tk()
main.geometry("386x179")
main.title("SL-Name")
main.resizable(0, 0)

#frames
frame1 = Frame(main)
frame1.pack()
frame2 = Frame(main)
frame2.pack()
frame3 = Frame(main)
frame3.pack()
frame4 = Frame(main)
frame4.pack()
frame5 = Frame(main)
frame5.pack()
frame6 = Frame(main)
frame6.pack()
frame7 = Frame(main)
frame7.pack()
frame8 = Frame(main)
frame8.pack()

#Label for display index number
lblindex = Label(frame1, width = 60, foreground = "white", background = "cyan" )
lblindex.bind("<Enter>", lblindex_enter)
lblindex.bind("<Leave>", lblindex_leave)
lblindex.pack(side = "left")

#Entry for display the name
display_area = Entry(frame2, width = 60, foreground = "black", background = "#ffffff", justify = "right" )
display_area.bind("<Button-1>", btn_reverseisclicked)
display_area.bind("<Button-3>", clear)
display_area.pack(side = "left")

#button area in frame3
btn_s = Button(frame3, text = "s", command = btn_s_isclicked)
btn_s.pack(side = "left")
btn_a = Button(frame3, text = "a", command = btn_a_isclicked)
btn_a.pack(side = "left")
btn_h = Button(frame3, text = "h",command = btn_h_isclicked)
btn_h.pack(side = "left")

#button area in frame4
btn_n = Button(frame4, text="n", command = btn_n_isclicked)
btn_n.pack(side = "left")
btn_l = Button(frame4, text="l", command = btn_l_isclicked)
btn_l.pack(side = "left")
btn_i = Button(frame4, text="i", command = btn_i_isclicked)
btn_i.pack(side = "left")

#button area in frame5
btn_y = Button(frame5, text="y", command = btn_y_isclicked)
btn_y.pack(side = "left")
btn_g = Button(frame5, text="g", command = btn_g_isclicked)
btn_g.pack(side = "left")
btn_e = Button(frame5, text="e", command=btn_e_isclicked)
btn_e.pack(side = "left")

#button area in frame6
btn_space = Button(frame6, width = 18, text = "space", command = btn_space_isclicked)
btn_space.pack(side = "left")
btn_reverse = Button(frame6, width = 18, text = "reverse", command = btn_reverseisclicked)
btn_reverse.pack(side = "left")

#name display area
lbl_name = Label(frame7, width = 60, foreground = "black", background = "#ffffff" )
lbl_name.bind("<Enter>", lblname_enter)
lbl_name.bind("<Leave>", lblname_leave)
lbl_name.pack(side = "left")

##### color selection area #####
lbl_color_color_selection = Label(frame8, text = "Select the Display Color:")
lbl_color_color_selection.pack(side = "left")

#### color labels ####
#red
lbl_red = Label(frame8, width = 5, background = "red")
lbl_red.bind("<Button-1>", lbl_redisclicked)
lbl_red.pack(side = "left")
#blue
lbl_blue = Label(frame8, width = 5, background = "blue")
lbl_blue.bind("<Button-1>", lbl_blueisclicked)
lbl_blue.pack(side = "left")
#yellow
lbl_yellow = Label(frame8, width = 5, background = "yellow")
lbl_yellow.bind("<Button-1>", lbl_yellowisclicked)
lbl_yellow.pack(side = "left")
#green
lbl_green = Label(frame8, width = 5, background = "green")
lbl_green.bind("<Button-1>", lbl_greenisclicked)
lbl_green.pack(side = "left")

############ END UI ##############
#mainloop
mainloop()
