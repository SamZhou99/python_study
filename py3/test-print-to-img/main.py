import win32print
import win32ui
from PIL import Image, ImageWin


ROOT_PATH = 'D:/www/python/py3/test-print-to-img/'
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

    # hDC.SetMapMode (win32con.MM_TWIPS)
    # hDC.DrawText ("TEST HELLO  WORLD! CORSS FIREWALL, WE TOUCH THE WORLD!",(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)

    dib = ImageWin.Dib(bmp)
    dib.draw(hDC.GetHandleOutput(), (PX, PY, PW, PH))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()


# for i in range(len(SOURCE_IMGS)):
#     IMG_PATH = ROOT_PATH+SOURCE_IMGS[i]
#     BMP = readImage(IMG_PATH)
#     printImage(IMG_PATH, BMP)

for i in range(9):
    printers = win32print.EnumPrinters(i)
    # 设置打印机名称
    # win32print.SetDefaultPrinter('EPSON Stylus C86 Series')
    print('打印机列表', i, printers)

print('初始化')
