import sys
try:
    import tkinter as tk

    import pytube
except ImportError as e:
    print(e)
    sys.exit(1)


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Youtube Downloader")

        self.geometry("500x200")

        self.start()

    def start(self):
        url_label = tk.Label(self, text="Entrez l'url de la vidéo à télécharger")
        url_label.pack()

        url_var = tk.StringVar()

        url_entry = tk.Entry(self, textvariable=url_var, width=50)
        url_entry.pack()

        url_btn = tk.Button(self, text="Télécharger", command=lambda url=url_var:
            self.download(url=url))
        url_btn.pack(pady=(10, 20))

    def download(self, event=None, **kwargs):
        url = kwargs["url"].get()
        if len(url) > 0:
            youtube = pytube.YouTube(url)

            video = youtube.streams.first()
            starting_label = tk.Label(self, text="Début du téléchargement")
            starting_label.pack()

            video.download()

            starting_label['text'] = "Vidéo téléchargé !"


# Kaaris feat Sid les 3 éléments - Tout est prêt 
# https://www.youtube.com/watch?v=pTvEicldwiw

root = App()
root.mainloop()
sys.exit(0)
