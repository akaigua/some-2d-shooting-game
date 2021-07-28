from PIL import Image
SCALE = 0.7

i = 1
image = Image.open("../assets/character_file/stand_right.png")
image = image.resize((int(222 * SCALE * 1721 / 3449), int(222 * SCALE)), Image.ANTIALIAS)
image.save(f"./stand_right.png")
i += 1
image = Image.open("../assets/character_file/stand_left.png")
image = image.resize((int(222 * SCALE * 1721 / 3449), int(222 * SCALE)), Image.ANTIALIAS)
image.save(f"./stand_left.png")
i += 1
image = Image.open("../assets/character_file/move_right.png")
image = image.resize((int(222 * SCALE * 1721 / 3449), int(222 * SCALE)), Image.ANTIALIAS)
image.save(f"./move_right.png")
i += 1
image = Image.open("../assets/character_file/move_left.png")
image = image.resize((int(222 * SCALE * 1721 / 3449), int(222 * SCALE)), Image.ANTIALIAS)
image.save(f"./move_left.png")
i += 1
