# библиотека на которой это все писали
import disnake

# импорт нужных библиотек
import os
from random import sample
import requests
from PIL import Image

# создание рандомного названия
def randName(gif=False) -> str:
    numbers = "1234567890"
    abc = "qwertyuiopasdfghjklzxcvbnm"
    title_abc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    combinations = numbers + abc + title_abc
    if gif:
        ras = '.gif'
    else:
        ras = '.png'
    return './data/temp/' + "".join(
        sample(combinations, 15)) + ras  # './data/temp/' туда сохраняется файл аватарки (потом он удалится)

file_in = randName(False)
avatar = member.display_avatar  # member замените на свою переменную пользователя
response = requests.get(avatar)

# дальше идет код с какогото сайта чуть подредактированый для этого
# открытие файла во временной директории и запись в него полученной информации из requests.get(avatar)
with open(file_in, "wb") as file:
    file.write(response.content)

img = Image.open(file_in)

obj_for_count = img.load()

f = open('pon.jpg', "rb")  # Файл для размера
img_for_size = Image.open(f)

sq = [0, 0, 0]  # Массив для общего подсчета
count = img_for_size.size[0] * img_for_size.size[1]  # Ширина * Высота

width = img_for_size.size[0]  # Ширина
height = img_for_size.size[1]  # Высота

f.close

for i in range(width):  # Цикл по ширине
    for j in range(height):  # Цикл по высоте
        sq[0] += obj_for_count[i, j][0]  # r
        sq[1] += obj_for_count[i, j][1]  # g
        sq[2] += obj_for_count[i, j][2]  # b

out = [0, 0, 0]  # Массив для средних значений

out[0] = int(sq[0] / count)  # Средние значения
out[1] = int(sq[1] / count)
out[2] = int(sq[2] / count)

hexed = '0x' + format(out[0], 'x') + format(out[1], 'x') + format(out[2], 'x')  # Перевод в HEX

os.remove(file_in)  # удаление файла
