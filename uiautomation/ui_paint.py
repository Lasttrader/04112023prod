#!python3
# -*- coding: utf-8 -*-
# works on windows XP, 7, 8, 8.1 and 10
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto

auto.uiautomation.DEBUG_EXIST_DISAPPEAR = True  # set it to False and try again, default is False
auto.uiautomation.DEBUG_SEARCH_TIME = True  # set it to False and try again, default is False
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out



square =''

#определяем окно paint
paintwindow = auto.WindowControl(searchDepth=1, ClassName='MSPaintApp')
if paintwindow.Exists(1):
    print('найдено окно paint')
auto.ButtonControl(searchFromControl=paintwindow, Name="Pencil").Click()

#определяем родительский элеиент
shapes = auto.GroupControl(searchFromControl=paintwindow, Name="Shapes")
#кликаем по дочернему элементу - квадрат
auto.ListItemControl(searchFromControl=shapes, Name="Rectangle").Click()
#рисуем квадрат
auto.PaneControl(searchFromControl=paintwindow, 
                 Name = "Using Rectangle tool on Canvas").DragDrop(100, 100, 200, 200)
print('rectangle success')

element1=auto.WindowControl(searchDepth=1, ClassName='MSPaintApp', Name='Untitled - Paint')
element1.SetActive()
element2=element1.PaneControl(ClassName='UIRibbonCommandBarDock', Name='UIRibbonDockTop', AutomationId='')
element3=element2.PaneControl(ClassName='UIRibbonCommandBar', Name='Ribbon', AutomationId='')
element4=element3.PaneControl(ClassName='UIRibbonWorkPane', Name='Ribbon', AutomationId='')
element5=element4.PaneControl(ClassName='NUIPane', Name='', AutomationId='')
element6=element5.PaneControl(ClassName='NetUIHWND', Name='Ribbon', AutomationId='')
element7=element6.PaneControl(ClassName='', Name='Lower Ribbon', AutomationId='')
element8=element7.CustomControl(ClassName='', Name='', AutomationId='')
element9=element8.CustomControl(ClassName='', Name='Home', AutomationId='')
element10=element9.ToolBarControl(ClassName='', Name='Shapes', AutomationId='')
element11=element10.GroupControl(ClassName='', Name='Shapes', AutomationId='')
element12=element11.ListControl(ClassName='', Name='Shapes', AutomationId='')
element13=element12.CustomControl(ClassName='', Name='', AutomationId='')
element13.ListItemControl(ClassName='', Name='Rectangle', AutomationId='').Click()

#paint_window.SetFocus()

# # Установите инструмент "Карандаш"
# auto.PaneControl(AutomationId="4103").Click()
# # Установите цвет чернил
# auto.PaneControl(AutomationId="1008").Click()
# # Выберите черный цвет
# auto.PaneControl(AutomationId="8041").Click()
# # Перейдите к рабочей области Paint
# work_area = auto.PaneControl(AutomationId="PositioningContainer")
# work_area.Click(100, 100)  # Выберите начальные координаты
# # Рисуем квадрат
# auto.MouseDragTo(200, 200)