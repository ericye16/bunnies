import webbrowser, random

URLS = [
        "https://i.imgur.com/TgyTYlX.gifv",
        "https://i.imgur.com/zwK7XG6.gifv",
        ]

if __name__ == "__main__":
    webbrowser.open(random.choice(URLS))
