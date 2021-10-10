from PIL import Image
from imoji.imoji import unicode_action

unicode_img = unicode_action()
card = Image.new("RGBA", (1280, 720), (255, 100, 23))
x, y = unicode_img.size
card.paste(unicode_img, (0, 0, x, y), unicode_img)
card.show()
