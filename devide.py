from PIL import Image
def cut(id,vx,vy):
    name1 = "/home/zihao/Downloads/project/test/york-21810-2.tif"
    name2 = "/home/zihao/Downloads/project/test/"+ id
    im =Image.open(name1)

    dx = 80
    dy = 150
    n = 1

    x1 = 0
    y1 = 0
    x2 = vx
    y2 = vy

    while x2 <= 7800:

        while y2 <= 11500:
            name3 = name2 + str(n) + ".jpg"
            im2 = im.crop((y1, x1, y2, x2))
            im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + vy
            n = n + 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy

    print ("sub-picture-number")
    return n-1


if __name__=="__main__":


    id = "1"

    res = cut(id,200,400)

    print (res)
