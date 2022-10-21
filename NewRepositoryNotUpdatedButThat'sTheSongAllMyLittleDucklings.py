from tkinter import *
import pyautogui
import winsound
import tkinter.messagebox
root=Tk(className="piano")
root.config(bg="white")
song="CDEFGGAAAAGAAAAGFFFFEEDDDDC"
root1=Tk()
root1.tk.eval(f'tk::PlaceWindow {root1._w} center')
root1.withdraw()
tkinter.messagebox.showinfo(title="Piano App",message=song,parent=root1)
b1=Button(bg="black",height=15,width=5,text="C#/Db",fg="white",command=lambda: (winsound.Beep(277,500),get_note(b1)))
b1.grid(row=0,column=1)
b2=Button(bg="white",height=20,width=5,text="C",command=lambda: (winsound.Beep(262,500),get_note(b2)))
b2.grid(row=0,column=0)
b3=Button(bg="black",height=15,width=5,text="D#/Eb",fg="white",command=lambda: (winsound.Beep(311,500),get_note(b3)))
b3.grid(row=0,column=3)
b4=Button(bg="white",height=20,width=5,text="D",command=lambda: (winsound.Beep(294,500),get_note(b4)))
b4.grid(row=0,column=2)
b5=Button(bg="white",height=20,width=5,text="E",command=lambda: (winsound.Beep(330,500),get_note(b5)))
b5.grid(row=0,column=4)
b6=Button(bg="white",height=20,width=5,text="F",command=lambda: (winsound.Beep(349,500),get_note(b6)))
b6.grid(row=0,column=5)
b7=Button(bg="black",height=15,width=5,text="F#/Gb",fg="white",command=lambda: (winsound.Beep(370,500),get_note(b7)))
b7.grid(row=0,column=6)
b8=Button(bg="black",height=15,width=5,text="G#/Ab",fg="white",command=lambda: (winsound.Beep(415,500),get_note(b8)))
b8.grid(row=0,column=8)
b9=Button(bg="white",height=20,width=5,text="G",command=lambda: (winsound.Beep(392,500),get_note(b9)))
b9.grid(row=0,column=7)
b10=Button(bg="black",height=15,width=5,text="A#/B",fg="white",command=lambda: (winsound.Beep(466,500),get_note(b10)))
b10.grid(row=0,column=10)
b11=Button(bg="white",height=20,width=5,text="A",command=lambda: (winsound.Beep(440,500),get_note(b11)))
b11.grid(row=0,column=9)
b12=Button(bg="white",height=20,width=5,text="H",command=lambda: (winsound.Beep(493,500),get_note(b12)))
b12.grid(row=0,column=11)
b13=Button(bg="white",height=20,width=5,text="C8",command=lambda: (winsound.Beep(523,500),get_note(b13)))
b13.grid(row=0,column=12)
list=[]
def get_note(Button)->Button:
    print(Button.cget("text"))
    list.append(Button.cget("text"))
    if list==["C","D","E","F","G","G","A","A","A","A","G","A","A","A","A","G","F","F","F","F","E","E","D","D","D","D","C"]:
        tkinter.messagebox.showinfo("Piano App","You've played the song!",parent=root)
    if not "".join(map(str,list)).startswith(song[0:len(list)]):
        tkinter.messagebox.showinfo("Oh no!","You've played a bit wrong!",parent=root)
    return Button.cget("text")
root.mainloop()
