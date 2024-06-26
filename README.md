# библиотеки которые нужно импортировать
```
# библиотека на которой это на писано , но подойдет всеромто любая другая дискорд библиотека к примеру discord.py
import disnake

#библиотеки которые для этого всего нужны
import os
from random import sample
import requests
from PIL import Image
import random
```
# инструкция
1 - создайте в вашем проэкте или гдето в другом месте папку "data" в ней еще папку "temp" главное чтоб небыло еще одной папки с названиес "data"
2 - ```member.display_avatar``` замените на вашу переменную , к примеру :
```
@bot.event
async def on_message(message)
```
и тогда переменная будет ```message.author.display_avatar```
3 - все переменая ```hexed``` будет средний цвет аватарки пользователя в hex
если вы хотите встроить его в embed то ког будет такой
```
color = int(hexed, 0)

    embed = disnake.Embed(
        title='',
        description='',
        colour=color,
    )
```
вот мой пример к использованию :

![Снимок](https://github.com/TWOCHEG/discord-color-avatar/assets/150810031/35c3e59a-c99d-45fd-a5c1-4eed9f08a474)
