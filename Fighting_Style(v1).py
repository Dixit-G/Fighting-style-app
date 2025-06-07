from tkinter import *
from PIL import Image, ImageTk
import threading
from time import sleep

Vermelho_escuro = "#9c0303"
Preto = "#000000"
Branco = "#ffffff"


gif_path = "Beat Up Knock Out Sticker by Paul Layzell.gif"

  #Não está sendo usado  
def exibir_gif():
    gif = Image.open(gif_path)
    frames = []

    try:
        while True:
            frame = gif.copy().convert("RGBA").resize((800, 600))  # Redimensionar para caber na janela
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass

    canvas = Canvas(FS, width=500, height=900, highlightthickness=0)
    canvas.pack(fill= BOTH, expand=True)


    bg_image = canvas.create_image(0, 0, anchor="w", image=frames[0])



    # Função para atualizar os frames
    def atualizar(i):
        canvas.itemconfig(bg_image, image=frames[i])
        FS.after(35, atualizar, (i+1) % len(frames))

    atualizar(0)

    threading.Thread(target=exibir_gif).start()





def criar_frame_boxe():

    def voltar():
        Boxe_Frame.pack_forget()
        Boxe_BT.pack()
        MuayThai_BT.pack()
        Sumo_BT.pack()
        Karate_BT.pack()
        Jiujitsu_BT.pack()

    Boxe_BT.pack_forget()
    MuayThai_BT.pack_forget()
    Sumo_BT.pack_forget()
    Karate_BT.pack_forget()
    Jiujitsu_BT.pack_forget()


    Boxe_Frame = Frame(FS, width=500, height=800, bg=Preto)
    Boxe_Frame.pack(fill=BOTH)

    Boxe_LB = Label(Boxe_Frame, text="BOXE", anchor="w", width=10, height=30, font="Time 30 bold", fg=Vermelho_escuro, bg=Preto)
    Boxe_LB.place(x=0, y=-650)

    Voltar_BT = Button(Boxe_Frame, text="Voltar", anchor="w", width=5, height=1, font="Time 15 bold", fg=Branco, bg=Vermelho_escuro,
                       command=voltar)
    Voltar_BT.place(x=0, y=750)

    Jab_BT = Button(Boxe_Frame, text="Jab", anchor="w", width=30, height=2, font="Time 15 bold", fg=Vermelho_escuro,
                    bg=Roxo_escuro)
    Jab_BT.pack(fill= tkinter.X, pady=3, padx=1)

    Hook_BT = Button(Boxe_Frame, text="Hook", anchor="w", width=30, height=2, font="Time 15 bold", fg=Vermelho_escuro,
                     bg=Roxo_escuro)
    Hook_BT.pack(fill=tkinter.X, pady=3, padx=1)




# Rodar em thread separada




FS = Tk()
FS.title('Fighting Styles')
FS.geometry('500x900+1035+0')
FS.configure(bg=Vermelho_escuro)

Boxe_BT = Button(FS, text='Boxe', anchor= 'w', width=30, height=2, font='Time 15 bold', command=criar_frame_boxe)
Boxe_BT.pack(pady=2)



MuayThai_BT = Button(FS, text='Muay Thai', anchor= 'w', width=30, height=2, font='Time 15 bold')
MuayThai_BT.pack(pady=2)



Karate_BT = Button(FS, text='Karaté', anchor= 'w', width=30, height=2, font='Time 15 bold')
Karate_BT.pack(pady=2)



Sumo_BT = Button(FS, text='Sumo', anchor= 'w', width=30, height=2, font='Time 15 bold')
Sumo_BT.pack(pady=2)



Jiujitsu_BT = Button(FS, text='Jiujitsu', anchor= 'w', width=30, height=2, font='Time 15 bold')
Jiujitsu_BT.pack(pady=2)



FS.mainloop()

