from tkinter import *
from auth import *
from math import pow
window = Tk()
window.attributes('-fullscreen',True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
#window.geometry("%dx%d+100+100" % (w, h))
window.title("Welcome to ISAA Bank")
window.configure(background = "LightSeaGreen")
hashDir ={'d84305873370ac353a4aaa3df835104df5a4dd1fe6f88a88fff50ae08564a85c':'Priyal', #7828
'16a05870017ccb4b0f94bb191e8952eb77365e3f1b265d0f46fdde8f1297d820':'Ritika', #6774
'5ba3df1057fcddf3c60a1699fb0e736634809c0b6dd41d9c6dfd0d6f24ccd79f':'Ruchita', #8367
'f4df4c0e33686c9bc43272be64bcb4ad4a6e3e24f4db0ea40ba4aa7b0303b615':'Tamanna' #5046
} 
hashDirLen = len(hashDir)
hashList = list(hashDir.keys())
#nameList = list(hashDir.values())
def authenticate():
    newWin = Toplevel(window)
    newWin.attributes('-fullscreen',True)
    newWin.title("Authentication")
    newWin.configure(background = "LightSeaGreen")
    Label(
        newWin,
        text = " Welcome to ISAA Bank ",
        bg = "LightSeaGreen",
        fg = "DarkCyan",
        font = "Consolas 72"
    ).place(
        x = 90,
        y = 50
    )
    P = PINEntry.get()
    PINEntry.delete(0,END)
    if len(P) == 4 and P.isdigit():
        q = 123456789987654321234567898
        #random.randint(pow(10,20),pow(10,50))
        g = 23931164504956447807213117212663825326210289577470
        key = gen_key(q) #Receiver_Private_key
        h = power(g,key,q)
        en_msg, p, out = encrypt(P,q,h,g)
        dr_msg = decrypt(en_msg,p,key,q)
        dmsg = ''.join(dr_msg)
        print("Decrypted Message: ",dmsg)
        flag = 0
        for i in range(len(hashList)):
            if out == hashList[i]:
                flag = 1
                pos = i
                break
        if flag == 1:
            Label(
                newWin,
                text = "PIN Matched. Hello, " + hashDir[hashList[pos]] + "!",
                bg = "LightSeaGreen",
                fg = "Navy",
                font = "Consolas 20"
            ).place(
                x = 430,
                y = 300
            )
            Button(
                newWin,
                text = "Back",
                width = 20,
                font = "Calibri 15",
                bg = "LightSeaGreen",
                fg = "White",
                command = newWin.destroy
            ).place(
                x = 550,
                y = 425
            )
        else:
            Label(
                newWin,
                text = "No match found. Please try again.",
                bg = "LightSeaGreen",
                fg = "Maroon",
                font = "Consolas 20"
            ).place(
                x = 430,
                y = 300
            )
            Button(
                newWin,
                text = "Back",
                width = 20,
                font = "Calibri 15",
                bg = "LightSeaGreen",
                fg = "White",
                command = newWin.destroy
            ).place(
                x = 550,
                y = 425
            )
    else:
        Label(
            newWin,
            text = "Invalid PIN. Please try again.",
            bg = "LightSeaGreen",
            fg = "Maroon",
            font = "Consolas 20"
        ).place(
            x = 430,
            y = 300
        )
        Button(
            newWin,
            text = "Back",
            width = 20,
            font = "Calibri 15",
            bg = "LightSeaGreen",
            fg = "White",
            command = newWin.destroy
        ).place(
            x = 550,
            y = 425
        )
Label(
    text = " Welcome to ISAA Bank ",
    bg = "LightSeaGreen",
    fg = "DarkCyan",
    font = "Consolas 72"
).place(
    x = 90,
    y = 50
)
Label(
    text = "Enter your 4-digit PIN:",
    bg = "LightSeaGreen",
    fg = "White",
    font = "SegoeUILight 20",
).place(
    x = 525,
    y = 250
)
PINEntry = Entry(
    window,
    width = 4,
    font = "Consolas 50",
    show = "*"
)
PINEntry.place(
    x = 582,
    y = 300
)
PINEntry.focus_set()
Button(
    window,
    text = "Proceed",
    width = 20,
    font = "Calibri 15",
    bg = "LightSeaGreen",
    fg = "White",
    command = authenticate
).place(
    x = 550,
    y = 425
)
Button(
    window,
    text = "Quit",
    width = 20,
    font = "Calibri 15",
    bg = "LightSeaGreen",
    fg = "White",
    command = window.destroy
).place(
    x = 550,
    y = 475
)
window.mainloop()
