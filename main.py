'''
Created by Metehan BAŞ -- 14.10.2022
İmage Filter Generator
'''
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
import cv2
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


window = tk.Tk()
window.geometry("600x600+400+100")
window.resizable(False,False)
window.title("İmage Filter Generator")
window.configure(bg="#E0E0E0")


buttonupload = tk.Button(window,text="Upload İmage",width=12, height=1,command=lambda:searchimage())
buttonupload.place(x=200,y=20)
buttonupload.config(border=2)

canvas=tk.Canvas(window,height=400,width=400,background="gray")
canvas.place(x=100,y=175)

canvasline=tk.Canvas(window,height=2,width=500,background="gray")
canvasline.place(x=50,y=160)

control = 0

versionlabel = tk.Label(window,text="V-1.0")
versionlabel.place(x=560,y=580)
versionlabel.configure(bg="#E0E0E0")

def searchimage():
        global img
        filetype=[("jpeg files","*.jpg"),("png files","*.png")]
        imgname = filedialog.askopenfilename(title="Select image",filetypes=filetype)
        img=Image.open(imgname)
        img_resized = img.resize((400,400))
        img = ImageTk.PhotoImage(img_resized) 
        l1 = tk.Label(window,image=img)
        l1.place(x=100,y=175)
        
        buttongray = tk.Button(window,text="GRAY",width=10, height=1,command=lambda:gray())
        buttongray.place(x=100,y=110)
        buttongray.config(border=2)

        buttonbgr = tk.Button(window,text="BGR",width=10, height=1,command=lambda:bgr())
        buttonbgr.place(x=100,y=70)
        buttonbgr.config(border=2)

        buttonsave = tk.Button(window,text="SAVE",width=12, height=1,command=lambda:save())
        buttonsave.place(x=300,y=20)
        buttonsave.config(border=2)

        buttonblur = tk.Button(window,text="BLUR",width=10, height=1,command=lambda:blur())
        buttonblur.place(x=200,y=70)
        buttonblur.config(border=2)

        buttoncontour = tk.Button(window,text="CONTOUR",width=10, height=1,command=lambda:contour())
        buttoncontour.place(x=300,y=110)
        buttoncontour.config(border=2)
        
        buttonemboss = tk.Button(window,text="EMBOSS",width=10, height=1,command=lambda:emboss())
        buttonemboss.place(x=300,y=70)
        buttonemboss.config(border=2)

        buttonsharp = tk.Button(window,text="SHARPEN",width=10, height=1,command=lambda:sharp())
        buttonsharp.place(x=200,y=110)
        buttonsharp.config(border=2)

        buttonedge = tk.Button(window,text="EDGE",width=10, height=1,command=lambda:edge())
        buttonedge.place(x=400,y=70)
        buttonedge.config(border=2)

        buttondetail = tk.Button(window,text="DETAİL",width=10, height=1,command=lambda:detail())
        buttondetail.place(x=400,y=110)
        buttondetail.config(border=2)


        def gray():
                global img
                global control 
                control = 1
                img = Image.open(imgname).convert(mode="L")
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)


        def bgr():

                global img
                global control 
                control = 2
                img = Image.open(imgname).convert(mode="RGB")
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)
        
        def blur():

                global img
                global control 
                control = 3
                img = Image.open(imgname)
                img = img.filter(ImageFilter.BoxBlur(3))
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)

        def contour():
                global img
                global control 
                control = 4
                img = Image.open(imgname)
                img = img.filter(CONTOUR)
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)

        def emboss():
                global img
                global control 
                control = 5
                img = Image.open(imgname)
                img = img.filter(EMBOSS)
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)

        def sharp():
                global img
                global control 
                control = 6
                img = Image.open(imgname)
                img = img.filter(SHARPEN)
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)

        def detail():
                global img
                global control 
                control = 7
                img = Image.open(imgname)
                img = img.filter(DETAIL)
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)
        
        def edge():
                global img
                global control 
                control = 8
                img = Image.open(imgname)
                img = img.filter(EDGE_ENHANCE_MORE)
                img_resized = img.resize((400,400))
                img = ImageTk.PhotoImage(img_resized)
                l1 = tk.Label(window,image=img)
                l1.place(x=100,y=175)

        def save():
                global img
                if control == 1:
                        img = Image.open(imgname).convert("L")
                        img.save("C:/Users/Metehan/Masaüstü/Grayİmage.jpg")
                elif control ==2:
                        img = Image.open(imgname).convert("RGB")
                        img.save("C:/Users/Metehan/Masaüstü/RGBİmage.jpg")
                elif control == 3:
                        img = Image.open(imgname)
                        img = img.filter(ImageFilter.BoxBlur(3))
                        img.save("C:/Users/Metehan/Masaüstü/Blurİmage.jpg")
                elif control == 4:
                        img = Image.open(imgname)
                        img = img.filter(CONTOUR)
                        img.save("C:/Users/Metehan/Masaüstü/Contourİmage.jpg")
                elif control == 5:
                        img = Image.open(imgname)
                        img = img.filter(EMBOSS)
                        img.save("C:/Users/Metehan/Masaüstü/Embossİmage.jpg")
                elif control == 6:
                        img = Image.open(imgname)
                        img = img.filter(SHARPEN)
                        img.save("C:/Users/Metehan/Masaüstü/Sharpenİmage.jpg")
                elif control == 7:
                        img = Image.open(imgname)
                        img = img.filter(DETAIL)
                        img.save("C:/Users/Metehan/Masaüstü/Detailİmage.jpg")
                elif control == 8:
                        img = Image.open(imgname)
                        img = img.filter(EDGE_ENHANCE_MORE)
                        img.save("C:/Users/Metehan/Masaüstü/Detailİmage.jpg")
                else:
                        img = Image.open(imgname)
                        img.save("C:/Users/Metehan/Masaüstü/İmage.jpg")
        

window.mainloop()