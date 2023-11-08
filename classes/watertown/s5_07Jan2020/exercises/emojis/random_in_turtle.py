#random_in_turtle.py 01Dec2020  crs
"""
Play with emojis in the turtle scene
The emojis were cliped off the Internet and
pasted into text for demonstration purposes
For some reason only every other is displayed
We display them with random position and size
"""
import sys
from turtle import *
import random

emojis = """
😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 😞 😔
😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦
😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿
"""
colors = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
lenc = len(colors)
i = 0
size = 800              # Screen size
angle = 15
font_size = 100
fsize_min = font_size*.1    # limit small font
fsize_max = font_size
font = ("", font_size, "")
speed("fast")        # Speedup display
for em in emojis:
    if em == " ":
        continue    # Skip spaces between emoji
    i += 1
    rxoff = random.randint(0, size)
    rx = rxoff - size/2                   # Center about 0,0 in size by size
    ryoff = random.randint(0, size)
    ry = ryoff - size/2
    rfsize = random.randint(fsize_min, fsize_max)
    goto(rx, ry)
    print(f"rx:{rx} ry:{ry} {em}")  # Debugging display
    fsize = rfsize
    font = ("", fsize, "")
    col = colors[i%lenc]        # Repeat colors in list
    color(col)
    write(em, align="center", font=font)    # Display emoji
