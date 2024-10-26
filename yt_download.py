from yt_dlp import YoutubeDL
import os, shutil


def my_hook(d):
    if d['status'] != 'finished':
        print('[status] ', d['_percent_str'], '\t', d['_speed_str'], '\t', d['_total_bytes_str'])
    if d['status'] == 'finished':
        print('[finished] Video downloaded, now convertering')


class MyLogger(object):
    def debug(self, msg):
        if 'just video' in msg:
            print('[video] Downloading just video')
        if '[youtube:tab] playlist' in msg:
            print('[playlist]', msg.replace('[youtube:tab] playlist ', ''))
        if '[download] Downloading video' in msg:
            print(msg)
        if '[ffmpeg] Destination:' in msg:
            print('[succesfull]', msg.replace('[ffmpeg] Destination: ', ''), '\n')
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def download(url):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp4a',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'noplaylist': 'list' in url,
        'ignoreerrors': True,
        }
    res = 0
    with YoutubeDL() as ydl:
        tries = 3
        for i in range(tries):
            try:
                ydl.download([url])
                res += 1
            except:
                if i == tries-1:
                    print('Not this time...')
                    continue
                else:
                    print(f'Error, try {i + 1}/{tries}')

    if res:
        my_path = os.path.abspath(__file__)[:len('\music_downloader_v2_python.py')]
        directory = os.fsencode(my_path)
        newpath = input(f'Скачано файлов {res}\n'
                        f'Введите путь куда переместить скачанные файлы: ')
        if newpath:
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if '.mp3' in filename:
                    shutil.move(fr'{my_path}\{filename}', fr'{newpath}\{filename}')
