'''
Created on Feb 27, 2018

@author: Monica
'''
from tkinter import  StringVar, Label
import time
from tkinter.constants import TOP
class stopwatch:
    def __init__(self,parent):
        self.parent=parent
        self.start=0.0
        self.elapsed_time=0.0
        self.time_str=StringVar()
        self.make_widget()
        
    def make_widget(self):
        '''
        make the label
        '''
        lab=Label(self.parent,textvariable=self.time_str)
        self.set_time(self.elapsed_time)
        lab.pack()
        #self.start_stopwatch()
        
    def set_time(self,elap):
        '''
        set the string time into minutes:seconds:hundreths
        '''
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.time_str.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def start_stopwatch(self):
        self.start=time.time()-self.elapsed_time
        self.update()
        
    def update(self):
        """ Update the label with elapsed time. """
        self.elapsedtime = time.time() - self.start
        self.set_time(self.elapsedtime)
        self.timer = self.parent.after(50, self.update)
        
        


