'''
Given Lab03t.pgm is Text PGM file, has a text header
as described below and rest of the part is sequences
of bytes as binary for the shade of gray of specific pixel

Header
	P2 as fisrt two characters followed by a newline
	then two integers width and height of image in pixels
				seperated by a space followed by a newline
	then the total number of shades of gray followed by a newline
	and lastly the data in binary form of length width X height
'''


class TextPGM:
    pass


def ReadTextPGM(pgmFileName):
    img = TextPGM()

    f = open(pgmFileName)

    img.header = f.readline().rstrip()
    img.width, img.height = f.readline().rstrip().split(" ")
    img.shades = f.readline().rstrip()

    img.width = int(img.width)
    img.height = int(img.height)
    img.shades = int(img.shades)

    lines = f.readlines()
    f.close()
    
    img.data = []
    for line in lines:
        nums = line.rstrip().split(" ")
        for num in nums:
            img.data.append(int(num))
    
    img.da = [[0 for i in range(img.width)] for j in range(img.height)]
    
    y = 0
    for i in range(img.height):
        for j in range(img.width):
            img.da[i][j] = img.data[y]
            y += 1

    return img

def rotate_image(img):    # updated by idrees
    timg = TextPGM()
    timg.header = img.header
    timg.width = img.height
    timg.height = img.width
    timg.shades = img.shades

    timg.da = [[0 for i in range(timg.width)] for j in range(timg.height)]
    for i in range(timg.height):
        for j in range(timg.width):
            timg.da[i][j] = img.da[j][i]

    timg.data = []
    for i in range(timg.height):
        for j in range(timg.width):
            timg.data.append(timg.da[i][j])

    return timg

def WriteTextPGM(newpgmFileName, img):
    f = open(newpgmFileName, "w")

    f.write(img.header + "\n")
    f.write(str(img.width) + " " + str(img.height) + "\n")
    f.write(str(img.shades) + "\n")
    count = 0
    line = 0

    for num in img.data:
        f.write(str(num))
        line += 1
        if line % 10 == 0:
            f.write("\n")
        else:
            f.write(" ")

    f.close()

def main():
    img = ReadTextPGM("Lab03t1.pgm")

    print("Image properties")
    print("================")
    print("Signature", img.header)
    print("Width", img.width)
    print("Height", img.height)
    print("Shades", img.shades)
    print("Data Size from different ways")
    print(len(img.data))
    print(img.width * img.height)

    newImg = rotate_image(img)  # added by idrees

    '''
    # commented by idrees
    for i in range(img.width):
        for j in range(img.height):
            newImg.data[i][j] = int((img.data[i][j] - 100) / 100 * 255)
            if newImg.data[i][j] < 0:
                newImg.data[i][j] = 0
            if newImg.data[i][j] > 255:
                newImg.data[i][j] = 255
    '''
    
    WriteTextPGM("Lab03t5.pgm", newImg)

    return


main()