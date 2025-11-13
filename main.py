import tkinter as tk
import winsound
import gi_hangok
import gi_akkordok


class GI_Zongora:
    def __init__(self, root):
        self.root = root
        self.root.title("GI Zongora - HCFLJZ")
        self.root.geometry("800x300")

        self.gi_hangok = gi_hangok.GI_Hangok()
        self.gi_akkordok = gi_akkordok.GI_Akkordok()

        self.gi_csinald_felület()

    def gi_csinald_felület(self):

        feher_keret = tk.Frame(self.root, bg="gray")
        feher_keret.pack(pady=20)

        feher_hangok = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.feher_gombok = []

        for hang in feher_hangok:
            gomb = tk.Button(feher_keret, text=hang, width=6, height=10,
                             bg="white", fg="black", font=("Arial", 12),
                             command=lambda h=hang: self.gi_jatsz_hang(h))
            gomb.pack(side=tk.LEFT, padx=2)
            self.feher_gombok.append(gomb)


        fekete_keret = tk.Frame(self.root, bg="gray")
        fekete_keret.pack()

        fekete_hangok = ['C#', 'D#', '', 'F#', 'G#', 'A#', '']
        self.fekete_gombok = []

        for i, hang in enumerate(fekete_hangok):
            if hang:
                gomb = tk.Button(fekete_keret, text=hang, width=4, height=6,
                                 bg="black", fg="white", font=("Arial", 10),
                                 command=lambda h=hang: self.gi_jatsz_hang(h))
                gomb.place(x=i * 58 + 40, y=0)
                self.fekete_gombok.append(gomb)


        akkord_keret = tk.Frame(self.root)
        akkord_keret.pack(pady=10)

        akkordok = ['C', 'Dm', 'Em', 'F', 'G', 'Am']
        for akkord in akkordok:
            tk.Button(akkord_keret, text=akkord, width=6,
                      command=lambda a=akkord: self.gi_jatsz_akkord(a),
                      bg="lightblue", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)


        self.info_label = tk.Label(self.root, text="Kattints a billentyűkre!",
                                   font=("Arial", 12))
        self.info_label.pack(pady=10)

    def gi_jatsz_hang(self, hang):
        frekvencia = self.gi_hangok.gi_frekvencia(hang)
        winsound.Beep(frekvencia, 500)
        self.info_label.config(text=f"Hang: {hang}")

    def gi_jatsz_akkord(self, akkord):
        hangok = self.gi_akkordok.gi_akkord_hangok(akkord)
        for hang in hangok:
            self.gi_jatsz_hang(hang)
        self.info_label.config(text=f"Akkord: {akkord}")


if __name__ == "__main__":
    root = tk.Tk()
    zongora = GI_Zongora(root)
    root.mainloop()