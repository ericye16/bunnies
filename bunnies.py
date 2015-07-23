#!/usr/bin/env python
import webbrowser, random

URLS = [
        "https://i.imgur.com/TgyTYlX.gifv",
        "https://i.imgur.com/zwK7XG6.gifv",
        "https://i.imgur.com/gumTewz.gifv",
        "http://i.imgur.com/XTuRoOs.gif",
        "https://gfycat.com/PessimisticBrilliantGroundhog",
        "https://i.imgur.com/stivcuE.jpg",
        "http://i.imgur.com/MKhq0Zc.gifv",
        ]

if __name__ == "__main__":
    webbrowser.open(random.choice(URLS))
