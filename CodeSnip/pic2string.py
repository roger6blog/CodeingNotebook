# -*- coding: UTF-8 -*-
# Source:
# https://blog.csdn.net/qq_38330148/article/details/79858360
'''

解釋一下圖片轉文字簡單的原理：首先，每一張彩色的圖片，之所以能夠呈現出colorful或者dim的畫面

只因為每一張圖都由很多個像素點組成，而每一個像素點都有不同的顏色

而這個顏色就由三個值（rgb）對應三原色的百分比構成，所以每一個像素點都有三個值（rgb，範圍0-255）

那麽我們就可以將每一個像素點轉換成一個字符這樣就能形成一個字符圖畫了。

那麽問題就來了，總共有256*256*256種顏色

可是我們不可能有有這麽多種字符來一一對應啊，所以接下來就要引入新的概念：灰度值。

灰度值：指黑白圖像中點的顏色深度，範圍一般從0到255，白色為255，黑色為0，故黑白圖片也稱灰度圖像

rgb轉換成灰度值公式：

gray=int(r*0.299+g*0.587+b*0.114)

也就是說通過這個公式瞬間將256*256*256的範圍瞬間減少到0-255

有些人可能還會問，那我也沒有256個單色字符去一一對應範圍啊

這個時候不就可以靈活變通，將兩到三個灰度值對應為一種字符不就ok了。

那麽至於這個公式怎麽來的或者怎麽實現的，我們就不需要深究了，或者也可以去了解了解其中的算法，這裏提供博客鏈接：

https://blog.csdn.net/xdrt81y/article/details/8289963

===================================

簡單介紹pillow庫

1.要想簡單了解pillow庫，就需要簡單了解下一些相關基本概念：

通道（bands）：每張圖片由一個或多個數據通道構成，例如常見的rgb圖像

每張圖片都由三個數據通道構成，即R、G和B通道，而上面說的灰度圖像只有一個通道。

獲取圖片的通道方法是：getbands()，以元組數據類型返回。

模式（mode）：圖像的模式定義了圖像的類型和像素的位寬，有一些常見模式：
1：1位像素，表示黑和白，但是存儲的時候每個像素存儲為8bit。

L：8位像素，表示黑和白。

P：8位像素，使用調色板映射到其他模式。

RGB：3x8位像素，為真彩色。

RGBA：4x8位像素，有透明通道的真彩色。

CMYK：4x8位像素，顏色分離。

YCbCr：3x8位像素，彩色視頻格式。

I：32位整型像素。

F：32位浮點型像素。

可以通過Image.made返回圖片模式

濾波器：將多個輸入像素映射為一個輸出像素的幾何操作（比較覆雜，做個參考就好）
2.其中Image模塊中的常用方法：

Image.save("save.gif"，"GIF")  #保存為GIF格式，至於前一個參數是保存路徑
如果不寫絕對路徑自動保存在當前文件夾下

Image.new(mode，size，color)  #創建新圖片
註意保存時是new創建圖片對象，再用對象的save方法保存

Image.conver("RGBA")  #圖像類型轉換
Image.size  #返回的是一個二元組，即該圖片的大小，size[0]為水平長，size[1]為豎直高
Image.getpixel((w,h))  #獲取某個點的像素值（即rgb值）
注意其參數是必須（wedith，height）不能換順序！！！切記

==============================


程式碼簡析：
首先第一行是導入pillow庫和Image模塊，第三行中變量codelib是一個字符串序列

而count變量為其長度；第6行開始到第20行是一個transform函數（該程序的靈魂）

形參是文件對象，第8-9行是用於測試用的返回圖片文件的模式和通道（前面概念所說的）

以判斷該圖片是rgb模式還是rgba模式。接下來的雙重for循環中表示對圖片的像素點進行遍歷

其中13-16行就是我加的一個圖片模式的判斷，防止變量在接收每個像素點的rgb值時出現indexerror

因為有一些圖片是rgba模式，就是增加了一個透明度值

所以如果每次都是用r，g，b三個變量存儲getpoxel()返回的值就會有溢出）

第17行就是進行灰度值轉換。而18行中字符串變量codePic則是用於存儲所對應出來的字符

其中：codeLib[int(((count-1)*gray)/256)]

就是用於轉換成codelib中字符索引；第19行：就是在圖片每一次行遍歷完後字符尾部添加“\t和\n”

用於return這個字符串列表時打印出來能夠自動換行，而不是直接一行打印出來。

22-29行就是文件的打開和寫入了，soeasy！！

'''
from PIL import Image
import argparse

codeLib = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,~"
count = len(codeLib)

def transform(image):
    codePic = ''
    imode = list(image.getbands())
    print(imode)
    print(imode[-1])
    for h in xrange(0, image.size[1]):
        for w in xrange(0, image.size[0]):
            if imode[-1] == "A":
                r, g, b, a = image.getpixel((w, h))
            elif imode[-1] == "B":
                r, g, b = image.getpixel((w, h))
            gray = int(r*0.299 + g*0.587 + b*0.114)
            codePic = codePic + codeLib[int(((count-1) * gray) / 256)]
        codePic = codePic + '\r'
    return codePic


parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

fp = open(args.file, 'rb')
imageFile = Image.open(fp)
imageFile = imageFile.resize((int(imageFile.size[0]*0.35), int(imageFile.size[1]*0.175)))
print("Info:{} {} {}".format(imageFile.size[0], imageFile.size[1], count))

tmp = open("output.txt", 'w')
tmp.write(transform(imageFile))
tmp.close