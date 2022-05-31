from PIL import Image

monro = Image.open("monro.jpg")
monro_red, monro_green, monro_blue = monro.split()

crop_pixels = 60
coordinates = (crop_pixels * 2, 0, monro_red.width, monro_red.height)
monro_red_left = monro_red.crop(coordinates)

coordinates = (crop_pixels, 0, monro_red.width - crop_pixels, monro_red.height)
monro_red_middle = monro_red.crop(coordinates)

monro_red_blend = Image.blend(monro_red_left, monro_red_middle, 0.5)

coordinates = (0, 0, monro_blue.width - crop_pixels * 2, monro_blue.height)
monro_blue_right = monro_blue.crop(coordinates)

coordinates = (crop_pixels, 0, monro_blue.width - crop_pixels, monro_red.height)
monro_blue_middle = monro_blue.crop(coordinates)

monro_blue_blend = Image.blend(monro_blue_right, monro_blue_middle, 0.5)

coordinates = (crop_pixels, 0, monro_green.width - crop_pixels, monro_green.height)
monro_green_cropped = monro_green.crop(coordinates)

monro_style = Image.merge("RGB", (monro_red_blend, monro_green_cropped, monro_blue_blend))
monro_style.save("monro_style.jpg")

side = 80
monro_style.thumbnail((side, side))
monro_style.save("monro_style_thumbnail.jpg")

