
from PIL import Image
import os.path
import glob


def convertjpg(jpgfile,outdir,width=227,height=227):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("C:\\Users\\ZCZ\\Desktop\\青蛙\\test-1\\*.jpg"):
    convertjpg(jpgfile,"C:\\Users\\ZCZ\\Desktop\\青蛙\\new\\")