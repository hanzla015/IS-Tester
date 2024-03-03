from tkinter import *
from tkinter.constants import *
from threading import *
import speedtest

def check():
    start_btn.config(text="Checking...")
    start_btn.config(state=DISABLED)
    try:
        speed_test = speedtest.Speedtest()
        start_btn.pack_forget()
        exit_btn.pack_forget()
        dl_spd.config(text="Downloading Speed = Calculating....")
        dl_spd.pack(side=TOP)
        up_spd.config(text="Uploading Speed = Calculating....")
        up_spd.pack(side=TOP)
        ping_spd.config(text="Ping = Calculating....")
        ping_spd.pack(side=TOP)
        start_btn.pack(side=TOP,pady=5)
        exit_btn.pack(side=TOP,pady=5)
        main.geometry("350x300")
        download_spd = speed_test.download()
        upload_spd = speed_test.upload()
        ping = speed_test.results.ping
        dl_spd.config(text=f"Downloading Speed = {download_spd/1024/1024:.2f} Mbs per second")
        up_spd.config(text=f"Uploading Speed = {upload_spd/1024/1024:.2f} Mbs per second")
        ping_spd.config(text=f"Ping = {ping}")
        start_btn.config(text="Check")
        start_btn.config(state=ACTIVE)
    except Exception as e:
        main.geometry("320x230")
        start_btn.config(text="Check")
        start_btn.config(state=ACTIVE)
        error_label.config(text=f"An error occurred while connecting.\nTry again later.")
        error_label.pack(side=BOTTOM)

def testThread():
    thread = Thread(target=check)
    thread.start()

def exit():
    main.destroy()

main = Tk()
main.title("Internet Speed Checker")
main.geometry("300x200")
main.iconbitmap("icon.ico")
# main.config(bg="blueviolet")

heading = Label(main,text="Internet Speed Checker",font=("Feast of Flesh BB",22))
heading.pack(side=TOP)

dl_spd = Label(main,font=("Feast of Flesh BB",16),foreground='black')
# dl_spd.pack(side=TOP,pady=5)

up_spd = Label(main,font=("Feast of Flesh BB",16),foreground='black')
# up_spd.pack(side=TOP,pady=5)

ping_spd = Label(main,font=("Feast of Flesh BB",16),foreground='black')
# ping_spd.pack(side=TOP,pady=5)

start_btn = Button(main,text="Check",activeforeground="green",command=testThread,font=("Feast of Flesh BB",20))
start_btn.pack(side=TOP,pady=5)

exit_btn = Button(main,text="Exit",activeforeground="green",font=("Feast of Flesh BB",20),command=exit)
exit_btn.pack(side=TOP,pady=5)

error_label = Label(main,font=("Feast of Flesh BB",16),foreground="red")

author = Label(main,text="@HANZLA",font=("Feast of Flesh BB",20),justify=CENTER)
author.pack(side=BOTTOM)
main.mainloop()
