'''
-окно офис
-insert
-shape
-basic_shape
-rectangle
-нарисовать

'''

#!python3
# -*- coding: utf-8 -*-
# works on windows XP, 7, 8, 8.1 and 10
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto
import time

office_window = auto.WindowControl(searchDepth=1, 
                                ClassName='SALFRAME')
office_window.SetActive()
insert = office_window.MenuItemControl(Name='Insert')
insert.Click()
time.sleep(1.5) #задержка перед кликом, ожидание выпадающего меню
shape = insert.MenuItemControl(Name='Shape')
shape.Click()
time.sleep(1.5) #задержка перед кликом, ожидание выпадающего меню
basic_shape = shape.MenuItemControl(Name='Basic Shapes')
basic_shape.Click()
time.sleep(1.5) #задержка перед кликом, ожидание выпадающего меню
rectangle = basic_shape.GetChildren()[0]
rectangle.Click()

base_area = office_window.GetChildren()[2]
base_area.Click()
work_area = base_area.GetChildren()[0]
work_area.Click()
work_area.MouseDragTo(1450, 2049)