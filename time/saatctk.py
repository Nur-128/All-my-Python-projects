#kütüphanelerimiz
import customtkinter as ctk
from datetime import datetime

#bu pencere ne güzel pencere, bu pencdereyi açan insan ne güzel insan
window=ctk.CTk()
window.title("saat")
window.geometry("943x337")
window.resizable(False, False)
window._set_appearance_mode("light")

#saati gösteren fonksiyon
def saati_yenile():
    saat= datetime.now().strftime("%H:%M:%S")
    Vaktin_tayin_olunduğu_ibare.configure(text=saat)
    window.after(1000, saati_yenile)

#saati çağıralım
Vaktin_tayin_olunduğu_ibare=ctk.CTkLabel(
    window,
    text_color="#d9c1a7",
    text="00:00:00",font=("Arial", 100) )

Vaktin_tayin_olunduğu_ibare.pack(expand=True)

saati_yenile()
window.mainloop()