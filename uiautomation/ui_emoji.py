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

'''
- выбрать браузер с webinar
- нажать на иконку эмодзи
- првоерить есть ли эмодзи на экране IsOffscreen
---если есть, то click()
---если нет, то envoke()
- нажать на иконку с отправкой сообщения
'''

element1=auto.WindowControl(searchDepth=1, ClassName='YandexBrowser_WidgetWin_1', Name='12762. Python: Эксперт - платформа МТС Линк — Yandex Browser')
element1.SetActive()
element2=element1.DocumentControl(ClassName='Chrome_RenderWidgetHostHWND', Name='12762. Python: Эксперт - платформа МТС Линк', AutomationId='385518400')
element3=element2.GroupControl(ClassName='', Name='', AutomationId='')
element4=element3.GroupControl(ClassName='', Name='', AutomationId='')
element5=element4.GroupControl(ClassName='', Name='', AutomationId='')
element6=element5.GroupControl(ClassName='', Name='', AutomationId='')
element7=element6.GroupControl(ClassName='', Name='', AutomationId='')
element8=element7.GroupControl(ClassName='', Name='', AutomationId='')
element8.ButtonControl(ClassName='', Name='', AutomationId='').Click()


