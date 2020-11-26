from PIL import Image as img

col = img.open('images/11773.JPG')
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("dump/bw.png")