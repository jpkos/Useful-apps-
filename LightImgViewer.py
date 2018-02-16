# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:38:05 2018

@author: Jani
"""

import tkinter as tk
import cv2
import os
from tkinter import ttk

from PIL import Image,ImageTk 

class ImgViewer(tk.Frame):
    img = None
    newimgs = []
    kehykset = []
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.images = []
        self.tiedostot = ""
        self.currentimg = 0
        self.create_widgets()
        
        
    def create_widgets(self):
        
        v = tk.StringVar(self, value='blinkgraafit/')
        
        self.polku = tk.Entry(self, textvariable=v)
        self.polku.grid(row=0, column=0, columnspan=2)
        self.polku.config(width=50)
        
        self.ImgLoad = tk.Button(self, text='load image', command = self.load_img)
        self.ImgLoad.grid(row=1, column=0)

        self.NextImg = tk.Button(self, text='Next image', command = lambda: self.change_img(1))
        self.NextImg.grid(row=3, column=2)
        self.PrevImg = tk.Button(self, text='Prev. image', command = lambda: self.change_img(-1))
        self.PrevImg.grid(row=3, column=1)
        
        self.kuvanimi = tk.Label(self, text='kuvan nimi')
        self.kuvanimi.grid(row=2, column=1)
        
        self.NewWindow = tk.Button(self, text='New window', command = self.create_window)
        self.NewWindow.grid(row=3, column=0)
    
    def fetch_path(self):
        print('fetch toimii')
        if self.polku.get() != self.tiedostot:
            self.tiedostot = self.polku.get()
            self.images = os.listdir(self.tiedostot)
            self.images = [self.tiedostot + kuva for kuva in self.images]
    
    def load_img(self):
        print('load toimii')
        self.fetch_path()
        if self.images:
            
            print('Toimii self.images')
            im = Image.open(self.images[self.currentimg])
            self.kuva = ImageTk.PhotoImage(im)
            ImgViewer.img = self.kuva
            self.kehys = tk.Label(self, image=self.kuva)
            self.kehys.grid(row=4, column=0, columnspan=2)
            self.kuvanimi.configure(text=self.images[self.currentimg%len(self.images)])
        
    def change_img(self, s):
        self.currentimg = self.currentimg + s
        
        im = Image.open(self.images[self.currentimg%len(self.images)])
        self.kuva = ImageTk.PhotoImage(im)
        ImgViewer.img = self.kuva 
        self.kehys.configure(image=self.kuva)
        
        self.kuvanimi.configure(text=self.images[self.currentimg%len(self.images)])
        
        
    def create_window(self):
        window = tk.Toplevel(self)
        window.wm_title(self.images[self.currentimg%len(self.images)])
        im = Image.open(self.images[self.currentimg])
        self.kuva2 = ImageTk.PhotoImage(im)
        ImgViewer.newimgs.append(self.kuva2)
        self.kehykset.append(tk.Label(window, image=ImgViewer.newimgs[-1]))
        self.kehykset[-1].grid(sticky='S')
        
            
        
        
def main():        
    root = tk.Tk()
    root.geometry('400x400')
    appi = ImgViewer(master=root)
    appi.master.title('LIV')
    appi.mainloop()
    
if __name__=='__main__':
    main()