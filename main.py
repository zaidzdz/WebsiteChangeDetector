import time
import requests
import customtkinter
import threading
import plyer
import pyobjus
inputtedUrl = ""
global OldHtml
OldHtml = ""
stop = False

checking = False
errorText = ""

plyer.notification.notify(title="s", message="s", app_name="s",timeout=10)
def getoldHtml():

    oldhtml = requests.get(entry.get()).text
    return oldhtml



def error():
    global errorText
    print("Somthing Went Wrong")
    errorText = "Somthing went wrong"
    ErrorLabel.configure(text=errorText)
    time.sleep(1)
    errorText = ""
    ErrorLabel.configure(text=errorText)
def mainloop():
    root.update()


def checkingStarted():


    global stop

    if stop == False:
        global OldHtml,checking,inputtedUrl
        try:
            OldHtml = getoldHtml()
            print(OldHtml)
            checking = True
            inputtedUrl = entry.get()
            button2.configure(text="Stop", fg_color="#e2020a", hover_color="#7e0106")
            threading.Thread(target=loop, daemon=True).start()
            stop = not stop
        except:
            threading.Thread(target=error, daemon=True).start()

    else:
        button2.configure(text="Start", fg_color=OrginalColor, hover_color=OrginalHoverColor)
        checking = False




def checkingEnded():
    return False
def loop():
    global OldHtml
    while checking == True:
        time.sleep(5)
        print(checking)

        currenthtml = requests.get(inputtedUrl).text

        if currenthtml != OldHtml:
            print("Html Changed")
            OldHtml = getoldHtml()
        else:
            print("Html Same")

    print(checking)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.resizable(False, False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(frame, text="Website Change Dectector")
label.pack(padx=10, pady=10)
label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
ErrorLabel = customtkinter.CTkLabel(frame, text=errorText, text_color="red")
ErrorLabel.place(relx=0.5, rely=0.4, anchor = customtkinter.CENTER)
entry = customtkinter.CTkEntry(frame, placeholder_text="https://")
entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(master=frame, text="Start", command=checkingStarted)
button2.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
OrginalColor = button2.cget("fg_color")
OrginalHoverColor = button2.cget("hover_color")
root.mainloop()



