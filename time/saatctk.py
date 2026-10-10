#kütüphanelerimiz
import customtkinter as ctk
from datetime import datetime

#pencerem pencerem benim güzel pencerem🦍💨
window=ctk.CTk()
window.title("saat")
window.geometry("943x337")
window.resizable(False, False)
window._set_appearance_mode("light")

#saat oğlim gel bura
def saati_yenile():
    saat= datetime.now().strftime("%H:%M:%S")
    Vaktin_tayin_olunduğu_ibare.configure(text=saat)
    window.after(1000, saati_yenile)

#saat gel artık oğlim
Vaktin_tayin_olunduğu_ibare=ctk.CTkLabel(
    window,
    text_color="#d9c1a7",
    text="00:00:00",font=("Arial", 100) )

Vaktin_tayin_olunduğu_ibare.pack(expand=True)
#GEL
saati_yenile()
window.mainloop()