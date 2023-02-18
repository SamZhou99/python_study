import win32print
import win32ui
from PIL import Image, ImageWin


ROOT_PATH = 'D:/www/python/py3/test-print-to-img/web-site-print'
SOURCE_IMGS = ['p1.png', 'test-1.jpg']

PRINTER_NAME = win32print.GetDefaultPrinter()


def readImage(img_file):
    DOT = img_file.rfind('.')
    SAVE_AS = img_file[0:DOT]+'_RGB_'+img_file[DOT:len(img_file)]
    bmp = Image.open(img_file)
    bmp = bmp.convert('RGB')
    bmp.save(SAVE_AS)
    return bmp


def printImage(img_path, bmp):
    DOUBLE = 7
    PX, PY = 10, 10
    PW, PH = 768*DOUBLE, 1024*DOUBLE

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(PRINTER_NAME)
    hDC.StartDoc(img_path)
    hDC.StartPage()

    dib = ImageWin.Dib(bmp)
    dib.draw(hDC.GetHandleOutput(), (PX, PY, PW, PH))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()


def startPrint(img_path):
    IMG_PATH = img_path
    BMP = readImage(IMG_PATH)
    printImage(IMG_PATH, BMP)

# for i in range(len(SOURCE_IMGS)):
#     IMG_PATH = ROOT_PATH+SOURCE_IMGS[i]
#     BMP = readImage(IMG_PATH)
#     printImage(IMG_PATH, BMP)

# print('111')
