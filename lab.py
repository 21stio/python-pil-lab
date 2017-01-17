from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def image_text(image, text):
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype("Montserrat-Bold.otf", 120)

  text_width, text_height = draw.textsize(text, font=font)

  draw.text(((image.width - text_width)/2, (image.height - text_height)/2),text ,(255,255,255),font=font)

  return image


def resize_image(image):
  image_squared = (image.height == image.width)
  image_horizontal = (image.width > image.height)

  if image_squared is False:
    left = 0
    upper = 0
    right = image.width
    lower = image.height

    if image_horizontal:
      length = image.height
      left = (image.width - length) / 2
      right = (image.width - length) / 2 + length
    else:
      length = image.width
      upper = length / 2
      lower = length + upper

    image = image.crop([left, upper, right, lower])

  return image.resize([1000, 1000])


def enhance_image(image):
  contrast = ImageEnhance.Contrast(image)

  return contrast.enhance(1.3)


def filter_image(image):
  return image.filter(ImageFilter.GaussianBlur(2))

def darken(image):
  return image.point(lambda i: i * 0.5)

def bzz(image):
  red = range(0, 256)
  green = range(0, 256)
  blue = range(0, 256)

  green[0] = 10

  return image.point(red + green + blue)


image = Image.open('nosecrets.png')
  
image = image_text(image, 'NO SECRETS')
 
image.save('output.png','png')

