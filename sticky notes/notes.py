#kütüphanelermiz
import customtkinter as ctk
import os 
#penceremizi oluşturalım
app=ctk.CTk()
app.title("Notes App")
app.geometry("384x392")
app.resizable(False, False)
app._set_appearance_mode("light")

for i in range(11):
    app.rowconfigure(i, weight=1)
for i in range(2):
    app.columnconfigure(i, weight=1)

#notu okumak için fonksiyonumuz

def notu_oku(dosya_adi):
     with open(f"notes/{dosya_adi}.txt", "r", encoding="utf-8") as dosya:
          içerik=dosya.read()

     not_penceresi=ctk.CTkToplevel(app)
     not_penceresi.title(dosya_adi)
     app.resizable(False, False)
     not_penceresi.geometry("265x382")

     metin_kutusu=ctk.CTkTextbox(
          not_penceresi,
          width=200,
          height=200
     )
     metin_kutusu.pack(padx=20, pady=20)
#içerik kaydetmek
     metin_kutusu.insert("1.0", içerik)
     def kaydetmek():
      yeni_içerik = metin_kutusu.get("1.0", "end-1c")
      with open(f"notes/{dosya_adi}.txt", "w", encoding="utf-8") as dosya:
            dosya.write(yeni_içerik)

     #otomatik kaydetmek
     sayaç=None
     def oto_kayıt(event=None):
          nonlocal sayaç
          if sayaç is not None:
               not_penceresi.after_cancel(sayaç)
          sayaç=not_penceresi.after(1000, kaydetmek)
     metin_kutusu.bind("<KeyRelease>", oto_kayıt)
    
#yeni not butonu
def not_ekle():
    """Prompt for a note and add it to the notes window."""
    not_metni = ctk.CTkInputDialog(
        text="Notunuzu yazın:",
        title="Yeni Not Ekle"
    ).get_input()

    if not_metni and not_metni.strip():
            dosya_adi=not_metni.strip()
            with open(f"notes/{dosya_adi}.txt", "w", encoding="utf-8") as dosya:
                 pass

            not_etiketi = ctk.CTkButton(
            master=app,
            text=not_metni.strip(),
            width=130,
            height=34,
            fg_color="#33022f",
            hover_color="#470445",
            text_color="#d9c1a7",
            command=lambda  dosya_adi=dosya_adi:  notu_oku(dosya_adi)
        )
            not_etiketi.grid(
            row=app.grid_size()[1],
            column=0,
            columnspan=1,
            sticky="ew",
            padx=10,
            pady=5
    )
#program açılınca tüm dosyalar görünsün diye
note=os.listdir("notes")
for dosya in note:
     dosya_adi=dosya.removesuffix(".txt")
     not_etiketi = ctk.CTkButton(
        master=app,
        text=dosya_adi,
        width=130,
        height=34,
        fg_color="#33022f",
        hover_color="#470445",
        text_color="#d9c1a7",
        command=lambda dosya_adi=dosya_adi: notu_oku(dosya_adi)
    )

     not_etiketi.grid(
        row=app.grid_size()[1],
        column=0,
        columnspan=1,
        sticky="ew",
        padx=10,
        pady=5
    )

not_ekle_butonu=ctk.CTkButton(
    app, 
    text="Yeni Not Ekle",
    width=124,
    height=39,
    fg_color="#33022f",
    hover_color="#470445",
    text_color="#d9c1a7",
    command=not_ekle
)
not_ekle_butonu.grid(row=0, column=1, pady=10, padx=10)

app.mainloop()