from turtle import bgcolor, color
import kivy 
import re
# Import kivy dependencies first
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.screenmanager import ScreenManager, Screen

# Import kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Import other kivy stuff
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger
from kivy.lang import Builder

# Import standard dependencies
import cv2
import os

import pandas as pd

#declaring global/ default variables
layout = BoxLayout
date=""
black = [0, 0, 0, 0] 
white=[1, 1, 1, 1]
from datetime import date
data_from_ocr=""
Dict = {}
today = date.today()

class LoginPage(layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout components 
        self.add_bill_label = Label(text="Add new bill", size_hint=(1,.1), font_size=18)
        self.new_bill_details = TextInput(text='New bill details', multiline=False, size_hint=(1,.1))
        self.button1 = Button(text="Submit new bill", on_press=self.submit1, size_hint=(1,.1), background_color=black, font_size=18)
        self.get_bill = Label(text="Get bill", size_hint=(1,.1), font_size=18)
        self.date = TextInput(text='Enter the date', multiline=False, size_hint=(1,.1))
        self.button2 = Button(text="Get old bill details", on_press=self.submit2, size_hint=(1,.1), background_color=black, font_size=18)
        

        # Add items to layout
        self.add_widget(self.add_bill_label)
        self.add_widget(self.new_bill_details)
        self.add_widget(self.button1)
        self.add_widget(self.get_bill)
        self.add_widget(self.date)
        self.add_widget(self.button2)

    def submit1(self, *args):

        cwd = str(os.getcwd())
        targetFile=cwd+'\input_image\input_image'+str(self.new_bill_details.text)+'.jpg'
        #Apply ocr here on target image
        global data_from_ocr
        #data_from_ocr=

        key=today
        if key in Dict.keys():
            print("Key exist, ", end =" ")
            dict.update({key:(str(Dict.get(key))+str(data_from_ocr))})
            print("value updated =", str(Dict.get(key))+str(data_from_ocr))
        else:
            Dict[today]=data_from_ocr


    def submit2(self, *args):
        global date
        date=str(self.date.text)
        cam_app.screen_manager.current = 'Home'


class HomePage(layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add items to layout
        self.act_data = TextInput(text='Actual data', multiline=True, size_hint=(1,.1))
        self.add_widget(self.act_data)

        my_data=str(Dict.get(date))
        self.act_data.text=str(my_data)

class CamApp(App):
    def build(self):

        self.screen_manager = ScreenManager()

        # Info page
        self.login_page = LoginPage()
        screen = Screen(name='Login')
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        self.home_page= HomePage()
        screen = Screen(name='Home')
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    cam_app=CamApp()
    cam_app.run()