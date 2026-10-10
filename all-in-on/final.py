#modüller
import customtkinter as ctk
import os
import subprocess
import sys

if getattr(sys, "frozen", False):
    klasor = os.path.dirname(sys.executable)
else:
    klasor = os.path.dirname(os.path.abspath(__file__))

#program açma functionu
def program_ac(dosya):
    yol = os.path.join(klasor, dosya)
    subprocess.Popen(yol)

#penceremiz
app=ctk.CTk()
app.title("FİNAL")
app.geometry("640x620")
ctk.set_appearance_mode("light")
app.resizable(False,False)

#column row düzeni
for i in range(2):
    app.grid_columnconfigure(i, weight=1)

for i in range(4):
    app.grid_rowconfigure(i, weight=1)

#yazı
yazı=ctk.CTkLabel(
    app,
    text="Hoşgeldininz ....! Araçlarınızın Hepsi Burada.",
    text_color="#33022f",
    font=("Arial", 24)
)
yazı.grid(row=0, column=0, columnspan=2, sticky="nsew")

#calculator butonu
hesap_makinesi=ctk.CTkButton(
    app,
    text="Hesap Makinesi",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command=lambda: program_ac("calculator_gui.exe")
)
hesap_makinesi.grid(row=1, column=0, pady=20, padx=20)

#weather
hava_durumu=ctk.CTkButton(
    app,
    text="Hava Durumu",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command=lambda: program_ac("weather.exe")
)
hava_durumu.grid(row=1, column=1, pady=20, padx=20)

#yapışkan notlar
yapışkan_notlar=ctk.CTkButton(
    app,
    text="Yapışkan Notlar",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command=lambda: program_ac("notes.exe") 
)
yapışkan_notlar.grid(row=2, column=1, pady=20, padx=20)

#saat
saat=ctk.CTkButton(
    app,
    text="Saat",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command=lambda: program_ac("saatctk.exe")
)
saat.grid(row=2, column=0, pady=20, padx=20)

#taş kağıt makas
taş_kağıt_makas=ctk.CTkButton(
    app,
    text="Taş Kağıt Makas",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command= lambda: program_ac("tas_kagit_makasctk.exe")
)
taş_kağıt_makas.grid(row=3, column=1, pady=20, padx=20)

#sayı_tahmin
number_guess=ctk.CTkButton(
    app,
    text="Sayı Tahmin",
    height=68,
    width=222,
    fg_color="#33022f",
    hover_color="#660467",
    text_color="#d9c1a7",
    command= lambda: program_ac("number_guessctk.exe")
)
number_guess.grid(row=3, column=0, pady=20, padx=20)
app.mainloop()