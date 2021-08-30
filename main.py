from tkinter import *
from tkinter import ttk,messagebox
from pytube import YouTube
import _thread



storagePath= "C:\\Users\\Ayush\\Desktop\\yb downloader\\Downloads"


#main window
root=Tk()
root.title("Youtube Downloader")
root.geometry("500x320")
root.resizable(0,0)

#download function

def show_progress_bar(stream,chunk,bytes_remaining):
    progress = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)
    bar["value"] = progress

def download():
    quality=ytbchoices.get()
    url = link.get()
    if len(url) > 0:
        msg["text"] = "Extracting video from Youtube..."
        ytb_url = YouTube(url,on_progress_callback=show_progress_bar)
        video = ytb_url.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc()
        msg["text"] = "Downloading" + ytb_url.title
        if quality == choices[0]:
            video.last().download(storagePath)
        else:
            video.first().download(storagePath)
        
        msg["text"] = "Downloaded Successfully"
        messagebox.showinfo("Download Info","Downloaded successfully and saved to \n" + storagePath)
          
    else:
        urlErr["text"] = "Please Enter the url"

#Heading

Label(root,text="Youtube Vidoe Downlaoder",font="arial 20 bold").pack()

#url entry

Label(root,text="Paste the link here",font="arial 15 bold").pack()
link = StringVar()
link_entry=Entry(root,textvariable=link,width=70).pack()


#url error message

urlErr=Label(root,font="arial 12",fg="red")
urlErr.pack(pady=5)



#quality
Label(root,text="Select the quality of video",font="arial 12 bold").pack(pady=10)
choices=["Low","High"]
ytbchoices=ttk.Combobox(root,values=choices)
ytbchoices.pack()

#progress bar

bar=ttk.Progressbar(root,length=300)
bar.pack(pady=5)


#msg

msg=Label(root,font="arial 12",fg="green")
msg.pack()


#downlaod button

Button(root,text="Download",fg="white",bg="blue",width=17,height=2,command=lambda : _thread.start_new_thread(download,())).pack(pady=10)


root.mainloop()