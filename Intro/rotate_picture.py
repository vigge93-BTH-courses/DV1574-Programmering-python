from PIL import Image, ImageDraw

input_image = Image.open('input.png')
input_pixels = input_image.load()

output_image = Image.new('RGB', input_image.size)
draw = ImageDraw.Draw(output_image)

for x in range(output_image.width):
    for y in range(output_image.height):
        draw.point((x, output_image.height - y), input_pixels[x, y])

output_image.save('output.png')
print('Done!')
