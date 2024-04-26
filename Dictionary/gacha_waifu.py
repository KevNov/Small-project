from random import randint

gacha = randint(1,31)

#waifu dictionary list

waifu_list = {
    7 : "Miku nakano",
    11 : "Emilia",
    16 : "Yukino Yuknioshita",
    22 : "Mai sakurajima",
    26 : "Makima",
    30 : "Marin kitagawa"
}

prize = waifu_list.get(gacha)
if gacha:
    print(f"congratulations, you get {prize}")
else:
    print(None)

