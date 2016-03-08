import Image,ImageEnhance,ImageFilter

leftFirst=11
rightFirst=21
width=12
top=2
bottom=15

fonts=open('fonts.txt')
matrix={}
for i in range(10):
    matrix[i]=[]
    fonts.readline()
    for j in range(13):
        t=fonts.readline()
        t=list(t)
        for l in range(10):
            if(l==0):
                matrix[i].append(t[l])
            else:
                matrix[i].append(t[l*2])
fonts.close()

img=Image.open('./img/plateBinary2.jpg')
img=img.filter(ImageFilter.MedianFilter())
img_denoise=ImageEnhance.Contrast(img)
img_denoise=img_denoise.enhance(3.0)

imgs={}
left=[]
right=[]
img_number={}
result={}
for i in range(4):
    left.append(leftFirst+i*width)
    right.append(rightFirst+i*width)
    box=(left[i],top,right[i],bottom)
    imgs[i]=img_denoise.crop(box)
    img_number[i]=[]
    for j in range(13):
        for k in range(10):
            if(imgs[i].getpixel((k,j))<(50,50,50)):
                img_number[i].append(1)
            else:
                img_number[i].append(0)
    maxCount=0
    for k in range(10):
        count=0
        for j in range(130):
            if(int(img_number[i][j])==int(matrix[k][j])):
                count+=1
        if(count>maxCount):
            maxCount=count
            result[i]=k
print(result.values())