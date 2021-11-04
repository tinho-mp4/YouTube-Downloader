from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""
#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#download video
def DownloadVideo():
    choice =ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

    if(choice == choices[0]):
        select = yt.streams.filter(progressive=True).first()
    elif(choice == choices[1]):
        select = yt.streams.filter(progressive=True,file_extension ='mp4').last()
    elif(choice == choices[2]):
        select = yt.streams.filter(only_audio=True).first()
    else:
        ytdError.config(text="Paste Link again", fg="red")

#download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!")

root = Tk()
root.title("YTD Downloader")
root.geometry("500x400") #Window size
root.columnconfigure(0,weight=1) # Content in center
#YTD Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("Arial",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Message
ytdError = Label(root,text="Error Message", fg="#ff4c38",font=("Arial",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("Arial",15,"bold"))
saveLabel.grid()

#btn for save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Message location
locationError = Label(root,text="Error Message for Path", fg="#ff4c38",font=("Arial",10))
locationError.grid()

#Download Quality
ytdQuality = Label (root,text="Select Quality",font=("Arial",15,"bold"))
ytdQuality.grid()

#combobox
choices = ("1080p","720p","Only Audio")
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download btn
downloadbtn = Button(root,text="Download",width=10,bg="#ff4c38",fg="#d6d6d6",command=DownloadVideo)
downloadbtn.grid()
root.mainloop()
