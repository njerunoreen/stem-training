

from tkinter import*
root = Tk()

#create a frame 

my_label1 = Label (root,text ="hello world ")

my_label2 = Label (root,text ="hello world ")
#show it on screen
my_label1 . grid (row= 3 ,column = 4)
my_label2 . grid (row= 4,column = 5)

root. mainloop()