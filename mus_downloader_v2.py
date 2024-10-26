from yt_download import download
from files_sorting import sorting

case = bool(int(input('Скачать или отсортировать? (0 | 1): ')))


if not case:
    directory_in_str = input('Куда скачивать: ')
    url = input('Ссылка на видео или плейлист: ')
    download(url)


if case:
    directory_in_str = input('Путь к папке с музыкой: ')
    prizn_nums = int(input('\nПо скольки признакам сортировать файлы (название): '))
    priznaki = []
    for i in range (prizn_nums):
        priznaki.append(input(f'{i + 1}/{prizn_nums} признак: '))
    sorting(directory_in_str, priznaki)