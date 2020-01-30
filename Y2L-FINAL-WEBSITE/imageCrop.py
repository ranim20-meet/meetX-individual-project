from PIL import Image
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
img = Image.open("static/images/aslfull.jpg").convert(mode='RGB').resize((650, 650))

def crop(img, counter, shift, amount):
    global letters
    width, height = img.size
    print(img.size)
    for x in range(amount):
        size = (width//(amount))
        crop_area = (x*size, 0, size*(x+1)+shift, 150)
        new_img = img.crop(crop_area)
        new_img.save("static/images/CROPPED/" + letters[counter] + ".jpg")
        counter+=1

#A-G, counter = 0, shift = 10, amount = 7
crop_area = (40, 25, 610, 175)
new_img = img.crop(crop_area)
pix = new_img.load()
crop(new_img, 0, 10, 7)
print("Done A-G")

#H-M, counter = 7, amount = 6
crop_area = (40, 180, 610, 330)
new_img = img.crop(crop_area)
pix = new_img.load()
crop(new_img, 7, 7, 6)
print("Done H-M")

#N-S, counter = 13, amount = 6
crop_area = (40, 325, 610, 475)
new_img = img.crop(crop_area)
pix = new_img.load()
crop(new_img, 13, 7, 6)
print("Done N-S")

#T-Z, counter = 19, shift = 10, amount = 7
crop_area = (40, 470, 610, 620)
new_img = img.crop(crop_area)
pix = new_img.load()
crop(new_img, 19, 10, 7)
print("Done T-Z")
