from backend import Bot


if __name__ == "__main__":
    bot = Bot()
    res = bot.ping_ai("return the name, time, location into json", "img.png")
    print(res["choices"][0]["message"]["content"])