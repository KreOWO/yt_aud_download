from __future__ import unicode_literals
import youtube_dl
import os, sys, shutil
from inspect import getsourcefile
from os.path import abspath

case = bool(int(input('Скачать или отсортировать? (0 | 1): ')))

def my_hook(d):
    if d['status'] != 'finished':
        print('[status] ', d['_percent_str'], '\t', d['_speed_str'], '\t', d['_total_bytes_str'])
    if d['status'] == 'finished':
        print('[finished] Video downloaded, now convertering')

class MyLogger(object):
    def debug(self, msg):
        if 'just video' in msg: print('[video] Downloading just video')
        if '[youtube:tab] playlist' in msg: print('[playlist]', msg.replace('[youtube:tab] playlist ', ''))
        if '[download] Downloading video' in msg: print(msg)
        if '[ffmpeg] Destination:' in msg: print('[succesfull]', msg.replace('[ffmpeg] Destination: ', ''), '\n')
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

if not case:
    directory_in_str = input('Куда скачивать: ')
    pl = bool(int(input('Плейлист (0 | 1): ')))
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'noplaylist': not pl,
        'ignoreerrors': True,
        }

    if pl: url = input('Ссылка на плейлист: ')
    else: url = input('Ссылка на видео: ')
    
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in range(5):
            try:
                ydl.download([url])
            except:
                print(f'Error, try {i + 1}/10')
                if i == 9: 
                    print('Not this time...')
                    continue

    my_path = abspath(getsourcefile(lambda:0)).replace('\\music_downloader_v2_python.py', '')
    directory = os.fsencode(my_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if '.mp3' in filename:
            shutil.move(f'{my_path}\{filename}', f'{directory_in_str}\{filename}')

if case:
    directory_in_str = input('Путь к папке с музыкой: ')
    directory = os.fsencode(directory_in_str)
    prizn_nums = int(input('\nПо скольки признакам сортировать файлы (название): '))
    priznaki = []
    for i in range (prizn_nums):
        priznaki.append(input(f'{i + 1}/{prizn_nums} признак: '))
    print('\n')
    for i in priznaki:
        if not os.path.isdir(directory_in_str + r'\\' + i): os.mkdir(directory_in_str + r'\\' + i)
    if not os.path.isdir(directory_in_str + r'\\' + 'other'): os.mkdir(directory_in_str + r'\\' + 'other')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        for j in priznaki:
            if j in filename:
                shutil.move(f'{directory_in_str}\{filename}', f'{directory_in_str}\{j}\{filename}')
                print(f'{filename} ---------- {j}')
                break
            elif j == priznaki[-1]: 
                shutil.move(f'{directory_in_str}\{filename}', f'{directory_in_str}\other\{filename}')
                print(f'{filename} ---------- other')