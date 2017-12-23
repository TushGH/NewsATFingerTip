# -*- coding: utf-8 -*-
"""
************ disclaimer ************************
This is a student project for non- commercial use
This Project retrives news articles from  many news feed (News Stories) provided by 
1) Times of India (https://timesofindia.indiatimes.com/rssfeeds/1221656.cms)
2) The Hindu(http://www.thehindubusinessline.com/news/?service=rss)
3) BBC (http://feeds.bbci.co.uk/news/world/asia/rss.xml)

The Author does not take any responsibility for any news .

Any commercial use of this project should be done only by seeking the permission of the
News portal mention above.

All credit of news goes to the  online portals of The Times of India , The Hindu,
and BBC. 

***********************************************
"""
"""
Created on Mon Dec 18 19:44:46 2017

@author: Tushar Vishvas Deshpande
@email : tushardeshpande24@gmail.com

1) Graphical User Interfaces with Tk  
   retrived form :https://docs.python.org/3/library/tk.html
2)Programming GUIs and windows with Tkinter and Python Introduction
  retrived from : https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/
3) Geeks For Geeks  -XML Parsing
   retrived from - http://www.geeksforgeeks.org/xml-parsing-python/
5) Python software foundation - for The ElementTree XML API
   retrived from - https://docs.python.org/2/library/xml.etree.elementtree.html#finding-interesting-elements
5) Tutorials Point - for Xpath Query Examples 
   retrived from - https://www.tutorialspoint.com/xpath/xpath_expression.htmv
6) Python For Beginners [ Request Library In Python ]
   retrived from http://www.pythonforbeginners.com/requests/using-requests-in-python
"""

import tkinter as tk
import requests
import xml.etree.ElementTree as ET
LARGE_FONT = ("Verdana" , 12)
class UserGui(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack( side="top" ,fill="both", expand = True)
        
        container.grid_rowconfigure(0 , weight=1)
        container.grid_columnconfigure(0 , weight=1)
        
        self.frames = {}
        for F in (startPage, page1 , TimesNews , BBC , disclaimer):
            frame = F(container , self)
            self.frames[F] = frame
            frame.grid(row = 0 , column = 0 , sticky = "nsew")
        
        self.show_frame(disclaimer)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


        
class startPage(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="WelCome To News Today" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label1 = tk.Label(self,text="Get The Latest Top News " , font = LARGE_FONT , justify= 'left')
        label1.pack(pady=10,padx=10)
        
        button = tk.Button(self,text="Times Of India " , command = lambda : controller.show_frame(TimesNews))
        button.pack()
        
        button = tk.Button(self,text="Hindu " , command = lambda : controller.show_frame(page1))
        button.pack()
        
        button = tk.Button(self,text="BBC " , command = lambda : controller.show_frame(BBC))
        button.pack()


class BBC(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="WelCome To News Today" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        resp = requests.get('http://feeds.bbci.co.uk/news/world/asia/rss.xml')
        with open('BBC.xml', 'wb') as f:
            f.write(resp.content)
        tree = ET.parse('BBC.xml')
        root = tree.getroot()
        abc = root.findall("channel/item")
        count = 1
        for a in abc:   
            label1 = tk.Label(self,text= a.find("title").text.upper(), font = LARGE_FONT)
            label1.pack(pady=10,padx=10)
            count = count + 1
            if(count == 10):
                break ;
        button = tk.Button(self,text="click to Home page " , command = lambda : controller.show_frame(startPage))
        button.pack() 
    
class TimesNews(tk.Frame):       
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="WelCome To News Today" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        resp = requests.get('https://timesofindia.indiatimes.com/rssfeeds/1221656.cms')
        with open('timesofindia.xml', 'wb') as f:
            f.write(resp.content)
        tree = ET.parse('timesofindia.xml')
        root = tree.getroot()
        abc = root.findall("channel/item")
        count = 1
        for a in abc:   
            label1 = tk.Label(self,text= a.find("title").text.upper(), font = LARGE_FONT)
            label1.pack(pady=10,padx=10)
            count = count + 1
            if(count == 10):
                break ;
        button = tk.Button(self,text="click to Home page " , command = lambda : controller.show_frame(startPage))
        button.pack() 
            
class page1(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="WelCome To News Today" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        resp = requests.get('http://www.thehindubusinessline.com/news/?service=rss')
        with open('Hindu.xml', 'wb') as f:
            f.write(resp.content)
        tree = ET.parse('Hindu.xml')
        root = tree.getroot()
        abc = root.findall("channel/item")
        count = 1
        for a in abc:   
            label1 = tk.Label(self,text= a.find("title").text.upper(), font = LARGE_FONT)
            label1.pack(pady=10,padx=10)
            count = count + 1
            if(count == 10):
                break ;
        button = tk.Button(self,text="click to Home page " , command = lambda : controller.show_frame(startPage))
        button.pack()
        
class disclaimer(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text=" DISCLAIMER" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="This is a student project for non- commercial use" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="This Project retrives news articles from  many news feed (News Stories) provided by" , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="1) Times of India \n 2) The Hindu \n 3) BBC " , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="The Author does not take any responsibility for any news ." , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="Any commercial use of this project should be done only by seeking the permission of the \n \
        News portal mention above." , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="All credit of news goes to the  online portals of The Times of India , The Hindu, \
        and BBC." , font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = tk.Button(self,text="Enter  " , command = lambda : controller.show_frame(startPage))
        button.pack()
        
       
    
        
app= UserGui()
app.mainloop()