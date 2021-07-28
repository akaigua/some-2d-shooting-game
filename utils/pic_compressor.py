from PIL import Image

i = 1
image = Image.open("../assets/character_file/stand_right.png")
image = image.resize((int(222 * 0.9 * 1721 / 3449), int(222 * 0.9)), Image.ANTIALIAS)
image.save(f"./{i}.png")
i += 1
image = Image.open("../assets/character_file/stand_left.png")
image = image.resize((int(222 * 0.9 * 1721 / 3449), int(222 * 0.9)), Image.ANTIALIAS)
image.save(f"./{i}.png")
i += 1
image = Image.open("../assets/character_file/move_right.png")
image = image.resize((int(222 * 0.9 * 1721 / 3449), int(222 * 0.9)), Image.ANTIALIAS)
image.save(f"./{i}.png")
i += 1
image = Image.open("../assets/character_file/move_left.png")
image = image.resize((int(222 * 0.9 * 1721 / 3449), int(222 * 0.9)), Image.ANTIALIAS)
image.save(f"./{i}.png")
i += 1
