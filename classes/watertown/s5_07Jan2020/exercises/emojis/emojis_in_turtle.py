#emojis_in_turtle.py 01Dec2020  crs
# Play with emojis
from turtle import *
emojis = """
😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 😞 😔
😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦
😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿
"""
colors = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
lenc = len(colors)
per_line = 20
i = 0
side = 20
angle = 15
font_size = 50
font = ("", font_size, "")
penup()
goto(0, side*25)
pendown()
for em in emojis:
    if em == " ":
        continue    # Skip spaces
    i += 1
    fsize = int(font_size*i*.5/lenc)
    font = ("", fsize, "")
    col = colors[i%lenc]
    color(col)
    right(angle*i/lenc)    
    forward(side*i*7/lenc)
    write(em, align="center", font=font)
