
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import emoji
import os

cwd = os.path.abspath(os.getcwd())

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from utils.file import read_file
from utils.file import replace_file

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\victo\Desktop\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def Change_Message(newMessage):
<<<<<<< HEAD
    replace_file(f"{cwd}\_internal\assets\message.txt",newMessage)
=======
    replace_file(f"{cwd}/assets/message.txt",newMessage)
>>>>>>> parent of 1eddfcf (Bug Fixes & First Build)

def Change_Contacts(newMessage):
    replace_file(f"{cwd}/assets/contacts.txt",newMessage)


def Init(Trigger):
    window = Tk()
    window.iconbitmap(cwd +  r"\_internal\utils\gui\assets/frame0\sparta.ico")
    window.title("Sparta")
    window.attributes('-fullscreen',True)
    width= window.winfo_screenwidth()   
    height= window.winfo_screenheight()
    height -= (height / 10)   

    window.geometry("%dx%d" % (width, height))
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1081,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1920.0,
        1080.0,
        fill="#460101",
        outline="")

    canvas.create_text(
        1570.0,
        1033.0,
        anchor="nw",
        text="&",
        fill="#FFFFFF",
        font=("Inconsolata Regular", 40 * -1)
    )

    canvas.create_text(
        1599.0,
        1006.0,
        anchor="nw",
        text="\nエドゥジタヴァレス\n\n\n",
        fill="#FFFFFF",
        font=("IslandMoments Regular", 32 * -1)
    )

    canvas.create_text(
        1465.0,
        window.winfo_screenheight() - 50,
        anchor="nw",
        text="ヘルツ",
        fill="#FFFFFF",
        font=("IslandMoments Regular", 32 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        933.5,
        526.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#340303",
        fg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=535.0,
        y=458.0,
        width=797.0,
        height=134.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        933.5,
        304.0,
        image=entry_image_2
    )
    entry_2 = Text(
        wrap="word",
        bd=0,
        bg="#340303",
        fg="#FFFFFF",
        highlightthickness=0,
    )




    entry_2.place(
        x=535.0,
        y=236.0,
        width=797.0,
        height=134.0,
    )


    entry_2.bind()

    entry_2.insert(tkinter.INSERT,emoji.emojize("Escreva a mensagem aqui  :thumbs_up:"))
    entry_1.insert(tkinter.INSERT,"Escreva os contatos aqui (separados por linha)")


    def UpdateFilesAndDeploy():
        Change_Message(entry_2.get("1.0",tkinter.END))
        Change_Contacts(entry_1.get("1.0",tkinter.END))

        Trigger() # Initializes browser

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UpdateFilesAndDeploy(),
        relief="flat"
    )
    button_1.place(
        x=535.0,
        y=643.0,
        width=797.0,
        height=111.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        923.0,
        101.0,
        image=image_image_1
    )

    canvas.create_text(
        40.0,
        27.0,
        anchor="nw",
        text="勝利は働く者にのみ与えられる勝利は働く者にのみ与えられる",
        fill="#FFFFFF",
        font=("IslandMoments Regular", 32 * -1),
        angle="-90",
    )
    window.resizable(True, True)
    window.mainloop()
