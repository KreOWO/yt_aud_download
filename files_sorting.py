import os, shutil


def sorting(directory_in_str, priznaki):
    directory = os.fsencode(directory_in_str)
    print('\n')
    for i in priznaki:
        if not os.path.isdir(directory_in_str + r'\\' + i): os.mkdir(directory_in_str + r'\\' + i)
    if not os.path.isdir(directory_in_str + r'\\' + 'other'): os.mkdir(directory_in_str + r'\\' + 'other')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        for j in priznaki:
            if j in filename:
                shutil.move(fr'{directory_in_str}\{filename}', f'{directory_in_str}\{j}\{filename}')
                print(f'{filename} ---------- {j}')
                break
            elif j == priznaki[-1]:
                shutil.move(fr'{directory_in_str}\{filename}', f'{directory_in_str}\other\{filename}')
                print(f'{filename} ---------- other')
