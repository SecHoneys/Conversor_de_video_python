from pytube import YouTube # PARA INSTALAR ESSE BIBLIOTECA "PIP3 INSTALL PYTUBE"
import os

# Cole o link do vídeo aqui
url = input("Digite o link: ")
# Cria uma instancia do objeto Youtube
youtube = YouTube(url)
# Escolha a melhor opção de audio
audio = youtube.streams.filter(only_audio=True).order_by('abr').last()
# Baixa o arquivo de áudio
audio.download()
# Renomeia o arquivo baixado para ter extensão mp3
default_filename = audio.default_filename
new_filename = os.path.splitext(default_filename)[0] + '.mp3'
os.rename(default_filename, new_filename)

print(f'Arquivo MP3 baixado: {new_filename}')