from pytube import YouTube
from tkinter import *

def Search():
    url =YouTube(str(link.get()))
    for stream, x in iter(url.streams()):
        

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
    
root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(relx=0.4, rely=0.08)
link_enter = Entry(root, width = 70,textvariable = link).place(relx=0.1, rely=0.13)


Button(root,text = 'SEARCH', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Search).place(x=320 ,y = 150)

root.mainloop()