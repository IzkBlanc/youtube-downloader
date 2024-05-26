import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pathlib import Path

def get_download_folder():
    # caminho pra onde vai o download
    home = str(Path.home())
    if os.name == 'nt':  # Windows
        download_folder = os.path.join(home, 'Downloads')
    else:  # macOS e Linux
        download_folder = os.path.join(home, 'Downloads')
    return download_folder

def baixar_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return

    try:
        yt = YouTube(url)
        status_label.config(text=f'Baixando: {yt.title}')
        
        # escolher mp4 e com maior resolução possível 
        stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
        
        # Define o caminho de download (vc pode mudar se quiser)
        download_folder = get_download_folder()
        stream.download(download_folder)
        
        status_label.config(text='Download concluído!')
        messagebox.showinfo("Sucesso", f'O vídeo "{yt.title}" foi baixado com sucesso em "{download_folder}".')
    except Exception as e:
        status_label.config(text='Erro ao baixar o vídeo.')
        messagebox.showerror("Erro", f'Ocorreu um erro: {e}')

# Interface
app = tk.Tk()
app.title("YouTube Video Downloader")

# label onde vai o URL
url_label = tk.Label(app, text="URL do vídeo do YouTube:")
url_label.pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

# Botão para iniciar o download
download_button = tk.Button(app, text="Baixar Vídeo", command=baixar_video)
download_button.pack(pady=20)

# Rótulo para exibir o status
status_label = tk.Label(app, text="")
status_label.pack(pady=5)

# Inicia o loop principal da interface
app.mainloop()
